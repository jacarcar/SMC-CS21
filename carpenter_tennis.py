# Jake Carpenter
# CS 21, Fall 2018
# Program: tennis

from random import random

# plays a single game
def play_game(prob_a):
    a=0
    b=0
    points = ['0','15','30','40']
    # plays the game until someone wins or it goes into deuce
    while a<=3 and b<=3 and (a!=3 or b!=3):
        # see who won the point
        if random() < prob_a:
            a+=1
        else:
            b+=1
        # tell the score
        if a<4 and b<4:
            print('Current score:',points[a]+'-'+ points[b])
    # checks if the game is at deuce
    if a==b:
        print('Deuce')
        # continues the game in deuce
        while a!=b+2 and b!=a+2:
            # see who won the point
            if random() < prob_a:
                a+=1
            else:
                b+=1
            # checks if back at deuce or who has advantage or if someone won
            if a==b:
                print('Deuce')
            elif a==(b+1):
                print('Advantage Player A')
            elif a==(b+2):
                None
            elif b==(a+2):
                None
            else:
                print('Advantage Player B')
        # checks who won the deuce
        if a>b:
            # tells that player A won this game
            print('Winner: Player A \n')
            return('A')
        else:
            # tells that player B won this game
            print('Winner: Player B \n')
            return('B')
    # checks who won the game
    elif a>b:
        # tells that player A won this game
        print('Winner: Player A \n')
        return('A')
    else:
        # tells that player B won this game
        print('Winner: Player B \n')
        return('B')

# shows the overall wins and what percentage player A won
def print_summary(num_a_wins, num_b_wins):
    # prints the results
    print('Here are the results:')
    print('Player A won', num_a_wins,'games.')
    print('Player B won', num_b_wins,'games.')
    percent = num_a_wins/(num_a_wins+num_b_wins)*100
    print('Player A won {0:0.1f}'.format(percent) +'% of the games.')

# plays the specified number of games with the specified probability
def play_games(num_games,prob_a):
    num_a_wins = 0
    num_b_wins = 0
    # plays all the games
    for i in range(num_games):
        if play_game(prob_a) == 'A':
            num_a_wins += 1
        else:
            num_b_wins += 1
    # returns how many wins each player had
    return(num_a_wins, num_b_wins)

# prints an intro telling how the game works
def print_intro():
    print('This program takes the diference in skill level of the players')
    print('to determine the outcome of a tennis match in any number of')
    print('games in tennis')

# gets the inputs from the user
def get_inputs():
    # checks to see if the inputs are valid
    num_games = 0
    while num_games < 1:
        try:
            num_games = int(input('Enter a positive number of games: '))
        except ValueError:
            print('The input should have been an integer.')
    #checks if the inputs are valid
    prob_a = -1
    while 0 > prob_a or prob_a > 1:
        try:
            prob_a = float(input('Probability that A wins each point' +
                                 ' between 0 and 1: '))
        except ValueError:
            print('The input should have been a float.')
    # returns the inputs to use in other function(s)
    return(num_games,prob_a)

def main():
    # puts all the functions together to run as one funciton
    print_intro()
    num_games, prob_a = get_inputs()
    num_a_wins, num_b_wins = play_games(num_games,prob_a)
    print_summary(num_a_wins,num_b_wins)
    
main()
