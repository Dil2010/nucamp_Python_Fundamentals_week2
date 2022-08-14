import random

r=random.randint(1,6)

print("You roll the die...it lands with", r,"pips showing")

prize=['car','pony','lion','monkey']

k=random.choice(prize)

print("You turn the wheel of fortune", k,"this is the prize")

card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


random.shuffle(card)

print("The card set after suffling is", card)