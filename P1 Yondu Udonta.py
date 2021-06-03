"""
Project Name: Yondu Udonta
Author: Keaton Proctor
Due Date: 
06/05/2021
Course: CS1400-603

This program will ask the user for a number of pirates and the amount of units they plundered. It will then calculate how
many units each person receives with the captain and first mate getting more than the rest. Remaining is donated to the
Reavers Benevolant Fund (RBF).
"""
def main(): #main function need in all programs for automated testing
    """
    Program starts here
    """
    try:
        reavers = int(input("How many Reavers: "))
        units = int(input("How many units: "))
    
    except ValueError:
        print("Enter positive integers for Reavers and units.")
        return
    
    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return 
    
    if reavers < 3:
        print("Not enough crew.")
        return
    
    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    crew = reavers - 2
    party_money = crew * 3
    rem_units = units - party_money
    
    yondu = int(rem_units * .13)
    rem_units = rem_units - yondu
    
    peter = int(rem_units * .11)
    rem_units = rem_units - peter
    
    share = int(rem_units / reavers)
    rb_fund = rem_units - (reavers * share)
    
    peter = peter + share
    yondu = yondu + share
    
    print("Yondu's share: ",str(yondu))
    print("Peter's share: ",str(peter))
    print("Crew: ",str(share))
    print("RBF: ",str(rb_fund))


#end of main program
    
if __name__ == '__main__':
    main()  #excucte main function
