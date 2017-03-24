#_*_ coding:utf-8 _*_

# learn python guess number

from random import randint

import time



total = 0    #总轮数

times = 0    #猜对次数

t1 = time.time()   #开始时间

while True:
    
    choice = input('1.start the game; 2.exit\n')

    if str(choice)=='1':

        number = randint(1,100)

        total += 1
        
        guess_time = 0

        while guess_time<5:

            guess_time +=1

            guess = input('please guess the number(1-100):')

            if guess<number:

                print'too small'

            elif guess>number:

                print 'too big'

            if guess == number:

                times += 1

                print 'Great, You are right!'

                break
        
            if guess_time == 5:

                print 'guess failed, the number is:',number

                break
    
    
    if str(choice)=='2':

        t2 = time.time()    #结束时间

        if total != 0:

            ratio = times*100.0/total

            print 'You have played %.2f second'% (t2-t1)

            print 'play games %d times, success %d times, success ratio %.2f%%' %(total,times,ratio)

        break




    
