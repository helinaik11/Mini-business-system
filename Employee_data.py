#ACCESS THE EMPLOYEE DATA PART OF THE SYSTEM
import pandas as pd
d={'EMP NAME':['Ms. A.R. Swaminathan','Ms. Kuldeep Singh','Mr. Jignesh Bhatt',
               'Mr. Krushiv Chanu','Ms. Rochel Perez','Mr. George Smith',
               'Ms Chiyoko Nohara','Mr Hong Ji Hong'],'COUNTRY':['India(South)',
                'India(North)','India(West)','India(East)','Spain','USA',
                'Japan','Korea'],'Salary(in INR)':[7000000,6500000,6600000,
                6700000,7000000,7500000,8000000,8000000],'Experience(in years)':
                [20,17,18,19,20,25,30,30]}
df=pd.DataFrame(d,index=['E01','E02','E03','E04','E05','E06','E07','E08'])
df.index.name='EMPNO'
print('BELOW IS THE DATAFRAME OF THE HEAD-DEPARTMENT OF TECHZILLION INC. ')
print(df)
print('TO ADD DATA INTO THE GIVEN DATAFRAME,ENTER 1')
a=int(input('ENTER YOUR NUMBER:'))
if a==1:
    empno=input('EMPLOYEE NUMBER:')
    empname=input('EMPLOYEE NAME:')
    country=input('COUNTRY HEADED BY THE EMPLOYEE:')
    sal=input('SALARY EARNED BY THE EMPLOYEE PER ANNUM IN INR:')
    exp=input('EXPERIENCE OF THE EMPLOYEE IN YEARS:')
    df.loc[empno,:]=[empname,country,sal,exp]
else:
    print('Thank you!')
