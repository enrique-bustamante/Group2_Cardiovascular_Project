# Cardiovascular Disease Project

## Overview Heart disease is the leading cause of death for both men and
women, and people of most racial and ethnic groups in the US. About 665,000
individuals die from heart disease each year in the US - 1 in every 4 deaths.
It is also the most preventable.  Our group is reviewing a dataset that looks
at patient data (age, weight, gender, smoking, activity level, etc) and the
prevalence of cardiovascular disease. We're going to analyze which factors
might contribute more heavily to the disease and shed light on a condition
that can be preventable by taking a proactive approach to our lifestyle.

How can we improve our daily activities to prevent Cardiovascular disease? In
this dataset we're given medical records with key health factors including if
someone had a cardiovascular event.

Using medically examined data we aim to answer the following questions: - What
group of factors have the largest impact on a Cardiovascular event? - From the
5-7 factors, can we narrow it down with PCA? - Can we create a model that
would predict a Cardiovascular event?

## Link to video

[Group 2 Video Demonstration](https://drive.google.com/file/d/1bPojAP_Pgbk2DqdMQK33KtKmLkLSnYTX/view?usp=sharing)

## Resources
The cardiovascular disease dataset is an open-source [dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)
that is found on Kaggle.

## Dataset

The dataset contains 70,000 records (34,979 who have cardiovascular disease
and 35,021 who do not have cardiovascular disease) and contains 11 features
(consisting of 4 demographic, 4 examination and 3 social history).

- Age (demographic) Height (demographic) Weight (demographic) Gender
- (demographic) Systolic blood pressure (examination) Diastolic blood pressure
- (examination) Cholesterol (examination) Glucose (examination) Smoking
- (social history) Alcohol intake (social history) Physical activity (social
- history)

The 11 features above can assist in helping us predict a cardiovascular event.

## Limitations in Dataset

Information given by the patient cannot be trusted, which is subjective,
listed below:

- Smoking
- Alcohol intake
- Physical activity

Difficult to take patients answers into account since they might not be
accurate due to bias. We all like to think that we do a little more exercise
than what we really report and individuals might be embarrassed to admit how
much they smoke and/or drink.

## Outline of project

#### Database
* Input raw dataset
* Perform EDA and identify outliers to
exclude
* Create BMI category from height and weight calculation
* Split dataset into a Medical and Behavior table
* Join tables to have a full table with all attributes

#### Analysis
* Pull data from database
* Create charts for visualization
* Push charts to Resources folder for access by other programs

#### Machine Learning
* Pull data from database
* Separate dataset into attributes and labels
* Split data into training and testing sets
* Run dataset through Random Forest model (finetune parameters with GridSearchCV)
* Enable model to take an input array from index.html and outputting a
prediction

#### Dashboard
* Use index.html to set up framework for the dashboard
* Pull images from the Resources folder to display on dashboard
* Create an interactive component where user fills out information and that information is
fed through ML model
* The model returns the outcome and displays it on the dashboard

![Flowchart of Outline](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/Group%202%20Cardiovascular%20Swimlane%20chart.png)

## Dashboard

![Dashboard](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/dashboard.png)

### Tools Used

#### Front End: - HTML, CSS, JS, Bootstrap #### Back End: - Flask App, Amazon
AWS (Host)

#### Interactive Elements - Added input fields and submit button to calculate
BMI - Added input fields and submit button to see if the user might have
cardiovascular disease or not

### GoogleSlides
Click [here](https://docs.google.com/presentation/d/1CLlYEob1KDY201-xxJQNkHgQrruSIw2wHYbGwUDNzWc/edit?usp=sharing)
to access the GoogleSlides presentation.

## Cardio Data Analysis

After exploring all the data visually and numerically we can observe multiple
trends. The goal in our analysis was first to reveal trends and understand the
distribution of the data by histogram of various parameters such as BMI,
cholesterol, age, blood pressure, habits, glucose against main predictor/label
(cardio event).

 **BMI** When we binned the BMI data, we observed that most of the population
in our data is overweight to obese BMI levels. Later in the data analysis we
see that BMI can indeed be a leading indicator, however, given the population
bias of the dataset we need to remember that this can be skewing our results.

![Chart 1 - BMI Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/static/BMI_Breakdown.png)

 **Age**

We looked at the age, and there is no data for age below 36, which may not be
the limiting factor given it's known that cardio risk increases with age.
However, if we are trying to predict cardio events for people at the younger
end of our dataset, e.g., 40 years old, we may be biasing the predictions by
those at the older end.

**Blood Pressure**

 When looking at the blood pressure records, 40K of the data points fall
 strictly into the normal range for AP high and AP Low (as defined dy the
 chart). 1/3 of that population had a cardio event(~14K). However, it's hard
 to reveal if blood pressure is a predictor based on that alone. When we look
 at data outside of normal ranges there is a high relationship between being
 outside of normal range and having a cardio event. It is inherently hard to
 bin into strict bounds because some people may have high upper but normal
 lower or vice versa. Therefore, We tested different bounds and observed
 consistent results, although we have a small population of people with low
 blood pressure.

 ![Chart 2 - Diastolic Blood Pressure Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/static/Diastolic_Blood_Pressure_Breakdown.png)

 ![Chart 3 - Systolic Blood Pressure Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/static/Systolic_Blood_Pressure_Breakdown.png)


**Cholesterol**

 Cholesterol 3 is a predictor, can be seen from box plot and data analysis.
 When we divided the data into people who had cardio and non cardio events and
 then further divide those samples into cholesterol levels we observed a
 higher percentage of cholesterol 2 & 3 in the cardio events.

 ![Chart 4 - Cholesterol Distribution](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/static/Cholesterol_Distribution.png)

 **Glucose**

 Didn't seem a reliable indicator from box plot as well as we observed the
 highest number of cases in glucose level 1 which healthy level.

 **Gender**

 We have more female entries, but proportionally the percentage of cardio
 events was evenly distributed between male and female.

 **Habits Analysis**

Looking at the habits such as smoking, our total population is ~67K and we
only have ~6K smokers which is about 9% and the US estimated is 15%(ref.:
CDC). The data analysis suggests there is 50/50 chance for cardio event based
on smoking habits. But there is a chance smokers are being under reported in
our population.

Similar trend is observed for alcohol habits, data suggests that 50/50 percent
chance alcohol contributes to cardio events. Our population is very low, out
of ~67K only ~3K reported they drank. In the 2018 National Institute of Health
(NIH) national survey on drug use and health only 55% reported they drank in
the past month. There is a high chance that drinkers are being under reported
in our population.

With exercise, we have almost ~50K records out of ~67K, however, Human Health
Services (HSS), US Government body, reported that only 1 in 3 adults receive
the recommended amount of physical activity each week. It's highly likely that
physical activity is or may be being over reported.

Based on the above, we have to question the reliability of the habits data in
our dataset, particularly if it is self-reported. We may need to potentially
consider excluding it for Machine Learning if our model does not score high.

## Preliminary Conclusions
BMI, Cholesterol and Blood Pressure are likely
going to be the main factors in predicting the cardio outcome successfully.

## Machine Learning

### Preprocessing

When creating a Machine Learning model data preprocessing is the next step in
marking the process. We cleaned up the data by removing the outliers in a few
of the categories. Finally, we separated the dataset into attributes and
labels by splitting all but the cardio column into attributes, leaving cardio
in the labels group.

### Feature engineering and selection

Fortunately, the data was already in a codified format, so encoding such as
OneHotEncoder wasn't needed to make the data usable in the machine learning
model. We then standardized the data using StandardScaler, to ensure that one
feature doesn't skew the data.

### Splitting, Training, and Testing Set

Train_test_split was used to split data into training and testing sets at the
default 75/25 split. This would allow us to have enough data to fit the model
and have a decent sized test set. We may change the setting to be an 80/20 but
that is still a consideration that can be made before the finalization of this
project.


### Model Selection: Benefits and Limitations

For our Cardiovascular project, we chose the random forest model in order to
obtain a higher level of accuracy and its ability to handle higher
dimensionality. Random forest is also less susceptible to outliers and is
indifferent to non-linear features. It also has a tendency to have low bias
and moderate variance.

Some of the limitations of random forest include potential for overfitting, a
moderate level of interpretability, and since this is a large dataset, a large
amount of memory is utilized.

### Training

##### GridSearchCV
Prior to fitting the model, we utilized GridSearch CV in order to find the
optimal parameter settings for Random Forest. After running a grid search for
n_estimators and max_features, the optimal parameter setting yielded were 250
for n_estimators and 2 for max_features.

##### PCA
We tried narrowing down our scaled data (with behavioral data) to
more than 4 principal components and the variance ratio suggested that the
first 4 components carry most information: 21% PCA1, 16% PCA2, 11% PCA3 and
10% PCA4. This, however, did led to a decrease in accuracy for our model (69.95%),
leading to the decision to cut out PCA from the final project.

##### No Scaler
We attempted the Random Forest without scaling the data but,
again, this did not impact the accuracy. We, as a team, decided to keep the
scaler in the model (70.46%).

##### Removal of behavioral data
Since the behavioral data seemed to be
suspicious, due to self-reporting, we decided to try the random forest model
without it. The accuracy ended up being 70.86%, which was the best result yielded.

##### Accuracy
We ended up using random forest, with 250 n_estimators and 2
max features, with standard scaling, but no PCA. We also did remove the
behavioral components and yieled an accuracy of 70.86%.


## Resources Used
- [Center for Disease Control: Heart Disease](https://www.cdc.gov/heartdisease/facts.htm)
- [Heart Disease: Facts, Statistics, and You](https://www.healthline.com/health/heart-disease/statistics)
- [Mayo Clinic - HeartDisease](https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118)

### Team Members: Enrique Bustamante, Sara St. Jean, Ali Merchant, Anna
### Shvilpe, Ricardo Vasquez, Victor Rodriguez IV
