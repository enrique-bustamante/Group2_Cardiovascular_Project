# Cardiovascular Disease Project

## Overview
Heart disease is the leading cause of death for both men and women, and people of most racial and ethnic groups in the US. About 665,000 individuals die from heart disease each year in the US - 1 in every 4 deaths. It is also the most preventable.  Our group is reviewing a dataset that looks at patient data (age, weight, gender, smoking, activity level, etc) and the prevalence of cardiovascular disease. We're going to analyze which factors might contribute more heavily to the disease and shed light on a condition that can be preventable by taking a proactive approach to our lifestyle.

How can we improve our daily activities to prevent Cardiovascular disease? In this dataset we're given medical records with key health factors including if someone had a cardiovascular event.

Using medically examined data we aim to answer the following questions:
- What group of factors have the largest impact on a Cardiovascular event?
- From the 5-7 factors, can we narrow it down with PCA?
- Can we create a model that would predict a Cardiovascular event?

## Resources
The cardiovascular disease dataset is an open-source [dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset) that is found on Kaggle.

## Database

## Dataset

The dataset contains 70,000 records (34,979 who have cardiovascular disease and 35,021 who do not have cardiovascular disease) and contains 11 features (consisting of 4 demographic, 4 examination and 3 social history).

- Age (demographic)
- Height (demographic)
- Weight (demographic)
- Gender (demographic)
- Systolic blood pressure (examination)
- Diastolic blood pressure (examination)
- Cholesterol (examination)
- Glucose (examination)
- Smoking (social history)
- Alcohol intake (social history)
- Physical activity (social history)

The 11 features above determine

## Limitations in Dataset

## Dashboard

- screenshot of dashboard here

### Tools Used

#### Front End:
- HTML, CSS, JS, Bootstrap
### Back End:
- Flask App, Heroku (Host)

### Interactive Elements

### GoogleSlides
Click [here](https://docs.google.com/presentation/d/1CLlYEob1KDY201-xxJQNkHgQrruSIw2wHYbGwUDNzWc/edit?usp=sharing) to access the GoogleSlides presentation.

## Communication Protocols

This set of rules will help unify our code and prevent issues.
* Before working on your portion it is best to pull in from the remote repository. To do so use "git pull origin main".
* When your push your commits, please either create a pull request and leave a message in the Group2 slack channel so that the git handler can merge the push with the main.
* When committing, please leave a comment to says what was either added or changed on the code and to which file. This will help when merging.
* When naming your variables, it would be preferable to use camel case (e.g. fileDatabaseCleaned) and have the name be more specific to the action taken and to the data it is taken on.
* ABC: Always be committing
* Please add comments on your scripts, particularly your pseudocode. While good code shouldn't need that many comments, it should include comments to guide the reader.
* As git handler, I will keep an eye on how many commits a group member's branch is behind the main. If it is a large amount, I'll reach out to the owner of the branch to pull and update from the main branch.
* When creating a new branch, use the following format: <Username> Segment <Segment number>

## Resources Used
- [Center for Disease Control: Heart Disease Facts](https://www.cdc.gov/heartdisease/facts.htm)
- [Heart Disease: Facts, Statistics, and You](https://www.healthline.com/health/heart-disease/statistics)

### Team Members: Enrique Bustamante, Sara St. Jean, Ali Merchant, Anna Shvilpe, Ricardo Vasquez, Victor Rodriguez IV

## Cardio Data Analysis

After exploring all the data visually and numerically we can observe multiple trends. The goal in our analysis was first to reveal trends and understand the distribution of the data by histogram of various parameters such as BMI, cholesterol, age, blood pressure, habits, glucose against main predictor/label (cardio event).

 **BMI**
When we binned the BMI data, we observed that most of the population in our data is overweight to obese BMI levels. Later in the data analysis we see that BMI can indeed be a leading indicator, however, given the population bias of the dataset we need to remember that this can be skewing our results.

![Chart 1 - BMI Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/BMI_Breakdown.png)

 **Age**
We looked at the age, and there is no data for age below 36, which may not be the limiting factor given it's known that cardio risk increases with age. However, if we are trying to predict cardio events for people at the younger end of our dataset, e.g., 40 years old, we may be biasing the predictions by those at the older end.

**Blood Pressure**
 When looking at the blood pressure records, 40K of the data points fall strictly into the normal range for AP high and AP Low (as defined dy the chart). 1/3 of that population had a cardio event(~14K). However, it's hard to reveal if blood pressure is a predictor based on that alone. When we look at data outsdie of normal ranges there is a high relationship between being outside of normal range and having a cardio event. It is inhertly hard to bin into strict bounds because some people may have high upper but normal lower or vice versa. Therefore, We tested different bounds and observed consistent results, although we have a small population of people with low blood pressure.

 ![Chart 2 - Diastolic Blood Pressure Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/Diastolic_Blood_Pressure_Breakdown.png)

 ![Chart 3 - Systolic Blood Pressure Breakdown](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/Systolic_Blood_Pressure_Breakdown.png)


**Cholesterol**

 Cholesterol 3 is a predictor, can be seen from box plot and data analysis. When we divided the data into people who had cardio and non cardio events and then further divide those samples into cholesterol levels we observed a higher percentage of cholesterol 2 & 3 in the cardio events.

 ![Chart 4 - Cholesterol Distribution](https://github.com/enrique-bustamante/Group2_Cardiovascular_Project/blob/main/Resources/Cholesterol_Distribution.png)

 **Glucose**
 Didn't seem a reliable indicator from box plot as well as we observed the highest number of cases in glucose level 1 which healthy level.

 **Gender**

 We have more female entries, but proportionally the percentage of cadio events was evenly distributed between male and female.

 **Habits Analysis**

Looking at the habits such as smoking, our total population is ~67K and we only have ~6K smokers which is about 9% and the US estimated is 15%(ref.: CDC). The data analysis suggests there is 50/50 chance for cardio event based on smoking habits. But there is a chance smokers are being underreported in our population.

Similar trend is observed for alcohol habits, data suggests that 50/50 percent chance alcohol contributes to cardio events. Our population is very low, out of ~67K only ~3K reported they drank. In the 2018 National Institute of Health (NIH) national survey on drug use and health only 55% reported they drank in the past month. There is a high chance that drinkers are being underreported in our population.

With excercise, we have almost ~50K records out of ~67K, however, Human Health Services (HSS), US Government body, reported that only 1 in 3 adults receive the recommended amount of physical activity each week. It's highly likely that physical activity is or may be being overreported.

Based on the above, we have to question the reliability of the habits data in our dataset, particulraly if it is self-reported. We may need to potentially consider excluding it for Machine Learning if our model does not score high.

## Preliminary Conclusions
BMI, Cholesterol and Blood Pressure are likely going to be the main factors in predicting the cardio outcome successfully.


