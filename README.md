[
![logo](https://user-images.githubusercontent.com/97288194/154069960-07591e0b-f6fe-49a6-81ad-5b0d85a6c83a.png)
](url)

# Mielsen - Predict absenteeism at work

# Context

The problem this time was the turnover. Mielsen (fictional), a company that operates in the field of research, information and data analysis, used its expertise internally to answer a big question: knowing why people are leaving the company.

# Challenge 

You are the Data Scientist alocated into HR People Analytics assigned to the task of discovering the cause of the problem, you will be responsible for identifying the key indicators, focusing your attention on absenteeism at work and building a basic model that can measure and predict the magnitude of the scenario they are facing. facing.

3.0 Business Assumptions
stores.csv: This file contains anonymized information about the 45 stores, indicating the type and size of store.

train.csv: This is the historical training data, which covers to 2010-02-05 to 2012-11-01. Within this file you will find the following fields:

Store - the store number

Dept - the department number

Date - the week

Weekly_Sales - sales for the given department in the given store

IsHoliday - whether the week is a special holiday week

test.csv

This file is identical to train.csv, except we have withheld the weekly sales. You must predict the sales for each triplet of store, department, and date in this file.

features.csv: This file contains additional data related to the store, department, and regional activity for the given dates. It contains the following fields:

Store - the store number

Date - the week

Temperature - average temperature in the region

Fuel_Price - cost of fuel in the region

MarkDown1-5 - anonymized data related to promotional markdowns that Walmart is running. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA.

CPI - the consumer price index

Unemployment - the unemployment rate

IsHoliday - whether the week is a special holiday week

For convenience, the four holidays fall within the following weeks in the dataset (not all holidays are in the data):

Super Bowl: 12-Feb-10, 11-Feb-11, 10-Feb-12, 8-Feb-13

Labor Day: 10-Sep-10, 9-Sep-11, 7-Sep-12, 6-Sep-13

Thanksgiving: 26-Nov-10, 25-Nov-11, 23-Nov-12, 29-Nov-13

Christmas: 31-Dec-10, 30-Dec-11, 28-Dec-12, 27-Dec-13

4.0 Solution Strategy
The strategy adopted was the following:

Step 01. Data Description: I searched for NAs, checked data types (and adapted some of them for analysis) and presented a statistical description.

Step 02. Feature Engineering: New features were created to make possible a more thorough analysis.

Step 03. Data Filtering: Entries containing no information or containing information which does not match the scope of the project were filtered out.

Step 04. Exploratory Data Analysis: I performed univariate, bivariate and multivariate data analysis, obtaining statistical properties of each of them, correlations and testing hypothesis (the most important of them are detailed in the following section).

Step 05: Data Preparation: Here I chose to use the resize features with StandardScaler

Step 06. Feature selection: The statistically most relevant features were selected using the Boruta package. 

Step 07. Machine learning modelling: Some machine learning models were trained. The one that presented best results after cross-validation went through a further stage of hyperparameter fine tunning to optimize the model's generalizability.

Step 08. Model-to-business: The models performance is converted into business values.

5.0 Conclusions

6.0 Next steps and Improvements