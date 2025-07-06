import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Siapkan data per ruas jalan
def prepare_data(df, ruas):
    df_ruas = df[df["ruas_jalan"] == ruas].copy()
    df_ruas = df_ruas.sort_values("tanggal")

    df_ruas["bulan"] = df_ruas["tanggal"].dt.month
    df_ruas["rolling_3"] = df_ruas["kecepatan"].rolling(window=3).mean()
    df_ruas = df_ruas.dropna()

    X = df_ruas[["bulan", "rolling_3"]]
    y = df_ruas["kecepatan"]

    return X, y, df_ruas

# Latih model + evaluasi RMSE
def train_model_with_evaluation(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    return model, rmse

# Prediksi besok (pakai fitur bulan & rolling)
def predict_besok(model, bulan, rolling_3):
    input_data = pd.DataFrame({"bulan": [bulan], "rolling_3": [rolling_3]})
    return model.predict(input_data)[0]
