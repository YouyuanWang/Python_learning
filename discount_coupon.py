# coding: utf-8
'''
design 200 discount coupon, consist of english characters ,
each one with 8 characters

'''
import random
import string

total_coupon = set()
character = string.ascii_letters

while len(total_coupon)<200:
    coupon = set()

    while len(coupon)<8:
        coupon.add(random.choice(character))
    coupon = '-'.join(coupon)
    total_coupon.add(coupon)
print 'The 200 coupons are:'
for i in total_coupon:
    print i
   
    
