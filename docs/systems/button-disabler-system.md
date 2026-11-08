---
icon: lucide/mouse-pointer-2-off
# status: modified
tags: 
    - Coding
    - ㅤLast Updated
    - ㅤㅤOctober 
    - ㅤㅤㅤ31
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If the date matches up with the last date-range entry in the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Button Disabler System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

The Button Disabler System is a custom game system in Monster Silhouette that controls button interactivity across the entire game 
through three independent disabler levels. 

Rather than hardcoding `sensitive False` directly into screen definitions — which would 
require manual management and create conflicts during script execution — this system provides a centralized set of statements and 
functions that toggle button states cleanly from script, screens, and Python code alike.
Every button that participates in this system is registered in `valid_button_ids` under its respective assigned button type. 

Disabling can happen at three levels: globally across all buttons, per type across all buttons of a given type, or individually 
per button ID. 
Each level operates independently — disabling at a higher level overrides lower levels, but enabling at a level 
only clears that level's disabler without affecting others.

??? info "Components Overview Legend"

    === "Legend"

        <p id="components-overview-legend"></p>

        | :lucide-variable: | :lucide-function-square: | :lucide-square-play: | 
        | ----------------- | ------------------------ | -------------------- |
        | Variable          | Function                 | Statement            |
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-wrench:  | :lucide-bug:      | :lucide-zodiac-libra:            |
        | ------------------------------------- | ---------------- | ----------------- | -------------------------------- |
        | Required argument/parameter           | Utility function | Debugger function | Function equivalent to statement |

    === "Go To Component Overviews"

        !!! cards col single no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards col three centered-content ""

                    -   :lucide-variable: **Disable Buttons**
                        [][disable-buttons]{ .card-link }
                    
                    -   :lucide-variable: **Disabled Button Types**
                        [][disabled-button-types]{ .card-link }
                    
                    -   :lucide-variable: **Disabled Button IDs** 
                        [][disabled-button-ids]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-variable: **Valid Button IDs**
                        [][valid-button-ids]{ .card-link }

                    -   :lucide-variable: **App To Exit**
                        [][app-to-exit]{ .card-link }

                !!! cards centered-content ""

                    -   :lucide-function-square: **Button Disabled** 
                        [][button-disabled]{ .card-link }
                    
                    -   :lucide-function-square: **Button Disabler Status** 
                        [][button-disabler-status]{ .card-link }
                
                !!! cards col four centered-content ""

                    -   :lucide-square-play: **Disable Global** 
                        [][disable-global]{ .card-link }
                    
                    -   :lucide-square-play: **Enable Global** 
                        [][enable-global]{ .card-link }
                    
                    -   :lucide-square-play: **Disable All** 
                        [][disable-all]{ .card-link }
                    
                    -   :lucide-square-play: **Enable All** 
                        [][enable-all]{ .card-link }
                
                !!! cards col four centered-content ""

                    -   :lucide-square-play: **Disable Type** 
                        [][disable-type]{ .card-link }

                    -   :lucide-square-play: **Enable Type** 
                        [][enable-type]{ .card-link }

                    -   :lucide-square-play: **Disable All Type** 
                        [][disable-all-type]{ .card-link }

                    -   :lucide-square-play: **Enable All Type** 
                        [][enable-all-type]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-square-play: **Disable ID** 
                        [][disable-id]{ .card-link }

                    -   :lucide-square-play: **Enable ID** 
                        [][enable-id]{ .card-link }

=== "How It Works"

    !!! tip "Learn more about the Scene System in the [Scene System][scene-system] page"

    ## How It Works 

    The system resolves whether a button is disabled by checking three conditions in order: the global disabler, 
    the button type disabler, and the button ID disabler. If any one of them is active for a given button, the button is 
    considered disabled. 

    Screens check this via `button_disabled()` and respond with `NullAction()` rather than `sensitive False`, which preserves hover 
    events while blocking click functionality.

    `valid_button_ids` is the roster — a dictionary mapping button type names to sets of valid button IDs. 
    Any button type or ID not registered here will be rejected with a console printed error when passed to a statement or function. 
    This prevents silent failures from typos or unregistered buttons.

    `app_to_exit` maps each app button ID to its corresponding exit button ID. 
    This is used by the Scene System's `show_app` and `hide_app` statements to automatically sync exit button state with app visibility.

    === "Global Level"

        ### Global Level

        The global disabler is a single boolean — `disable_buttons` — that when `True` disables all registered buttons regardless 
        of any other disabler state. It is the highest priority level and overrides everything below it.

        At Global Level,
        `disable_buttons` can be toggled on or off in different parts of the code or script using one of four functions/statements 
        — `disable_global`, `enable_global`, `disable_all`, or `enable_all` — rather than having to reassign the 
        variable a value directly. 

        Disabling globally (`disable_global`) only turns on `disable_buttons`.
        
        Enabling globally (`enable_global`) only turns off `disable_buttons`. 
        <br>
        Button type and ID disablers are left untouched — meaning buttons may still be disabled through those levels after the 
        global disabler is cleared.

        `disable_all` turns on all three levels simultaneously. 
        
        `enable_all` clears all three levels simultaneously.

    === "Type Level"

        ### Type Level

        The type disabler is a dictionary — `disabled_button_types` — with one boolean per registered button type. 
        When a type's disabler is `True`, all buttons of that type are disabled regardless of their individual ID disabler state.

        At Type Level, 
        `disabled_button_types` key values can be toggled on or off in different parts of the code or script using one of four 
        functions/statements — `disable_type`, `enable_type`, `disable_all_type`, or `enable_all_type` — 
        rather than having to reassign the variable's keys a value directly. 

        Disabling a type (`disable_type`) turns on that type's disabler. 

        Enabling a type (`enable_type`) turns off that type's disabler and also clears the global disabler if it was on. 
        ID disablers for buttons of that type are left untouched.

        `disable_all_type` turns on both the type disabler and all ID disablers for that type. 
        
        `enable_all_type` clears the type disabler, all ID disablers for that type, and the global disabler.

    === "ID Level"

        !!! tip "Learn more about the Freeze System in the [Freeze System][freeze-system] page"

        !!! tip "Learn more about the Chat System in the [Chat System][chat-system] page"

        ### ID Level

        The ID disabler is a dictionary — `disabled_button_ids` — mapping each button type to a set of individually disabled button IDs. 
        A button whose ID is in its type's set is disabled regardless of whether the type disabler is on or off.

        At ID Level, 
        `disabled_button_ids` can be added to or popped in different parts of the code or script using one of two functions/statements
        — `disable_id` or `enable_id` — rather than having to assign or remove a value from the variable directly. 

        Disabling an ID (`disable_id`) adds the button's ID to the disabled set it belongs to. 

        Enabling an ID (`enable_id`) removes the button's ID from the disabled set. 
        
        If the type disabler for that button's type is on and the disabled set is empty, it adds all other buttons of that type to the 
        disabled set before turning off the type disabler — effectively enabling just that one button while keeping the rest disabled. 
        It also clears the global disabler if it was on.

        This makes `enable_id` the standard tool for “enable one specific button while everything else stays locked” — 
        which is the common pattern used during Freeze blocks and chat blocks.

=== "Components"

    ??? info "About Button Disabler System Functions"

        The Button Disabler System's functions are all equivalent to their statement counterparts. 
        
        Exceptions include the two functions that serve as debugger functions and have no statement counterparts.

    ## Components 

    Overview of the three components (**variables**, **functions** and **statements**) of the Button Disabler System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Button Disabler System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details (**Init Value** if not Dictionary)
        - **Keys** (for Dictionaries)
            - Hover over cards for **Init Value(s)**
        - Methods to **Toggle On** and **Toggle Off** (for disablers)
            - Hover over cards for details on each method
        - **Notes**
        
        === "Disablers"
        
            #### Disable Buttons

            ??? grid col single "Disable Buttons [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable Buttons Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `disable_buttons`
                
                    Type 

                    !!! cards col single centered-content ""

                        -   Boolean
                            { title="Init Value: False." }
                        
                    Toggle On

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disable_buttons` :lucide-variable:
                                { title="disable_buttons = True" }

                        !!! cards centered-content ""

                            -   `global_disable` :lucide-function-square: :lucide-square-play:
                                { title="Function: global_disable(). Statement: global_disable ''." }
                            
                            -    `disable_all` :lucide-function-square: :lucide-square-play:
                                { title="Function: disable_all(). Statement: disable_all ''. Toggles ON ALL disablers."}

                    Toggle Off

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disable_buttons` :lucide-variable:
                                { title="disable_buttons = False" }
                    
                        !!! cards centered-content ""

                            -   `global_enable` :lucide-function-square: :lucide-square-play:
                                { title="Function: global_enable(). Statement: global_enable ''." }
                            
                            -   `enable_all` :lucide-function-square: :lucide-square-play:
                                { title="Function: enable_all(). Statement: enable_all ''. Toggles OFF ALL disablers."}
                    
                    Notes

                    !!! cards col single centered-content ""

                        -   The global disabler
                        -   When `True`, all registered buttons are disabled regardless of Type or ID disabler state
                        -   Will also be toggled ON by: `disable_all_types` 
                            { title="Do NOT use for Global Level toggling."}

                        -   Will also be toggled OFF by: `enable_type`, `enable_all_type`, and `enable_id`
                            { title="Do NOT use for Global Level toggling."}
                
            #### Disabled Button Types 

            ??? grid col single "Disabled Button Types [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disabled Button Types Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `disabled_button_types`
                
                    Type 

                    !!! cards col single centered-content ""

                        -   Dictionary 
                            { title="{str: bool}" }
                    
                    Keys 

                    !!! grid col single no-pad no-border ""

                        !!! cards centered-content ""

                            -   `"app_exit"`
                                { title="Init Value(s): False."}

                            -   `"app_button"`
                                { title="Init Value(s): False."}
                            
                        !!! cards col single centered-content ""

                            -   `"contact_button"`
                                { title="Init Value(s): False."}
                        
                        !!! cards centered-content ""
                            -   `"prep_busy"`
                                { title="Init Value(s): False."}

                            -   `"closet_busy"`
                                { title="Init Value(s): False."}

                    Toggle On

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disabled_button_type` :lucide-variable:
                                { title="disabled_button_type[button_type] = True" }
                            
                            -   `disable_type` :lucide-function-square: :lucide-square-play:
                                { title="Function: disable_type(button_type). Statement: disable_type 'button_type'."}

                            -   `disable_all_type` :lucide-function-square: :lucide-square-play:
                                { title="Function: disable_all_type(button_type). Statement: disable_all_type 'button_type'. Toggles ON TYPE disabler AND all ID disablers of button_type." }

                    Toggle Off

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disabled_button_type` :lucide-variable:
                                { title="disabled_button_type[button_type] = False" }
                    
                            -   `enable_type` :lucide-function-square: :lucide-square-play:
                                { title="Function: enable_type(button_type). Statement: enable_type 'button_type'. Toggles OFF GLOBAL disabler AND TYPE disabler."}
                        
                            -   `enable_all_type` :lucide-function-square: :lucide-square-play:
                                { title="Function: enable_all_type(button_type). Statement: enable_all_type 'button_type'. Toggles OFF GLOBAL disabler, TYPE disabler AND all ID disablers of button_type." }
                    
                    Notes 

                    !!! cards col single centered-content ""

                        -   Per-type disablers
                        -   Keys are button type names
                        -   When a type's value is `True`, all buttons of that type are disabled.
                        -   Will also be toggled ON by: `disable_all` 
                            { title="Do NOT use for Type Level toggling."}

                        -   Will also be toggled OFF by: `enable_all` and `enable_id`
                            { title="Do NOT use for Type Level toggling."}

            #### Disabled Button IDs

            ??? grid col single "Disabled Button IDs [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disabled Button IDs Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `disabled_button_ids`
                
                    Type 

                    !!! cards col single centered-content ""

                        -   Dictionary 
                            { title="{str: set}" }
                    
                    Keys 

                    !!! grid col single no-pad no-border ""

                        !!! cards centered-content ""

                            -   `"app_exit"`
                                { title="Init Value(s): empty set."}

                            -   `"app_button"`
                                { title="Init Value(s): empty set."}
                            
                        !!! cards col single centered-content ""

                            -   `"contact_button"`
                                { title="Init Value(s): empty set."}
                        
                        !!! cards centered-content ""
                            -   `"prep_busy"`
                                { title="Init Value(s): empty set."}

                            -   `"closet_busy"`
                                { title="Init Value(s): empty set."}

                    Toggle On

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disabled_button_id` :lucide-variable:
                                { title="disabled_button_ids[button_type].add(id)" }
                            
                            -   `disable_id` :lucide-function-square: :lucide-square-play:
                                { title="Function: disable_id(id). Statement: disable_id 'id'."}

                    Toggle Off

                    !!! grid col single no-pad no-border no-row-gap ""

                        !!! cards col single centered-content ""

                            -   `disabled_button_id` :lucide-variable:
                                { title="disabled_button_ids[button_type].discard(id)" }
                    
                            -   `enable_id` :lucide-function-square: :lucide-square-play:
                                { title="Function: enable_id(id). Statement: enable_id 'id'. Toggles OFF GLOBAL disabler, corresponding TYPE disabler AND ID disabler."}
                    
                    Notes 

                    !!! cards col single centered-content ""

                        -   Per-ID disablers
                        -   Keys are button type names
                        -   Values are sets of disabled button IDs under corresponding button type keys
                        -   Will also be toggled ON by: `disable_all`, `disable_all_type`
                            { title="Do NOT use for ID Level toggling."}

                        -   Will also be toggled OFF by: `enable_all`, `enable_all_type`
                            { title="Do NOT use for ID Level toggling."}

        === "Mappings"

            #### Valid Button IDs

            ??? grid col single "Valid Button IDs [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Valid Button IDs Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `valid_button_ids`
                
                    Type 

                    !!! cards col single centered-content ""

                        -   Dictionary 
                            { title="{str: set}" }
                    
                    Keys 

                    !!! grid col single no-pad no-border ""

                        !!! cards centered-content ""

                            -   `"app_exit"`
                                { title="Init Value(s): 'Profile', 'Chat', 'Draft'."}

                            -   `"app_button"`
                                { title="Init Value(s): 'profile_app', 'chat_app', 'draft_app'."}
                            
                        !!! cards col single centered-content ""

                            -   `"contact_button"`
                                { title="Init Value(s): 'And', 'At You', 'Golden Manager', 'The Abyss Stares Back', 'Stare Into The Abyss'"}
                        
                        !!! cards centered-content ""
                            -   `"prep_busy"`
                                { title="Init Value(s): empty."}

                            -   `"closet_busy"`
                                { title="Init Value(s): empty."}

                    Notes 

                    !!! cards col single centered-content ""

                        -   Initialized in `init python`
                        -   The full roster of all registered button types and their valid button IDs. 
                        -   Used for input validation across all Button Disabler statements and functions. 
                        -   Invalid types or IDs cause a console print error and early return.

            #### App To Exit 

            ??? grid col single "App To Exit [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: App To Exit Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `app_to_exit`
                
                    Type 

                    !!! cards col single centered-content ""

                        -   Dictionary 
                            { title="{str: str}" }
                    
                    Keys 

                    !!! grid col single no-pad no-border ""

                        !!! cards centered-content ""

                            -   `"profile_app"`
                                { title="Init Value(s): 'Profile'."}

                            -   `"chat_app"`
                                { title="Init Value(s): 'Chat'."}
                            
                        !!! cards col single centered-content ""

                            -   `"draft_app"`
                                { title="Init Value(s): 'Draft'"}

                    Notes 

                    !!! cards col single centered-content ""

                        -   Initialized in `init python`
                        -   Maps app button IDs to their corresponding exit button IDs
                        -   Used by Scene System's `show_app` and `hide_app` statements to automatically manage exit button state

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        !!! warning "This section does not include functions directly equivalent to their statements"

        ### Functions 

        Below the utility and debugger functions for Monster Silhouette's Button Disabler System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters and any of their default values
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - **Non-Default Parameter Values**
            - Hover over cards for explanation on their effects
        - Other places in code it's **Used In**
            - Hover over cards for details

        #### Button Disabled :lucide-wrench: :lucide-bug:

        ??? grid col single "Button Disabled [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Button Disabled Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `button_disabled(button=None, report=False)`
                
                Parameters 

                !!! cards ""

                    -   `button`
                        { title="What to check for disabled status" }
                    -   `report`
                        { title="Control console print" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Checks whether a button, button type, or the global disabler is currently disabled
                    -   Returns `True` if disabled, `False` if enabled, `1` if invalid input
                
                Non-Default Parameter Values

                !!! cards col single centered-content ""

                    -   `button=None` 
                        { title="Checks global disabler only" }

                    -   `button=button_type` 
                        { title="Checks if all buttons of that type are disabled"}

                    -   `button=button_id`
                        { title="Checks if that specific button is disabled" }

                    -   `report=True`
                        { title="Prints a detailed console report explaining which disabler level is responsible and the state of all relevant flags" }
                
                Used In

                !!! cards col single centered-content ""

                    -   `screens.rpy` 
                        { title="As the in-screen check condition for all registered buttons." }
        
        #### Button Disabler Status :lucide-bug:

        ??? grid col single "Button Disabler Status [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Button Disabler Status Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `button_disabler_status(global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=False)`
                
                Parameters 

                !!! cards ""

                    -   `global_btn`
                        { title="Control console print for global disabler status" }
                    -   `btn_type`
                        { title="Control console print for type disabler statuses" }
                    -   `btn_id`
                        { title="Control console print for id disabler statuses" }
                    -   `disabled`
                        { title="Control console print for disabled statuses" }
                    -   `enabled`
                        { title="Control console print for enabled status" }
                    -   `inline`
                        { title="Control console print format" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Prints an organized status report of all disablers.
                    -   All parameters are optional booleans controlling what appears in the report
                    -   If `global_btn`, `btn_type` and `btn_id` are all `False`, treated as if `global_btn=True`
                    -   If `disabled` and `enabled` are both `False`, treated as if `disabled=True`
                
                Non-Default Parameter Values

                !!! cards col single centered-content ""

                    -   `global_btn=False`
                        { title="Omits global disabler status"}

                    -   `btn_type=False`
                        { title="Omits button type disabler status" }

                    -   `btn_id=False`
                        { title="Omits button ID disabler status"}

                    -   `disabled=False` 
                        { title="Omits disabled items from the lists" }
                        
                    -   `enabled=False`
                        { title="Omits enabled items from the lists" }
                        
                    -   `inline=True` 
                        { title="Prints type and ID lists on one line per type instead of vertically" }
                
                Used In

                !!! cards col single centered-content ""

                    -   Console 
                        { title="This is a Console-only debugger function. It won't do anything other than a console print." }

    === "Statements"

        ### Statements 

        Below all the statements for Monster Silhouette's Button Disabler System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
        - **Functionality**
        - **Functions Embedded**
        
        === "Global Disabling"
        
            #### Disable Global

            ??? grid col single "Disable Global [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable Global Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `disable_global ""` 

                    Arguments 

                    !!! cards col single "" 

                        -    N/A
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns ON Global Disabler (`disable_buttons`)
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_global()` :lucide-zodiac-libra:
        
            #### Enable Global

            ??? grid col single "Enable Global [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Enable Global Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `enable_global ""` 

                    Arguments 

                    !!! cards col single "" 

                        -    N/A
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns OFF Global Disabler (`disable_buttons`)
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `enable_global()` :lucide-zodiac-libra:
            
            #### Disable All

            ??? grid col single "Disable All [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable All Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `disable_all ""` 

                    Arguments 

                    !!! cards col single "" 

                        -    N/A
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns on all disablers at all three levels simultaneously
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_all()` :lucide-zodiac-libra:
                
            #### Enable All

            ??? grid col single "Enable All [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Enable All Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `enable_all ""` 

                    Arguments 

                    !!! cards col single "" 

                        -    N/A
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Clears all disablers at all three levels simultaneously
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `enable_all()` :lucide-zodiac-libra:
        
        === "Type Disabling"

            #### Disable Type 
            
            ??? grid col single "Disable Type [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable Type Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `disable_type "button_type"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_type` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns ON Type disabler (`disabled_button_types`) for `button_type`
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_type(button_type)` :lucide-zodiac-libra:
            
            #### Enable Type 
            
            ??? grid col single "Enable Type [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Enable Type Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `enable_type "button_type"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_type` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns OFF Type disabler (`disabled_button_types`) for `button_type`
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `enable_type(button_type)` :lucide-zodiac-libra:
            
            #### Disable All Type 
            
            ??? grid col single "Disable All Type [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable All Type Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `disable_all_type "button_type"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_type` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns ON Type disabler for `button_type`
                        -   Turns ON all ID disablers for `button_type`
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_all_type(button_type)` :lucide-zodiac-libra:
            
            #### Enable All Type 

            ??? grid col single "Enable All Type [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Enable All Type Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `enable_all_type "button_type"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_type` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns OFF Type disabler for `button_type`
                        -   Clears all ID disablers for `button_type`
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `enable_all_type(button_type)` :lucide-zodiac-libra:
                        
        === "ID Disabling"

            #### Disable ID

            ??? grid col single "Disable ID [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Disable ID Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `disable_id "button_id"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_id` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns ON ID disabler for `button_id` (adds `button_id` to its type's disabled set)
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_id(id)` :lucide-zodiac-libra:

            #### Enable ID

            ??? grid col single "Enable ID [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Enable ID Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `enable_id "button_id"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `button_id` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Turns OFF ID disabler for `button_id` (removes `button_id` to its type's disabled set)
                        -   If corresponding `button_type` Type disabler is on and set is empty, adds all other button ids of that type to the set
                        -   Turns OFF corresponding Type disabler 
                        -   Turns OFF Global disabler 
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `disable_id(id)` :lucide-zodiac-libra: 
                        


                
