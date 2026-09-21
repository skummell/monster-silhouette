## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

# The script of the game goes in this file.

# Internal States 
# Hidden Flags 
default true_name = False
default early_day = False
default suck_up = False 
default theo_chat_volume = False 
default wallet_on_person = False 
default semiformal_top = False
default contour_top = False 
default many_pockets = False 
# Stats
default rapport = None
default suspicion = None
default deadline = 7 
# Visible Flags 
default player_name = ""
default date = "Sep 26"
default time = "3:00 AM"
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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "mephisto happy.png" to the images
    # directory.

    show mephisto happy

    c "hey"

    # These display lines of dialogue.

    m "You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    m "shdkshds"

    m "dsbmdbs"

    m "hdkshkdsha"

    m "dksahkkdshads"

    m " dhskadk"

    m "dhskadhs"

    m "hkashdksjhfkahfkshfkhdkjfdhs"

    m "dhskadskua d"

    m "shdkshds"

    m "dsbmdbs"

    m "hdkshkdsha"

    m "dksahkkdshads"

    m " dhskadk"

    m "dhskadhs"

    m "hkashdksjhfkahfkshfkhdkjfdhs"

    m "dhskadskua d"

    m "shdkshds"

    m "dsbmdbs"

    m "hdkshkdsha"

    m "dksahkkdshads"

    m " dhskadk"

    m "dhskadhs"

    m "hkashdksjhfkahfkshfkhdkjfdhs"

    m "dhskadskua d"

    m "shdkshds"

    m "dsbmdbs"

    m "hdkshkdsha"

    m "dksahkkdshads"

    m " dhskadk"

    m "dhskadhs"

    m "hkashdksjhfkahfkshfkhdkjfdhs"

    m "dhskadskua d"

    m "shdkshds"

    m "dsbmdbs"

    m "hdkshkdsha"

    m "dksahkkdshads"

    m " dhskadk"

    m "dhskadhs"

    m "hkashdksjhfkahfkshfkhdkjfdhs"

    m "dhskadskua d"

    # This ends the game.

    return
