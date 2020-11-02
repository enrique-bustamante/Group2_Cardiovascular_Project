## Machine Learning

### Preprocessing

When creating a Machine Learning model data preprocessing is the next step in marking the process. We cleaned up the data by removing the outliers in a few of the categories. Finally, we separated the dataset into attributes and labels by splitting all but the cardio column into attributes, leaving cardio in the labels group.
   
### Feature engineering and selection

Fortunately, the data was already in a codified format, so encoding such as OneHotEncoder wasn't needed to make the data usable in the machine learning model. We then standardized the data using StandardScaler, to ensure that one feature doesn't skew the data.

# Splitting, Training, and Testing Set 

Train_test_split was used to split data into training and testing sets at the default 75/25 split. This would allow us to have enough data to fit the model and have a decent sized test set. We may change the setting to be an 80/20 but that is still a consideration that can be made before the finalization of this project.
  

# Explanation of model selections as well as benefits and limitations

For our Cardiovascular project, we chose the random forest model in order to obtain a higher level of accuracy and its ability to handle higher dimensionality. Random forest is also less susceptible to outliers and is indifferent to non-linear features. It also has a tendency to have low bias and moderate variance.      

Some of the limitations of random forest include potential for overfitting, a moderate level of interpretability, and since this is a large dataset, a large amount of memory is utilized.  
