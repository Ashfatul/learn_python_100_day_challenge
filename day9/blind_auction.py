import random
import time
items = ["Chair", "Table", "Car", "Bike", "Bed", "Furniture", "Gold", "Silver"]
auction_item = random.choice(items)
number_of_bidder = 0
bids = {}
bidder_entry = True
max_bid = 0
winner = ""
print("\n" * 200)
print("=====================================\nWelcome to blind auction\n=====================================")

print(f"Next auction is for: {auction_item}\n\n")

while bidder_entry:
    bidder_dictionary = "bidder" + str(number_of_bidder + 1)
    bids[bidder_dictionary] = {}
    bids[bidder_dictionary]["name"] = input(f"Name for bidder {number_of_bidder + 1}: ").capitalize()
    bids[bidder_dictionary]["bid_amount"] = int(input("Your bid amount: $"))
    number_of_bidder += 1

    continue_entry = input("Add another bidder? (yes/no)").lower()
    
    if continue_entry == "no" or continue_entry == "n":
        print("\n" * 200)
        print("Closing Entry")
        bidder_entry = False
    elif continue_entry == "yes" or continue_entry == "y":
        print("\n" * 200)
        print("Add another entry")

for key in bids:
    if bids[key]["bid_amount"] > max_bid:
        winner = bids[key]["name"]
        max_bid = bids[key]["bid_amount"]

print("And the winnder is: \n==================================")
time.sleep(2)
print(f"\nAuction Item: {auction_item}\nBidder Name: {winner}\nBidding Price: ${max_bid}\nCongratulations! {winner}\n\n")