import random


# data base of account
# we can add a or multiple account in it, like this '{'account': 'xxxxxxxxxxx', 'password': 'yyyyyyyy'},'
_VALID_ACCOUNT = (
    # {'username': '18011111111', 'password': '1234'},
    {'username': '15313756957',"password":"vanthink2018"},
    # {'username': '18011111111', 'password': '12345'},
)
_VALID_ACCOUNT1 = (
    # {'username': '18011111111', 'password': '1234'},
    {'username': '14444444445', 'password': '123321'},
    # {'username': '18011111111', 'password': '12345'},
)



class Account:
    def __init__(self):
        self.valid_account = _VALID_ACCOUNT[random.randint(0, len(_VALID_ACCOUNT)) - 1]

    def account(self):
        return self.valid_account['username']

    def password(self):
        return self.valid_account['password']

class Account1:
    def __init__(self):
        self.valid_account = _VALID_ACCOUNT1[random.randint(0, len(_VALID_ACCOUNT)) - 1]

    def account1(self):
        return self.valid_account['username']

    def password1(self):
        return self.valid_account['password']
# global variable
# a instance of account
# it can be used in any place via 'from App.student.test_data.account import VALID_ACCOUNT'
VALID_ACCOUNT = Account()
VALID_ACCOUNT.account()
VALID_ACCOUNT.password()
VALID_ACCOUNT1 = Account1()
VALID_ACCOUNT1.account1()
VALID_ACCOUNT1.password1()