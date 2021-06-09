from abc import ABC, abstractmethod
import csv

class Operation(ABC): #Command

    @abstractmethod
    def execute(self):
        pass


class Balance(Operation): #ConcreteCommand: client's bank account balance

    def __init__(self, client_balance):
        self.client_balance = client_balance

    def execute(self):
        self.client_balance.verify_balance()


class Statement(Operation): #ConcreteCommand: client's bank account statement

    def __init__(self, client_statement):
        self.client_statement = client_statement

    def execute(self):
        self.client_statement.verify_statement()


class Transfer(Operation): #ConcreteCommand: bank transfer

    def __init__(self, client_transfer):
        self.client_transfer = client_transfer

    def execute(self):
        self.client_transfer.transfer()


class Bank: #Receiver

    def verify_balance(self):
        with open('balance.csv') as balance:
            reader = csv.DictReader(balance, fieldnames=['value'])
            for row in reader:
                aux = str(row['value'])
            print("Balance account: " + aux)
        print('')

    def verify_statement(self):
        print("Month Statement:")
        with open('month_statement.csv') as statement:
            reader = csv.DictReader(statement, fieldnames=['establishment', 'cost', 'day'], delimiter=',')
            for row in reader:
                print(str(row['establishment']) + str(row['cost']) + str(row['day']))
        print('')

    def transfer(self):
        with open('transfer.csv') as statement:
            reader = csv.DictReader(statement, fieldnames=['receiver', 'value'], delimiter=',')
            for row in reader:
                print("Transfer from " + str(row['value']) + " to " + str(row['receiver']) + " completed.")

class Agent: #Invoker

    def __init__(self):
        self.operation_queue = []

    def execute_operation(self, operation):
        self.operation = operation
        operation.execute()



