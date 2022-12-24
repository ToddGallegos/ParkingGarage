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
                    self.currentTicket = self.takenTickets.pop()
                else:
                    self.currentTicket = {}
        else:
            print("I'm sorry but you don't have a ticket. How did you get in here?")
            
    def printStatus(self):
        print(f"Tickets: {self.tickets}, Spaces: {self.spaces}, CurrentTicket: {self.currentTicket}, TakenTickets: {self.takenTickets}")
            
            
def playGarage():
    playing = True
    while playing == True:
        size = int(input("How many spaces would you like in your garage?"))
        yourGarage = ParkingGarage(size)
        choice = input("Press 'T' to take a ticket.  Press 'P' to pay.  Press 'L' to leave garage.  Type 'print' to print garage status.  Press 'Q' to quit.").lower()
        
        if input == 't':
            yourGarage.takeTicket()
        elif input == 'p':
            yourGarage.payForParking()
        elif input == 'l':
            yourGarage.leaveGarage()
        elif input == 'print':
            yourGarage.printStatus()
        elif input == 'q':
            playing = False