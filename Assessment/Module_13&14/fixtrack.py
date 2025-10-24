import datetime 
Records = []
id = 1
exit = False

for rec in Records:
    print(rec['_id'])


def insertRecord(id):
    print("-----Insert Record-----")
    CusName = input("Enter Customer Name: ")
    CusDevice = input("Enter Device Type: ")
    IssueDate = input("Enter Issued Date: ")
    DueDate = input("Enter Due Date: ")
    di = {
        "_id": id,
        "name": CusName,
        "device": CusDevice,
        "issued": IssueDate,
        "due": DueDate,
        "Parts Repaired": None,
        "Repair Fees": None,
        "Taxes": None,
        "Discount": None,
        "Final Amt": None
    }
    # print(di)
    Records.append(di)

def generateBill():
    print("-----Generate Bill-----")
    recId = int(input("Enter Record Id to Generate the Bill: "))

    # Enter Parts and Calc Total of all Parts
    Parts = []
    print("Enter the Parts Repared:- 1->Add Part | 0-> Exit")
    exit=False
    while exit==False:
        choice = int(input("Choice: "))
        if(choice==1):
            part,price = str(input("->")), int(input("->"))
            Parts.append({part: price})
        elif(choice==0):
            exit=True
    totalParts = 0
    for part in Parts:
        for value in part.values():
            totalParts += value
    
    # Calculate other amounts
    taxes = totalParts * 0.18  # 18% GST
    discount  = int(input("Enter Discount: "))
    
    final_amount = totalParts + taxes - discount
    
    # Update the record with all calculated values
    for rec in Records:
        if rec['_id'] == recId:
            rec["Parts Repaired"] = Parts
            rec["Repair Fees"] = totalParts
            rec["Taxes"] = taxes
            rec["Discount"] = discount
            rec["Final Amt"] = final_amount

            # Print the Bill 
            print("\n----- Bill Details -----")
            print(f"Customer Name: {rec['name']}")
            print(f"Device: {rec['device']}")
            print(f"Parts Repaired:")
            for part in Parts:
                for part_name, price in part.items():
                    print(f"  - {part_name}: ₹{price}")
            print(f"\nTotal Parts Cost: ₹{totalParts}")
            print(f"GST (18%): ₹{taxes}")
            print(f"Discount: -₹{discount}")
            print(f"Final Amount: ₹{final_amount}")
            break

    
    



while exit==False:
    print("----------Welcome to FixTrack----------")
    print("1->Insert New Record \n2->Generate the Bill \n0->Exit")
    choice = int(input("Choice: "))
    if(choice==0):
        break
    elif(choice==1):
        insertRecord(1)
        id+=1
    elif(choice==2):
        generateBill()
    else:
        print("invalid Choice!")

