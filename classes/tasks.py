import random
import time
import classes.utilities as utilities

class avatars:
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.utilities = utilities

    def does_avatar_exist(self, avatar_name):
        response = self.wrapper.get_data("neoboards/preferences.phtml")
        avatar_data = self.utilities.get_between(response.text, "value='default'>", "</select>")
        if self.utilities.contains(avatar_data, avatar_name):
            return True

    def lever_of_doom(self, limit=10000):
        neopoints_spent = 0
        if not self.does_avatar_exist("Lever of Doom"):
            response = self.wrapper.get_data("space/strangelever.phtml", referer="https://www.jellyneo.net/?go=leverofdoom")
            if self.utilities.neopoints_on_hand(response.text) >= 100:
                game_hash = self.utilities.get_between(response.text, "name=\"_ref_ck\" value=\"", "\">")
                response = self.wrapper.post_data("space/leverofdoom.phtml", data={"_ref_ck": game_hash}, referer=response.url)
                neopoints_spent += 100
                if self.utilities.contains(response.text, "You are now eligible to use"):
                    print("Received lever of doom avatar.")
                else:
                    print(f"Pulled the lever, no avatar. Spent {neopoints_spent} neopoints so far..")
                while True:
                    response = self.wrapper.post_data("space/strangelever.phtml", referer=response.url)
                    if self.utilities.neopoints_on_hand(response.text) >= 100:
                        response = self.wrapper.post_data("space/leverofdoom.phtml", data={"_ref_ck": game_hash}, referer=response.url)
                        neopoints_spent += 100
                        if neopoints_spent >= limit:
                            print(f"Reached {limit} neopoints spent, task stopped.")
                            break
                        if self.utilities.contains(response.text, "You are now eligible to use"):
                            print("Received lever of doom avatar, task stopped.")
                            break
                        else:
                            print(f"Pulled the lever, no avatar. Spent {neopoints_spent} neopoints so far..")
                    else:
                        print(f"You don\'t have enough neopoints to pull the lever, attempting to withdraw {limit - neopoints_spent - self.utilities.neopoints_on_hand(response.text)} from your bank..")
                        if not bank_manager(self.wrapper).withdraw_neopoints(limit - neopoints_spent - self.utilities.neopoints_on_hand(response.text)):
                            break
                        response = self.wrapper.get_data("space/strangelever.phtml", referer="https://www.jellyneo.net/?go=leverofdoom")
            else:
                print(f"You don\'t have enough neopoints to pull the lever, attempting to withdraw {limit - neopoints_spent - self.utilities.neopoints_on_hand(response.text)} from your bank..")
                bank_manager(self.wrapper).withdraw_neopoints(limit - neopoints_spent - self.utilities.neopoints_on_hand(response.text))
                response = self.wrapper.get_data("space/strangelever.phtml", referer="https://www.jellyneo.net/?go=leverofdoom")
        else:
            print("You already own the Lever of Doom avatar!")

    def rorru(self, limit=100):
        print("Checking if you have the Rorru avatar yet..")
        if not self.does_avatar_exist("Rorru"):
            print("You don\'t own the Rorru avatar, navigating to the Haiku Generator..")
            for _ in range(limit):
                response = self.wrapper.get_data("island/haiku/haiku.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
                if self.utilities.contains(response.text, "You are now eligible to use"):
                    print("Received Rorru avatar, task stopped.")
                    return
                else:
                    print(f"Refreshed {_ + 1}/{limit} times, no avatar..")
                self.check_for_breaks(_ + 1, limit, "Neomail Addict")
            print(f"Reached {limit} refreshes, task stopped.")
        else:
            print("You already own the Rorru avatar!")

    def mutant_graveyard_of_doom(self, limit=100):
        print("Checking if you have the Mutant Graveyard of Doom avatar yet..")
        if not self.does_avatar_exist("Mutant Graveyard of Doom"):
            print("You don\'t own the Mutant Graveyard of Doom avatar, navigating to the Game Graveyard..")
            for _ in range(limit):
                response = self.wrapper.get_data("halloween/gamegraveyard.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
                if self.utilities.contains(response.text, "You are now eligible to use"):
                    print("Received Mutant Graveyard of Doom avatar, task stopped.")
                    return
                else:
                    print(f"Refreshed {_ + 1}/{limit} times, no avatar..")
                self.check_for_breaks(_ + 1, limit, "Neomail Addict")
            print(f"Reached {limit} refreshes, task stopped.")
        else:
            print("You already own the Mutant Graveyard of Doom avatar!")

    def helpful_zafara(self, limit=100):
        print("Checking if you have the Helpful Zafara avatar yet..")
        if not self.does_avatar_exist("Helpful Zafara"):
            print("You don\'t own the Helpful Zafara avatar, navigating to the Avatars FAQ..")
            for _ in range(limit):
                response = self.wrapper.get_data("help_search.phtml?help_id=16", referer="http://www.jellyneo.net/?go=avatars&id=easy")
                if self.utilities.contains(response.text, "You are now eligible to use"):
                    print("Received Helpful Zafara avatar, task stopped.")
                    return
                else:
                    print(f"Refreshed {_ + 1}/{limit} times, no avatar..")
                self.check_for_breaks(_ + 1, limit, "Neomail Addict")
            print(f"Reached {limit} refreshes, task stopped.")
        else:
            print("You already own the Helpful Zafara avatar!")

    def neomail_addict(self, limit=100):
        print("Checking if you have the Neomail Addict avatar yet..")
        if not self.does_avatar_exist("Neomail Addict"):
            print("You don\'t own the Neomail Addict avatar, navigating to your neomails..")
            for _ in range(limit):
                response = self.wrapper.get_data("neomessages.phtml", referer="http://www.jellyneo.net/?go=avatars&id=other")
                if self.utilities.contains(response.text, "You are now eligible to use"):
                    print("Received Neomail Addict avatar, task stopped.")
                    return
                else:
                    print(f"Refreshed {_ + 1}/{limit} times, no avatar..")
                self.check_for_breaks(_ + 1, limit, "Neomail Addict")
            print(f"Reached {limit} refreshes, task stopped.")
        else:
            print("You already own the Neomail Addict avatar!")

    def clickable_avatars(self):
        if not self.does_avatar_exist("Pirate! - Krawk"):
            response = self.wrapper.get_data("pirates/academy.phtml?room=2", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Pirate! - Krawk avatar!")
        
        if not self.does_avatar_exist("Pirate! - Shoyru"):
            response = self.wrapper.get_data("pirates/academy.phtml?room=15", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Pirate! - Shoyru avatar!")

        if not self.does_avatar_exist("Pirate! - Aisha"):
            response = self.wrapper.get_data("pirates/academy.phtml?room=45", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Pirate! - Aisha avatar!")

        if not self.does_avatar_exist("Pirate! - Scorchio"):
            response = self.wrapper.get_data("pirates/academy.phtml?room=2149", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Pirate! - Scorchio avatar!")

        if not self.does_avatar_exist("Angelpuss - Angel"):
            response = self.wrapper.get_data("search.phtml?selected_type=object&string=Angelpuss", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Angelpuss - Angel avatar!")

        if not self.does_avatar_exist("Grey Faerie"):
            response = self.wrapper.get_data("neopedia.phtml?neopedia_id=179", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Grey Faerie avatar!")

        if not self.does_avatar_exist("Techo Master"):
            response = self.wrapper.get_data("island/training.phtml?type=wisdom", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Techo Master avatar!")

        if not self.does_avatar_exist("Dr. Death"):
            response = self.wrapper.get_data("pound/abandon.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Dr. Death avatar!")

        if not self.does_avatar_exist("Grundo Warehouse"):
            response = self.wrapper.post_data("space/warehouse/prizecodes1.phtml", data={"prizecode": "A384J-228P1"}, referer="http://www.neopets.com/space/warehouse/prizecodes.phtml")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Grundo Warehouse avatar!")

        if not self.does_avatar_exist("Kass Minion"):
            response = self.wrapper.get_data("evil/showcreature.phtml?villain=16", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Kass Minion avatar!")

        if not self.does_avatar_exist("Jeran - Hero"):
            response = self.wrapper.get_data("medieval/plot_bfm.phtml?current_day=7", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Jeran - Hero avatar!")

        if not self.does_avatar_exist("Bleh!!"):
            response = self.wrapper.get_data("bleh.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Bleh!! avatar!")

        if not self.does_avatar_exist("Baby Buzz"):
            response = self.wrapper.get_data("search.phtml?s=i+love+baby+buzz!", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Baby Buzz avatar!")

        if not self.does_avatar_exist("Good or Bad?"):
            response = self.wrapper.get_data("water/plot_com.phtml?chapter=5", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Good or Bad? avatar!")

        if not self.does_avatar_exist("Captain Scarblade"):
            response = self.wrapper.get_data("art/misc/scarblade2.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Captain Scarblade avatar!")

        if not self.does_avatar_exist("Gloomy"):
            print("Attempting to get Gloomy avatar, this may take a while..")
            worlds = [14, 11, 12, 4, 9, 16, 3, 17, 2, 18, 10, 5, 13, 6, 7, 15, 8, 1, 19]
            response = self.wrapper.get_data("weather.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if not self.utilities.contains(response.text, "You are now eligible to use"):
                for world in worlds:
                    response = self.wrapper.get_data(f"weather.phtml?world={world}", referer=response.url)
                    if self.utilities.contains(response.text, "You are now eligible to use"):
                        print("Received Gloomy avatar!")
                        break
            else:
                print("Received Gloomy avatar!")

        if not self.does_avatar_exist("Quiggle - Cheesy Grin"):
            response = self.wrapper.get_data("browseshop.phtml?owner=Cosmic145236987", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Quiggle - Cheesy Grin avatar!")

        if not self.does_avatar_exist("Ixi - Sophie the Swamp Witch"):
            response = self.wrapper.get_data("halloween/costumes.phtml", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Ixi - Sophie the Swamp Witch avatar!")

        if not self.does_avatar_exist("Grarrl - Galem Darkhand"):
            response = self.wrapper.get_data("search.phtml?selected_type=object&string=Galem%2BDarkhand", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Grarrl - Galem Darkhand avatar!")

        if not self.does_avatar_exist("Lupe - King Altador"):
            response = self.wrapper.get_data("altador/hallofheroes.phtml?view_statue_id=12", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Lupe - King Altador avatar!")

        if not self.does_avatar_exist("Yurble - Forefitor"):
            response = self.wrapper.get_data("altador/hallofheroes.phtml?janitor=1", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Yurble - Forefitor avatar!")

        if not self.does_avatar_exist("Acara - Roberta of Brightvale"):
            response = self.wrapper.get_data("objects.phtml?obj_type=78&type=shop", referer="http://www.jellyneo.net/?go=avatars&id=easy")
            if self.utilities.contains(response.text, "You are now eligible to use"):
                print("Received Acara - Roberta of Brightvale avatar!")

    def check_for_breaks(self, interation, limit, task):
        if limit > 100:
            if not interation % 100:
                delay = random.randint(180, 510)
                print(f"[{task}] Taking a break for {delay} seconds..")
                time.sleep(delay)

class bank_manager:
    def __init__(self, wrapper, pin = None):
        self.wrapper = wrapper
        self.utilities = utilities
        self.pin = pin

    def has_bank_account(self):
        response = self.wrapper.get_data("bank.phtml", referer="https://www.jellyneo.net/?go=dailies")
        if not self.utilities.contains(response.text, "To open an account"):
            return response.text

    def withdraw_neopoints(self, amount):
        response = self.has_bank_account()
        if response:
            if self.utilities.bank_balance(response) >= amount:
                game_hash = self.utilities.get_between(response, "name='ref_ck' value='", "'>")
                response = self.wrapper.post_data("process_bank.phtml", data={"type": "withdraw", "ref_ck": game_hash, "amount": amount})
                if self.utilities.contains(response.text, "You have deposited and/or withdrawn Neopoints today."):
                    print(f"Withdrew {amount} neopoints successfully!")
                    return True
                elif self.utilities.contains(response.text, "you have already attempted to withdraw Neopoints"):
                    print("You have withdrawn too many times today, try again tomorrow.")
            else:
                print("You don\'t have enough neopoints to withdraw!")

class wizard:
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.utilities = utilities

    def buy_item(self, item, max_price, quantity, search):
        #TODO: Detect when the user is banned from the shop wizard
        for _ in range(int(quantity)):
            cheapest_shop, cheapest_price = None, None
            for _ in range(search):
                response = self.wrapper.get_data("market.phtml?type=wizard")
                response = self.wrapper.post_data("market.phtml", data={"type": "process_wizard", "feedset": "0", "shopwizard": item, "table": "shop", "criteria": "exact", "min_price": "0", "max_price": max_price}, referer=response.url)
                if not self.utilities.contains(response.text, "I did not find anything."):
                    with open('w.html', 'w', encoding="utf8") as f:
                        f.write(response.text)
                    if int(self.utilities.get_between(response.text, "&buy_cost_neopoints=", "\"><b>")) <= int(max_price):
                        cheapest_price = int(self.utilities.get_between(response.text, "&buy_cost_neopoints=", "\"><b>"))
                        shop_link = self.utilities.get_between(response.text, "<a href=\"/browseshop.phtml?owner=", "\"><b>")
                        cheapest_shop = f"browseshop.phtml?owner={shop_link}"
                        print(f"Found {item} for {cheapest_price}, attempting to snipe it..")
            if cheapest_shop:
                if self.utilities.neopoints_on_hand(response.text) >= cheapest_price:
                    response = self.wrapper.get_data(cheapest_shop, referer=response.url)
                    buy_link = self.utilities.get_between(response.text, "<A href=\"buy_item.phtml?", "\" onClick=\"if")
                    response = self.wrapper.get_data(f"buy_item.phtml?{buy_link}", referer=response.url)
                    if self.utilities.contains(response.text, "here</b></a> to report shop"):
                        print(f"Bought {item} for {cheapest_price} neopoints successfully!")
            if not cheapest_price:
                print(f"Unable to find {item} for {max_price} neopoints..")

    def sniper(self):
        while True:
            with open("lists/shop_wizard.txt", "r") as wizard:
                for data in wizard:
                    item, price = data.strip().split(":")
                    self.buy_item(item, price, 1, 1) #item:price:quantity:search

class quests:
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.utilities = utilities

    def illusens_glade(self):
        current_neopoints = 0
        response = self.wrapper.get_data("medieval/earthfaerie.phtml", referer="https://www.jellyneo.net/?go=illusens_glade")
        response = self.wrapper.post_data("medieval/process_earthfaerie.phtml", data={"type": "accept", "username": self.parse_username()}, referer=response.url)
        if self.utilities.contains(response.text, "If you fail this quest you will be reset"):
            quest_item = self.utilities.get_between(response.text, "Where is my <b>", "</b>?<p>")
            print(f"Checking your SDB for {quest_item}..")
            if not sdb(self.wrapper).withdraw_from_sdb(quest_item):
                current_neopoints = self.utilities.neopoints_on_hand(response.text)
                if self.utilities.neopoints_on_hand(response.text) < 35000:
                    if not bank_manager(self.wrapper).withdraw_neopoints(35000 - self.utilities.neopoints_on_hand(response.text)):
                        return
                wizard(self.wrapper).buy_item(quest_item, "35000", "1", 3)
            response = self.wrapper.get_data("medieval/earthfaerie.phtml", referer="https://www.jellyneo.net/?go=illusens_glade")
            if self.utilities.neopoints_on_hand(response.text) != current_neopoints:
                response = self.wrapper.post_data("medieval/process_earthfaerie.phtml", data={"type": "finished"}, referer=response.url)
                if self.utilities.contains(response.text, "You have completed "):
                    quest_number = self.utilities.get_between(response.text, "You have completed <font color=green><b>Illusen's Quest ", "</b></font> - Congratulations!")
                    print(f"Completed Illusen's Quest #{quest_number} successfully!")

    def parse_username(self):
        with open("accounts/accounts.txt", "r") as f:
            return f.read().strip().split(":")[0]

class dailies:
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.utilities = utilities

    def lottery(self):
        response = self.wrapper.get_data("games/lottery.phtml", referer="https://www.jellyneo.net/?go=dailies")
        if self.utilities.neopoints_on_hand(response.text) < 2000:
            if not bank_manager(self.wrapper).withdraw_neopoints(2000 - self.utilities.neopoints_on_hand(response.text)):
                return
        game_hash = self.utilities.get_between(response.text, "name='_ref_ck' value='", "'>")
        for _ in range(20):
            lottery_numbers = random.sample(range(1, 31), 6)
            response = self.wrapper.post_data("games/process_lottery.phtml", data={"_ref_ck": game_hash, "one": lottery_numbers[0], "two": lottery_numbers[1], "three": lottery_numbers[2], "four": lottery_numbers[3], "five": lottery_numbers[4], "six": lottery_numbers[5]}, referer=response.url)
            if self.utilities.contains(response.text, "you cannot buy any more"):
                print("Finished buying lottery tickets, task stopped.")
                return
            print(f"Bought ticket #{_ + 1} - {lottery_numbers[0]}, {lottery_numbers[1]}, {lottery_numbers[2]}, {lottery_numbers[3]}, {lottery_numbers[4]}, {lottery_numbers[5]}")
        print("Finished buying lottery tickets, task stopped.")

class sdb: 
    def __init__(self, wrapper):
        self.wrapper = wrapper
        self.utilities = utilities

    def withdraw_from_sdb(self, item):
        response = self.search_sdb(item)
        if response:
            if self.utilities.get_between(response.text, "border=\"1\"></td>\n<td align=\"left\"><b>", "<br><span ") == item:
                back_to_inventory = self.utilities.get_between(response.text, "name='back_to_inv", "' size=")
                response = self.wrapper.post_data("process_safetydeposit.phtml?checksub=scan", data={f"back_to_inv{back_to_inventory}": "1", "obj_name": item, "category": "0", "offset": "0"}, referer=response.url)
                if self.utilities.contains(response.url, "offset"):
                    print(f"Withdrew {item} from your SDB successfully!")
                    return True

    def search_sdb(self, item):
        response = self.wrapper.get_data("safetydeposit.phtml", params=f"obj_name={item}&category=0")
        if not self.utilities.contains(response.text, "Not finding any items with that criteria!"):
            return response