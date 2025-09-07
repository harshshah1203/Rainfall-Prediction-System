🌦️ Weather & Rainfall Data Analysis

This project demonstrates a complete data science workflow on a rainfall dataset, including Exploratory Data Analysis (EDA), Data Transformation, and Feature Selection.
It is implemented in Python (Jupyter Notebook) using libraries such as Pandas, NumPy, Seaborn, Matplotlib, and Scikit-learn.

The goal is to prepare the dataset for downstream tasks like machine learning modeling (classification or regression).

🔍 Workflow
1. Exploratory Data Analysis (EDA)

Inspected dataset shape, datatypes, summary statistics.

Identified and handled missing values & duplicates.

Visualized feature distributions with histograms & boxplots.

Plotted correlation heatmap to detect multicollinearity.

2. Data Transformation

Missing value imputation:

Numerical: Mean

Categorical: Mode

Encoded categorical features using Label Encoding.

Scaled numerical features using StandardScaler.

Handled outliers and ensured data consistency.

3. Feature Selection

Two approaches were applied:

Univariate Feature Selection

Used ANOVA F-test (for classification) or F-regression (for regression).

Selected top-k significant features.

Model-based Feature Importance

Trained RandomForestClassifier/Regressor based on target type.

Extracted and ranked feature importances.
