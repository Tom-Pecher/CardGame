
from card import Card
from board import Board


c1 = Card(
    attack=4,
    health=2,
    pattern=(
        '-x*x--',
        '--O-H-',    )
)
c2 = Card(
    attack=3,
    health=6,
    pattern=(
        '--*-//',
        '-F-//-',
    )
)

b = Board()
b.player_1_cards[0] = c1
b.player_2_cards[2] = c2
b.print_board()
