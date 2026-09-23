## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

# The script of the game goes in this file.

# Imports
init python: 
    import datetime

# Utility Functions
init python: 

    def show_scene(screen_name):     
        renpy.scene(layer="master") # Clear Layer
        renpy.show_screen(screen_name, _layer="master") # Call Screen on Master (Scene) Layer

# Internal States 
# Hidden Flags 
default true_name = False # Affects Player Character POV narration, Dialogue options and more
default early_day = False # Affects time you arrive in Victor's lounge
default suck_up = False # Unlocks and locks dialogue options in chat with Theo
default theo_chat_volume = False # Affects how often Theo sends you messages without being prompted
default wallet_on_person = False # Affects some scenes and narration in the lounge
default semiformal_top = False # Extra Character Dialogue
default contour_top = False # Extra Character Dialogue
default many_pockets = False # Extra scenes
# Stats
default rapport = None # Affects Mephisto's attitude towards you 
default suspicion = None # Affects Player's attitude towards Mephisto 
default deadline = 7 # Progresses to next game day 
# Visible Flags 
default player_name = ""
default abyss_date = datetime.date(2025, 9, 26) # (Fri) Sep 26
default abyss_time = "3:00 AM"
default day = 1

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mephisto", color="#0000ff")
define t = Character("Theo", color="#890095")
define v = Character("Victor", color="#009500")
define c = Character("[player_name]", color="#950000")

define chat_t = Character("And", color="#890095", kind=nvl)
define chat_c = Character("The Abyss Stares Back", color="#950000", kind=nvl)
define chat_l = Character("Golden Manager", color="#ffb700", kind=nvl)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    call demo_intro

    # This ends the game.

    return
