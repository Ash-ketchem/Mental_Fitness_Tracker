# -*- coding: utf-8 -*-
"""Mental Fitness Tracker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oO-VOulNKABAurEXlMdBUbsMhoKN-7E9
"""

pip install pandas numpy matplotlib seaborn scikit-learn

import numpy as np
import pandas as pd
import os

INPUT_DIR = "Dataset"
if not os.path.exists(INPUT_DIR): os.mkdir(INPUT_DIR)
# upload the csv files to this directory

print("files used are")
for file in os.listdir("Dataset"):
  print(file)

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# dataset walkthrough

dataset = [pd.read_csv(os.path.join(INPUT_DIR,file)) for file in os.listdir(INPUT_DIR) if ".csv" in file]

for df in dataset:
  print(df.head().to_string())
  print()

# filling missing values

for df in dataset:
  numeric_columns = df.select_dtypes(include=[np.number]).columns
  df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# merging dataframes

merged_df = pd.merge(*dataset, on=["Entity", "Code", "Year"])
merged_df.head()

# preprocessing of the df

# convert data types
for col in [col for col in merged_df.columns if col not in ["Entity", "Code", "Year"]] :
  merged_df[col] = merged_df[col].astype(float)

# Renaming columns
merged_df = merged_df.set_axis(['Country','Code','Year','mental_fitness', 'Schizophrenia', 'Bipolar_disorder', 'Eating_disorder','Anxiety','drug_usage','depression','alcohol'], axis='columns', copy=False)
merged_df.head()

merged_df.isnull().sum()
merged_df.drop('Code', axis=1, inplace=True)
merged_df.size,merged_df.shape

# EXPLORATORY ANALYSIS

merged_df.info()

mean = merged_df['mental_fitness'].mean()
mean

#heatmap

plt.figure(figsize=(12,6))
sns.heatmap(merged_df.corr(), annot=True, cmap='viridis')
plt.plot()

sns.jointplot(merged_df, x="Schizophrenia", y="mental_fitness" ,kind="reg", color="m")
plt.show()

sns.jointplot(merged_df, x="depression", y="mental_fitness" ,kind="reg", color="m")
plt.show()

sns.jointplot(merged_df,x='Bipolar_disorder',y='mental_fitness',kind='reg',color='blue')
plt.show()

sns.pairplot(merged_df,corner=True)
plt.show()

fig = px.pie(merged_df, values='mental_fitness', names='Year', color_discrete_sequence=px.colors.qualitative.Safe)
fig.show()

fig=px.bar(merged_df.head(20), x='Year', y='mental_fitness',color='Year',template='plotly_dark',)
fig.show()

# YEARWISE VARIATIONS IN MENTAL FITNESS OF DIFFERENT COUNTRIES

fig = px.line(merged_df, x="Year", y="mental_fitness", color='Country',markers=True,color_discrete_sequence=['#1f77b4', '#ff7f0e'], template='plotly_dark')
fig.show()

# Training models

# transform categorical variables into numerical values
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in merged_df.columns:
    if merged_df[i].dtype == 'object':
        merged_df[i]=l.fit_transform(merged_df[i])

#THE  X AND y VARIABLES

X = merged_df.drop('mental_fitness', axis=1)
Y = merged_df['mental_fitness']

# TEST-TRAIN SPLIT
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("xtrain: ", X_train.shape)
print("xtest: ", X_test.shape)
print("ytrain: ", y_train.shape)
print("ytest: ", y_test.shape)

from sklearn.linear_model import  Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# creating a dictionary to strore the models and metrics

models = {
    "Linear Regression" : {
        "model" : LinearRegression,
        "performance":{}
    },
    "Random Forest" : {
        "model" : RandomForestRegressor,
        "performance":{}
    },
    "Gradient Boosting Regression" : {
        "model" : GradientBoostingRegressor,
        "performance":{}
    },
    "Lasso Regression" : {
        "model" : Lasso,
        "performance":{}
    }
}

# Train multiple models and store their performance metrics

# Iterate over each model in the 'models' dictionary
for key in models.keys():
    # Initialize the model
    model = models.get(key).get("model")()

    # Fit the model using the training data
    model.fit(X_train, y_train)

    # Evaluate model performance on the training set
    y_pred_train = model.predict(X_train)
    models.get(key)["performance"]["train"] = {
        "mse": mean_squared_error(y_train, y_pred_train),
        "rmse": np.sqrt(mean_squared_error(y_train, y_pred_train)),
        "r2": r2_score(y_train, y_pred_train)
    }

    # Evaluate model performance on the testing set
    y_pred_test = model.predict(X_test)
    models.get(key)["performance"]["test"] = {
        "mse": mean_squared_error(y_test, y_pred_test),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred_test)),
        "r2": r2_score(y_test, y_pred_test)
    }

# Sort models based on their performance metrics

models = dict(sorted(models.items(), key=lambda x: (
    x[1]["performance"]["test"]["mse"],          # Sort by mean squared error (lower is better)
    x[1]["performance"]["test"]["rmse"],         # Sort by root mean squared error (lower is better)
    -x[1]["performance"]["test"]["r2"]           # Sort by negative R-squared (higher is better)
)))

models

# evaluating the performance of models

for key, value in models.items():
    print(f"Model: {key}\n" + (len(key) + 10) * "-" + "\n")

    # Print model performance on the training set
    print("* Model performance on the training set\n")
    performance = value["performance"]["train"]
    print(f'\tMSE: {format(performance["mse"])}')
    print(f'\tRMSE: {format(performance["rmse"])}')
    print(f'\tR2 score: {format(performance["r2"])}\n')

    # Print model performance on the testing set
    print("* Model performance on the testing set\n")
    performance = value["performance"]["test"]
    print(f'\tMSE: {format(performance["mse"])}')
    print(f'\tRMSE: {format(performance["rmse"])}')
    print(f'\tR2 score: {format(performance["r2"])}\n')

import matplotlib.pyplot as plt

# Determine the number of rows and columns for the subplot grid
num_models = len(models.keys())
num_cols = 2
num_rows = (num_models + num_cols - 1) // num_cols

# Create the subplot grid
fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 6*num_rows))

# Flatten the axs array if there is only one row
if num_rows == 1:
    axs = [axs]

# Iterate over each model and subplot
for i, key in enumerate(models.keys()):
    # Creating an instance of the model
    model = models[key].get("model")()

    # Fit the model using the training data
    model.fit(X_train, y_train)

    # Predict on the testing set
    y_test_pred = model.predict(X_test)

    # Determine the subplot position
    row = i // num_cols
    col = i % num_cols

    # Plotting scatter plot of predicted vs. actual values
    axs[row][col].scatter(y_test, y_test_pred, label='Testing Set')

    # Add labels and title to the subplot
    axs[row][col].set_xlabel('Original Values')
    axs[row][col].set_ylabel('Predicted Values')
    axs[row][col].set_title(f'Scatter Plot of Actual vs. Predicted Values\nModel: {key}')

    # Add legend
    axs[row][col].legend()

# Remove any empty subplots if exists
if num_models % num_cols != 0:
    for j in range(num_models % num_cols, num_cols):
        fig.delaxes(axs[-1][j])

# Adjust spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()

# getting the best performing and worst performing model

print(f"The best performing model is {next(iter(models.keys()))}")
print(f"The worst performing model is {next(reversed(models.keys()))}")

print("""SUMMARY
-------

The following summary provides an overview of the performance metrics for each regression model on both the training and testing sets:

Random Forest:
- Training Set:
  - MSE: 0.0051
  - RMSE: 0.0715
  - R2 score: 0.9990
- Testing Set:
  - MSE: 0.0318
  - RMSE: 0.1784
  - R2 score: 0.9937

The Random Forest model demonstrated exceptional performance on both the training and testing sets. It achieved a very low MSE and RMSE, indicating high predictive accuracy. The R2 score suggests that the model explains a significant proportion of the variance in the target variable. Overall, the Random Forest model outperformed the other models in terms of predictive accuracy.

Gradient Boosting Regression:
- Training Set:
  - MSE: 0.2389
  - RMSE: 0.4888
  - R2 score: 0.9550
- Testing Set:
  - MSE: 0.2983
  - RMSE: 0.5461
  - R2 score: 0.9414

The Gradient Boosting Regression model also performed well on both the training and testing sets. Although it had higher MSE and RMSE values compared to the Random Forest model, it still achieved a relatively high R2 score, indicating good predictive performance. The model demonstrated the ability to capture relationships between the predictors and the target variable.

Linear Regression:
- Training Set:
  - MSE: 1.3249
  - RMSE: 1.1511
  - R2 score: 0.7502
- Testing Set:
  - MSE: 1.4000
  - RMSE: 1.1832
  - R2 score: 0.7248

The Linear Regression model exhibited higher MSE and RMSE values compared to the Random Forest and Gradient Boosting Regression models. The R2 score indicates that the model explained a moderate amount of the variance in the target variable. However, its predictive accuracy was relatively lower compared to the other models.

Lasso Regression:
- Training Set:
  - MSE: 3.7099
  - RMSE: 1.9261
  - R2 score: 0.3006
- Testing Set:
  - MSE: 3.5372
  - RMSE: 1.8807
  - R2 score: 0.3046

The Lasso Regression model demonstrated the poorest performance among the evaluated models. It yielded higher MSE and RMSE values and had a lower R2 score, indicating less explanatory power. The model's predictive accuracy was limited compared to the Random Forest and Gradient Boosting Regression models.

In summary, based on the performance metrics, the Random Forest model displayed the best overall performance, followed by the Gradient Boosting Regression model. The Linear Regression model performed moderately, while the Lasso Regression model showed the poorest performance among the four models.
""")