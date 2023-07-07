# Mental_Fitness_Tracker
The Mental Health Fitness Tracker: Analyzing mental fitness levels worldwide, using regression techniques (Linear, Lasso, Random Forest, Gradient Boosting). Provides insights, accurate predictions, and informs interventions/support. Impacting global mental well-being.

# Mental Fitness Tracker

The Mental Fitness Tracker project is a data-driven initiative that aims to analyze and predict mental fitness levels across different countries and various mental disorders. By leveraging regression techniques such as linear regression, Lasso regression, and random forest regression, the project provides insights into mental health and accurate predictions based on the available data.

## Features

- Data preprocessing: The project handles missing values by filling them with mean values, ensuring a complete dataset for analysis.
- Merging dataframes: Multiple datasets are merged based on common columns (Entity, Code, Year), creating a comprehensive dataset for further analysis.
- Exploratory data analysis: The project utilizes various visualizations, including heatmaps, scatter plots, pie charts, and line plots, to gain insights into the relationships between different variables and mental fitness levels.
- Model training and evaluation: Four models (Linear Regression, Random Forest, Gradient Boosting Regression, Lasso Regression) are trained using the dataset, and their performance is evaluated using metrics such as mean squared error, root mean squared error, and R-squared.
- Best performing model determination: The project identifies the best performing model based on the evaluation metrics, helping to prioritize the most accurate model for predicting mental fitness levels.

## Usage

1. Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn plotly
```

2. Prepare the dataset:
   - Create a directory named "Dataset".
   - Place the necessary CSV files in the "Dataset" directory.

3. Run the code:
   - Execute the provided Jupyter Notebook, "Mental Fitness Tracker Final.ipynb", or copy the code to your preferred development environment.
   - Ensure that the dataset file paths and names are correctly specified.
   - Run the code cell by cell to perform data preprocessing, exploratory analysis, model training, and evaluation.

4. Analyze the results:
   - The code generates visualizations and performance metrics for each model.
   - Interpret the results to understand the relationships between variables and mental fitness levels, as well as the performance of different models.

## Summary

The Mental Fitness Tracker project offers a comprehensive approach to understanding mental health by analyzing and predicting mental fitness levels. By leveraging regression techniques and a thorough data analysis pipeline, the project provides insights and predictions based on available data. The provided code allows for further exploration and analysis, empowering researchers and practitioners to gain a deeper understanding of mental well-being.

## REFRENCES

# Dataset
- The dataset used in this project includes two CSV files available from [Kaggle](https://www.kaggle.com/datasets/programmerrdai/mental-health-dataset)
    - `mental-and-substance-use-as-share-of-disease.csv`
    - `prevalence-by-mental-and-substance-use-disorder.csv`
- The files files were also provided by Edunet 

- This project was made during my internship period for [Edunet Foundation](https://edunetfoundation.org) in association with [IBM SkillsBuild](https://skillsbuild.org) and [AICTE](https://internship.aicte-india.org)

