## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

## This file contains Custom Statements for Game Systems used in this project
## Mainly to interact with different systems through easy to use statements 
## inside of the script
##
## List of Statements currently registered: 
##      chat_start "contact"    - begin recording chat range 
##      chat_end "contact"      - end recording chat range
##      show_scene "screen"     - shows a screen on the scene layer (acts exactly like scene "picture.png")
##      show_app "screen"       - show a app screen on the scene layer (above current scene or show_scene)
##      show_app_e "screen"     - same as above but enables app screen exit button 
##      hide_app "screen"       - hide app screen on scene layer
##
## List of Game System Utility Functions
##      get_chat_entries(contact)   - read chat entries / history linked to contact 
##      show_scene                  - show a screen on scene (master) layer
##      show_app
##      hide_app

################################################################################
## Chat System #################################################################
##
## Tracks chat conversation ranges in script so Chat App can render 
## per-conversation history and stay accurate across save / load. 
##
## Usage format: 
##      chat_start "contact"
##      nvl_character "message 1" (records)
##      nvl_character "message 2" (records)
##      no_character "narration 1"
##      nvl_character "message 3" (records)
##      no_character "narration 1"
##      chat_end "contact"

init offset = -1 

## Chat Range Storage 
## chat_ranges = { "And": [(0, 5), (12, 18)], "Golden Manager": [(6, 11)], ...}
## (start_index, end_index)
default chat_ranges = {}

# Chat Timestamps Storage
## chat_timestamps = { "And": [(0, "Fri Sep 26", " 3:00 AM"), (12, "", " 5:00 PM")]}
## (start_index, abyss_date if changed from last date saved otherwise blank, abyss_time)
default chat_timestamps = {}

## Temporary state between chat_start and chat_end
default _chat_start_index = None 
default _chat_start_contact = None

## In Chat Flag 
default _in_chat_block = False

# Chat Timestamp flags
default _chat_time_change = False
default _chat_date_change = True

## Chat System Statements 
python early: 
    
    ## chat_start "contact"
    def parse_chat_start(lex): 
        contact = lex.string()
        lex.eol()
        return contact 

    def execute_chat_start(contact): 
        store._chat_start_index = len(_history_list)
        store._chat_start_contact = contact 
        store._in_chat_block = True

        # Timestamps
        existing = store.chat_timestamps.get(contact, [])
        last_date = next((e[1] for e in reversed(existing) if e[1]), None) # Last non empty date

        store._chat_date_change = (last_date != store.abyss_date)
        store._chat_time_change = True

    renpy.register_statement(
        name = "chat_start",
        parse = parse_chat_start, 
        execute = execute_chat_start,
    )

    ## chat_end "contact"
    def parse_chat_end(lex): 
        contact = lex.string()
        lex.eol()
        return contact 

    def execute_chat_end(contact):

        if contact != store._chat_start_contact:
            raise Exception(
                "chat_end contact (%r) doesn't match chat_start (%r)"
                % (contact, store._chat_start_contact)
            )

        store.chat_ranges.setdefault(contact, []).append(
            (store._chat_start_index, len(_history_list))
        )

        if store._chat_date_change:
            date = date = store.abyss_date.strftime("%a, %b %d")  # "Fri, Sep 26" etc
        else:
            date = ""

        if store._chat_time_change:

            time = store.abyss_time
        else:
            time = ""

        store.chat_timestamps.setdefault(contact, []).append(
            (store._chat_start_index, date, time)
        )

        store._chat_start_index = None
        store._chat_start_contact = None
        store._in_chat_block = False
        store._chat_date_change = False
        store._chat_time_change = False

        if renpy.get_screen("chat_app", layer="master"): 
            # Enable Exit Button
            show_app("chat_app")

    renpy.register_statement(
        name = "chat_end",
        parse = parse_chat_end,
        execute = execute_chat_end,
    )

## Chat History Reader
init python: 
    def get_chat_entries(contact): 
        """
        Returns a list of HistoryEntry objects belong to `contact`, 
        concatenated from all its recorded ranges in script order, 
        filter to kind == "nvl"
        """

        result = []

        for i, (start, end) in enumerate(chat_ranges.get(contact, [])):
            # Grab corresponding timestamp
            ts = chat_timestamps.get(contact, [])[i]

            # If timestamp date not empty append date value
            if ts[1]: 
                result.append({"type": "date", "value": ts[1]})
            
            # Append time value
            result.append({"type": "time", "value": ts[2]})

            for h in _history_list[start:end]: 
                if h.kind == "nvl": 
                    result.append(h) # Flag type message

        return result

################################################################################
## Scene System ################################################################
##
## Allows Screens to be treated the same way as Scenes by putting them in the 
## Master (Scene) Layer 

## Scene System Statements 
python early: 
    
    ## show_scene "screen"
    def parse_show_scene(lex): 
        screen = lex.string()
        lex.eol()
        return screen 

    def execute_show_scene(screen): 
        show_scene(screen)

    renpy.register_statement(
        name = "show_scene",
        parse = parse_show_scene, 
        execute = execute_show_scene,
    )

    ## show_app "screen"
    ## show_app_e "screen"
    def parse_show_app(lex): 
        screen = lex.string()
        lex.eol()
        return screen

    def execute_show_app(screen): # Disabled Exit Button
        show_app(screen, True) 

    def execute_show_app_e(screen): # Enabled Exit Button
        show_app(screen)

    renpy.register_statement(
        name = "show_app", 
        parse = parse_show_app,
        execute = execute_show_app,
    )

    renpy.register_statement(
        name = "show_app_e", 
        parse = parse_show_app,
        execute = execute_show_app_e,
    )

    ## hide_app "screen"
    def parse_hide_app(lex): 
        screen = lex.string()
        lex.eol()
        return screen

    def execute_hide_app(screen): 
        hide_app(screen)

    renpy.register_statement(
        name = "hide_app",
        parse = parse_hide_app, 
        execute = execute_hide_app,
    )

# Call Screens on Master (Scene) Layer
init python: 

    # Show a screen on scene (master) layer 
    # Acts like a classic scene and clears master layer to replace 
    # previous scenes and prevent endless stacking

    def show_scene(screen_name):     
        renpy.scene(layer="master") # Clear Layer
        renpy.show_screen(screen_name, _layer="master") 

    # Show a screen above the current scene on the scene (master) layer
    # Intended for modal screens (specifically app screens)
    # Enables app screen exit button by default 
    # Use disabled=True to disable the exit button 
    def show_app(screen_name, disabled=False): 
        renpy.show_screen(screen_name, _layer="master", disable=disabled) 

    # Hide a screen on the scene (master) layer 
    # Intended for intended for screens shown through show_app
    # As those shown with show_scene will get replaced by any new scene 
    # shown automatically
    def hide_app(screen_name): 
        renpy.hide_screen(screen_name, layer="master")