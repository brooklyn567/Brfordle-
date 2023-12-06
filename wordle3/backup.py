import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30
WORD_LIST = ["apple", "banana", "cherry", "orange", "grape"]

# Functions
def draw_word(word, guesses):
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    return display_word

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle Game")
clock = pygame.time.Clock()

# Game variables
target_word = random.choice(WORD_LIST)
guesses = set()
max_attempts = 6

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in range(97, 123):  # Check if a valid letter key is pressed
            letter = chr(event.key)
            guesses.add(letter)

    # Draw background
    screen.fill(WHITE)

    # Draw target word
    font = pygame.font.Font(None, FONT_SIZE)
    word_display = draw_word(target_word, guesses)
    text = font.render(word_display, True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

    # Draw guessed letters
    guessed_text = font.render("Guessed: " + ", ".join(guesses), True, BLACK)
    screen.blit(guessed_text, (10, HEIGHT - FONT_SIZE - 10))

    # Draw remaining attempts
    attempts_text = font.render(f"Attempts left: {max_attempts - len(set(guesses).difference(set(target_word)))}", True, BLACK)
    screen.blit(attempts_text, (WIDTH - attempts_text.get_width() - 10, HEIGHT - FONT_SIZE - 10))

    # Check for win or loss
    if set(target_word) == guesses:
        print("You win!")
        running = False
    elif len(set(guesses).difference(set(target_word))) >= max_attempts:
        print("You lose! The word was:", target_word)
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()