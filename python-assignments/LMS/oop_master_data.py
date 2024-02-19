# ################################################
# Script Name: master_data.py
# Author: venkata b
# Notes: This has the LMS rules master data
# ################################################
class master_data():
    # Class variable
    # # Rules
    loan_rules_md = [
    {"min_cs":200, "max_cs":299, "min_loan_amt":10000, "max_loan_amt":19999, "interest":5, "duration":72}
    ,{"min_cs":200, "max_cs":299, "min_loan_amt":20000, "max_loan_amt":29999, "interest":5.5, "duration":72}
    ,{"min_cs":200, "max_cs":299, "min_loan_amt":30000, "max_loan_amt":39999, "interest":6, "duration":72}
    ,{"min_cs":200, "max_cs":299, "min_loan_amt":40000, "max_loan_amt":50000, "interest":.65, "duration":72}
    ,{"min_cs":300, "max_cs":399, "min_loan_amt":10000,"max_loan_amt":19999, "interest":5, "duration":72}
    ,{"min_cs":300, "max_cs":399, "min_loan_amt":20000,"max_loan_amt":29999, "interest":5.5, "duration":72}
    ,{"min_cs":300, "max_cs":399, "min_loan_amt":30000,"max_loan_amt":39999, "interest":6, "duration":72}
    ,{"min_cs":300, "max_cs":399, "min_loan_amt":40000,"max_loan_amt":50000, "interest":.65, "duration":72}
    ,{"min_cs":400, "max_cs":500, "min_loan_amt":10000,"max_loan_amt":19999, "interest":5, "duration":72}
    ,{"min_cs":400, "max_cs":500, "min_loan_amt":20000,"max_loan_amt":29999, "interest":5.5, "duration":72}
    ,{"min_cs":400, "max_cs":500, "min_loan_amt":30000,"max_loan_amt":39999, "interest":6, "duration":72}
    ,{"min_cs":400, "max_cs":500, "min_loan_amt":40000,"max_loan_amt":50000, "interest":.65, "duration":72}
    ]