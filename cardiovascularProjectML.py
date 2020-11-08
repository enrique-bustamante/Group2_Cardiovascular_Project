# %%

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

# %%
#export all reqiurements into requirements.txt for replicating the env for other users
#pip freeze > requirements.txt (pip freeze will show all the dependancies currently used, the > take output and puts it into a file)
#pip install -r requirements.txt (will install requirements for other users)
#I had to run psycopg2 installation again '%pip install psycopg2-binary
# Set up the database connection
#Setting up if statement to switch from local host to Heroku environmentSetting = 'dev'
#if environmentSetting = 'dev':\n",
    
#databaseString = f\"postgres://postgres:{postgreSQLKey}@localhost:5432/CardioDatabase
#else:\n",
#databaseString = \"\" #placeholder for now
# Set up the database connection
# Setting up if statement to switch from local host to Heroku environmentSetting = 'dev'
    
#if environmentSetting = 'dev':  databaseString = f\"postgres://postgres:{password}@localhost:5432/CardioDatabase\"else:databaseString = \"\" #placeholder for now 37b57e9c5305e3b74cd06ed5958ec62afd8096f0 databaseEngine = create_engine(databaseString) databaseConnection = databaseEngine.connect()
    

# %%
# Load the CSV
cardio_df = pd.read_csv('cardio_train.csv',con=databaseConnection, index_col='id')
cardioDf.head(20)

# %%
