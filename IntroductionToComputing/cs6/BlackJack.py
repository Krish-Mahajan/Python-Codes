

import random


class BlackJack:
    'Python simulation of black jack game'
    
    def shuffledDeck(self):
        'returns shuffled deck'
        # suits is a set of 4 Unicode symbols : black spade and club ,
        # and white diamond and heart 
        
        suits = {'\u2660' , '\u2661' , '\u2662' , '\u2663'}
        ranks = {'2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K' , 'A'}
        deck = [] 
        
        # create deck of 52 cards 
        for suit in suits : 
            for rank in ranks:                       # card is the concatenation of suit and rank
                deck.append(rank + " " +suit) 
                
                
                
        #shuffle the deck and return 
        random.shuffle(deck)
        return deck
    
    
    def dealCard(self,deck , participant):
        'deals single card from deck to participant'
        card = deck.pop()
        participant.append(card)
        return card 
    
    
    def total(self,hand):
        'returns the value of the blackjack hand'
        values = {'2' :2  , '3' :3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8
                  ,'9':9 ,'10':10 , 'J':10 , 'Q':10,'K':10, 'A':11 } 
        result = 0
        numAces = 0
         #add up the values of the cards in the hand 
         # also add the number of aces
        for card in hand:
            result += values[card[0]]
            if card[0] =='A' :
                numAces += 1
                
                
        # while value of hand is > 21 and there is an ace
        # in the hand with value 11 , convert its value to 1
        while result > 21 and numAces > 0:
            result -= 10
            numAces -= 1 
            
        return result
    
    
    def compareHands(self, house, player):
        'compares house and player hands and prints outcome'
        
        # compute house and player hand total 
        
        houseTotal , playerTotal = self.total(house) , self.total(player)
        
        
        if houseTotal > playerTotal :
            print('You lose.')
        elif houseTotal < playerTotal :
            print('You win.') 
        elif houseTotal == 21 and 2 == len(house) < len(player):
            print('You lose.') #house wins with a blackJack
        elif playerTotal ==21 and 2 == len(player) < len(house):
            print('You win.') #playe wins with a blackjac
        else :
            print('A tie.')
    
    def __init__(self):
        'simulates the house in a game of blackJack' 
        deck = self.shuffledDeck() # get shuffled deck 
        
        house = [] # house hand
        player = [] # player hand
        
        for i in range(2):   # dealing initial hands in 2 rounds
            self.dealCard(deck,player)     #deal to player first 
            self.dealCard(deck, house)     #deal to house second
            
        # print hands
        print('House:{:>7}{:>7}'.format(house[0], house[1]))
        print('  You:{:>7}{:>7}'.format(player[0],player[1]))
        
        #while user requests and additional card , house deals it. 
        answer = input('Hit or stand? (default : hit): ')
        while answer in {'' , 'h' ,'hit'}:
            card = self.dealCard(deck,player) 
            print('You got {:>7}'.format(card))
            
            if self.total(player) > 21:  #player total is >21
                print('You went over.. You lose.')
                return 
            
            answer = input('Hit or stand? (default : hit): ')
            
        # house must play the "house rules"
        while self.total(house) < 17:
            card = self.dealCard(deck,house)
            print('House got{:>7}'.format(card))
            
            if self.total(house) > 21 : #house total is > 21 
                print('House went over... You win.')
                return 
        #compare house amd player hands and print result 
        self.compareHands(house,player)
        
        
    
if __name__ == "__main__" :
    bj = BlackJack()
