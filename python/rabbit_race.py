import random
import time
import os

# --- Game Setup ---
# You can change these values to customize the game
RACE_LENGTH = 50
RABBIT_A_NAME = "Flash"
RABBIT_B_NAME = "Sheldon"
RABBIT_A_ICON = '🐇'
RABBIT_B_ICON = '🐢'

# Starting positions
pos_a = 0
pos_b = 0

def clear_screen():
    """Clears the console screen for a clean animation effect."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def print_race_track(name, icon, position):
    """Prints a single racer's progress bar."""
    # Create the track with dots
    track = ['.'] * RACE_LENGTH
    
    # Place the racer on the track, making sure it doesn't go out of bounds
    if position < RACE_LENGTH:
        track[position] = icon
    else:
        # If racer finishes, place them at the end
        track[RACE_LENGTH - 1] = icon

    # Print the racer's name and their track
    print(f"{name.ljust(8)}: |{''.join(track)}| 🏁")


# --- The Race Begins ---
clear_screen()
print(f"🏁 THE GREAT RACE: {RABBIT_A_NAME} the {RABBIT_A_ICON} vs. {RABBIT_B_NAME} the {RABBIT_B_ICON} 🏁")
input("Press Enter to start the race...")

# The main game loop. It continues as long as neither racer has finished.
while pos_a < RACE_LENGTH and pos_b < RACE_LENGTH:
    clear_screen()

    # --- Move the racers ---
    # Flash (the rabbit) is fast but sometimes naps (big moves or no move)
    move_a = random.choice([0, 0, 1, 2, 6, 7])
    pos_a += move_a

    # Sheldon (the tortoise) is slow but very steady (small, consistent moves)
    move_b = random.choice([1, 2, 2, 3, 3])
    pos_b += move_b

    # --- Display the current race state ---
    print("--- GO! GO! GO! ---")
    print_race_track(RABBIT_A_NAME, RABBIT_A_ICON, pos_a)
    print_race_track(RABBIT_B_NAME, RABBIT_B_ICON, pos_b)
    print("-" * (RACE_LENGTH + 15))
    print(f"{RABBIT_A_NAME} is at position {pos_a}. {RABBIT_B_NAME} is at position {pos_b}.")

    # Pause the program for a moment to create a sense of speed and animation
    time.sleep(0.4)

# --- Announce the Winner ---
print("\n" + "="*30)
print("           RACE FINISHED!")
print("="*30)

if pos_a >= RACE_LENGTH and pos_b >= RACE_LENGTH:
    print("It's a PHOTO FINISH! A tie! 🤯")
elif pos_a >= RACE_LENGTH:
    print(f"🎉 {RABBIT_A_NAME} the {RABBIT_A_ICON} is the winner! 🎉")
else:
    print(f"🎉 {RABBIT_B_NAME} the {RABBIT_B_ICON} is the winner! 🎉")