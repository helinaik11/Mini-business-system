#THIS FILE CONTAINS ALL THE OTHER FILES IN THE REPOSITORY (CONSOLIDATED VERSION)
import pandas as pd
import matplotlib.pyplot as py
u='TECHZILLION INC.'
p='aahr'
print('TO ACCESS THE REQUIRED INFORMATION OF TECHZILLION INC.ENTER USERNAME AND PASSWORD')
x=input('USERNAME:')
y=input('PASSWORD:')
if x==u and y==p:
    print('WELCOME TO THE OFFICIAL SYSTEM OF TECHZILLION INC.')
    print('TO GET INFORMATION ABOUT THE BALANCESHEET OF THE COMPANY,PRESS B')
    print('TO GET INFORMATION ABOUT THE STOCKS OF THE COMPANY,PRESS S')
    print('TO GET INFORMATION ABOUT THE HEAD EMPLOYEES OF THE COMPANY,PRESS E')
    print('TO GET INFORMATION ABOUT THE VALUATION OF THE COMPANY,PRESS V')
    z=input('ENTER THE ALPHABET:')
    if z=='B':
        curas=pd.Series({'CASH':2000000,'ACCOUNTS RECEIVABLE':500000,'INVENTORY':20000000,
                  'PREPAID RENT':1000000})
        longas=pd.Series({'LAND':250000000,'BUILDINGS AND IMPROVEMENTS':600000000,
                  'FURNITURE AND FIXTURES':3500000,'GENERAL EQUIPMENTS':220000000})
        curlia=pd.Series({'ACCOUNTS PAYABLE':200000000,"TAXES PAYABLE":100000000,
                  'WAGES PAYABLE':100000000,'INTEREST PAYABLE':50000000})
        longlia=pd.Series({'LOAN1':50000000,'LOAN2':50000000,'LOAN3':7000000})
        owneq=pd.Series({'PAID IN CAPITAL':200000000,'RETAINED EARNINGS':340000000})
        s='BALANCE SHEET'
        t='TECHZILLION INC.'
        d="04-04-2021"
        print('YOU CAN ACCESS THE ELEMENTS OF THE BALANCE SHEET OF TECHZILLION INC. HERE.')
        print("TO SEE THE WHOLE BALANCE SHEET,ENTER 1.")
        print('TO SEE THE CURRENT ASSETS,ENTER 2.')
        print('TO SEE THE LONG-TERM ASSETS,ENTER 3.')
        print('TO SEE THE CURRENT LIABILITIES,ENTER 4.')
        print('TO SEE THE LONG-TERM LIABILITIES,ENTER 5.')
        print("TO SEE THE OWNER'S EQUITY,ENTER 6.")
        x=int(input('ENTER A NUMBER FROM 1-6:'))
        if x==1:
            print(t.center(40))
            print(s.center(40))
            print(d.center(40))
            print('ASSETS')
            print('Current Assets:')
            print(curas)
            print("Total Current Assets:- INR",curas.sum())
            print('Long-Term Assets:')
            print(longas)
            print("Total Long-Term Assets:- INR",longas.sum())
            print('TOTAL ASSETS= INR',curas.sum()+longas.sum())
            print('LIABILITIES')
            print('Current Liabilities:')
            print(curlia)
            print("Total Current Liabilities:- INR",curlia.sum())
            print('Long-Term Liabilities:')
            print(longlia)
            print("Total Long-Term Liabilities:- INR",longlia.sum())
            print('TOTAL LIABILITIES=INR',curlia.sum()+longlia.sum())  
            print("OWNER'S EQUITY")
            print(owneq)
            print("Total Owner's Equity:- INR",owneq.sum())
            print("TOTAL LIABILITIES AND OWNER'S EQUITY=INR",curlia.sum()+longlia.sum()+owneq.sum())
        if x==2:
            print('Current Assets:')
            print(curas)
            print("Total Current Assets:- INR",curas.sum())
        if x==3:
            print('Long-Term Assets:')
            print(longas)
            print("Total Long-Term Assets:- INR",longas.sum())
        if x==4:
            print('Current Liabilities:')
            print(curlia)
            print("Total Current Liabilities:- INR",curlia.sum())
        if x==5:
            print('Long-Term Liabilities:')
            print(longlia)
            print("Total Long-Term Liabilities:- INR",longlia.sum())
        if x==6:
            print("OWNER'S EQUITY")
            print(owneq)
            print("Total Owner's Equity:- INR",owneq.sum())
    if z=='S':
        st={'2019-06-08':1500,'2019-07-09':1460 ,'2019-10-08':1510,
            '2019-11-01':1570.8,'2019-11-20':1550.8,'2019-12-10':1590.77,
            '2020-01-01':1670.99,'2020-01-31':1660.87,'2020-02-10':1690.87,
            '2020-03-10':1680.87,'2020-07-18':1690.8,'2020-10-19':1710.9,
            '2020-12-25':1800,'2021-01-23':1800.25,'2021-02-23':1810.25,
            '2021-05-14':1880.29,'2021-08-19':1887.86,'2021-10-07':1889.86,
            '2021-11-28':1500.86,'2021-12-31':1900.86}
        stdf=pd.Series(st)
        stdf.plot()
        print('THE GRAPH OF STOCKS OF PREVIOUS YEARS IS:')
        py.show()
    if z=='E':
        d={'EMP NAME':['Ms. A.R. Swaminathan','Ms. Kuldeep Singh','Mr. Jignesh Bhatt',
                       'Mr. Krushiv Chanu','Ms. Rochel Perez','Mr. George Smith',
                       'Ms Chiyoko Nohara','Mr Hong Ji Hong'],'COUNTRY':['India(South)',
                       'India(North)','India(West)','India(East)','Spain','USA',
                       'Japan','Korea'],'Salary(in INR)':[7000000,6500000,6600000,6700000,7000000,7500000,8000000,8000000],
                       'Experience(in years)':[20,17,18,19,20,25,30,30]}
        df=pd.DataFrame(d,index=['E01','E02','E03','E04','E05','E06','E07','E08'])
        df.index.name='EMPNO'
        print('BELOW IS THE DATAFRAME OF THE HEAD-DEPARTMENT OF TECHZILLION INC. ')
        print(df)
        print('TO ADD DATA INTO THE GIVEN DATAFRAME,ENTER 1')
        print('TO DELETE COLUMN FROM THE DATAFRAME,ENTER 2')
        print('TO DELETE ROW FROM THE DATAFRAME,ENTER 3')
        a=int(input('ENTER YOUR NUMBER:'))
        if a==1:
            empno=input('EMPLOYEE NUMBER:')
            empname=input('EMPLOYEE NAME:')
            country=input('COUNTRY HEADED BY THE EMPLOYEE:')
            sal=input('SALARY EARNED BY THE EMPLOYEE PER ANNUM IN INR:')
            exp=input('EXPERIENCE OF THE EMPLOYEE IN YEARS:')
            df.loc[empno,:]=[empname,country,sal,exp]
        elif a==3:
            print('THE ROW TO BE DELETED IS:')
            f=input('ENTER THE EMPNO IN THE ROW:')
            if f=='E01':
                df.drop('E01',inplace=True)
                print(df)
            elif f=='E02':
                df.drop('E02',inplace=True)
                print(df)
            elif f=='E03':
                df.drop('E03',inplace=True)
                print(df)
            elif f=='E04':
                df.drop('E04',inplace=True)
                print(df)
            elif f=='E05':
                df.drop('E05',inplace=True)
                print(df)
            elif f=='E06':
                df.drop('E06',inplace=True)
                print(df)
            elif f=='E07':
                df.drop('E07',inplace=True)
                print(df)
            elif f=='E08':
                df.drop('E08',inplace=True) 
                print(df)
        elif a==2:
            print('THE COLUMN TO BE DELETED IS:')
            g=input('ENTER THE COLUMN TO BE DELETED:')
            if g=='EMP NAME':
                del df['EMP NAME']
                print(df)
            elif g=='COUNTRY':
                del df['COUNTRY']
                print(df)
            elif g=='SALARY':
                del df['SALARY']
                print(df)
            elif g=='EXPERIENCE':
                del df['EXPERIENCE'] 
                print(df)
            else:
                print('NOTHING MATCHES YOUR INPUT. THANK YOU!')
        else:
            print('YOU CANNOT MAKE CHANGES TO THE DATAFRAME. THANK YOU!')
    if z=='V':
        a={'Market Capitalisation':5670000000,'Enterprise Value(MQR)':4730000000,
           'Enterprise Value(TTM)':18.67,
           'Total Shares':1100000000,'No. of Employees':30000,'No. of Shareholders':1500,
           'Price of Earnings Ratio':30.23,'Price of Revenue Ratio':5.34,
           'Price to Book':7.92,'Price to Sales':8.003}
        s2=pd.Series(a)
        print('THE VALUATION OF THE COMPANY CAN BE OBSERVED BELOW:')
        print(s2)
elif x==u and y!=p:
    print('ERROR!! WRONG PASSWORD!!')
elif x!=u and y==p:
    print('ERROR!! WRONG USERNAME!!')
else:
    print('ERROR!! WRONG PASSWORD AND WRONG USERNAME!!')


    
    
    
    
    
    
