# Canadian Rental Prices Regression Project

This project analyses the rental prices all accross Canada and explores different regression models to find one that predicts the price the most accurately.

## Data source

The data used for this project is a [Kaggle dataset](https://www.kaggle.com/datasets/sergiygavrylov/25000-canadian-rental-housing-market-june-2024) containing rental prices for units across Canada in 2024.

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

When doing the [exploratory data analysis](DataAnalysis.ipynb), the thing that stood out the most is the high number of outliers, even if the data is grouped by province or city. The analysis of the outliers suggests that the neighbourhood and the type of rental are key predictors of the price.

To simplify the model, one feature was kept for the location, which is the 3 first characters of the postal code, so the neighbourhood is accounted for.

In the [feature engineering and data preprocessing](DataPreprocessing.ipynb) phase, the categorical variables were encoded with One Hot Encoding. The postal codes were encoded with Frequency Encoding, so the neighbourhoods with the most ads would have more weight in the price prediction. Also, 10 features were selected out of 17 using the Mutual Information Regression.

After testing different regression models, a model with the target variable transformed was chosed. The R-squared of the model is 0.4262 and the RMSE of 0.2777. The data modeling can be found [here](DataModeling.ipynb).

## Future work

The model could have performed better if another machine learning algorithm was used or if the analysis and modeling was made for one city. Even analyzing one province could have been better.