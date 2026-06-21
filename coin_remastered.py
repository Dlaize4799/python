from random import randint

total_chance_of_streak = 0
coin_readings=[]
no_of_streaks = 0
NO_OF_EXP = 10000

for exp_no in range(NO_OF_EXP):

    for j in range(0,100):
        flip_no=randint(0,1)
        if flip_no == 0:
            coin_readings.append('T')
        else:
            coin_readings.append('H')
        
    for i in range(0,95):
        if (coin_readings[i:i+6] == (['H']*6) or
         coin_readings[i:i+6] == (['T']*6)):
            no_of_streaks += 1
            break        # break, to speed up.
        
    coin_readings=[]

Chance = (no_of_streaks/(NO_OF_EXP))
print(Chance)