---
icon: lucide/pause
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

# Freeze System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

The Freeze System is a custom game system in Monster Silhouette that pauses script progression until a specific condition is met 
by the player. Rather than using Ren'Py's built-in interaction model — which advances on click — the Freeze System holds the script 
in a polling loop until a registered flag condition evaluates to True. This allows the narrative to wait for player-driven UI 
actions like opening an app, selecting a contact, or completing the Prep Phase before continuing.

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

                    -   :lucide-variable: **Freeze Conditions**
                        [][freeze-conditions]{ .card-link }
                    
                    -   :lucide-variable: **Freeze Hints**
                        [][freeze-hints]{ .card-link }
                    
                    -   :lucide-variable: **Current Hint**
                        [][current-hint]{ .card-link }

                !!! cards col four centered-content ""

                    -   :lucide-function-square: **Flag Check** 
                        [][flag-check]{ .card-link }
                    
                    -   :lucide-function-square: **App Open** 
                        [][app-open]{ .card-link }
                    
                    -   :lucide-function-square: **Contact Open** 
                        [][contact-open]{ .card-link }

                    -   :lucide-function-square: **Prep Done Condition** 
                        [][prep-done-condition]{ .card-link }
                
                !!! cards col single centered-content ""

                    -   :lucide-square-play: **Freeze Until** 
                        [][freeze-until]{ .card-link }

=== "How It Works"

    ## How It Works 

    `freeze_until` is called in script with a flag name. 

    The system looks up that flag name in `freeze_conditions` — a dictionary mapping flag names to condition strings. 
    It evaluates the condition string via `eval()` in a tight loop with 0.05 second pauses until the condition is `True`, 
    then returns and lets the script continue.

    While frozen, `_current_hint` is set from `freeze_hint` — a parallel dictionary mapping flag names to hint strings or callables. 
    If the hint source is a callable, it is called each loop iteration so the hint can update dynamically based on current state. 
    The hint displays via the `freeze_hint_display` screen and clears when the freeze ends.

    === "Variable Initialization"

        !!! tip "Learn more about Button Disabler System variables in the [Button Disabler System][button-disabler-system] page"

        ### System Variable Initialization

        Conditions and hints are populated dynamically at init time from `valid_button_ids` and `app_to_exit` — so every registered app, 
        contact, and exit button automatically gets a freeze condition and hint without manual entry. 
        Additional conditions like `prep_done` are added manually.

        === "Freeze Conditions Initialization"

            `freeze_conditions` maps flag names to condition strings evaluated via `eval()`. Populated at init:

            - App open conditions — one per app button ID: `'app_open("app_screen")'`
            - App close conditions — one per app exit ID: `'not app_open("app_screen")'`
            - Contact open conditions — one per contact button ID: `'contact_open("contact_name")'`
            - Prep done condition — `prep_done_condition()`

        === "Freeze Hints Initialization"

            `freeze_hint` maps flag names to hint strings or callables. Populated at init:

            - App open hints — `“Click on the {app_name} Icon or Notification to open {app_name} App.”`
            - App close hints — `“Click on the {app_name} Exit button to close {app_name} App.”`
            - Contact open hints — `“Click {contact}'s Contact to open {contact}'s Chat Box.”`
            - Prep done hint — a callable `prep_done_hint()` that returns different hints depending on which prep requirements remain unmet

    === "Substitution Support"

        ### Substitution Support

        `freeze_until` passes the flag name through `renpy.substitute()` before lookup, which means `freeze_until "[variable_name]"` works 
        — the variable's value is used as the flag name at runtime. 
        
        This is used for `freeze_until "[_chat_contact]"` to freeze until the currently active chat contact's button is clicked.

    === "Freeze Screens"

        !!! tip "Learn more about the Freeze Hint Display screen in the [Overlay Screens][overlay-screens] page"

        ### Screens

        The Freeze System's visual output lives in overlay screens.

        Screens that make up Freeze System UI functionality include: `freeze_hint_display`.

        `freeze_hint_display` is the overlay screen that renders `_current_hint` during a freeze. 
        <br>
        The Freeze System sets and clears `_current_hint` — the screen just renders whatever is currently there.

=== "Components"

    ??? info "About Freeze System Functions"

        The Freeze System's functions are all Utility Functions.

    ## Components 

    Overview of the three components (**variables**, **functions** and **statements**) of the Freeze System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Freeze System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details (**Init Value** if not Dictionary)
        - **Keys** (for Dictionaries)
            - Hover over cards for **Init Value(s)**
            - Or **Init Key(s) and Value(s)** if populated dynamically at init
        - **Notes**

        #### Freeze Conditions

        ??? grid col single "Freeze Conditions [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Freeze Conditions Variable Overview Card -->
                
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `freeze_conditions`
                
                Type 

                !!! cards col single ""

                    -   Dictionary
                        { title="{str: str}" }
                    
                Keys 

                !!! cards col single ""

                    -   N/A
                        { title="Init Key(s) & Value(s): App Open Conditions, App Close Conditions, Contact Open Conditions, Prep Phase Condition" }

                Notes 

                !!! cards col single centered-content ""

                    -   Initialized in `init python`
                    -   Maps flag names to condition strings
        
        #### Freeze Hints

        ??? grid col single "Freeze Hints [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Freeze Hints Variable Overview Card -->
                
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `freeze_hints`
                
                Type 

                !!! cards col single ""

                    -   Dictionary
                        { title="{str: str | callable}" }
                    
                Keys 

                !!! cards col single ""

                    -   N/A
                        { title="Init Key(s) & Value(s): App Open Hint, App Close Hints, Contact Open Hints, Prep Phase Dynamic Hints" }

                Notes 

                !!! cards col single centered-content ""

                    -   Initialized in `init python`
                    -   Maps flag names to hint strings or callables
                    -   Supports dynamic hints through callables
        
        #### Current Hint

        ??? grid col single "Current Hint [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Current Hint Variable Overview Card -->
                
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `_current_hint`
                
                Type 

                !!! cards col single ""

                    -   Str | None
                        { title="Init Value: None." }

                Notes 

                !!! cards col single centered-content ""

                    -   The currently active hint string displayed by `freeze_hint_display`
                    -   Set at the start of a freeze
                    -   Updated each loop iteration if the hint source is callable
                    -   Cleared back to Init Value when the freeze ends

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        !!! warning "This section does not include functions directly equivalent to their statements"

        !!! tip "Learn more about the Game Mode System in the [Game Mode System][game-mode-system] page"

        ### Functions 

        Below the utility functions for Monster Silhouette's Freeze System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - Other places in code it's **Used In**
            - Hover over cards for details

        #### Flag Check :lucide-wrench:

        ??? grid col single "Flag Check [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Flag Check Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `flag_check(flag_name)`
                
                Parameters 

                !!! cards col single ""

                    -   `flag_name`
                        { title="Name of Freeze Flag to check" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Evaluates `freeze_conditions[flag_name]` via `eval()` and returns the boolean result
                    
                Used In

                !!! cards col single centered-content ""

                    -   `freeze_until()` function
                        { title="At each loop iteration to determine whether to continue freeze or move forward" }
        
        #### App Open :lucide-wrench:

        ??? grid col single "App Open [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: App Open Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `app_open(app_screen)`
                
                Parameters 

                !!! cards col single ""

                    -   `app_screen`
                        { title="Name of App Screen to check" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Checks whether a screen is currently being shown
                    -   Returns `True` if `app_screen` is currently showing on the master layer via `renpy.get_screen()`
                    
                Used In

                !!! cards col single centered-content ""

                    -   App Open Conditions
                        { title="To check whether an app screen is open (showing)" }

                    -   App Close Conditions
                        { title="To check whether an app screen is closed (hidden)" }
        
        #### Contact Open :lucide-wrench:

        ??? grid col single "Contact Open [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Contact Open Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `contact_open(contact_name)`
                
                Parameters 

                !!! cards col single ""

                    -   `contact_name`
                        { title="Name of Contact to check" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Checks active contact
                    -   Returns `True` if `contact_name` matches `active_contact`
                    
                Used In

                !!! cards col single centered-content ""

                    -   Contact Open Conditions
                        { title="To check whether a specified contact is currently active" }

        #### Prep Done Condition :lucide-wrench:

        ??? grid col single "Prep Done Condition [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Prep Done Condition Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `prep_done_condition()`
                
                Parameters 

                !!! cards col single ""

                    -   N/A
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Checks Ready To Leave flag
                    -   Returns `True` if `ready_to_leave` is `True`.
                    
                Used In

                !!! cards col single centered-content ""

                    -   Prep Done Condition
                        { title="To check whether a player is ready to end Prep Phase" }

    === "Statements"

        ### Statements 

        Below all the statements for Monster Silhouette's Freeze System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
            - Hover over cards for more details
        - **Functionality**
        - Additional **Notes**
            - Hover over cards for more details
        - **Functions Embedded**

        #### Freeze Until 

        ??? grid col single "Freeze Until [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Freeze Until Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `freeze_until "flag_name"` 

                Arguments 

                !!! cards col single "" 

                    -   `"flag_name"` :octicons-north-star-24:{ .red-icon }
                        { title="Name of Freeze Flag"}
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Looks up `flag_name` in `freeze_conditions`
                    -   Sets hint from `freeze_hint`
                    -   Loops until condition is `True` 
                    -   Clears hint once loop ends
                
                Notes 

                !!! cards col single centered-content ""

                    -   Supports variable interpolation
                        { title="By passing through renpy.substitute()" }
                
                Functions Embedded

                !!! cards col single ""

                    -   `freeze_until(flag_name)` :lucide-zodiac-libra: 