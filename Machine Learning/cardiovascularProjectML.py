#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from config import password, passwordAWS
import pickle
from sklearn.metrics import plot_confusion_matrix


# In[2]:
environmentSetting = 'production'

# Starting database engine.
databaseString = f"postgres://postgres:{password}@localhost:5432/CardioDatabase"
databaseStringAWS = f"postgres://postgres:{passwordAWS}@group2cardio.cl2wtm3wzyhx.us-east-2.rds.amazonaws.com"

# %%
if environmentSetting == 'dev':
        databaseEngine = create_engine(databaseString)
else:
        databaseEngine = create_engine(databaseStringAWS)

databaseConnection = databaseEngine.connect()


# In[3]:


# Load the CSV
cardioDf = pd.read_sql('cardio_combined', con=databaseConnection, index_col='id')
cardioDf.head(20)


# In[4]:


cardioDf = cardioDf.astype('int64')
cardioDf.dtypes


# In[5]:


cardioDf = cardioDf.drop(['smoke', 'alco', 'active', 'weight', 'height'], axis=1)
cardioDf.head(10)


# In[6]:


# Scale data
scaler = StandardScaler()
cardioAttributes = cardioDf.drop('cardio', axis=1)
cardioLabels = cardioDf['cardio']
cardioAttributesScaled = scaler.fit_transform(cardioAttributes)
print(cardioAttributesScaled)


# In[7]:


# Split training/test datasets
trainingCardioAttributes, testingCardioAttributes, trainingCardioLabels, testingCardioLabels = train_test_split(cardioAttributesScaled, cardioLabels, random_state=78)


# In[8]:


# Create a random forest classifier.
rfModel = RandomForestClassifier(n_estimators=250, random_state=2, max_features=2)


# In[9]:


# Fitting the model
rfModel = rfModel.fit(trainingCardioAttributes, trainingCardioLabels)


# In[10]:


# Evaluate the model
cardioLabelPredictions = rfModel.predict(testingCardioAttributes)


# In[11]:


accuracy_score(testingCardioLabels, cardioLabelPredictions)


# In[12]:


print(f"Accuracy Score: {accuracy_score(testingCardioLabels, cardioLabelPredictions)}")


# In[13]:


matrix = confusion_matrix(testingCardioLabels, cardioLabelPredictions)
print(matrix)


# In[14]:


report = classification_report(testingCardioLabels, cardioLabelPredictions)
print(report)


# In[17]:


# Plot non-normalized confusion matrix
titles_options = [ ("Normalized confusion matrix", 'true'),
           ("Confusion matrix, without normalization", None)]
for title, normalize in titles_options:
        disp = plot_confusion_matrix(rfModel, testingCardioAttributes, testingCardioLabels,
                                display_labels=cardioLabels,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
        disp.ax_.set_title(title)
        #plt.savefig('../Resources/confusion_matrix.png')
print(title)
print(disp.confusion_matrix)
plt.show()


# In[ ]:
#inputArray = pd.Series([61, 1, 157, 93, 130, 80, 3, 1, 38.0])
#inputArrayScaled = scaler.transform(inputArray.values.reshape(1,9))


# %%
#outputValue = rfModel.predict(inputArrayScaled)
#outputValue[0]


# %%
pickle.dump(rfModel, open('cardioPrediction.pkl','wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
cardioPrediction = pickle.load(open('cardioPrediction.pkl','rb'))