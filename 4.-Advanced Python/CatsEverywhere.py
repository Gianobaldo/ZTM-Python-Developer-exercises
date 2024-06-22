# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
#SCROLL FOR ANSWERS

# 1 Instantiate the Cat object with 3 cats.
persian = Cat('Poppy', 3)
ragdoll = Cat('Misty', 2)
toyger = Cat('Nidalee',5)

# 2 Create a function that finds the oldest cat.
allCats = [persian,ragdoll,toyger]
def oldestCat(allCats)
  oldest_cat = allCats[0]
  for cat in allCats:
    if cat.age > oldest_cat:
      oldest_cat = cat
  return oldest_cat


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
oldest = oldestCat(allCats)
print("The oldest cat is ", oldest.age, ' years old.')
