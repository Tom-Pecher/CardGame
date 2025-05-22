
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

c3 = Card(
    attack=1,
    health=10,
    pattern=(
        '--*-//',
        '-F-//-',
    )
)

b = Board()
b.player_1_cards[0] = c1
b.player_2_cards[0] = c3
b.player_2_cards[2] = c2

b.print_board()
for i in range(3):
    print('\n\n' + '='*70 + '\n\n')
    b.play_turn(is_player_1_attack=(i%2==0))
