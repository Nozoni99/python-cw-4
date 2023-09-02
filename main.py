def my_name():
    print("My name is Noor")

my_name()
##############################################################

def my_meal (food,drink):

    print(f"I like eating {food} while drinking {drink}")

my_meal("cookies","milkshake")

################################################################

def cube(number):
    return int(number**3)

def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
    
print(by_three(8))
