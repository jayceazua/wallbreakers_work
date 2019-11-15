"""
Yelp has a product, "Yelp waitlist", that lets parties join the waitlist to be seated at th restaurant.
You are given an initial list of parties in the waitlist, each party having a "name", "size", and "time"
which is the time the party has waited in seconds. You can assume the "name" for a party is unique.


Question

Part 1
Let's implement seating a party from a waitlist. For this, we want to find a party who has waited the longest and has a size 
less than or equal to the capacity of the table, and remove them from the waitlist. 
Your solution should print the name of the party so that the host can then find them.

Sample waitlist data:
{
  "size" : 2,
  "name" : "Hammy Hamster",
  "time" : 100
},
{
  "size" : 4,
  "name" : "Darwin Dog",
  "time" : 200
}

Part 2
Some restaurants are small and only want to seat a party if their size exactly matches the size of the table.
Larger restaurants want to seat the first party from the waitlist whose size is less than or equal to the table.
Regardless of the restaurant size, if a party has waited more than 30 minutes and a table opens ip that can fit them
we seat that party.


Part 3
Our product team did some research and discovered that many restaurants have at least 1 communal table. 
When a party gets up from a communal table, we can seat multiple parties so long as the total size of the parties is less than the capacity.
Given our desire for small restaurants to maximize table usage and large retaurants to minimize party wait times, how
can we accomodate "communal tables" into our implementation?
"""

# Part 1

waitlist = [{
    "size": 2,
    "name": "Hammy Hamster",
    "time": 100
},
    {
    "size": 4,
    "name": "Darwin Dog",
    "time": 200
}]

capacity = 4

def solution(waitlist, capacity):
  pass
