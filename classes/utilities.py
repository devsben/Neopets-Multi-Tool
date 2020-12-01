import time

def get_between(data, first, last):
    return data.split(first)[1].split(last)[0]

def contains(data, string):
    return True if string in data else False

def neopoints_on_hand(data):
    neopoints = get_between(data, "/inventory.phtml\">", "</a> ")
    if contains(neopoints, ","):
        neopoints = neopoints.replace(",", "")
    return int(neopoints)

def bank_balance(data):
    bank_balance = get_between(data, "<td bgcolor='#ffffff'><b>", " NP</b></td>")
    if contains(bank_balance, ","):
        bank_balance = bank_balance.replace(",", "")
    return int(bank_balance)
