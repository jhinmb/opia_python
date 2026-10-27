from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = datasets.fetch_california_housing(as_frame=True).frame

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predicciones
)

print("MAE:", mae)

joblib.dump(
    modelo,
    "modelo_california.pkl"
)

print("Modelo guardado.")