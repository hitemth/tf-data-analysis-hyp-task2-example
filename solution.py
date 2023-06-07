import pandas as pd
import numpy as np



chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    #from scipy.stats import ks_2samp
    from scipy.stats import anderson_ksamp

    if anderson_ksamp([x, y]).significance_level < 0.07:
        return True
    else:
        return False

