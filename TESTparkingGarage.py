### ParkingGarage class which instantiates with variables for tickets, spaces, currentTicket, and takenTickets.
### 5 methods allow for taking tickets, paying for parking, leaving the garage, printing out the garage status, and clearing the terminal screen.

import time
class ParkingGarage():
    def __init__(self, size):
        self.tickets = [{"paid": False} for i in range(size)]
        self.spaces = [{} for i in range(size)]
        self.currentTicket = {}
        self.takenTickets = []
    
    def takeTicket(self):
        if self.tickets:
            self.currentTicket = self.tickets.pop()
            self.spaces.pop()
            self.takenTickets.append(self.currentTicket)
            print("You took 1 ticket. Please park your car.")
        else:
            print("I'm sorry, there are currently no spaces available. Please try again later.")
    
    def payForParking(self):
        if self.currentTicket:
            if self.currentTicket["paid"] == False:
                payment = input("Enter amount to pay: ")
                if payment:
                    print('Your payment has been processed. You have 15 minutes to leave the garage.')
                    self.currentTicket["paid"] = True
            else:
                print("The current ticket has already been paid.")
        else:
            print("Please take a ticket first.")
    
    def leaveGarage(self):
        if self.currentTicket:
            if self.currentTicket["paid"] == False:
                self.payForParking()
            if self.currentTicket["paid"] == True:
                print("Thank you. Have a nice day.")
                self.tickets.append({"paid":False})
                self.spaces.append({})
                self.takenTickets.pop()
                if self.takenTickets:
                    self.currentTicket = self.takenTickets[len(self.takenTickets) - 1]
                else:
                    self.currentTicket = {}
        else:
            print("I'm sorry but you don't have a ticket. How did you get in here?")
            
    def printStatus(self):
        print(f"TICKETS: {self.tickets}\nSPACES: {self.spaces}\nCURRENT TICKET: {self.currentTicket}\nTAKEN TICKETS: {self.takenTickets}")
        
    def clrscr(self):
        print("\n" * 20)
            


### playGarage is a function that allows the user to interact with the ParkingGarage Class.   
### there is also a hidden game mode, where if the user chooses a garage size of 10, the game will track how long it takes you from instantiating your ParkingGarage object,
### to fill your garage up, empty it, and then quit. It will print out your time if you meet the objectives.
      
def playGarage():
    size = int(input("How many spaces would you like in your garage?\n"))
    yourGarage = ParkingGarage(size)
    playing = True
    empty = False
    full = False
    if size == 10:
        start_time = time.time()
    while playing == True:
        
        choice = input("\nCHOOSE AN OPTION:\n'T' to take a ticket.\n'P' to pay.\n'L' to leave garage.\n'Q' to quit.\n'print' to print garage status.\nCHOICE: ").lower()
        yourGarage.clrscr()
        
        if choice == 't':
            yourGarage.takeTicket()
            if not yourGarage.tickets:
                empty = True
        elif choice == 'p':
            yourGarage.payForParking()
        elif choice == 'l':
            yourGarage.leaveGarage()
            if empty == True and len(yourGarage.tickets) == 10:
                full = True
        elif choice == 'print':
            yourGarage.printStatus()
        elif choice == 'q':
            playing = False
            end_time = time.time()
            if empty == True and full == True:
                print(f"Your time was {round(end_time - start_time, 1)}. Write that score down, I don't have a database.")
            
playGarage()