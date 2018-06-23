import pandas as pd
import numpy as np



data = pd.read_csv("german.data",delim_whitespace=True, header=None)

#print(data)

#Naming the attributes for easy of our work
data.columns = ["Status_current_account", "Duration_in_month", "Credit_history", "Purpose","Credit_amount","Savings_account/bonds"
                 ,"Present_employment_since","Installment_rate_of_disposable_income","Personal_status_and_sex","Other_debtors_/_guarantors",
                "Present_residence_since","Property","Age_in_years","Other_installment_plans","Housing","Number_of_existing_credits_at_this_bank",
                "Job"," provide_maintenance","Telephone","foreign_worker","output"]



print(data)