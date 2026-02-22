from database import *
from account import *
import datetime


# user1 = BankAccount("Oli", "hello")

# # db_insert(user1)

# print(db_fetchdata_user('Oli'))

# # print(db_passwordcheck('Oli', "dfs"))

# print(db_userexistence('Oli'))

# db_updatebalance(user1, 100)


# now = datetime.datetime.now()

# print(type(user1))
# print(type(str(now)))

d = {}
n = str(datetime.datetime.now())
d.update({n: 23523})
print(d)
