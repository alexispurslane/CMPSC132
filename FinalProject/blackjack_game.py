from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer  = Dealer()
        self.player_list = [Player(name, self.dealer) for name in player_names]

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        string = ""
        for i in range(0, num_rounds):
            self.dealer.hand = []
            for p in self.player_list:
                p.hand = []
            self.dealer.shuffle_deck()
            # deal first two cards
            for _ in [1, 2]:
                for p in self.player_list:
                    self.dealer.signal_hit(p)
                self.dealer.signal_hit(self.dealer)

            # play out round
            for p in self.player_list:
                p.play_round()
            self.dealer.play_round()

            # score round
            if sum(self.dealer.hand[:2]) == 21:
                for p in self.player_list:
                    if sum(p.hand[:2]) == 21:
                        p.record_tie()
                    else:
                        p.record_loss()
            elif self.dealer.busted:
                for p in self.player_list:
                    p.record_win()
            else:
                for p in self.player_list:
                    if sum(p.hand[:2]) == 21:
                        p.record_win()
                    elif p.busted or p.card_sum < self.dealer.card_sum:
                        p.record_loss()
                    elif p.card_sum > self.dealer.card_sum:
                        p.record_win()
                    elif p.card_sum == self.dealer.card_sum:
                        p.record_tie()

            # build report
            string += f"Round {i + 1}\n"
            string += str(self.dealer) + "\n"
            for p in self.player_list:
                string += str(p) + "\n"
        return string[0:-1]

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        self.dealer  = Dealer()
        self.player_list = [Player(p.name, self.dealer) for p in self.player_list]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
