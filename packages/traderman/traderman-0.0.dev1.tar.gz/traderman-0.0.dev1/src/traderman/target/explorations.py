
# --- ------------------------------------------------------------------- --- #
# --- File: explorations.py
# --- ------------------------------------------------------------------- --- #

# Input file
file_name = "AVAXUSDC-1h-2024-05.csv"
file_route = "~/git/iteralabs/Traderman/files/datasets/"
data = load_csv(file_name, file_route)

# Thresholds for target class definition
y_th = [np.float64("inf")*-1, -2000, -100, 100, 2000, np.float64("inf")]

# Target generation
data["y_t"] = target_y(y_thresholds=y_th, df_data=data)
data["co_t"] = (data["close"] - data["open"])*1e4

# Lightweighted dataset for explorations
data_model = data[["opentime", 'co_t', "y_t"]]
# print(data_model.head(5))
# print(data_model.tail(5))
# data_eda = eda_y(target_y=data_model["y_t"], y_type="categorical")

