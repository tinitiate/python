# ################################################
# Script Name: lms_engine.py
# Author: venkata b
# Notes: This has code LMS processing function
# ################################################
class lms_engine():

    loan_application_status = None

    def lms_engine(self, p_loan_rules_md, p_custname,p_cust_cs,p_cust_loanamt):

        try:
            LoanApplicationStatus = "Denied"
            InterestRate = -1
            DurationInMonths = -1
            CustomerName = p_custname

            for rule in p_loan_rules_md:
                # print(rule)
                if p_cust_cs >= rule["min_cs"] and p_cust_cs <= rule["max_cs"] and p_cust_loanamt >= rule["min_loan_amt"] and p_cust_loanamt <= rule["max_loan_amt"]:
                    LoanApplicationStatus = "Approved"
                    InterestRate = rule["interest"]
                    DurationInMonths = rule["duration"]

            l_res = {}
            if LoanApplicationStatus == "Approved":
                return { "CustomerName":CustomerName
                        ,"LoanApplicationStatus":LoanApplicationStatus
                        ,"InterestRate":InterestRate
                        ,"DurationInMonths":DurationInMonths
                        ,"Message":"Congrats on your approval"
                    }
            elif LoanApplicationStatus == "Denied":
            # else:
                l_res["CustomerName"] = CustomerName
                l_res["LoanApplicationStatus"] = LoanApplicationStatus
                l_res["Message"] = "Not Qualified because of Credit Score and / or Loan Amount"
                
                return l_res
        except Exception as e:
            return { "CustomerName":CustomerName
                    ,"LoanApplicationStatus":"Technical Error"
                    ,"Message": str(type(e).__name__) + " " + str(e)}

    def __init__(self, p_loan_rules_md, p_custname,p_cust_cs,p_cust_loanamt):
        self.loan_application_status = self.lms_engine(p_loan_rules_md, p_custname,p_cust_cs,p_cust_loanamt)