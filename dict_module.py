classification_dict = {
    # ------ 内科系 ------
    "総合内科": [
        {
            "any": [("内科", "partial")]
        }
    ],
    "内科": [
        {
            "must": [("内科", "exact")]
        }
    ],
    "呼吸器内科": [
        {
            "must": [("内", "partial")],
            "any": [("呼吸", "partial"), ("呼", "partial")]
        }
    ],
    "消化器内科": [
        {
            # 例: 「内科」は必須（must）で、"消化" or "胃" or "腸" のいずれかを含めばOK (any)
            "any":  [("消化", "partial"), ("胃", "partial"), ("腸", "partial"), ('消', 'partial')]
        }
    ],
    "循環器内科": [
        {
            "must": [("内", "partial")],
            "any": [("循環器", "partial"), ("循", "partial")]
        }
    ],
    "腎臓・内分泌内科":[
        {
            "must": [("内", "partial")],
            "any": [("透析", "partial")]
        }
    ],
    "糖尿病・代謝内科":[
        {
            "must": [("内", "partial")],
            "any": [("糖", "partial"), ("代謝", "partial")]
        }
    ],
    "血液・腫瘍内科":[
        {
            "must": [("内", "partial")],
            "any": [("血", "partial"), ("腫瘍", "partial")]
        }
    ],
    "アレルギー科": [
        {
            # 「アレ」だけ単体なら exact、もし「アレルギー科」を含むなら "アレ" partial にするなど
            "must": [("アレ", "partial")]
        }
    ],
    "リウマチ科": [
        {
            "any": [("リウ", "partial"), ("膠原", "partial")]
        }
    ],
    "感染症内科": [
        {
            "any": [("感染", "partial"), ("性病", "partial")]
        }
    ],
    "老年病内科": [
        {
            "must": [("老年", "partial")]
        }
    ],
    "心療内科": [
        {
            "must": [("内", "partial")],
            "any": [("心療", "partial")]
        }
    ],

    # ------ 外科系 ------
    "総合外科": [
        {
            "any": [("外", "partial")]
        }
    ],
    "外科": [
        {
            "must": [("外科", "exact")]
        }
    ],
    "胃・腸外科": [
        {
            "must": [('外', "partial")],
            "any": [('腸', 'partial'), ('胃', 'partial')]
        }
    ],
    "大腸・肛門外科": [
        {
            "any": [('大腸', 'partial'), ('肛門', 'partial'), ('こう門', "partial")]
        }
    ],
    "肝・胆・膵外科": [
        {
            "must": [('外', 'partial')],
            "any": [("肝", "partial"), ("胆", "partial"), ("膵", "partial")]
        }
    ],
    "血管外科": [
        {
            "must": [('外', 'partial')],
            'any': [('血', 'partial')]
        }
    ],
    "乳腺・内分泌外科": [
        {
            "must": [('外', 'partial')],
            "any": [('乳', 'partial'), ('分泌', 'partial')]
        }
    ],
    "人工臓器・移植外科": [
        {
            "must": [('外', "partial")],
            "any": [('人工臓器', 'partial'), ('移植', 'partial')]
        }
    ],
    "心臓外科": [
        {
            "must": [("心臓","partial")]
        }
    ],
    "呼吸器外科": [
        {
            "must": [("外", "partial")],
            "any": [("呼吸", "partial")]
        }
    ],
    "脳神経外科": [
        {
            "any": [('脳', 'partial'), ('神経', 'partial'), ('脳神', 'partial')]
        }
    ],

    # ------ その他系 ------
    "麻酔科": [
        {
            # 「麻酔科」や「麻酔」で拾いたいなら partial でも良い
            "must": [("麻", "partial")]
        }
    ],
    "泌尿器科": [
        {
            "any": [('泌尿', 'partial'),('泌', 'partial'), ('頻尿', 'partial')]
        }
    ],
    "皮膚科": [
        {
            "any": [("皮", "partial")]
        }
    ],
    "眼科": [
        {
            "must": [('眼', 'partial')]
        }
    ],
    "整形外科": [
        {
            "must": [("整形", "partial")]
        }
    ],
    "耳鼻咽喉科・頭頸部外科": [
        {
            "any": [("耳鼻咽喉", "partial"), ("じび", "partial"), ("いんこう", "partial")]
        }
    ],
    "リハビリテーション科": [
        {
            "any": [('リハ', 'partial')]
        }
    ],
    "形成外科・美容外科": [
        {
            "any": [('形成', 'partial'), ('美容', 'partial')]
        }
    ],
    "口腔顎顔面外科・歯科": [
        {
            "any": [('歯', 'partial')]
        }
    ],
    "小児科": [
        {
            "must": [("小児", "partial")]
        }
    ],
    "小児外科": [
        {
            "must": [("小児", "partial"), ('外', 'partial')]
        }
    ],
    "産婦人科": [
        {
            "any": [("産", "partial"), ("婦", "partial")]
        }
    ],
    "精神神経科": [
        {
            "any": [('精神', 'partial')]
        }
    ],
    "放射線科": [
        {
            "any": [('放射', 'partial')]
        }
    ],
    "救急・集中治療科": [
        {
            "any": [('救急', 'partial'), ('集中', 'partial')]
        }
    ],
    "臨床腫瘍科": [
        {
            "must": [('臨床', 'partial'), ('腫瘍', 'partial')]
        }
    ],
    "病理診断科": [
        {
            "any": [('病理診断', 'partial')]
        }
    ],
    
    # どこにも該当しなかった場合
    "分類不可": []
}