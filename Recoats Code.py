import pandas as pd
# import matplotlib.pylot as plt

def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Display Total income by source")
        print("### 2. Display diffrent payment types")
        print("### 3. Display income on different days")    
        print("### 4. Exit")
        choice = input('Enter your number selection here: ')

        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        else:
            print("Invalid option. Please enter a number between 1 and 4.\n")
    return choice

def total_menu ():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")   
        print("### 2. Gift Shop") 
        print("### 3. Snack Stand")  
        print("### 4. Pictures")

        choice = input('Enter your number selction here: ')
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        else:
            print("Invalid option. Please enter a number between 1 and 4.\n")

    return choice   


def convert_total_men_coice(total_men_choice):
    
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice= "Snack Stand"
    else:
        tot_choice = "Pictures"  
    
    return tot_choice


def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data1.csv")
    
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg

def paymenttypes_incomesources():
    df = pd.read_csv("Task4a_data1.csv")
    
    cash = df.loc[(df['Pay Type'] == 'Cash')]
    cashsum = cash['Total'].sum()

    card = df.loc[(df['Pay Type'] == 'Card')]
    cardsum = card['Total'].sum()

    print("\nTotal income from Cash: £{}".format(cashsum))
    print("Total income from Card: £{}".format(cardsum))
    
    if "Pay Type" in df.columns:        
        payment_summary = df["Pay Type"].value_counts()
        print("\nPayment Types Breakdown:")
        print(payment_summary)
    else:
        print("Error: 'Payment Type' column not found.")

def incomediffrent_days():
    df = pd.read_csv("Task4a_data1.csv")

    if "Day" in df.columns:
        income_summary = df.groupby("Day").sum()
        print("\nIncome on Different Days:")
        print(income_summary)
    else:
        print("Error: 'Day' column not found.")



main_menu_choice = main_menu()

if main_menu_choice == 1:
    total_men_choice = total_menu()
    total_choice = convert_total_men_coice(total_men_choice)
    print(get_total_data(total_choice))

elif main_menu_choice == 2:
    paymenttypes_incomesources()

elif main_menu_choice == 3:
    incomediffrent_days()

elif main_menu_choice == 4:
    print("Exiting program. Goodbye!")
