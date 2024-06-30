
# --- ------------------------------------------------------------------- --- #
# --- File: directional.py
# --- ------------------------------------------------------------------- --- #

import numpy as np

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #

def target_y(y_thresholds, df_data):
    """
    A function to engineer the target variable. In particular, to calculate
    co_{t} = close_{t} - open_{t} as a continuous variabel to represent price
    change, to then create a multiclass-discrete variable.

    Args:
        y_thresholds: list
            A list of values that are used as lower bound to a condition for
            limiting the calculation.
        df_data: pd.DataFrame
            A dataframe with price-related data, it is required to have: 
                "opentime": unixtimestamp in GMT=0
                "close": close price
                "open": open price
    Returns:
        y_t: list of classes as derived from the internal algorithm for
            dynamic classes generation

    Raises:
        TBD

    """
    
    y_cl = { "d3" : y_thresholds[0],
             "d2" : y_thresholds[1], 
             "d1" : y_thresholds[2],
             "u1" : y_thresholds[3],
             "u2" : y_thresholds[4],
             "u3" : y_thresholds[5] }

    co_t = np.int32((df_data['close'] - df_data['open'])*1e4)
    
    y_t = ["d3" if y_cl["d3"] <= co_t[i] <= y_cl["d2"] - 1 else 
           "d2" if y_cl["d2"] <= co_t[i] <= y_cl["d1"] - 1 else 
           "d1" if y_cl["d1"] <= co_t[i] < 0 else 
           "u1" if 0 <= co_t[i] <= y_cl["u1"] else
           "u2" if y_cl["u1"] + 1 <= co_t[i] <= y_cl["u2"] else
           "u3" if y_cl["u2"] + 1 <= co_t[i] <= y_cl["u3"] else 
           "NA" for i in range(0, len(co_t))]
    
    return y_t

# ----------------------------------------------------------------------- --- #
# ----------------------------------------------------------------------- --- #

def eda_y(target_y, y_type:str = "categorical") -> dict:
    """
    Exploratory Data Analysis for Target variables, in particular, those
    that are discrete and multiclass. 

    Args:
        target_y: pd.Series
        
        y_type: str (default="categorical")

    Returns:
        r_eda: dict
            "counts": Counting of classes's occurrences 
        
    Raises:
        TBD
        

    """

    r_eda = {}
    
    if y_type == "categorical":
        
        # -- count classes proportion
        r_eda["counts"] = target_y.value_counts()

    return r_eda

