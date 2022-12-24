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
        print(self.tickets, self.spaces, self.currentTicket, self.takenTickets)
            