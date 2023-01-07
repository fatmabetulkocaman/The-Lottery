import random

def lottery():
    for i in range(6):
        lot = random.randint(1,100)

        print(lot, end =" ")

print("The Lottery\n") 
lottery()