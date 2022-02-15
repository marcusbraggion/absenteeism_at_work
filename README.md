[
![logo](https://user-images.githubusercontent.com/97288194/154069960-07591e0b-f6fe-49a6-81ad-5b0d85a6c83a.png)
](url)

# Mielsen - Predict absenteeism at work

# 1.0 Context

The problem this time was the turnover. Mielsen (fictional), a company that operates in the field of research, information and data analysis, used its expertise internally to answer a big question: knowing why people are leaving the company.

# 2.0 Challenge 

You are the Data Scientist alocated into HR People Analytics assigned to the task of discovering the cause of the problem, you will be responsible for identifying the key indicators, focusing your attention on absenteeism at work and building a basic model that can measure and predict the magnitude of the scenario they are facing. facing.

# 3.0 Business Assumptions

# 4.0 Solution Strategy
The strategy adopted was the following:

Step 01. Data Description: I searched for NAs, checked data types (and adapted some of them for analysis) and presented a statistical description.

Step 02. Feature Engineering: New features were created to make possible a more thorough analysis.

Step 03. Data Filtering: Entries containing no information or containing information which does not match the scope of the project were filtered out.

Step 04. Exploratory Data Analysis: I performed univariate, bivariate and multivariate data analysis, obtaining statistical properties of each of them, correlations and testing hypothesis (the most important of them are detailed in the following section).

Step 05: Data Preparation: Here I chose to use the resize features with StandardScaler

Step 06. Feature selection: The statistically most relevant features were selected using the Boruta package. 

Step 07. Machine learning modelling: Some machine learning models were trained. The one that presented best results after cross-validation went through a further stage of hyperparameter fine tunning to optimize the model's generalizability.

Step 08. Model-to-business: The models performance is converted into business values.

# 5.0 Conclusions

# 6.0 Next steps and Improvements