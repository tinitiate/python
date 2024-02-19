# ################################################
# Script Name: main.py
# Author: venkata b
# Notes: This is the entry script to the LMS 
#        application.
# ################################################

# Imports
from oop_lms_engine import lms_engine
from oop_master_data import master_data

# Inputs
# #######################
# Success Case
CustName = "AA"
CustCreditScore = 345
CustLoanAmount = 12245

# Create Objects
# ########################
md = master_data()
le = lms_engine( p_loan_rules_md = md.loan_rules_md
                ,p_custname      = CustName
                ,p_cust_cs       = CustCreditScore
                ,p_cust_loanamt  = CustLoanAmount
                )

print(le.loan_application_status)