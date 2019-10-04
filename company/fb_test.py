# BOGO on grapes
# 2 apples to get 20% off
# grapes = 5
# apples = 3
# peach = 7

STOCK = {
  'grapes': 5,
  'apples': 3,
  'peaches': 7
}
# Brute Force solution
def checkout(items):
  # variable store gross price
  gross_cost = 0
  # apple_discounts = False
  # loop input array
  for i in range(len(items)): # O(n) time
    # look for price in the dictionary 
    item = items[i][0]
    # print(item)
    quantity = items[i][1]
    price = STOCK[item]
    
    add_to_total = 0
    # multiply the quantity to the price
    if item == 'apples' and quantity >= 2:
      gross_apple = (price * quantity) * 0.20
      net_apple = (price * quantity) - gross_apple
      add_to_total = net_apple

    elif item == 'grapes' and quantity >= 2:
      odd_man_out = quantity % 2
      # print(odd_man_out)
      actual_grapes = (quantity - odd_man_out) / 2
      add_to_total += (actual_grapes + odd_man_out) * price 

    else:
      add_to_total = quantity * price
      # check if apples quantity is greater than or equal 2
    # condition for grades
    # if item == 'grapes':

    

    gross_cost += add_to_total
    # add it to the gross total

  return gross_cost
  




# 
if __name__ == "__main__":
  print("Total:", checkout([['grapes', 7], ['apples', 7], ['peaches', 7]]))
