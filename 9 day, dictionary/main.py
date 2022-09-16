def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        big_amount = bidding_record[bidder]
        if big_amount > highest_bid:
            highest_bid = big_amount
            winner_name = bidder
    print(f"The winner is {winner_name} with a bid of {highest_bid}")


def main():
    bids = {}
    bids_finished = False

    while not bids_finished:
        name = input("What is your name?\n")
        price = int(input("What is your bid?\n"))
        bids[name] = price
        should_continue = input("Are there any other bidders& Type 'yes' or 'no'.\n")
        if should_continue == "no":
            bids_finished = True
            find_highest_bidder(bids)


if __name__ == '__main__':
    main()

