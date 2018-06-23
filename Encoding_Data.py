import Data_Reading as dr





#Separating dependent and independent variable
D_V = dr.data.drop("output",axis=1)
#print(D_V)

Y = dr.data.ix[:,20:]
#print(Y)

# Encoding of Data to fit in Mathematical Model

# Attribute 1:  (qualitative)
# 	       Status of existing checking account
#                A11 :      ... <    0 DM = 0
# 	       A12 : 0 <= ... <  200 DM = 1
# 	       A13 :      ... >= 200 DM / = 2
# 		     salary assignments for at least 1 year
#                A14 : no checking account = 3

Att1 = D_V.replace(to_replace={'A11','A12','A13','A14'}, value={0, 1, 2, 3})
#print(Att1)

# Attribute 3:  (qualitative)
# 	      Credit history
# 	      A30 : no credits taken/
# 		    all credits paid back duly
#               A31 : all credits at this bank paid back duly
# 	      A32 : existing credits paid back duly till now
#               A33 : delay in paying off in the past
# 	      A34 : critical account/
# 		    other credits existing (not at this bank)

Att3 = Att1.replace(to_replace={'A30','A31','A32','A33','A34'}, value={0, 1, 2, 3, 4})
#print(Att3)

# Attribute 4:  (qualitative)
# 	      Purpose
# 	      A40 : car (new)
# 	      A41 : car (used)
# 	      A42 : furniture/equipment
# 	      A43 : radio/television
# 	      A44 : domestic appliances
# 	      A45 : repairs
# 	      A46 : education
# 	      A47 : (vacation - does not exist?)
# 	      A48 : retraining
# 	      A49 : business
# 	      A410 : others

Att4 = Att3.replace(to_replace={'A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A410'}, value={0, 1, 2, 3, 4,5, 6, 7, 8, 9,10})
#print(Att4)

# Attibute 6:  (qualitative)
# 	      Savings account/bonds
# 	      A61 :          ... <  100 DM
# 	      A62 :   100 <= ... <  500 DM
# 	      A63 :   500 <= ... < 1000 DM
# 	      A64 :          .. >= 1000 DM
#               A65 :   unknown/ no savings account

Att6 = Att4.replace(to_replace={'A61','A62','A63','A64','A65'}, value={0, 1, 2, 3, 4})
#print(Att6)


# Attribute 7:  (qualitative)
# 	      Present employment since
# 	      A71 : unemployed
# 	      A72 :       ... < 1 year
# 	      A73 : 1  <= ... < 4 years
# 	      A74 : 4  <= ... < 7 years
# 	      A75 :       .. >= 7 years

Att7 = Att6.replace(to_replace={'A71','A72','A73','A74','A75'}, value={0, 1, 2, 3, 4})
#print(Att7)


# Attribute 9:  (qualitative)
# 	      Personal status and sex
# 	      A91 : male   : divorced/separated
# 	      A92 : female : divorced/separated/married
#               A93 : male   : single
# 	      A94 : male   : married/widowed
# 	      A95 : female : single

Att9 = Att7.replace(to_replace={'A91','A92','A93','A94','A95'}, value={0, 1, 2, 3, 4})
#print(Att9)


# Attribute 10: (qualitative)
# 	      Other debtors / guarantors
# 	      A101 : none
# 	      A102 : co-applicant
# 	      A103 : guarantor


Att10 = Att9.replace(to_replace={'A101','A102','A103'}, value={0, 1, 2})
#print(Att10)

# Attribute 12: (qualitative)
# 	      Property
# 	      A121 : real estate
# 	      A122 : if not A121 : building society savings agreement/
# 				   life insurance
#               A123 : if not A121/A122 : car or other, not in attribute 6
# 	      A124 : unknown / no property

Att12 = Att10.replace(to_replace={'A121','A122','A123','A124'}, value={0, 1, 2, 3})
#print(Att12)

# Attribute 14: (qualitative)
# 	      Other installment plans
# 	      A141 : bank
# 	      A142 : stores
# 	      A143 : none

Att14 = Att12.replace(to_replace={'A141','A142','A143'}, value={0, 1, 2})
#print(Att14)


# Attribute 15: (qualitative)
# 	      Housing
# 	      A151 : rent
# 	      A152 : own
# 	      A153 : for free

Att15 = Att14.replace(to_replace={'A151','A152','A153'}, value={0, 1, 2})
#print(Att15)

# Attribute 17: (qualitative)
# 	      Job
# 	      A171 : unemployed/ unskilled  - non-resident
# 	      A172 : unskilled - resident
# 	      A173 : skilled employee / official
# 	      A174 : management/ self-employed/
# 		     highly qualified employee/ officer

Att17 = Att15.replace(to_replace={'A171','A172','A173','A174'}, value={0, 1, 2, 3})
#print(Att17)

# Attribute 19: (qualitative)
# 	      Telephone
# 	      A191 : none
# 	      A192 : yes, registered under the customers name

Att19 = Att17.replace(to_replace={'A191','A192'}, value={0, 1})
#print(Att19)

# Attribute 20: (qualitative)
# 	      foreign worker
# 	      A201 : yes
# 	      A202 : no

Att20 = Att19.replace(to_replace={'A201','A202'}, value={0, 1})
#print(Att20)

X = Att20
#print(X)

