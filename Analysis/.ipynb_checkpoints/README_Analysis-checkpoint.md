{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Analysis Summary\n",
    "\n",
    "After exploring all the data visually and numerically we can observe multiple trends. The goal is our analysis was first to understand the distribution of the data by histogram of various parameters such as BMI, cholesterol, age, blood pressure, habits, glucose against main predictor/label (cardio event). \n",
    "\n",
    "**BMI**\n",
    "\n",
    "When we binned BMI data, we observed that most of the population in our data is overweight to obese BMI levels. Later in the data analysis we see that BMI can indeed be a leading indicator, however, given the population bias of the dataset we need to remember that this can be skewing our results.\n",
    "\n",
    "**Age**\n",
    "\n",
    "We looked at the age, and there is no data for age below 36, which may not be the limiting factor given it's known that cardio risk increases with age. However, if we are trying to predict cardio events for people at the younger end of our dataset, we may be biasing the predictions by those at the older end.\n",
    "\n",
    "**Blood Pressure**\n",
    "\n",
    "When looking at the blood pressure records, 40K of the data points fall strictly into the normal range for AP high and AP Low (as defined dy the chart). 1/3 of that population had a cardio event. However, it's hard to reveal if blood pressure is a predictor based on that alone. So when we look at data outsdie of normal ranges there is a high relationship between being outside of normal range and having a cardio event. It is inhertly hard to bin into strict bounds because some people may have high upper but normal lower or vice versa. We tested different bounds and observed consistent results, although we have a small population of people with low blood pressure.  \n",
    "\n",
    "**Cholesterol**\n",
    "\n",
    "Cholesterol 3 is a predictor, can be seen from box plot and data analysis. When we divided the data into people who had cardio and non cardio events and then further divide those samples into cholesterol levels we observed a higher percentage of cholesterol 2 & 3 in the cardio events.\n",
    "\n",
    "**Glucose**\n",
    "\n",
    "Didn't seem a reliable indicator from box plot as well as we observed the highest number of cases in glucose level 1 which healthy level. \n",
    "\n",
    "**Gender**\n",
    "\n",
    "We have more female entries, but proportionally the percentage of cadio events was evenly distributed between male and female. \n",
    "\n",
    "**Habits Analysis**\n",
    "\n",
    "Looking at the habits such as smoking, our total population is 67K and we only have 6K smokers which is about 9% and the US estimated is 15%(ref.: CDC). The data anlysis suggests there is 50/50 chance for cardio event based on smoking habits. But there is a chance smokers are being underreported in our population.\n",
    "\n",
    "Similar trend is observed for alcohol habits, data suggests that 50/50 percent chance alcohol contributes to cardio events. Our population is very low, out of 67K only 3K reported they drank. In the 2018 National Institute of Health (NIH) natinal survey on drug use and health only 55% reported they drank in the past month. There is a high chance that drinkers are being underreported in our population.\n",
    "\n",
    "With excercise, we have almost 50K records out of 67K, however, Human Health Services (HSS), US Government body, reported that only 1 in 3 adults receive the recommended amount of physical activity each week. It's highly likely that physical activity is being overreported. \n",
    "\n",
    "Based on the above, we have to question the reliability of the habits data in our dataset. We may need to potentially consider excluding it for Machine Learning if our model does not score high.\n",
    "\n",
    "---\n",
    "\n",
    "**Final thoughts** - BMI, Cholesterol and Blood Pressure are the main factors in predicting the cardio outcome successfully.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
