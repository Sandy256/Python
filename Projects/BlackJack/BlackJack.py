import random

playing = True
suits = ('Черви', 'Буби', 'Пики', 'Крести')
ranks = ('Двойка', 'Трока', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка',
         'Валет', 'Дама', 'Король', 'Туз')
values = {'Двойка': 2, 'Трока': 3, 'Четверка': 4, 'Пятерка': 5, 'Шестерка': 6, 'Семерка': 7, 'Восьмерка': 8, 'Девятка': 9,
         'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return f'{self.deck[0]}'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.card.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces +=1

    def adjast_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('Сколько фишек поставить?'))

        except:
            print('Введите число')

        else:
            if chips.bet > chips.total:
                print(f'Недостаточно фишек. Доступно {chips.total} фишек')
            else:
                break


def hit(deck, hand):

    x = deck.deal()
    hand.add_card(x)


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Взять доп.карту (h), остаться при своих (s)')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Игрок остается при своих картах. Ход диллера.')
            playing = False
        else:
            print('Ответ непонятен, введите h или s')
            continue
        break

def show_all(player, dealer):
    print('\nКарты Диллера:', *dealer.card, sep='\n')
    print('Карты Диллера =', dealer.value)
    print('\nКарты Игрока:', *player.card, sep='\n')
    print('Карты Игрока =', player.value)

def show_some(player, dealer):
    print('\nКарты Диллера:')
    print('<карта срыта>')
    print(dealer.card[1])
    print('\nКарты Игрока:', *player.card, sep='\n')

def player_busts(player, dealer, chips):
    print('\nИгрок проиграл. Превышение суммы 21 для Игрока')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('\nИгрок выйграл')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('\nДиллер привысил сумму 21')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('\nДиллер выйграл')
    chips.lose_bet()

def push(player, dealer):
    print('\nНичья')

chips = Chips()
print('\nДобро пожаловать путник, перекинемся в картишки!')
print('\nВыигрывает тот кто будет ближе к 21, если больше, проигрыш.')
#Игра
while True:

    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()
    chips.bet = int(input(f'\nСколько хочешь поставить? У тебя {chips.total} фишек!'))

    hit(deck, player)
    hit(deck, player)

    hit(deck, dealer)
    hit(deck, dealer)
    show_some(player, dealer)
    while playing:
        hit_or_stand(deck, player)
        show_some(player, dealer)
        if player.value > 21:
            player_busts(player, dealer, chips)
            break
    if player.value <=21:

        while dealer.value < 17:
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, chips)
        elif dealer.value < player.value:
            player_wins(player, dealer, chips)
        else:
            push(player, dealer)

    print(f'\nУ тебя осталось {chips.total} фишек')

    new_game = input('Может еще разок? y или n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Ну и проваливай!')
        break

