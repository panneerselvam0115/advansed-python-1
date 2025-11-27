print("Government of Tamilnadu")
print("Electricty Board")
print("-----------------------")
no1=input("Enter the EB.NO")
no2=input("Enter the coustomer name:")
no3=int(input("Reading for previous month:"))
no4=int(input("Reading for current month:"))
Total=no4-no3
print("Total unit consumed:",Total)
paid=Total*5
print("Amount to be paid Rs:",paid)
