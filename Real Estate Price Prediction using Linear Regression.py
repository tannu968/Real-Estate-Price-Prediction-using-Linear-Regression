import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Load the dataset
df = pd.read_csv("E:/train.csv")

# Rename the target column for convenience
df.rename(columns={'TARGET(PRICE_IN_LACS)': 'price'}, inplace=True)

# Plotting price against Longitude and Latitude
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.xlabel('Longitude')
plt.ylabel('Price')
plt.scatter(df.LONGITUDE, df.price)

plt.subplot(1, 2, 2)
plt.xlabel('Latitude')
plt.ylabel('Price')
plt.scatter(df.LATITUDE, df.price)
plt.show()

# Plotting price against SQUARE_FT and BHK_OR_RK
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.ylim(20, 100)
plt.scatter(df.SQUARE_FT, df.price)

plt.subplot(1, 2, 2)
plt.xlabel('BHK or RK')
plt.ylabel('Price')
plt.ylim(20, 100)
plt.scatter(df.BHK_OR_RK, df.price)
plt.show()

# Model training using Linear Regression
model = linear_model.LinearRegression()
model.fit(df[['SQUARE_FT']], df.price)

# Predict price for a house with 1500 square feet
predicted_price = model.predict([[1500]])
print(f"Predicted price for a house with 1500 square feet: {predicted_price[0]}")

# Output model coefficient and intercept
print(f"Model Coefficient (Slope): {model.coef_[0]}")
print(f"Model Intercept: {model.intercept_}")

# Prediction for a house with 2000 square feet
predicted_price_2000 = 2000 * model.coef_ + model.intercept_
print(f"Predicted price for a house with 2000 square feet: {predicted_price_2000[0]}")
