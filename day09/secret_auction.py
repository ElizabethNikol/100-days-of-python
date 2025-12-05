import art

print(art.logo)

bid_dictionary = {}
new_bids = True

while new_bids:
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: $"))

    bid_dictionary[user_name] = user_bid

    user_answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if user_answer == "no":
        new_bids = False

        winner_name = ""
        winner_bid = 0

        for name in bid_dictionary:
            if bid_dictionary[name] > winner_bid:
                winner_name = name
                winner_bid = bid_dictionary[name]

        print(f"The winner is {winner_name} with a bid of ${winner_bid}")

    elif user_answer == "yes":
        print("\n" * 100)
