import os 
# Bash command to set localhost server to visualize data in XLaunch
os.system("export DISPLAY=localhost:0.0");
import pandas as pd
import scipy
import matplotlib as p
p.use("TkAgg");
import matplotlib.pyplot as plt

#Read in csv file for calculations.
df_train = pd.read_csv("./train.csv");
fig = plt.figure(figsize=(24,8))

#Bar graph of percentage of who survived and who did not.
plt.subplot2grid((3,3), (0,0))
df_train.Sex[df_train.Survived == 1].value_counts(normalize=True).plot(kind="bar", rot=0,alpha=0.5,color=["pink","blue"])
plt.title("% of Survived wrt Sex")

# Comput averages for age by all passengers, all men, all women respectively. 
df_avg_age = df_train.Age.mean();
men_avgage = df_train.loc[df_train.Sex == 'male', 'Age'].mean();
fem_avgage = df_train.loc[df_train.Sex == 'female', 'Age'].mean();

# Values for bar chart.
#plt.subplot2grid((3,3), (0,1)

# Generate bar graph. Set block to true when executing from script file. 
plt.subplot2grid((3,3), (0,1))
x_values = ["All", "Men", "Women"];
age_values = [df_avg_age, men_avgage, fem_avgage];
plt.bar(x_values,age_values,width=0.5, color=["black", "blue", "pink"])
plt.title("Average Age by Gender")

#Scatter plot by age and survial
plt.subplot2grid((3,3), (0,2))
plt.scatter(df_train.Survived, df_train.Age, alpha=.1) 
plt.title("Scatter by age & survival")

# Survival count by Class
plt.subplot2grid((3,3),(1,0))
df_train.Pclass.value_counts().plot(kind="Bar", alpha=1, color = ["green","blue","orange"])
plt.title("Passenger Count by Class")

# Plot survival with regards to age & class. 
plt.subplot2grid((3,3), (2,0), colspan=4)
for x in [1,2,3]:
	df_train.Survived[df_train.Pclass == x].plot(kind="kde")
plt.title("Survived in relation to Class")
plt.legend(("1st", "2nd", "3rd")) 

# Plot survival rate wrt to Class
plt.subplot2grid((3,3),(1,1))
df_train.Pclass[df_train.Survived == 1].value_counts(normalize=True).plot(kind='bar',alpha=1, color = ['blue','green','orange'])
plt.title("Surival Rate wrt Class")

# Plot mortality rate wrt to Class
plt.subplot2grid((3,3),(1,2))
df_train.Pclass[df_train.Survived == 0].value_counts(normalize=True).plot(kind='bar',alpha=1, color = ['green','orange','blue'])
plt.title("Mortality Rate wrt Class")



plt.show(block=True)



