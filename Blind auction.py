from setuptools.command.install_scripts import install_scripts

from art import logo


print(logo)
print("Welcome to Blind Auction")

bids = {}
is_game_finished = False 

def compare(bidding_record):
    highest_bidder = 0 
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidding_record]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
        print(f"The winner is {bidder} with the highest bid of {highest_bidder}. ")

while not  is_game_finished:
    name = input("Enter your name: ")
    bidding_amount = int(input("Enter your bidding amount: "))
    bids[name] = bidding_amount

    should_continue = input("Are there any other bider? Type 'yes' or 'no' :")
    if should_continue == "no":
        is_game_finished = True 
        compare(bids)
    elif should_continue == "yes":
        print("continue bidding")




