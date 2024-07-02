import argparse
import random
import string
from rich.console import Console
from rich.prompt import Prompt
import pyfiglet



console=Console()

def gen_random_word():
  words_list = [
    "able", "acid", "aged", "also", "amen", "arch", "atom", "avid", "axle", "axis",
    "badge", "baker", "bald", "bass", "beam", "bent", "biker", "bird", "blot", "boil",
    "cabin", "cage", "calm", "canal", "carol", "chief", "clay", "climb", "craft", "crawl",
    "daisy", "dance", "dawn", "decoy", "demon", "donor", "drift", "drive", "dusty", "eagle",
    "early", "earth", "erase", "error", "event", "exist", "fable", "false", "farmer", "fence",
    "final", "flute", "foggy", "force", "frail", "frost", "giant", "glide", "grain", "guest",
    "habit", "happy", "hazel", "hefty", "honor", "hotel", "human", "humor", "ideal", "image",
    "jolly", "joint", "juicy", "jumbo", "karma", "knock", "labor", "laser", "lemon", "level",
    "magic", "major", "mango", "medal", "merit", "merry", "model", "music", "noble", "nurse",
    "oasis", "olive", "opera", "orbit", "other", "piano", "pilot", "pixel", "plaid", "plant",
    "quack", "queen", "quick", "quiet", "quote", "radar", "radio", "rally", "raven", "rebel",
    "saber", "saint", "scale", "scarf", "scope", "scout", "shame", "sharp", "shelf", "shine",
    "siren", "skate", "slice", "smart", "snack", "spicy", "spine", "spoon", "stake", "steel",
    "table", "tango", "teach", "theme", "torch", "tough", "trace", "trade", "uncle", "unity",
    "urban", "valid", "vapor", "venue", "video", "vivid", "voice", "wager", "waste", "water",
    "wheel", "whale", "witty", "xerox", "yacht", "yield", "young", "zebra", "zesty", "zoom",
    "abide", "acute", "adopt", "agile", "alert", "amber", "amuse", "angel", "apple", "array",
    "award", "banjo", "batch", "bento", "blame", "bliss", "blush", "brave", "brick", "brisk",
    "buddy", "candy", "carve", "charm", "cheer", "chime", "civil", "clean", "clerk", "cling",
    "coast", "comic", "crane", "cream", "crisp", "crown", "curse", "cycle", "dairy", "debit",
    "debut", "defer", "demon", "diary", "disco", "dizzy", "dream", "drift", "drone", "dwarf",
    "eager", "early", "elbow", "emote", "empty", "enjoy", "equal", "essay", "event", "exact",
    "extra", "fairy", "favor", "ferry", "fiber", "fifty", "filth", "flame", "flask", "float",
    "foamy", "forge", "forum", "fresh", "front", "fudge", "funny", "genre", "giant", "glory",
    "grade", "grain", "grape", "grass", "guide", "habit", "happy", "heart", "honey", "honor",
    "hotel", "human", "ideal", "image", "index", "ivory", "jolly", "joint", "judge", "juice",
    "jumbo", "karma", "kayak", "keen", "knock", "laser", "lemon", "level", "lunar", "lunch",
    "magic", "major", "mango", "medal", "merit", "metal", "model", "music", "noble", "nurse",
    "oasis", "opera", "orbit", "other", "piano", "pilot", "pixel", "plaid", "plant", "queen",
    "quick", "radio", "rally", "raven", "rebel", "saint", "scale", "scarf", "scope", "scout",
    "shame", "sharp", "shine", "siren", "skate", "smart", "spicy", "spoon", "stake", "steel",
    "table", "tango", "teach", "theme", "torch", "trace", "trade", "uncle", "urban", "valid",
    "vapor", "venue", "video", "voice", "wager", "waste", "water", "wheel", "whale", "witty",
    "xerox", "yacht", "yield", "young", "zebra", "zesty", "zoom"]
  
  return random.choice(words_list)

# this game has three helper dunctions one is_palyer won here will see if all thr letters in the guessed letters are in the secret word
def is_player_won(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

# the second helper function is to check the word progress if the guessed word present in the secret word then will append the progress wirth the guesses letter other wise will append * for wrong guess
def word_progress(secret_word, letters_guessed):
    progress = ""
    for i in secret_word:
        if i in letters_guessed:
            progress += i
        else:
            progress += "*"
    return progress

#the letters guessed in the game and the available letters after guessing the letter
def get_available_letters(letters_guessed):
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters


# the hangman function
def hangman(secret_word, help_enabled):
    guesses_remaining = 10
    letters_guessed = []
    console.print(f"The secret word is a {len(secret_word)}-lettered word.", style="bold cyan")
    if help_enabled:
        console.print("Type '!' to get a hint (costs 3 guesses).", style="bold yellow")

    while guesses_remaining > 0 and not is_player_won(secret_word, letters_guessed):
        console.print("=============================================", style="bold magenta")
        console.print(f"Guesses remaining: {guesses_remaining}", style="bold green")
        console.print("Available letters:", get_available_letters(letters_guessed), style="bold blue")
        guess = Prompt.ask("Please guess a letter").lower()

        if guess == '!' and help_enabled:
            if guesses_remaining >= 3:
                hint_letters = [letter for letter in secret_word if letter not in letters_guessed]
                if hint_letters:
                    hint_letter = random.choice(hint_letters)
                    letters_guessed.append(hint_letter)
                    console.print(f"Hint letter: {hint_letter}", style="bold yellow")
                    guesses_remaining -= 3
                    console.print(f"Your word progress is: {word_progress(secret_word, letters_guessed)}", style="bold cyan")
                else:
                    console.print("No hint available.", style="bold red")
            else:
                console.print(f"Sorry, not enough guesses remaining ({guesses_remaining}).", style="bold red")
        elif not guess.isalpha() or len(guess) != 1:
            console.print("Please enter a valid single alphabet.", style="bold red")
        elif guess in letters_guessed:
            console.print(f"You have already guessed this letter. Your word progress is: {word_progress(secret_word, letters_guessed)}", style="bold red")
        elif guess in secret_word:
            letters_guessed.append(guess)
            console.print(f"You guessed correctly! Your word progress is: {word_progress(secret_word, letters_guessed)}", style="bold green")
        else:
            letters_guessed.append(guess)
            console.print(f"Sorry, that letter is incorrect. Your word progress is: {word_progress(secret_word, letters_guessed)}", style="bold red")
            guesses_remaining -= 2 if guess in 'aeiou' else 1

    if is_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = guesses_remaining + 4 * unique_letters + 3 * len(secret_word)
        console.print("=========================================", style="bold magenta")
        console.print("Congratulations, you won the game!", style="bold green")
        console.print(f"Your total score is {score}", style="bold cyan")
    else:
        console.print(f"You lost the game. The secret word was '{secret_word}'.", style="bold red")

def main():
    console.print(pyfiglet.figlet_format("Hangman", font="slant"), style="bold magenta")
    console.print("Welcome to Hangman!", style="bold cyan")
    help_enabled = True
    help_response = Prompt.ask("Press Y for assistance in the game, N for not required").strip().lower()
    while help_response not in ['y', 'n']:
        help_response = Prompt.ask("Invalid input. Please press Y for assistance in the game, N for not required").strip().lower()

    if help_response == 'y':
        console.print("---Good Choice! You are now assisted throughout the game---", style="bold green")
        help_enabled = True
    elif help_response == 'n':
        console.print("---Good Choice! You are not assisted throughout the game---", style="bold yellow")
        help_enabled = False
    secret_word = gen_random_word()
    hangman(secret_word, help_enabled)

