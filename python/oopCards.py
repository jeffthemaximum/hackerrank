class Deck(object):
    pass


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Ace(Card):
    def __init__(self, rank, suit):
        Card.__init__(self, rank, suit)


class FaceCard(Card):
    def __init__(self, rank, suit):
        Card.__init__(self, rank, suit)
