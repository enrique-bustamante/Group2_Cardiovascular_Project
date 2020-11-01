# Preprocessing

- When creating a Machine Learning model data preprocessing is the next step in marking the process.  In the real world data is incomplete, inaccurate, and inconsistent.  Data preprocessing helps to clean, organize, and format the raw data to make it ready for Machine Learning models.  In our project the attributes were scaled and labels were separated.  
- In our Cardiovascular project Jupyter is being utilize to create the Machine Learning models.  We imported all the crucial libraries that were needed for our Cardiovascular project.  The libraries are the following: sqlalchemy import create_engine, MetaData, Table, import pandas as pd, import numpy as np, import psycopg2, from config import password, import matplotlib.pyplot as plt, and from scipy.stats import linregress.  
- It is necessary to separate the independent variables and dependent variables in a dataset for every Machine Learning model.  
   
# Feature engineering and selection

- Process for creating features and mapping from raw data to Machine Learning is feature engineering.  This is what we have done in our Cardiovascular project is that we have transformed the raw data and created a Machine Learning model to show the results.  By doing so we utilized Grid Search CV in our project for our results.     
- Machine Learning functions on a plain rule, if you place garbage in you will only get garbage to come out.  By using the word garbage, I mean noise in data.  

- Here are some of the top reasons to utilize feature selection as follows:

1. It improves the accuracy of a model if the right subset is chose.
2. It enables the machine learning algorithm to train faster.
3. It reduces overfitting.
4. It reduces the complexity of a model and makes it easier to interpret.   

# Splitting, Training, and Testing Set 

- The problem of appropriate data splitting can be handled as a statistical sampling problem.  Various classical statistical sampling techniques can be employed to split the data.
- Train-test-split was used to split data into training and testing sets at the default 75/25 split.  
- These sampling methods can be divided into the following categories based on their principles, goals and algorithmic and computational complexity:

1. Simple random sampling (SRS),
2. Trial-and-error methods,
3. Systematic sampling,
4. Convenience sampling,
5. Stratified sampling.

- Training data is the dataset used to train the algorithm or model so it can accurately predict our outcome of our Cardiovascular project data.  Training data trains an algorithm to recognize patterns in our dataset.
- Test data is used to measure the accuracy and efficiency of our measurements of our Cardiovascular data, to detect how well it can predict the answers we are trying to compare based on its training.  

# Explanation of model selections as well as benefits and limitations

- Model selection is the procedure of choosing one of the models as the final model that will address the problem, in this case the advantages and disadvantages of our Cardiovascular results.
- The benefits of model selection is a measure that can be utilize across different types of models.
- In our Cardiovascular project we chose the random forest model due to obtaining a higher accuracy and valuable interpretability.      
- Some of the limitations of model selection is that many predictors with many possible interactions, can make it difficult to search for the best model.  