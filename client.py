import classes.utilities as utilities
from classes.wrapper import wrapper
from classes.tasks import avatars, wizard, quests, sdb, dailies

class client:
    def __init__(self):
        self.wrapper = wrapper()
        self.utilities = utilities

    def login(self):
        account_data = self.parse_account()
        if len(account_data) > 2:
            self.wrapper.set_proxy(f"{account_data[2]}:{account_data[3]}")
        response = self.wrapper.post_data("login.phtml", data={"destination": "", "return_format": "1", "username": account_data[0], "password": account_data[1]}, referer="http://www.neopets.com/login/")
        if self.utilities.contains(response.text, f"var appInsightsUserName = '{account_data[0]}'"):
            print(f"Logged in as {account_data[0]}")

    def parse_account(self):
        with open("accounts/accounts.txt", "r") as f:
            account_data = f.read().strip().split(":")
        if len(account_data) > 2:
            return account_data[0], account_data[1], account_data[2], account_data[3]
        else:
            return account_data[0], account_data[1]

    def tasks(self):
        avatars(self.wrapper).mutant_graveyard_of_doom(10000)

if __name__ == "__main__":
    a = client()
    a.login()
    a.tasks()