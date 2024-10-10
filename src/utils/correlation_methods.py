
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import shapiro

def verificar_linearidade(x, y):
    model = LinearRegression().fit(x.reshape(-1, 1), y)
    pred = model.predict(x.reshape(-1, 1))
    return r2_score(y, pred) > 0.8  # Se R² for maior que 0.8, considere linear

def verificar_normalidade(x):
    stat, p_value = shapiro(x)
    return p_value > 0.05  # Se p > 0.05, os dados são normalmente distribuídos

def verificar_monotonicidade(x, y):
    rank_x = np.argsort(np.argsort(x))
    rank_y = np.argsort(np.argsort(y))
    return np.corrcoef(rank_x, rank_y)[0, 1] > 0.8  # Se a correlação dos ranks for alta

def detectar_outliers(x):
    z_scores = np.abs((x - np.mean(x)) / np.std(x))
    return np.any(z_scores > 3)  # Se houver outliers com z-score maior que 3

def escolher_melhor_correlacao(x, y):
    if detectar_outliers(x) or detectar_outliers(y):
        return "Kendall"  # Mais robusto a outliers
    elif verificar_linearidade(x, y):
        return "Pearson"  # Relação linear
    elif verificar_monotonicidade(x, y):
        return "Spearman"  # Relação monotônica, mas não linear
    else:
        return "Kendall"  # Não-linear, ordinal ou muitos empates
