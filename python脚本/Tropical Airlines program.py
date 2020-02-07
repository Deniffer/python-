# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:11:32 2020

@author: HASEE
"""


def display_menu():
    #to display the initial menu chioce
    print("Tropical Airlines Ticket Ordering System")
    print("(I)nstructions")
    print("(O)rder ticket")
    print("(E)xit")
def order_ticket(name):
    #to order ticket 
    while(True):
        passenger=input("%s, is this ticket for:\n(Y)ou \n(S)omeone else\n"%name).upper()
        if passenger=="Y":
            passenger=name
            break
        elif passenger=="S":
            passenger=input("Please enter the name of the person travelling\n")
            break
        else:
            print("Invalid input.")
    
    trip_type=input("Is this a return trip(R) or One-Way(O)\n").upper()
    while(trip_type not in ["R","O"]):
        print("invalid trip type!")
        trip_type=input("Is this a return trip(R) or One-Way(O)\n").upper()
    if trip_type=="R":
        trip_type="return-trip "
        print("\nPlease select destination for your %s trip.Fare prices are listed below."%trip_type)
        print("(C)airns – $400")
        print("(S)ydney – $575 ")
        print("(P)erth - $700")
        destination=input().upper()
        while(destination not in ["C","S","P"]):
            print("invalid destination,input again")
            destination=input().upper()
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare.Please note choosing Frugal fare means you will not be offered a seat choice. ")
        print("(B)usiness - $275\n(E)conomy - $25\n(F)rugal - $0")
        class_type=input().upper()
        while(class_type not in ["B","E","F"]):
            print("invalid class type.")
            class_type=input().upper()
        if class_type!="F":
            print("\nPlease choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.")
            print("(W)indow  $75 \n(A)isle  $50 \n(M)iddle -$25 ")
            seat_type=input().upper()
            while (seat_type not in ["W","A","M"]):
                print("invalid seat_type")
                seat_type=input().upper()
        else:
            seat_type="W"
        passenger_age=input("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.\n")
        while( eval(passenger_age)<=0):
            print("invalid passenger age!")
            passenger_age=input("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.\n")
    else:
        trip_type="One-Way"
        print("\nPlease select destination for your %s trip.Fare prices are listed below."%trip_type)
        print("(C)airns – $250")
        print("(S)ydney – $420 ")
        print("(P)erth - $510")
        destination=input().upper()
        while(destination not in ["C","S","P"]):
            print("invalid destination,input again")
            destination=input().upper()
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare.Please note choosing Frugal fare means you will not be offered a seat choice. ")
        print("(B)usiness - $275\n(E)conomy - $25\n(F)rugal - $0")
        class_type=input().upper()
        while(class_type not in ["B","E","F"]):
            print("invalid class type.")
            class_type=input().upper()
        if class_type!="F":
            print("\nPlease choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.")
            print("(W)indow  $75 \n(A)isle  $50 \n(M)iddle -$25 ")
            seat_type=input().upper()
            while (seat_type not in ["W","A","M"]):
                print("invalid seat_type")
                seat_type=input().upper()
        else:
            seat_type="W"
        passenger_age=input("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.\n")
        while( eval(passenger_age)<=0):
            print("invalid passenger age!")
            passenger_age=input("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.\n")
    return passenger,trip_type,destination,class_type,seat_type,passenger_age

def cal_fare(passenger,trip_type,destination,class_type,seat_type,passenger_age):
    #cal the fare base on the order ticket
    total_fare=0
    child_discount=0.5
    return_destination_prize=[400,575,700]
    return_class_prize=[275,25,0]
    return_seat_prize=[75,50,-25]
    
    one_way_destination_prize=[250,420,510]
    one_way_class_prize=[275,25,0]
    one_way_seat_prize=[75,50,-25]
    print("Calculating fare...\n")
    print("Ticket for: %s"%passenger) 
    
    if trip_type=="return-trip":
        if destination=="C":
            total_fare+=return_destination_prize[0]
            print("Cairns (return) -	$400")
        elif destination=="S":
            total_fare+=return_destination_prize[1]
            print("Sydney (return) -	$575")
        else:
            total_fare+=return_destination_prize[2]
            print("Perth (return) -	$700")
            
        if class_type=="B":
            total_fare+=return_class_prize[0]
            print("Business -		$275")
        elif class_type=="E":
            total_fare+=return_class_prize[1]
            print("Economy -		$25")
        else:
            total_fare+=return_class_prize[2]
            print("Frugal -		$0")
            print("Window -		$0")
        if seat_type=="W" and class_type!="F" :
            total_fare+=return_seat_prize[0]
            print("Window -		$75")
        elif seat_type=="A"and class_type!="F":
            total_fare+=return_seat_prize[1]
            print("Aisle -		$50")
        elif seat_type=="M" and class_type!="F":
            total_fare+=return_seat_prize[2]
            print("Middle -		-$25")
                
        if eval(passenger_age)<=16:
            total_fare=total_fare*child_discount
            print("Age -			%s (eligible for child ticket, 50% discount applied)"%passenger_age)
        else:
            print("Age -			%s (not eligible for child ticket)"%passenger_age)

    else:
        if destination=="C":
            total_fare+=one_way_destination_prize[0]
            print("Cairns (one-way) -	$250")
        elif destination=="S":
            total_fare+=one_way_destination_prize[1]
            print("Sydney (one-way) -	$420")
        else:
            total_fare+=one_way_destination_prize[2]
            print("Perth (one-way) -	$510")
            
        if class_type=="B":
            total_fare+=one_way_class_prize[0]
            print("Business -		$275")
        elif class_type=="E":
            total_fare+=one_way_class_prize[1]
            print("Economy -		$25")
        else:
            total_fare+=one_way_class_prize[2]
            print("Frugal -		$0")
            print("Window -		$0")
        if seat_type=="W"and class_type!="F":
            total_fare+=one_way_seat_prize[0]
            print("Window -		$75")
        elif seat_type=="A"and class_type!="F":
            total_fare+=one_way_seat_prize[1]
            print("Aisle -		$50")
        elif seat_type=="W" and class_type!="F":
            total_fare+=one_way_seat_prize[2]
            print("Middle -		-$25")
                
        if eval(passenger_age)<=16:
            total_fare=total_fare*child_discount
            print("Age -			{0} (eligible for child ticket, 50% discount applied)".format(passenger_age))
        else:
            print("Age -			%s (not eligible for child ticket)"%passenger_age)
    
    print("Total prize:%.2f"%total_fare)
        
    return total_fare
def exit(name,total_fare):
    #to exit the order system
    fare=""
    for i in total_fare:
        fare+="$"+str(i)+","
    print("%s,your order are: %s your final total is $%.2f. Thank you for visiting Tropical Airlines"%(name,fare,sum(total_fare)))

def main():
    #maintian all functions  
    instructions="Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.\n"
    name=input("What is your name?")
    print("\nWelcome %s."%name)
    characters=["I","O","E"]
    total_fare=[]
    play=True
    while(play):
        display_menu()
        character=input().upper()
        if character not in characters:
            print("Invalid menu choice.")
        elif character==characters[0]:
            print(instructions)
        elif character==characters[1]:
            passenger,trip_type,destination,class_type,seat_type,passenger_age=order_ticket(name)
            total_fare.append(cal_fare(passenger,trip_type,destination,class_type,seat_type,passenger_age))
        elif character==characters[2]:
            exit(name,total_fare)
            play=False
if __name__=="__main__":
    main()