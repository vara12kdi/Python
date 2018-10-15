# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:07:47 2018

@author: PrasadK
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:54:17 2018

@author: PrasadK
"""

class BA:
    def __init__(self, Acno, Acname, Balance): 
        self.AccountNo = Acno
        self.AccountName = Acname
        self.CurrentBalance = Balance
        
    def Deposit(self, DepositAmount):
        self.CurrentBalance = self.CurrentBalance + DepositAmount
    
    def Withdraw(self, DepositAmount):
        self.CurrentBalance = self.CurrentBalance - DepositAmount
    
    
        

BA1 = BA(631201, "Ramesh", 1500)
BA1.Deposit(250)

BA1.AccountName
BA1.AccountNo
BA1.CurrentBalance

