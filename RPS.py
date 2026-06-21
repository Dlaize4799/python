
from sys import exit
from random import randint


print('ROCK, PAPER, SCISSORS')

W,L,T = 0,0,0

while True:

    print(str(W)+' Wins, '+ str(L)+' Loses, '+str(T)+' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit ')
    user_played = input('>')
    if user_played== 'p':
        print('PAPER verses ...')
    elif user_played=='r':
         print('ROCK verses ...')
    elif user_played=='s':
         print('SCISSORS verses ...')
    elif user_played=='q':
        print("""You've successfully quited the programme.
        final scores are: """)
        print(str(W)+' Wins, '+ str(L)+' Loses, '+str(T)+' Ties')
        exit() 
    
    print()
    pre_cc = randint(1,3)
    if pre_cc==1 :
        print('PAPER')
    elif pre_cc==2:
        print('ROCK')
    elif pre_cc==3:
        print('SCISSORS')



    if ((user_played=='r' and pre_cc==2) or (user_played=='p' and pre_cc==1) or (user_played=='s' and pre_cc==3)):
        print('It is a tie.')
        T=T+1
    elif user_played=='r' and pre_cc==3:
        print('You win!')
        W = W+1
    elif user_played=='p' and pre_cc==2:
        print('You win!')
        W=W+1
    elif user_played=='s' and pre_cc==1:
        print('You win!')
        W=W+1

    elif user_played=='r' and pre_cc==1:
        print('You lose!')
        L=L+1
    elif user_played=='p' and pre_cc==3:
        print('You lose!')
        L=L+1
    elif user_played=='s' and pre_cc==2:
        print('You lose!')
        L=L+1
