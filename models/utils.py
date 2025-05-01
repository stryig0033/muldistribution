# utils.py
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, RandomizedSearchCV
from scipy.stats import randint, uniform 
from sklearn.multioutput import MultiOutputRegressor

# --------- パスと列名 ---------
DATA_CSV   = Path("grid_features.csv")        # 先に作った特徴量 CSV
TARGETS    = ["Rehab_cnt", "Gastro_cnt", "Cardio_cnt", "Uro_cnt"]
# ここでは入力特徴量 = TARGETS 以外のすべて
def _feature_cols(df):                       
    return [c for c in df.columns if c not in TARGETS + ["geometry"]]

# --------- データロード ---------
def load_data():
    df = pd.read_csv(DATA_CSV)
    X  = df[_feature_cols(df)]
    y  = df[TARGETS]
    return X, y

# --------- 前処理パイプライン ---------
def make_preprocessor(num_cols):
    return ColumnTransformer(
        [("num", StandardScaler(), num_cols)],
        remainder="drop"
    )

# --------- ランダムフォレスト簡易サーチ ---------
# 変更①: RF の素の分布を返す関数名を _rf_base_dist に
def _rf_base_dist():
    return {
        "n_estimators":       randint(300, 1000),
        "max_depth":          randint(5,   30),
        "max_features":       uniform(0.3, 0.7),
        "min_samples_leaf":   randint(1, 10),
        "bootstrap":          [True, False],
    }


# 変更②: パイプラインに合わせて prefix を付けるヘルパー
def rf_param_dist(pipe, step_name="rf"):
    """
    Pipeline 内の RandomForest or MultiOutput(RandomForest) を判別して
    正しいキー付き param_distributions を返す
    """
    base = _rf_base_dist()
    step_obj = pipe.named_steps[step_name]

    # ▶ MultiOutputRegressor のときだけ estimator__ を付ける
    if isinstance(step_obj, MultiOutputRegressor):
        return {f"{step_name}__estimator__{k}": v for k, v in base.items()}
    else:  # 単一タスク RF
        return {f"{step_name}__{k}": v for k, v in base.items()}

# 変更③: tune_model で param_dist を pipe から動的生成
def tune_model(pipe, X, y, cv, n_iter=20, random_state=0):
    search = RandomizedSearchCV(
        pipe,
        rf_param_dist(pipe),          # ←ここを変更
        n_iter=n_iter, cv=cv,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1, random_state=random_state, verbose=0
    )
    search.fit(X, y)
    best = search.best_estimator_
    best_score = -search.best_score_
    return best, best_score, search.best_params_

# --------- 汎用 Cross-validation ---------
def get_cv(k=5, seed=42):
    return KFold(n_splits=k, shuffle=True, random_state=seed)

# ----------------------------- 評価ヘルパ -----------------------------
def cv_metrics(model, X, y, cv):
    """
    返り値:
        rmse_mean  : float   (Fold×タスク平均)
        r2_mean    : float   (Fold×タスク平均)
    """
    rmses, r2s = [], []
    for tr_idx, te_idx in cv.split(X):
        model.fit(X.iloc[tr_idx], y.iloc[tr_idx])
        pred = model.predict(X.iloc[te_idx])

        # multioutput="raw_values" → タスク別 array
        rmse_fold = mean_squared_error(
            y.iloc[te_idx], pred, multioutput="raw_values", squared=False
        )
        r2_fold = r2_score(
            y.iloc[te_idx], pred, multioutput="raw_values"
        )
        rmses.append(rmse_fold)
        r2s.append(r2_fold)

    rmse_mean = np.vstack(rmses).mean()      # Fold×task → scalar
    r2_mean   = np.vstack(r2s).mean()
    return rmse_mean, r2_mean