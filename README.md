# Canadian Rental Prices Regression Project

This project analyses the rental prices all accross Canada and explores different regression models to find one that predicts the price the most accurately.

## Data source

We will work with a [Kaggle dataset](https://www.kaggle.com/datasets/sergiygavrylov/25000-canadian-rental-housing-market-june-2024) containing rental prices for units across Canada in 2024.

The dataset was obtained from [rentfaster.ca](https://www.rentfaster.ca).

## Libraries used
- Geopy
- Joblib
- Matplotlib
- Numpy
- Pandas
- Pickle
- Scikit-learn
- Scipy
- Seaborn
- Statsmodels

## Results and evaluation

When doing the [exploratory data analysis](DataAnalysis.ipynb), the thing that stood out the most is the high number of outliers, even if the data is grouped by province or city. After analysing the outliers, we found out the neibourhood and type of rental are two important predictors of the price.

To simplify the model, we only kept one feature for the location, which is the 3 first characters of the postal code, so we can have the neighbourhood.

In the [feature engineering and data preprocessing](DataPreprocessing.ipynb) phase, we encoded the categorical variables with One Hot Encoding. The postal codes were encoded with Frequency Encoding, so the neighbourhoods with the most ads would have more weight in the price prediction. Also, 10 features were selected out of 17.

After testing different models, we found a regression model with a natural logarithmic transformed target variable with a R-squared of 0.4262 and a RMSE of 0.2777. The data modeling can be found [here](DataModeling.ipynb).

## Future work

We could have gotten better results if we used another machine learning algorithm or if we analyzed and modeled the data of only one city. Even analyzing one province could have been better.