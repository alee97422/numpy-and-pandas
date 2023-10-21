import pandas as pd

# Creating a dataframe for the first set of bank clients
bank_df_1 = pd.DataFrame({
    'Bank Client ID': ['1', '2', '3', '4', '5'],
    'First Name': ['Nancy', 'Alex', 'Shep', 'Max', 'Allen'], 
    'Last Name': ['Rob', 'Ali', 'George', 'Mitch', 'Steve']
})

# Creating a dataframe for the second set of bank clients
bank_df_2 = pd.DataFrame({
    'Bank Client ID': ['6', '7', '8', '9', '10'],
    'First Name': ['Bill', 'Dina', 'Sarah', 'Heather', 'Holly'], 
    'Last Name': ['Christian', 'Mo', 'Steve', 'Bob', 'Michelle']
})

# Creating a dataframe for all bank clients' annual salary information
bank_df_salary = pd.DataFrame({
    'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    'Annual Salary [$/year]': [25000, 35000, 45000, 48000, 49000, 32000, 33000, 34000, 23000, 22000]
})

# Merging all dataframes based on 'Bank Client ID'
bank_df_all = pd.merge(pd.concat([bank_df_1, bank_df_2]), bank_df_salary, on='Bank Client ID')

#print statement for before and after to test functionality of new method
print(bank_df_all)

# Adding a new bank client to the dataframe
new_client_df = pd.DataFrame({
    'Bank Client ID': ['11'],
    'First Name': ['Ry'], 
    'Last Name': ['Aly'],
    'Annual Salary [$/year]' : [1000]
})

#The original coursera course had used the commented out depreciated append method
#but since this course was made it has been proven to be better to use the concat method 
# which I have demontrated below

#Old depriciated method

## Appending the new client to the existing dataframe
#new_df = bank_df_all.append(new_client_df, ignore_index=True)

#new method
new_df = pd.concat([new_client_df, bank_df_all])

#print statement to test 
print(new_df)
print("Dataframe: Updated!")