#ACCESS THE BALANCESHEET PART OF THE SYSTEM
import pandas as pd
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
d="31/12/2021"
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
    
    
    
    
    
    
    
