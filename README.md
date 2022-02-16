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

Step 05: Data Preparation: Here I chose to scaling features by removing the mean and scaling to unit variance using StandardScaler method in sklearn.

Step 06. Feature selection: I used the Boruta package to find features with more importances.

Step 07. Machine learning modelling: Some machine learning models were trained. The one that presented best results after cross-validation went through a further stage of hyperparameter fine tunning to optimize the model's generalizability.

Step 08. Model-to-business: The models performance is converted into business values.

# 6.0 Conclusions

In this project we adopted a simple approach and some machine learning algorithms to build a predictive model capable of determining the organization's absenteeism.
I used the Random Forest Regressor model to learn all the behavior of the data and after modeling the data I used it to make predictions, using 70% of the dataset to train it and then test it on 30% of the unseen data by the model to measure its performance. After all the steps mentioned and with the predictions made, I performed the evaluation of the performance of the model, bringing the result of the prediction for each employee in the dataset denominated as id number, through two metrics: best and worst scenario. And MAE and MAPE: two metrics that are easy to understand so that the HR team can use the model data in a more practical way in their daily lives. I also brought 4 graphs that demonstrate the result and error of the model for each employee and finally we can conclude result of the model with a predict of 48 hours of absence.


# 8.0 Lesson Learned

Finding main factors that are associated with the employee's well-being and consequently with the absence rate through data analysis, we can extract insights that will serve as a guide for next actions within the organization, improving employee engagement and adherence with the business, making a healthier work environment, in addition to making HR decisions increasingly smart and data-driven.

# 9.0 Next steps

Improve model perfomance in 3%.