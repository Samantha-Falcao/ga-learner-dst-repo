# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt('census_data.csv', delimiter=",", skip_header=1)

#concatenating new record to data
census = np.concatenate((data, np.array(new_record, dtype="float64")))
print(census.shape)

# obtaining age data from census using index of age column
age = census[:,0]

# analysing the age distribution
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)

print("Minimum age of the population is: ", min_age)
print("Maximum age of the population is: ", max_age)
print("Mean age and standard deviation in age of the population are: ", age_mean, "and", age_std)

print("-"*30)

# filtering data based upon race
race_0 = census[census[:,2]==0][:,2]
race_1 = census[census[:,2]==1][:,2]
race_2 = census[census[:,2]==2][:,2]
race_3 = census[census[:,2]==3][:,2]
race_4 = census[census[:,2]==4][:,2]

# analysing the race distribution of the country's data
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = np.argmin([len_0, len_1, len_2, len_3, len_4])
print("Minority race is ", minority_race)

print("-"*30)

# obtaining data for senior citizens of the country
senior_citizens = census[age>60]

# analysing data for senior citizens

# obtaining the average working hours for senior citizens
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print("Average working hours for senior citizens: ", avg_working_hours)

print("-"*30)

# analysing the education and pay scale of the population

# filtering the data based upon level of education
education_num = census[:,1]
high = census[education_num > 10]
low = census[education_num <= 10]

# finding the average income based upon education levels
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print("% of people with education higher than 10 and income higher than 50K: ", avg_pay_high)
print("% of people with education lower than or equal to 10 and income higher than 50K: ", avg_pay_low)






