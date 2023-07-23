# Algerian Forest Fire

- EDA for Algerian Forest Fire dataset.
- Classification and Regression Models for predicting `Classes` between `fire` and `not-fire` and `Temperature` respectively.

# ML Models

## Regression

1. Linear
2. Lasso
3. Ridge
4. ElasticNet
5. SVR
6. Decision Tree
7. Random Forest
8. AdaBoost
9. XGBoost
10. CATBoost
11. Polynomial (degree 2)

## Classification

1. Logistic
2. K-Nearest Neighbor
3. SVC
4. Naive Bayes
5. Decision Tree
6. Random Forest
7. AdaBoost
8. XGBoost
9. CATBoost

# Deployed on Heroku

- Deployed Link: https://aff-prediction.herokuapp.com/
- Classification Prediction API
  - API: https://aff-prediction.herokuapp.com/classification
  - BODY: JSON data
  ```json
  {
  	"day": 21,
  	"month": "Aug",
  	"Temperature": 36,
  	"RH": 58,
  	"Ws": 19,
  	"Rain": 0.0,
  	"FFMC": 88.6,
  	"DMC": 29.6,
  	"DC": 141.1,
  	"ISI": 9.2,
  	"Region": "Bejaia"
  }
  ```
- Regression Prediction API
  - API: https://aff-prediction.herokuapp.com/regression
  - BODY: JSON data
  ```json
  {
  	"day": 21,
  	"month": "Aug",
  	"RH": 58,
  	"Ws": 19,
  	"Rain": 0.0,
  	"FFMC": 88.6,
  	"DMC": 29.6,
  	"DC": 141.1,
  	"ISI": 9.2,
  	"Classes": "fire",
  	"Region": "Bejaia"
  }
  ```
