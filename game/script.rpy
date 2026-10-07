## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

# The script of the game goes in this file.

# Imports
init python: 
    import datetime

# Routine Functions
init python: 
    # Format Player Name (First Letter Upper + Following Letters Lower)
    def format_player_name(raw): 
        raw = raw.strip()
        if not raw: 
            return ""
        return raw[0].upper() + raw[1:].lower()

    # NVL Characters 
    def nvl_char(name, **kwargs): 
        # Transparent "#00000000" color to avoid it printing out on nvl_window
        return Character(name, color="#00000000", kind=nvl, **kwargs) 

    def send_chat(who, what): 
        who(what, interact=False)
        renpy.restart_interaction()

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
default clock = { # Default Scheduled Times of Day
    # Default
    "wake_up": "11:00 AM",
    "work": "11:15 AM",
    "break": "5:00 PM",
    "lounge_arrival": "5:20 PM",
    "mephisto_arrival": "5:30 PM",
    "mephisto_leaves": "8:30 PM",
    "lounge_closes": "9:00 PM",

    # Early Day
    "early": { 
        "wake_up": "10:00 AM",
        "work": "10:15 AM",
        "break": "4:00 PM",
        "lounge_arrival": "4:20 PM"
    },

    # Special Occasion
    "special": { 
        "lounge_closes": "8:00 PM",
    }
}
default abyss_time = "3:00 AM"
default day = 1

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mephisto", color="#0000ff")
define t = Character("Theo", color="#890095")
define v = Character("Victor", color="#009500")
define c = Character("[player_name]", color="#950000")

define chat_t = nvl_char("And")
define chat_c = nvl_char("The Abyss Stares Back")
define chat_l = nvl_char("Golden Manager")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Loading Screen 

    # Warning Screen 

    # Black Screen 

    # Day 1 (Demo) Start

    call demo_intro # script/demo/demo_intro.rpy

    ```W.I.P```

    # This ends the game.

    return
