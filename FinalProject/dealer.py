from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self):
        super().__init__("Dealer", None)
        self.deck = CardDeck()

    def shuffle_deck(self):
        """
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> str(dealer.deck)[0:20]
        '10 8 10 6 8 9 3 10 2'
        """
        self.deck.shuffle()

    def signal_hit(self, player):
        """
        A method called by players when they want to hit
        Player objects should pass their `self` references to this method
        Should deal one card to the player that signalled a hit

        These doctests will not run properly if the `deal_to` method 
        in the `Player` class is not properly implemented

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, None)
        >>> dealer.signal_hit(player)
        >>> player.hand
        [10]
        """
        card = self.deck.draw()
        if card:
            player.deal_to(card)

    def play_round(self):
        """
        A dealer should hit if his hand totals to 16 or less

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> dealer.play_round()
        >>> dealer.hand
        [10, 8]
        """
        while not self.busted and self.card_sum <= 16:
            self.signal_hit(self)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
