import random
import time

n = random.randint(4,30)
print("Count  n = ", n)
bot = random.randint(0,1)
time.sleep(0.5)
if (bot == 1 ):
    while(n>1):
        if(n == 3 ):
            x= random.randint(1,2)
        elif (n==2):
            x=1
        else:
           x = random.randint(1,3)
        n = n - x
        time.sleep(0.5)
        print("Bot took %d " %x)
        if(n==1):

            print("Bot is win!")
            exit(0)
        time.sleep(1)
        print("N = %d" %n)
        time.sleep(0.5)
        print("Took 1-3  ")
        while(1):
           try:
              x1 = int(input())
           except ValueError:
               print("Error! You didn't enter a number")
               continue
           if (x1 < 0 or x1 > 3):
               print("TOOK 1-3!!!")
               continue
           else:
               break
        n= n - x1
        if(n==1):
            print("Player win!")
            exit(0)
        print("N = %d" %n)
else:
    while(n>1):
        time.sleep(0.5)
        print("Took 1-3 ")
        while(1):
            try:
                x1=int(input())
            except ValueError:
                print("Error! You didn't enter a number")
                continue
            if (x1 < 1 or x1 > 3):
                print("TOOK 1-3!!!")
                continue
            else:
                break
        n=n-x1
        if(n==1):
            print("Player is win!!!")
            exit(0)
        time.sleep(0.5)
        print("N = %d" %n)
        time.sleep(0.5)
        if(n==3):
            x=random.randint(1,2)
        elif(n==2):
            x=1
        else:
            x=random.randint(1,3)
            print("Bot took %d" %x)
        time.sleep(0.5)
        n=n-x
        print("N = %d" %n)
        time.sleep(0.5)
        if(n==1):
            print("Bot is wins!")
            exit(0)

























