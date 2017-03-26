# coding: utf-8


import random

cardType = ("Heart", "Plum", "Diamond", "Spade")
cardNum = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

card_list = []
for i in cardType:
    for j in cardNum:
        card_list.append([i,j])
card_list.append(["King","Red"])
card_list.append(["King","Black"])

for k in range(5):
    # 洗五次牌
    random.shuffle(card_list)


player_one = card_list[0:17]
player_two = card_list[17:34]
player_three = card_list[34:51]
cover_card = card_list[51:54]


print "the card for player_one:"

for i in player_one:
    print i
print

print "the card for player_two:"
for i in player_two:
    print i
print

print "the card for player_three:"
for i in player_three:
    print i
print

print "the cover_card:"
for i in cover_card:
    print i
