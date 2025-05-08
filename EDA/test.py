import pandas as pd
import geopandas as gpd
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score, r2_score, make_scorer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.utils import parallel_backend
import numpy as np
from tqdm import tqdm
import geopandas as gpd
from pathlib import Path
import os
import matplotlib.pyplot as plt
from sklearn.experimental import enable_halving_search_cv

from tqdm  import tqdm