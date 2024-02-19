# Rules
master_loan_rules = [
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

# Inputs

# Success Case
CustName = "AA"
CustCreditScore = 45
CustLoanAmount = 12245

for loan_rule in master_loan_rules:
    # print(loan_rule)
    if CustCreditScore>=loan_rule["min_cs"] and CustCreditScore<=loan_rule["max_cs"] and CustLoanAmount>=loan_rule["min_loan_amt"] and CustLoanAmount<=loan_rule["max_loan_amt"]:
        print(loan_rule["interest"])
        print(loan_rule["duration"])
        break


# failure Case
CustName = "AA"
CustCreditScore = 45
CustLoanAmount = 12245


# output
LoanApplicationStatus = "Denied"
InterestRate = -1
DurationInMonths = -1









"""
for rule in master_loan_rules:
    # print(rule)
    if CustCreditScore >= rule["min_cs"] and CustCreditScore <= rule["max_cs"] and CustLoanAmount >= rule["min_loan_amt"] and CustLoanAmount <= rule["max_loan_amt"]:
        LoanApplicationStatus = "Approved"
        InterestRate = rule["interest"]
        DurationInMonths = rule["duration"]

print("LoanApplicationStatus",LoanApplicationStatus)
if LoanApplicationStatus=="Approved":
    print("InterestRate",InterestRate)
    print("DurationInMonths",DurationInMonths)
"""