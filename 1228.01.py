from random import shuffle

class Card:
    suits = ["spades","hearts","diamonds","clubs"]

    values = [None, None,
              "2","3","4","5","6","7","8","9",
              "10","Jack","Queen","King","Ace"]

    def __init__(self ,v ,s ):
        """スート（マーク）も値です"""
        self.value = v
        self.suit = s

    def __lt__(self ,c2 ):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self ,c2 ):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __str__(self):
        v = self.values[self.value] + " of "\
            + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i ,j ))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
class Player:
    def __init__(self, name):
        self.wins = 0
        self.name = name
        self.card = None

    def draw(self, deck: Deck):
        self.card = deck.rm_card()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(input("プレイヤー１の名前: "))
        self.p2 = Player(input("プレイヤー２の名前: "))

    def printAction(self, fmt, *args):
        print(fmt.format(*args))

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay"
            response = input(m)
            if response == 'q':
                break
            self.p1.draw(self.deck)
            self.p2.draw(self.deck)
            self.printAction("{}は{}、{}は{}を引きました", self.p1.name, self.p1.card,
                             self.p2.name, self.p2.card)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.printAction("このラウンドは{}が勝ちました", self.p1.name)
            else:
                self.p2.wins += 1
                self.printAction("このラウンドは{}が勝ちました", self.p2.name)

        print("ゲーム終了、{}の勝利です！".format(self.judgeWinner(self.p1, self.p2)))

    def judgeWinner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()