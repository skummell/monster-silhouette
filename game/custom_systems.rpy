## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

## This file contains Custom Statements for Game Systems used in this project
## Mainly to interact with different systems through easy to use statements 
## inside of the script
## Usage intented for inside labels for script
##
## List of Game Systems currently handled: 
##      Chat System 
##      Scene System
##      Button Disabler System 
##
## List of Statements currently registered: 
##      chat_start "contact"    - begin recording chat range 
##      chat_end "contact"      - end recording chat range
##      show_scene "screen"     - shows a screen on the scene layer (acts exactly like scene "picture.png")
##      show_app "app_screen"   - show a app screen on the scene layer (above current scene or show_scene)
##      hide_app "app_screen"   - hide app screen on scene layer
##
## List of Game System Utility Functions:
##      show_scene(screen_name)     - show a screen on scene (master) layer
##      show_app(screen_name)       - show a app screen on scene (master layer) on top of current scene
##      hide_app(screen_name)       - hide a app screen on scene (master layer)
##      get_chat_entries(contact)   - read chat entries / history linked to contact 
##
## List of Debugger / Helper Functions:
##      button_disabled
##        (button=None, report=True)
##          - Check whether a button is disabled or not 
##          - (boolean & report on inner flags printed to console)
##      button_disabler_status
##        (global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=False)
##          - Check button disabler status 
##          - (prints organized list of status of disablers to console)

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
##      "narration 1"
##      nvl_character "message 3" (records)
##      "narration 2"
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

## Chat Timestamp flags
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

        ## Timestamps
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
            ## Grab corresponding timestamp
            ts = chat_timestamps.get(contact, [])[i]

            ## If timestamp date not empty append date value
            if ts[1]: 
                result.append({"type": "date", "value": ts[1]})
            
            ## Append time value
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
##
## Usage format: 
##      show_scene "screen"     # Show screen as scene 
##      character "line 1"
##      "narration 1"
##      character "line 2"
##      "narration 2"
##      "narration 3"
##      show_app "app_screen"   # Shows app_screen on top of scene (below dialogue)
##      "narration 4"
##      "narration 5"
##      hide_app "app_screen"   # Hides app_screen on top of scene
##

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

    ## show_app "app_screen"
    def parse_show_app(lex): 
        screen = lex.string()
        lex.eol()
        return screen

    def execute_show_app(app_screen):
        show_app(app_screen) 

    renpy.register_statement(
        name = "show_app", 
        parse = parse_show_app,
        execute = execute_show_app,
    )

    ## hide_app "app_screen"
    def parse_hide_app(lex): 
        screen = lex.string()
        lex.eol()
        return screen

    def execute_hide_app(app_screen): 
        hide_app(app_screen)

    renpy.register_statement(
        name = "hide_app",
        parse = parse_hide_app, 
        execute = execute_hide_app,
    )

## Call Screens on Master (Scene) Layer
init python: 

    ## Show a screen on scene (master) layer 
    ## Acts like a classic scene and clears master layer to replace 
    ## previous scenes and prevent endless stacking

    def show_scene(screen_name):     
        renpy.scene(layer="master") # Clear Layer
        renpy.show_screen(screen_name, _layer="master") 

    ## Show a screen above the current scene on the scene (master) layer
    ## and below the dialogue (say screen, which is on a layer above scene)
    ## Intended for modal screens (specifically app screens)
    def show_app(screen_name): 
        renpy.show_screen(screen_name, _layer="master") 

    ## Hide a screen on the scene (master) layer 
    ## Intended for screens shown through show_app
    ## As those shown with show_scene will get replaced by any new scene 
    #3 shown automatically
    def hide_app(screen_name): 
        renpy.hide_screen(screen_name, layer="master")

################################################################################
## Button Disabler System ######################################################
##
## Tracks, disables and enables buttons that can be disabled
##
## Usage format: 
##      

## Disable Buttons through the appropriate channels
init python: 

    ## Turn on global disabler
    ## Prevents all valid buttons (for disabling) from working
    ## Does not touch lower levels
    def global_disable(): 

        store.disable_buttons = True

    ## Turn off global disabler
    ## Buttons may still be disabled by lower levels
    def global_enable(): 

        store.disable_buttons = False

    ## Turn on all disablers
    ## Disables all buttons in all levels 
    def all_disabled(): 
        ## Turn on global disabler
        store.disable_buttons = True 

        ## Turn on all button type disablers
        for t in disabled_button_types:
            disabled_button_types[t] = True

        ## Turn on all button id disablers
        for t in valid_button_ids:
            disabled_button_ids[t] = set(valid_button_ids[t])
    
    ## Turn off all disablers (global, button type, button ids)
    ## Enables all buttons in all levels
    def all_enabled(): 
        ## Turn off global disabler 
        store.disable_buttons = False 

        ## Turn off all button type disablers 
        for t in disabled_button_types:
        disabled_button_types[t] = False

        ## Turn off all button id disablers
        for t in disabled_button_ids:
            disabled_button_ids[t] = set()

    ## Turn on button type disabler
    ## Prevents valid buttons (for disabling) of button type from working
    ## Does not touch lower levels but bubbles up to higher levels
    def disable_type(button_type): 

        # Invalid input 
        if button_type not in valid_button_ids:
            print(f"'{button_type}' is not a valid button type.")
            return

        # Turn on global disabler if it's not already on
        if not disable_buttons:
            store.disable_buttons = True

        # Turn on button type disabler for 'button_type'
        disabled_button_types[button_type] = True

    ## Turn off button type disabler
    ## Buttons may still be disabled by lower levels
    def enable_type(button_type): 

        # Invalid input
        if button_type not in valid_button_ids:
            print(f"'{button_type}' is not a valid button type.")
            return

        # Turn off global disbaler if it's not already off
        if disable_buttons:
            store.disable_buttons = False

        # Turn off button type disabler for 'button_type'
        disabled_button_types[button_type] = False

    ## Turn on button id disabler
    ## Prevent button of (valid) button id from working
    ## Bubbles up to higher levels 
    def disable_button(id): 

        ## Invaid input 
        if not any(id in valid_button_ids[t] for t in valid_button_ids):
            print(f"'{id}' is not a valid button id.")
            return

        ## Grab button type of button id
        button_type = next((t for t in valid_button_ids if id in valid_button_ids[t]), None)

        ## Add button id to set of disabled button ids
        if id not in disabled_button_ids[button_type]:
            disabled_button_ids[button_type].add(id)

        ## Turn on button type disabler if it's not already on
        if not disabled_button_types[button_type]:
            disabled_button_types[button_type] = True

        ## Turn on global disabler if it's not already on
        if not disable_buttons:
            store.disable_buttons = True

    ## Turn on all button disablers for button type
    ## Disables button type in all levels
    def disable_all_type(button_type): 
        # Invalid input 
        if button_type not in valid_button_ids:
            print(f"'{button_type}' is not a valid button type.")
            return

        ## Turn on global disabler
        store.disable_buttons = True
        
        ## Turn on button type disabler for 'button_type'
        disabled_button_types[button_type] = True

        ## Turn on all button id disablers for 'button_type'
        disabled_button_ids[button_type] = set(valid_button_ids[button_type])

    ## Turn off all button disablers for button type
    ## Enables button type in all levels
    def enable_all_type(button_type): 

        ## Invalid input 
        if button_type not in valid_button_ids:
            print(f"'{button_type}' is not a valid button type.")
            return
        
        ## Turn off global disabler
        store.disable_buttons = False

        ## Turn off button type disabler for 'button_type'
        disabled_button_types[button_type] = False

        ## Turn off button id disables for 'button_type'
        disabled_button_ids[button_type] = set()

    ## Turn off button id disabler
    ## Enables button id in all levels
    def enable_button(id): 

        ## Invalid input 
        if not any(id in valid_button_ids[t] for t in valid_button_ids):
            print(f"'{id}' is not a valid button id.")
            return

        ## Grab button type of button id
        button_type = next((t for t in valid_button_ids if id in valid_button_ids[t]), None)

        ## Remove button id from set of disabled button ids if it's there
        if id in disabled_button_ids[button_type]:
            disabled_button_ids[button_type].discard(id)

        else:
            ## If button_type set is empty 
            ## add all other valid buttons to button_type set except button id
            if not disabled_button_ids[button_type]:
                for other_id in valid_button_ids[button_type]:
                    if other_id != id:
                        disabled_button_ids[button_type].add(other_id)

        # Turn off button type disabler if it's not already off
        if disabled_button_types[button_type]:
            disabled_button_types[button_type] = False

        # Turn off global disabler if it's not already off
        if disable_buttons:
            store.disable_buttons = False
    

## Helper / Debug Functions 
##   button_disabled(button=None, report=True)
##   button_disabler_status(global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=False)
##
## Usage format: 
##      
##      (In console)
##
##      button_disabled: 
##          (Optionally can be used in a if statement since it returns a boolean)
##
##          (Note: if button is not a valid button type or button id it will return 1)
##
##          default parameters : button=None, report=True
##
##
##          button_disabled() - boolean check if global disabler is on or off
##              prints report on console stating whether buttons are globally disabled or not
##          button_disabled(button_type) - boolean check if button type is disabled or not
##              prints report on console stating how button type is disabled
##              through global disabler, button type disabler or both
##              or says it's enabled
##          button_disabled(button_id) - boolean check if button is disabled r noto
##              prints report on console stating how button id is disabled
##              through global disabler, button type disabler, button id disabler
##              a combination of two or all three 
##              or says it's enabled
##          button_disabled(report=false) - to disabler console report prints 
##
##      button_disabler_status: 
##          (Console only. It doesn't return anything. It only prints to console)
##
##          (status report is a organized list of all disablers, divided in groups between those who 
##          are disabled and those who aren't)
##
##          default parameters : 
##              global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=True
##
##          
##          button_disabler_status() -
##              prints out a full status report of button disablers in all levels
## 
##          button_disabler_status(global_btn=False) -
##              does not print out report on global button disabler status
##          button_disabler_status(btn_type=False) -
##              does not print out report on button type disabler status
##          button_disabler_status(btn_id=False) -
##              does not print out report on button id disabler status
##          (if global_btn=False, btn_type=False and btn_id=False it will be treated as though global_btn=True)
##          
##          button_disabled_status(disabled=False) - 
##              does not print out report on disabled button types and ids
##          button_disabled_status(enabled=False) - 
##              does not print out report on enabled button types and ids
##          (if both disabled=False and enabled=False it will be treated as though disabled=True)
##          (no effect if btn_type and btn_id are both set to False)
##
##          button_disabled_status(inline=True) - 
##              make status report for button type and button id disablers
##              print in a line (per button type for the button id disabler)
##               to prevent taking up space vertically on console print

init python: 

    ## Boolean check whether a button, button type or global disabler is disabled 
    ## leave button parameter empty if you want to check global disabler
    ## report=False if you don't want the report to print on console 
    def button_disabled(button=None, report=True):

        ## Searching by button type or button id
        if button != None:

            ## 'button' is a button type - Searching by button type
            if button in valid_button_ids:

                ## Disabled through global disabler
                if disable_buttons:
                    msg = f"Buttons of '{button}' type are DISABLED globally.\n\n"

                    msg += "Flags:\n"
                    msg += "  - global button disabler (True)\n"

                    # AND Disabled through button type
                    if disabled_button_types[button]:
                        msg += f"  - {button} type disabler (True)"
                    else:
                        msg += f"  - {button} type disabler (False)"

                    if report:
                        print(msg)

                    return True

                else:

                    ## Disabled through button type
                    if disabled_button_types[button]:
                        msg = f"Buttons of '{button}' type are DISABLED.\n\n"

                        msg += "Flags:\n"
                        msg += "  - global button disabler (False)\n"
                        msg += f"  - {button} type disabler (True)"

                        if report:
                            print(msg)

                        return True

                    else:
                        msg = f"Buttons of '{button}' type are ENABLED.\n\n"

                        msg += "Flags:\n"
                        msg += "  - global button disabler (False)\n"
                        msg += f"  - {button} type disabler (False)"

                        if report:
                            print(msg)

                        return False

            ## 'button' is a button id
            elif any(button in valid_button_ids[t] for t in valid_button_ids):

                ## Grab button type of button id
                button_type = next((t for t in valid_button_ids if button in valid_button_ids[t]), None)

                ## Disabled through global disabler
                if disable_buttons:
                    msg = f"Button '{button}' of '{button_type}' is DISABLED globally.\n\n"

                    msg += "Flags:\n"
                    msg += "  - global button disabler (True)\n"

                    ## AND Disabled through button type disabler
                    if disabled_button_types[button_type]:
                        msg += f"  - {button_type} type disabler (True)\n"

                        ## AND Disabled through button id disabler
                        if any(button in disabled_button_ids[t] for t in disabled_button_ids):
                            msg += f"  - {button} id disabler (True)"
                        else:
                            msg += f"  - {button} id disabler (False)"

                    else:
                        msg += f"  - {button_type} type disabler (False)\n"

                        if any(button in disabled_button_ids[t] for t in disabled_button_ids):
                            msg += f"  - {button} id disabler (True)"
                        else:
                            msg += f"  - {button} id disabler (False)"

                    if report:
                        print(msg)

                    return True

                else:
                    ## Disabled through button type disabler
                    if disabled_button_types[button_type]:
                        msg = f"Button '{button}' of '{button_type}' is DISABLED by {button_type} type.\n\n"

                        msg += "Flags:\n"
                        msg += "  - global button disabler (False)\n"
                        msg += f"  - {button_type} type disabler (True)\n"

                        if any(button in disabled_button_ids[t] for t in disabled_button_ids):
                            msg += f"  - {button} id disabler (True)"
                        else:
                            msg += f"  - {button} id disabler (False)"

                        if report:
                            print(msg)

                        return True

                    else:
                        ## Disabled through button id disabler
                        if any(button in disabled_button_ids[t] for t in disabled_button_ids):
                            msg = f"Button '{button}' of '{button_type}' is individually DISABLED.\n\n"

                            msg += "Flags:\n"
                            msg += "  - global button disabler (False)\n"
                            msg += f"  - {button_type} type disabler (False)\n"
                            msg += f"  - {button} id disabler (True)"

                            if report:
                                print(msg)

                            return True

                        else:
                            msg = f"Button '{button}' of '{button_type}' is ENABLED.\n\n"
                            msg += "Flags:\n"
                            msg += "  - global button disabler (False)\n"
                            msg += f"  - {button_type} type disabler (False)\n"
                            msg += f"  - {button} id disabler (False)"

                            if report:
                                print(msg)

                            return False
            
            ## Invalid Parameter
            else:
                msg = f"'{button}' is not a valid button type or button id."

                if report:
                    print(msg)

                return 1

        ## Search Global Disabler only
        else:
            if disable_buttons:
                msg = "Buttons are DISABLED globally."

                if report:
                    print(msg)

                return True

            else:
                msg = "Buttons are NOT disabled globally."

                if report:
                    print(msg)

                return False

    ## Check for disable status of buttons 
    ## Returns an global button status and a organized list of button types and button ids 
    ## global_btn, btn_type, btn_id = False 
    ##   if you don't the Global, Type, Individual status of buttons respectively
    ##      if you set both of them to False it will be treated as though global_btn is True
    ##
    ## enabled, disabled = False
    ##   if you don't want the enabled or disabled list of button types or button ids 
    ##       if you set both of them to False it will be treated as though disabled is True
    ##   
    def button_disabler_status(global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=False):

        report = ""

        if not global_btn and not btn_type and not btn_id: 
            global_btn = True

        if global_btn:
            if disable_buttons:
                report += "Buttons are Globally DISABLED."
            else:
                report += "Buttons are Globally ENABLED."
            
            report += "\n\n"

        if btn_type:

            if not disabled and not enabled:
                disabled = True

            disabled_types = [t for t in disabled_button_types if disabled_button_types[t]]
            enabled_types = [t for t in disabled_button_types if not disabled_button_types[t]]

            if disabled_types and disabled:
                report += "The following button types are DISABLED:\n"

                if inline:
                    report += "    " + ", ".join(f"'{t}'" for t in disabled_types)
                else:
                    report += "\n".join(f"    '{t}'" for t in disabled_types)

                report += "\n\n"

            if enabled_types and enabled:
                report += "The following button types are ENABLED:\n"

                if inline:
                    report += "    " + ", ".join(f"'{t}'" for t in enabled_types)
                else:
                    report += "\n".join(f"    '{t}'" for t in enabled_types)

                report += "\n\n"

        if btn_id:

            if not disabled and not enabled:
                disabled = True

            disabled_btns = [(t, disabled_button_ids[t]) for t in disabled_button_ids if disabled_button_ids[t]]
            enabled_btns = [id for t in valid_button_ids for id in valid_button_ids[t] if id not in disabled_button_ids[t]]

            if disabled_btns and disabled:
                report += "The following button ids are DISABLED:\n\n"

                for t, ids in disabled_btns:
                    if inline:
                        report += f"    '{t}': " + ", ".join(f"'{id}'" for id in ids) + "\n"
                    else:
                        report += f"    '{t}':\n"
                        report += "\n".join(f"        '{id}'" for id in ids)
                        report += "\n"

                report += "\n"

            if enabled_btns and enabled:
                report += "The following button ids are ENABLED:\n\n"

                if inline:
                    report += "    " + ", ".join(f"'{id}'" for id in enabled_btns)
                else:
                    report += "\n".join(f"    '{id}'" for id in enabled_btns)

                report += "\n"

        print(report)