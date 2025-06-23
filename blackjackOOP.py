import random


coloda = []

for i in range(4):
    coloda.append('King')
    coloda.append('Queen')
    coloda.append('Jack')
    coloda.append('Ace')
    for j in range(1,11):
        coloda.append(j)

random.shuffle(coloda)

def functioncalc(parametr):
    set = 0
    for card in parametr:
            if card == 'King' or card == 'Queen' or card == 'Jack':
                set += 10
            elif card == 'Ace':
                ace11or1 = input('1 or 11: ')
                if ace11or1 == '1':
                    set += 1
                else:
                    set += 11
            else:
                set += card
    return set



class Player:
    def __init__(self, player_id, money, bet):
        self.player_id = player_id
        self.money = money
        self.total = 0 
        if bet > self.money:
            print('Do not have enought money')
        elif bet == self.money:
            print('All in. Are you sure?')
        elif bet < 0:
            print('Cant do like this')
        else:
            self.bet = bet
        self.startset = random.sample(coloda, 2)
    def takecard(self):
        self.total = functioncalc(self.startset)
        while True:
            answer = input('Take card or skip: ')
            if answer == 'skip':
                break
            card = random.sample(coloda, 1)[0]
            self.startset.append(card)
            print(f"You got: {card}")
            self.total = functioncalc(self.startset)


class Dealer:
    def __init__(self):
        self.startsetdealer = random.sample(coloda, 2)
        self.dealerset = functioncalc(self.startsetdealer)
        while self.dealerset < 16:
            card = random.sample(coloda, 1)[0]
            self.startsetdealer.append(card)
            self.dealerset = functioncalc(self.startsetdealer)

def win(dealer12, player12):
    if dealer12.dealerset > player12.total:
        player12.bet = 0
        
    elif dealer12.dealerset == player12.total:
        print('Draw')

    else:
        print('You won')
        player12.money += 2 * player12.bet


player1 = Player(2, 100, 5)
dealer1 = Dealer()

print(f"Player cards: {player1.startset}")
print(f"Dealer cards: {dealer1.startsetdealer}")

player1.takecard()  # Игрок может добирать карты

print(f"Player total: {player1.total}")
print(f"Dealer total: {dealer1.dealerset}")

win(dealer1, player1)

print(f"Player money after game: {player1.money}")
