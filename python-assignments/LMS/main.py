# ################################################
# Script Name: main.py
# Author: venkata b
# Notes: This is the entry script to the LMS 
#        application.
# ################################################

# Imports
import lms_engine as le
import master_data as md

# Inputs
# #######################
"""
# Success Case
CustName = "AA"
CustCreditScore = 345
CustLoanAmount = 12245
"""

# failure Case
CustName = "AA"
CustCreditScore = 45
CustLoanAmount = 12245


# Call Engine
# #######################

status= le.lms_engine( p_loan_rules_md = md.loan_rules_md
                      ,p_custname      = CustName
                      ,p_cust_cs       = CustCreditScore
                      ,p_cust_loanamt  = CustLoanAmount
                      )

print(status)

if status["LoanApplicationStatus"]=="Approved":
    print("Approved")


status= le.lms_engine( p_loan_rules_md = 123
                      ,p_custname      = CustName
                      ,p_cust_cs       = CustCreditScore
                      ,p_cust_loanamt  = CustLoanAmount
                      )

print(status)