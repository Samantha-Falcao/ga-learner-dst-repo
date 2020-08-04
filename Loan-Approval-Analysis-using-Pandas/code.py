# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv('loan_data.csv')


# Checking all categorical attributes
categorical_var = bank_data.select_dtypes(include='object')
print("Categorical Variables:")
print(categorical_var.head())

print('='*60)

# Checking all numerical attributes
numerical_var = bank_data.select_dtypes(include='number')
print("Numerical Variables:")
print(numerical_var.head())

print('='*60)

# Dropping the Loan_ID column since it is just an identification number and is unique for all entries
banks = bank_data.drop('Loan_ID', axis=1)

# Are there any missing values in the dataframe?
null = banks.isnull().sum()
print("Missing values:")
print(null)

print('='*60)

# Filling the missing values using mode of each variable
bank_mode = banks.mode()
print('Mode of each variable:')
print(bank_mode.iloc[0])

print('='*60)

banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())
print('Missing values have been imputed using mode of each variable.')

print('='*60)

# average loan amount of a person
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values=['LoanAmount'])
print('Average loan amount based upon Gender, Martial Status, and Self employment:')
print(avg_loan_amount)

print('='*60)

# finding the percentage of loan approved based on a person's employment type

# number of loans approved for self employed people
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')]['Loan_Status'].count()

# number of loans approved for non self employed people
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status']== 'Y')]['Loan_Status'].count()

# total number of loans approved
loan_status_count = banks['Loan_Status'].count()

# percentage
percentage_se = (loan_approved_se/loan_status_count)*100
print("% of loan approved for self employed people: ",percentage_se)
percentage_nse = (loan_approved_nse/loan_status_count)*100
print("% of loan approved for non self employed people: ",percentage_nse)

print('='*60)

# finding applicants with long loan amount term

# converting term from months to years
banks['loan_term'] = banks['Loan_Amount_Term'].apply(lambda x: x/12)

# applicants having loan amount term greater than or equal to 25 years
big_loan_term = banks[banks['loan_term']>=25]['loan_term'].count()
print("Applicants having loan amount term greater than or equal to 25 years: ", big_loan_term)

print('='*60)

# checking the average income of an applicant and average loan given based upon their income

loan_groupby = banks.groupby(['Loan_Status'])[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
print("The average income of an applicant and average loan given based upon their income:")
print(mean_values)

# task ends here


