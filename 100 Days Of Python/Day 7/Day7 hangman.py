import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
for letter in chosen_word:
    display += '_'
life = 7
win = False
lose = False
end_of_game = False
wrong_guess = []
print(hangman_art.logo)
print(display)
while end_of_game == False:
    guess = input("To play, choose a letter:\n").lower()
    if len(guess) > 1:
        print("only one letter please")
    if guess in display:
        print(f'You have already guessed {guess} try again.')
    if guess in wrong_guess:
        print(f'You have already guessed {guess} try again.')
    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                if '_' not in display:
                    win = True
                    end_of_game = True 
        print(f'{display}\nCorrect!\n')        
    elif guess not in chosen_word and len(guess) == 1:
        life -= 1
        wrong_guess.append(guess)
        print(hangman_art.stages[life])
        print(display)
        print(f'{guess} was not in the word\n')
        if life == 0:
            lose = True
            end_of_game = True 
if win == True:
    print("you win")
if lose == True:
    print("You lose!")