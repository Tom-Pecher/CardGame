
class Board():
    def __init__(self):
        self.BOARD_WIDTH = 5
        self.CARD_HEIGHT = 7
        self.CARD_WIDTH = 10
        self.player_1_cards = [None] * self.BOARD_WIDTH
        self.player_2_cards = [None] * self.BOARD_WIDTH

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

        print_horizontal_edge()
        for i in range(self.CARD_HEIGHT):
            print_wrap('#'.join([player_1_images[j][i] for j in range(self.BOARD_WIDTH)]))
        print_horizontal_edge()
        for i in range(self.CARD_HEIGHT):
            print_wrap('#'.join([player_2_images[j][i] for j in range(self.BOARD_WIDTH)]))
        print_horizontal_edge()
        