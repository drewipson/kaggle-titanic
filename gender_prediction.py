# Script to predict survival rate based off of gender alone.

import pandas as pd

df_train = pd.read_csv('train.csv')

# Create columns to set Hypothesis and Results to make accurate guesses. I will compare these at the end to determine accuracy.
df_train["Hyp"] = 0;
df_train["Result"] = 0;

# Based off analysis of data, we can accurately determine and guess that if you meet the following demographics you most likely surived: you are a female, and you were located in an upper class area.
df_train.loc[df_train.Sex == 'female', "Hyp"] = 1;
# Set the results according to our accuracy. If surived and hyp are both true, set results equal to 1.
df_train.loc[df_train.Survived == df_train.Hyp, "Result"] = 1
# Print predictions in form of percentages to determine how accurate. 
gender_pred = df_train.Result.value_counts(normalize=True)
print(gender_pred)

# Predict 78 percent accuracy.




