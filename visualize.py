# Execute bash command to allow for creation of visualization files via Tkinter and Xming on Windows.
import os 
os.system("export DISPLAY=localhost:0.0");
import pandas as pd
import scipy
import matplotlib as p
p.use("TkAgg");
import matplotlib.pyplot as plt
#Read in csv file for calculations.
df_train = pd.read_csv("./train.csv");
fig = plt.figure(figsize=(18,6))
#Bar graph of percentage of who survived and who did not.
plt.subplot2grid((2,3), (0,0))
df_train.Survived.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("% of Survived and Deceased")
# Comput averages for age by all passengers, all men, all women respectively. 
df_avg_age = df_train.Age.mean();
men_avgage = df_train.loc[df_train.Sex == 'male', 'Age'].mean();
fem_avgage = df_train.loc[df_train.Sex == 'female', 'Age'].mean();
# Values for bar chart.
#plt.subplot2grid((2,3), (0,1)
x_values = ["All", "Men", "Women"];
age_values = [df_avg_age, men_avgage, fem_avgage];
# Generate bar graph. Set block to true when executing from script file. 
plt.subplot2grid((2,3), (0,1))
plt.bar(x_values,age_values,width=0.5)
plt.title("Average Age by Gender")
#Scatter plot by age and survial
plt.subplot2grid((2,3), (0,2))
plt.scatter(df_train.Survived, df_train.Age, alpha=.1) 
plt.title("Scatter by age & survival")
# Survival count by Class
plt.subplot2grid((2,3),(1,0))
df_train.Pclass.value_counts().plot(kind="Bar", alpha=1)
plt.title("Passenger Count by Class")
# Plot survival with regards to age & class. 
plt.subplot2grid((2,3), (1,1), colspan=2)
for x in [1,2,3]:
	df_train.Age[df_train.Pclass == x].plot(kind="kde")
plt.title("Survived in relation to Age & Class")
plt.legend(("1st", "2nd", "3rd")) 


#plt.show(block=True)

plt.show()


