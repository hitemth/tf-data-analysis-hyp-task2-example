import pandas as pd
import numpy as np



chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp

    stat, p_value = ks_2samp(x, y)
    
    # Отклоняем гипотезу однородности выборок, если p-value меньше уровня значимости
    return p_value < 0.07

