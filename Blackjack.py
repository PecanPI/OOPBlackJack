import numpy as np
class deck():
    def __init__(self):
        """
        creates a deck of 52 cards with 4 suits
        """
        self.cards = []
        self.build()

    def build(self):
        """
        builds a deck of 52 cards, self.cards, in order with 4 suits
        """
        suits = {'s','c','d','h'}
        for i in range(1, 14):
            for j in suits:
                self.cards.append(card(i,j))
    def shuffle(self):
        """
        shuffles self.cards
        """
        np.random.shuffle(self.cards)

    def drawCard(self):
        """Return the card on the top of the deck

        """
        return self.cards.pop()


class card():
    """
    card object stores number and suit of each card

    """
    def __init__(self, number, suit):
        self.number = number 
        self.suit = suit
    def __repr__(self):
        if self.suit == 's':
            return f"%s of Spades" % self.number
        elif self.suit == 'h':
            return f"%s of Hearts" % self.number 
        elif self.suit == 'c':
            return f"%s of Clubs" % self.number
        elif self.suit == 'd':
            return f"%s of Diamonds" % self.number 
    def __str__(self):
        if self.suit == 's':
            return f"%s of Spades" % self.number 
        elif self.suit == 'h':
            return f"%s of Hearts" % self.number 
        elif self.suit == 'c':
            return f"%s of Clubs" % self.number 
        elif self.suit == 'd':
            return f"%s of Diamonds" % self.number 

class player():
    """
    player stores self.name, self.hand, self.tot, self.bust
    """
    def __init__(self, name):
        """
        self.name - string player name
        self.hand - list of cards
        self.tot - int, total value of hand
        self.bust - boolean, true if total > 21 
        """
        self.name = name
        self.hand = []
        self.tot = 0 ### TODO make total account for ace as 1 or 11
        self.bust = False
    def draw(self, deck):
        """
        draws a card and adds it to players hand
        deck - deck object
        """
        self.hand.append(deck.drawCard())
    def total(self):
        #TODO Make total account for Aces as 1 or 11
        self.tot = 0
        for i in self.hand:
            if i.number < 10:
                self.tot += i.number
            else:
                self.tot += 10
        return self.tot
    def showHand(self):
        """prints the cards in players hand
        """
        print(self.name, "'s hand is:")
        for card in self.hand:
            print(card)
        self.total()
        print('Total is ', self.tot)
        print()
    def newGame(self):
        """
        resets variables to intial values
        """
        self.hand = []
        self.tot = 0
        self.bust = False
class dealer(player):
    """
    extension of player class
    """
    pass

def gameloop(player1, dealer1):
    """
    Loops through game until player breaks loop
    """
    while True:
        print()
        cards = deck()
        cards.shuffle()
        player1.draw(cards)
        dealer1.draw(cards)
        player1.draw(cards)
        dealer1.draw(cards)
        player1.showHand()
        dealer1.showHand()
        while True:
            move = input(f'%s hit or stay? \n' %player1.name)
            if move =='hit':
                player1.draw(cards)
                player1.showHand()
            else:
                break
            checkbust(player1)
            if player1.bust:
                print(player1.name, 'Busts :( \n')
                break
        print()
        while not player1.bust:
            if dealer1.tot <= 16:
                print('Dealer hits')
                dealer1.draw(cards)
                dealer1.showHand()
            else:
                break
            checkbust(dealer1)
            if dealer1.bust:
                print(dealer1.name, 'Busts :( \n')
                break
        if not dealer1.bust or player1.bust:
            checkWinner(player1, dealer1)
        
        if input('Play again(y/n) \n') == 'y':
            player1.newGame()
            dealer1.newGame()
        else:
            break

def checkWinner(p, d):
    """
    takes two players and prints the player with highest score, does not
    account for busts
    #TODO make checkWinner check for bust
    """
    if p.tot > d.tot:
        print(p.name, " is the Winner!!")
    else:
        print('Dealer wins!')

def checkbust(player):
    """
    checks for player bust, sets player.bust = True if player busts
    """
    if player.tot > 21:
        player.bust = True
def main():
    """
    main starts program
    """
    print('Welcome to Blackjack \n')
    print()
    gameloop(player(str(input('Who is playing? \n'))), dealer('Dealer'))
    print('Thanks for Playing!')

    


if __name__ == '__main__':
    main()



    
