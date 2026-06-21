import random, sys, time

WIDTH = 80 # The number of columns

try:
    columns=[0]*WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02 : # Generates a float from [0.0,1.0)
                columns[i]=random.randint(4,14)

            if columns[i] ==0:
                print(' ', end="")
            else:
                print(random.choice([0,1]),end='')
                columns[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
    