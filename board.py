
class Board():
    def __init__(self):
        self.BOARD_WIDTH = 5

        self.CARD_HEIGHT = 7
        self.CARD_WIDTH = 10

        self.player_1_cards = [None] * self.BOARD_WIDTH
        self.player_2_cards = [None] * self.BOARD_WIDTH

        self.player_1_health = 20
        self.player_2_health = 20

    def print_board(self):

        def get_image(card):
            if card is None:
                return ['.'*(self.CARD_WIDTH) for _ in range(self.CARD_HEIGHT)]
            return str(card).split('\n')
        
        player_1_images = list(map(get_image, self.player_1_cards))
        player_2_images = list(map(get_image, self.player_2_cards))

        def print_wrap(string, wrapper='#'):
            print(wrapper + string + wrapper)

        def print_horizontal_edge():
            print_wrap('X'.join('#'*self.CARD_WIDTH for _ in range(self.BOARD_WIDTH)))

        print(f'PLAYER 1 HEALTH: {self.player_1_health}\n')

        print_horizontal_edge()
        for i in range(self.CARD_HEIGHT):
            print_wrap('#'.join([player_1_images[j][i] for j in range(self.BOARD_WIDTH)]))
        print_horizontal_edge()
        for i in range(self.CARD_HEIGHT):
            print_wrap('#'.join([player_2_images[j][i] for j in range(self.BOARD_WIDTH)]))
        print_horizontal_edge()

        print(f'\nPLAYER 2 HEALTH: {self.player_2_health}')

    def play_turn(self, is_player_1_attack, display=True):
        if is_player_1_attack:
            attacker_cards = self.player_1_cards
            defender_cards = self.player_2_cards
            attacker_health = self.player_1_health
            defender_health = self.player_2_health
        else:
            attacker_cards = self.player_2_cards
            defender_cards = self.player_1_cards
            attacker_health = self.player_2_health
            defender_health = self.player_1_health

        for i in range(self.BOARD_WIDTH):
            if attacker_cards[i] is not None:
                if defender_cards[i] is not None:
                    defender_cards[i].change_health(-attacker_cards[i].get_attack())
                    attacker_cards[i].change_health(-defender_cards[i].get_attack())
                    if attacker_cards[i].get_health() <= 0:
                        attacker_cards[i] = None
                    if defender_cards[i].get_health() <= 0:
                        defender_cards[i] = None
                else:
                    defender_health -= attacker_cards[i].get_attack()

        if is_player_1_attack:
            self.player_1_cards = attacker_cards
            self.player_2_cards = defender_cards
            self.player_1_health = attacker_health
            self.player_2_health = defender_health
        else:
            self.player_1_cards = defender_cards
            self.player_2_cards = attacker_cards
            self.player_1_health = defender_health
            self.player_2_health = attacker_health

        if display:
            print(f'PLAYER 1 ATTACKS' if is_player_1_attack else f'PLAYER 1 DEFENDS')
            self.print_board()
