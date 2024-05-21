import os

keep_bidding = "yes"
person_bid = {}

while keep_bidding == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    person_bid[name] = bid
    keep_bidding = input("Will there be any more bids?(yes or no): ").lower()

if keep_bidding == "no":
   os.system('cls' if os.name == 'nt' else 'clear')
   highest_bidder = max(person_bid, key=person_bid.get)


print(f"The winner of the auction is {highest_bidder}")





