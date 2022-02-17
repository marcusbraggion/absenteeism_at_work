[
![logo](https://user-images.githubusercontent.com/97288194/154069960-07591e0b-f6fe-49a6-81ad-5b0d85a6c83a.png)
](url)

# Mielsen - Predict absenteeism at work

# 1.0 Context

The HR department was pressured to retention and improve attrition in firm. The CPO perceives the importance of having a more quantitative approach when taking decisions, reason why a small team of data scientists was hired and allocated in HR People Analytics Squad with a clear objective in mind: to build a predictive model which will support direct HR initiatives. Desirably, the success of these activities will prove the value of the approach and convince the more skeptical within the company.

# 2.0 Challenge 

You are the Data Scientist alocated into HR People Analytics assigned to the task of discovering the cause of the problem, you will be responsible for identifying the key indicators, focusing your attention on absenteeism at work and building a predictive model which will support HR initiatives.

# 3.0 Business Assumptions

1. Individual identification (ID)

2. Reason for absence (ICD).

Absences attested by the International Code of Diseases (ICD) stratified into 21 categories (I to XXI).

And 7 categories without (CID) patient follow-up (22), medical consultation (23), blood donation (24), laboratory examination (25), unjustified absence (26), physiotherapy (27), dental consultation (28).

3. Month of absence

4. Day of the week (Monday (2), Tuesday (3), Wednesday (4), Thursday (5), Friday (6))

5. Seasons (summer (1), autumn (2), winter (3), spring (4))

6. Transportation expense

7. Distance from Residence to Work (kilometers)

8. Service time

9. Age

10. Work load Average/day

11. Hit target

12. Disciplinary failure (yes=1; no=0)

13. Education (high school (1), graduate (2), postgraduate (3), master and doctor (4))

14. Son (number of children)

15. Social drinker (yes=1; no=0)

16. Social smoker (yes=1; no=0)

17. Pet (number of pet)

18. Weight

19. Height

20. Body mass index

21. Absenteeism time in hours (target)


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