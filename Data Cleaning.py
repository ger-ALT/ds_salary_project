# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#salary parsing  -- Done
#company name seperate from rating
# City seperated from state
#Job description pull info like Python required..etc


import pandas as pd

df = pd.read_csv('C:/Users/Harpreet.Singh/OneDrive - insidemedia.net/Documents/GitHub/Projects/ds_salary_project/glassdoor_jobs.csv')

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])

minus_Kd = salary.apply(lambda x : x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


min_hr = minus_Kd.apply(lambda x : x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

df['Company_text'] = df.apply(lambda x : x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3],axis=1 )
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['same_state'] =  df.apply(lambda x: 1 if x.Location==x.Headquarters else 0,axis=1)
df['company age'] = df.Founded.apply(lambda x: x if x<1 else 2020-x)

df['Job Description'][0]


df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df['python_yn'].value_counts()
df['R_yn'].value_counts()
df['spark_yn'].value_counts()
df['aws_yn'].value_counts()
df['excel_yn'].value_counts()


df.columns

df = df.drop(['Unnamed: 0'],axis=1)

df.to_csv('Salary_Data_cleaned.csv',index=False)



 