# Real-Estate-Price-Prediction-using-Linear-Regression

This project aims to predict real estate prices using linear regression based on various features of properties, such as square footage, location, and other factors. The dataset contains information about different properties, and the goal is to build a predictive model to estimate property prices.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Model Explanation](#model-explanation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required packages using pip:

```bash
pip install pandas matplotlib scikit-learn
Data Description
The dataset train.csv contains the following columns:

POSTED_BY: The type of poster (Owner/Dealer)
UNDER_CONSTRUCTION: Indicator if the property is under construction (0/1)
RERA: RERA registration status (0/1)
BHK_NO.: Number of bedrooms (BHK)
BHK_OR_RK: Type of property (BHK/RK)
SQUARE_FT: Area of the property in square feet
READY_TO_MOVE: Indicator if the property is ready to move in (0/1)
RESALE: Resale status (0/1)
ADDRESS: Address of the property
LONGITUDE: Longitude coordinate of the property
LATITUDE: Latitude coordinate of the property
price: Target price in lacs
Model Explanation
The model uses Linear Regression to predict property prices based on the SQUARE_FT feature. After fitting the model with the dataset, predictions can be made for different square footage values.

## Results
The script will print the predicted prices for properties with square footage of 1500 and 2000 square feet, along with the model's coefficient and intercept.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue for improvements.



