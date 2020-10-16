# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
cardioDf = pd.read_csv('Resources/cardio_train.csv', sep=';')
# %%
cardioDf['age'] = cardioDf['age']/365.25
# %%
cardioDf['bmi'] = cardioDf['weight']/(cardioDf['height']/100)**2
# %%
cardioDf['bmi'].plot.density()
# %%
cardioDf['age'].plot.hist()
# %%
cardioDfCardioPositive = cardioDf[cardioDf['cardio'] == 1]
# %%
cardioDfCardioPositive['age'].plot.hist()
# %%
plt.boxplot(x=cardioDf['bmi'])
# %%
cardioDf['bmi'].plot.hist()
cardioDf['bmi'].describe()
# %%
cardioDf['height'].describe()
# %%

plt.boxplot(cardioDf['weight'])
# %%
plt.boxplot(cardioDf['ap_hi'])
# %%
plt.boxplot(cardioDf['ap_lo'])
# %%
cardioDf['ap_hi'].hist()
# %%
cardioDf['ap_lo'].hist()
# %%
