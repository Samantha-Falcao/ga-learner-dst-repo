#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv('loan_data.csv')

#Code starts here

# Step 1

# Q] Company has more 'loan approvals' or 'loan disapprovals'?

#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind='bar')
plt.title('Loan Approval record of the company')
plt.xlabel('Loan approved: Yes(Y) or No(N)')
plt.ylabel('Count')
plt.show()

print("OBSERVATIONS: \n From the above bar chart, it can be clearly seen that the company has more loan approvals than disapprovals. This could be one of the company's health factors.")
print()
print('='*100)

# Step 2

# Q] Which is the region with the highest no. of loan approvals? lowest no. of loan approvals?
# Q] Which is the region with the maximum difference between loan approvals and loan rejections?

property_and_loan = data.groupby(by=['Property_Area', 'Loan_Status']).size().unstack()

#Plotting an unstacked bar plot
property_and_loan.plot(kind='bar', stacked=False)

#setting the title
plt.title('Loan Approval Distribution across regions')

#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

plt.show()

print("OBSERVATIONS: \n Some noticeable conclusions from the above unstacked bar chart are that Semi-Urban region has the highest number of loan approvals and Rural region has the lowest number of approved loans. Also, Semi Urban region has the lowest loan disapprovals count and also has the maximum difference between loan approvals and loan rejections amongst all three regions.")
print()
print('='*100)
# Step 3

# Q] Does higher education result in a better guarantee in issuing loans?

education_and_loan = data.groupby(by=['Education', 'Loan_Status']).size().unstack()

#Plotting a stacked bar plot
education_and_loan.plot(kind='bar', stacked=True)

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

plt.title('Loan Approval based upon Education')
plt.show()
print("OBSERVATIONS: \n Irrespective of the loan approvals or rejections, the group of Graduates form a majority amongst the applicants for housing loan. Loan Approvals is much higher than rejections for the group of Graduates, whereas looking at the chart we can say that there isn't a vast difference betweenthe number of approvals and rejections of loan for the Non-Graduates group.")
print()
print('='*100)

# Step 4

# Q] Check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values.

#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', color='red', label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density', color='green', label='Not Graduate')

plt.xlabel('Loan Amount')
#For automatic legend display
plt.title('Loan Amount Distribution based upon Education status')
plt.legend()
plt.show()

print("OBSERVATIONS: \n The average loan amount approved for both Graduates and Non Graduates is almost same")
print()
print('='*100)

# Step 5
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1)

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])

#Setting the subplot axis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])

#Setting the subplot axis title
ax_2.set_title('Co-applicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'], data['LoanAmount'])

#Setting the subplot axis title
ax_3.set_title('Total Income')
plt.tight_layout()
plt.show()

print('OBSERVATIONS: \n There is some positive correlation between the income and the loan amounts of the applicants. Also, Total amount gives a better relation with Loan amount than applicant and coapplicants income')
print()
print('='*100)

#code ends here