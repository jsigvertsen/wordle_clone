import wordle

game = wordle.Wordle()

print('---------------------------')
print('     Welcome to Wordle     ')
print('---------------------------')

while True:
    game.player_guess()
    game.display_board()
    if game.check_winner():
        if input('Play again? Enter "Y" or "N": ').lower() == 'y':
            game = wordle.Wordle()
            continue
        else:
            break
