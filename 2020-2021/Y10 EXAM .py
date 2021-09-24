#this is all of task 1,2 and 3 put together in one file/code. It all works flawlessly together.

import time

# this is so I can use the time.sleep command to slow down the printing of all the items

# task 1 variables: Description, Reserve_price,

item_number_list = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
list_buyer_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_descriptions = []
all_reserve_prices = []
Items = []

# task 1 code, this lets the user input 10 items each with their respective description, name an reserve price

while len(Items) != 10:
   for i in range(10):
       name = str(input("Item Name:"))
       Items.append(name)
       Description = str(input("a small description of the item:"))
       while len(Description) < 10 or len(Description) > 20:
           Description = str(input("Description must be between 10-20 characters:"))
       all_descriptions.append(Description)
       Reserve_Price = float(input("Minimum price ($) to pay for the item?:"))
       while Reserve_Price < 1:
           Reserve_Price = float(input("price ($) must be more than 1:"))
       all_reserve_prices.append(Reserve_Price)

print(all_descriptions)
print(all_reserve_prices)
print(Items)

# task 1 end task 2 variables: finish_bidding, User_buyer_number, Continue_bidding, chosen_item,
# current_bidding_Item, organised_list,Current_Bid ,

number_of_bids_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
highest_bid_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
present_buyers = []

# task 2 code, this is the bidding system where it asks for their buyer number, what item they are bidding on,
# and the bid they are placing. It allows for more than 1 bid to be made at a time and also allows different buyers
# to bid one after the other.

finish_bidding = input("begin bidding?:")
while finish_bidding not in ["no", "Nah", "NO"]:

   User_buyer_number = int(input("what is your buyer number?"))
   while User_buyer_number not in list_buyer_number:
       User_buyer_number = int(input("Invalid number please try again:"))
   present_buyers.append(User_buyer_number)

   for i in range(len(Items)):
       print("Item name:", Items[i])
       time.sleep(0.5)
       print("Item number:", item_number_list[i])
       time.sleep(0.5)
       print("Description:", all_descriptions[i])
       time.sleep(0.5)
       print("Reserve price:$", all_reserve_prices[i])
       time.sleep(0.5)
       print("Current Highest Bid:$", highest_bid_list[i])
       time.sleep(1.5)

   Continue_Bidding = input("continue to bidding?:")
   while Continue_Bidding in ["yes", "Yes", "ye", "yeah"]:
       chosen_item = int(input("Which item are you bidding on?:"))
       if chosen_item not in item_number_list:
           chosen_item = int(input("That number is not on the list:"))
       current_bidding_Item = chosen_item - 100
       organised_list = (list(zip(item_number_list, Items, all_descriptions, all_reserve_prices)))
       bidding = str(organised_list[current_bidding_Item - 1])
       print(*bidding, sep="")
       Current_Bid = int(input("What is your bid?:"))

       if Current_Bid < highest_bid_list[current_bidding_Item - 1]:
           Current_Bid = int(input("your bid has to be more than the current highest bid:"))
       elif Current_Bid > highest_bid_list[current_bidding_Item - 1]:
           highest_bid_list[current_bidding_Item - 1] = Current_Bid
           number_of_bids_list[current_bidding_Item - 1] = number_of_bids_list[current_bidding_Item - 1] + 1

       Continue_Bidding = input("Would you like to bid on another item?")
   finish_bidding = input("begin bidding?")

print(highest_bid_list)

# task 2 end
# task 3 variables: total_fee, percentage_taken,

total_fee = 0
no_bids = []
unsold_items = []
sold_items = []

# task 3 code. this is just simple calculations and final organisation of variables.

for i in range(10):
   if highest_bid_list[i] >= all_reserve_prices[i]:
       all_descriptions[i] = ("SOLD:", all_descriptions[i])
       percentage_taken = int(highest_bid_list[i]) * 0.1
       total_fee = total_fee + percentage_taken
       sold_items.append(item_number_list[i])
       sold_items.append(Items[i])
       sold_items.append(highest_bid_list[i])

   elif highest_bid_list[i] < all_reserve_prices[i]:
       unsold_items.append(item_number_list[i])
       unsold_items.append(highest_bid_list[i])
   if number_of_bids_list[i] == 0:
       no_bids.append(item_number_list[i])

# task 3 end
# displaying the results

print(all_descriptions)
print("$", total_fee)
print("the number of items that got no bids is", len(no_bids))
time.sleep(0.2)
print("the items that got no bids as follows:", no_bids)
time.sleep(0.5)
print("the number of items that were not sold is", int((len(unsold_items) / 2)))
time.sleep(0.2)
print("the items what were not sold as follows:", unsold_items)
time.sleep(0.5)
print("the number of items that were sold is", int((len(sold_items) / 3)))
time.sleep(0.2)
print("the items that were sold as follows:", sold_items)
time.sleep(0.5)

# that's the end of it, only 127 lines as well (95 if you don't count the ignored code and spaces)! gg and good luck
