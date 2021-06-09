#CES-22 COMP-23
#ExLab2
#Arthur José
#Example

from bank import *

client_account = Bank()
account_balance = Balance(client_account)
account_statement = Statement(client_account)
transfer = Transfer(client_account)

agent = Agent()
agent.execute_operation(account_balance)
agent.execute_operation(account_statement)
agent.execute_operation(transfer)