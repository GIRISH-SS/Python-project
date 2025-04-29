print("Welcome to Karnataka Bank ATM")

# Predefined PIN and available balance
correct_pin = 1234
available_balance = 10000

# Insert ATM card
card_inserted = int(input("Please insert ATM card (Press 1 to insert, 0 if not read): "))

if card_inserted == 0:
    print("Card not read. Please try again.")
elif card_inserted == 1:
    print("Card inserted. Moving on...")

    # Enter PIN
    pin = int(input("Enter your 4-digit PIN: "))
    
    if pin == correct_pin:
        print("\nChoose an option:")
        print("1. Banking")
        print("2. Balance Inquiry")
        print("3. Withdrawal")
        print("4. Enquiry")
        
        while True:
            option = input("\nEnter option number (1-4): ")

            if option == '1':
                print("Banking services are currently unavailable. Please try later.")
            
            elif option == '2':
                print(f"Available Balance: ₹{available_balance}")
            
            elif option == '3':
                amt = int(input("Enter withdrawal amount (in multiples of 100): "))
                
                if amt % 100 != 0:
                    print("Please enter the amount in multiples of 100.")
                elif amt > available_balance:
                    print("Insufficient balance.")
                else:
                    available_balance -= amt
                    print("Processing...")
                    print("Please collect your cash.")

                    show_balance = input("Would you like to see your balance? (yes/no): ").lower()
                    if show_balance == "yes":
                        print(f"Remaining Balance: ₹{available_balance}")
                    print("Thank you for banking with us!")
                    break  # Exit after successful withdrawal
            
            elif option == '4':
                print("For further enquiries, please contact customer support at 1800-XXX-XXXX.")
            
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. Access denied.")
else:
    print("Invalid input. Please restart.")
