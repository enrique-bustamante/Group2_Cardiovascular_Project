
**Random Forest with Classifier, without PCA**

Accuracy Score: 0.7086409544622291
Confusion Matrix
[[6167 2411]
 [2522 5831]]

  precision    recall  f1-score   support

           0       0.71      0.72      0.71      8578
           1       0.71      0.70      0.70      8353

    accuracy                           0.71     16931
   macro avg       0.71      0.71      0.71     16931
weighted avg       0.71      0.71      0.71     16931


**Random Forest with Classifier, with PCA**

We tried narrowing down our scaled data (with behavioral data) to more than 4 principal components and the variance ratio suggested that the first 4 components carry most information: 21% PCA1, 16% PCA2, 11% PCA3 and 10% PCA4.

>>>pca.explained_variance_ratio_
array([0.21066518, 0.16188511, 0.11218816, 0.10621535])

So our recommendation for PCA is to proceed with 4 n components.



