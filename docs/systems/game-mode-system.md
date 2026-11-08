---
icon: lucide/gamepad-directional
status: modified 
tags: 
    - Coding
    - ㅤLast Updated
    - ㅤㅤNovember
    - ㅤㅤㅤ8
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If the date matches up with the last date-range entry in the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Game Mode System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

!!! warning "Currently the only implemented Game Mode is the Prep Phase"

The Game Mode System is a custom game system in Monster Silhouette that switches script progression from linear narrative 
into a distinct interactive game mode with its own rules, screens, and completion conditions. 

It builds on the Scene System, Button Disabler System, and Freeze System to manage the transition in and out of a 
game mode cleanly. 

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

                !!! cards col four centered-content ""

                    -   :lucide-variable: **Ready To Leave**
                        [][ready-to-leave]{ .card-link }
                    
                    -   :lucide-variable: **Key Attempted**
                        [][key-attempted]{ .card-link }
                    
                    -   :lucide-variable: **Closet Clicked**
                        [][closet-clicked]{ .card-link }
                    
                    -   :lucide-variable: **Laptop Clicked**
                        [][laptop-clicked]{ .card-link }
                
                !!! cards col single centered-content ""

                    -   :lucide-variable: **Clothing Sprites**
                        [][clothing-sprites]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-variable: **Top Selected**
                        [][top-selected]{ .card-link }
                    
                    -   :lucide-variable: **Bottom Selected**
                        [][bottom-selected]{ .card-link }

                !!! cards col  centered-content ""

                    -   :lucide-function-square: **Open Wardrobe** 
                        [][open-wardrobe]{ .card-link }
                    
                    -   :lucide-function-square: **Close Wardrobe** 
                        [][close-wardrobe]{ .card-link }
                    
                !!! cards col  centered-content ""

                    -   :lucide-function-square: **Call Prep Script** 
                        [][call-prep-script]{ .card-link }

                    -   :lucide-function-square: **Call Prep Closet Script** 
                        [][call-prep-closet-script]{ .card-link }

                !!! cards col centered-content ""

                    -   :lucide-function-square: **Get Clothing Info**
                        [][get-clothing-info]{ .card-link }
                    
                    -   :lucide-function-square: **Get Same Category Flags** 
                        [][get-same-category-flags]{ .card-link }
                
                !!! cards col single centered-content ""

                    -   :lucide-square-play: **Prep Phase** 
                        [][prep-phase]{ .card-link }

=== "How It Works"

    !!! tip "Learn more about the Scene System in the [Scene System][scene-system] page"

    !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

    !!! tip "Learn more about the Freeze System in the [Freeze System][freeze-system] page"

    ## How It Works 

    The Game Mode System has one statement for each Game Mode, which can be used to trigger the respective game modes from within script. 

    Together with the Button Disabler, Freeze, and Scene Systems, the components of the Game Mode System committed to each game mode
    manage all parts of the game modes simultanously from within their dedicated statements. 

    === "Game Modes"

        !!! tip "Learn more about Prep Phase Mode in the [Prep & Wrap Modes][prep-wrap-mechanic] page"

        ### Modes

        Game Modes in the Game Mode System are the distinct sets of rules and configurations that alter gameplay experince by defining 
        how players interact with Monster Silhouette's world. Dictating mechanics, objectives and victory conditions.

        #### Prep Phase Mode

        `prep_phase` is called in script with a list of click script label names. 

        It maps each label to a click type based on naming convention, shows the bedroom scene with the resulting `click_map`, 
        and freezes script progression via `freeze_until "prep_done"` until all required interactions are completed. 
        Once the freeze ends, it restores the button disabler state and status bar.

    === "Game Mode Scenes"

        !!! tip "Learn more about the screens that make up Game Mode Scenes in the [Game Mode Screens](#screens) tab"

        ### Scenes

        Game Mode Scenes are special interactable scenes that Game Modes take place in. 

        Prep Phase and Wrap Phase game modes take place in the Bedroom Scene.

        #### Bedroom Scene 

        The `bedroom` screen receives the `click_map` and uses it to determine which interactable props are active and which labels to call 
        when clicked. Each click calls its corresponding label in a new context via one of the prep phase utility functions, keeping the 
        interactable scene and the narrative consequences of each click cleanly separated.

        The wardrobe is a special case — clicking it opens `wardrobe_panel` as a modal over the bedroom. 
        The panel handles clothing selection, and closing it returns to the bedroom with the closet click recorded as completed.

    === "Gated Continuation"

        ### Completion Gating 

        The Freeze System is used to gate completion of Game Modes through respective Freeze Conditions and Hints. 

        === "Prep Phase Gating"

        The Prep Phase has two required interactions — clicking the closet and completing an outfit selection, and 
        clicking the laptop. 
        
        These interactions are tracked by `closet_clicked` and `laptop_clicked`. 
        
        The key click is the exit gate — it checks both flags and only sets `ready_to_leave = True` if both are satisfied, 
        which ends the `freeze_until "prep_done"` loop and returns script to normal progression.

        `key_attempted` tracks whether the key has been clicked at least once without the required interactions being complete, 
        which triggers a more specific hint from `prep_done_hint()`.

    === "Game Mode Screens"

        !!! tip "Learn more about Game Mode screens in the [Game Mode Screens][game-mode-screens] page"

        ### Screens

        The Game Mode System's visual output lives in screens that make up the interactiveness and innards of Game Mode Scenes.

        Screens that make up Game Mode System UI functionality include: `bedroom` and `wardrobe_panel`.

        === "Prep Mode Screens"

        The Bedroom and Wardrobe Panel screens are the visual front end for the Prep Phase. 

        They handle the Prep Scene from Visual Interface to UI Interaction. 

=== "Components"

    ??? info "About Game Mode System Functions"

        The Game Mode System's functions are all Utility Functions.

    ## Components 

    Overview of the three components (**variables**, **functions** and **statements**) of the Game Mode System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Game Mode System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details (**Init Value** if not Dictionary)
        - **Keys** (for Dictionaries)
            - Hover over cards for more details (**Init Value(s)** if not nested)
            - If nested dictionary: includes nested keys which you can hover for:
                - **Category** or main key it's under
                - **Init Value(s)** or **Mapping**
        - **Notes**
         
        === "States"

            #### Ready To Leave 

            ??? grid col single "Ready To Leave [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Ready To Leave Variable Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `ready_to_leave`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether player has met exit requirements 
                        -   Exit gate for the Prep Phase freeze 
                        -   Set to `True` by a key click label when all required interactions are complete

            #### Key Attempted 

            ??? grid col single "Key Attempted [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Key Attempted Variable Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `key_attempted`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether the player has clicked the key at least once without exit meeting requirements
                        -   Used by `prep_done_hint()` to give more specific guidance with dynamic hints

            #### Closet Clicked 

            ??? grid col single "Closet Clicked [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Closet Clicked Variable Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `closet_attempted`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether the player has clicked the closet and finished its interaction successfully
                        -   Set to `True` when the player completes outfit selection in the `wardrobe_panel` screen
                        -   Required for the key click to succeed

            #### Laptop Clicked

            ??? grid col single "Laptop Clicked [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Laptop Clicked Variable Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `laptop_attempted`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether the player has clicked the laptop
                        -   Set to `True` when the player clicks the laptop and finishes its interaction script
                        -   Required for the key click to succeed.

            #### Top Selected 

            ??? grid col single "Top Selected [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Top Selected Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `top_selected`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether the player has chosen a top garment for their outfit
                        -   Set to `True` when the player selects a top in the `wardrobe_panel`
                        -   Gates `closet_clicked`

            #### Bottom Selected 

            ??? grid col single "Bottom Selected [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Bottom Selected Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `bottom_selected`
                        
                    Type 

                    !!! cards col single ""

                    -   Boolean
                        { title="Init Value: False." }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Tracks whether the player has chosen a bottom garment for their outfit
                        -   Set to `True` when the player selects a bottom in the `wardrobe_panel`
                        -   Gates `closet_clicked`
                        
        === "Mappings"

            #### Clothing Sprites

            ??? grid col single "Clothing Sprites [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Clothing Sprites Variable Overview Card -->
                        
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `clothing_sprites`
                        
                    Type 

                    !!! cards col single centered-content ""

                        -   Dictionary
                            { title="{str: {str: str}}" }
                    
                    Keys 

                    !!! grid col single no-pad no-border ""

                        !!! cards col centered-content ""

                            -   `"top"`
                                { title="Category for upper-body clothing. Maps sprite names to their flag names." }

                            -   `"bottom"`
                                { title="Category for lower-body clothing. Maps sprite names to their flag names." }

                        !!! cards col single centered-content ""

                            -   `"dress_shirt"`
                                { title="Under 'top'. Maps to flag 'semiformal_top'." }

                            -   `"thin_turtle_neck"`
                                { title="Under 'top'. Maps to flag 'contour_top'." }

                            -   `"lightweight_cargo_pants"`
                                { title="Under 'bottom'. Maps to flag 'many_pockets'." }

                            -   `"dress_jeans"`
                                { title="Under 'bottom'. Maps to flag 'heavy_pants'." }
                    
                    Notes 

                    !!! cards col single centered-content ""

                        -   Initialized with `define` rather than `default` — a static mapping, not gameplay state
                        -   Read by `get_clothing_info()` and `get_same_category_flags()`
                        -   Adding a new clothing item means adding its sprite name and flag here

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        !!! warning "This section does not include functions directly equivalent to their statements"

        ### Functions 

        Below the utility functions for Monster Silhouette's Game Mode System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - Other places in code it's **Used In**
            - Hover over cards for details

        #### Open Wardrobe :lucide-wrench:

        ??? grid col single "Open Wardrobe [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Open Wardrobe Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `open_wardrobe(click_map)`
                
                Parameters 

                !!! cards col single ""

                    -   `click_map`
                        { title="Mapping for click interactions to bedroom interactables" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Disables `prep_busy` button type
                    -   Shows `wardrobe_panel` via `show_app()`
                    
                Used In

                !!! cards col single centered-content ""

                    -   `bedroom` screen
                        { title="For closet click interaction" }

        #### Close Wardrobe :lucide-wrench:

        ??? grid col single "Close Wardrobe [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Close Wardrobe Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `close_wardrobe()`
                
                Parameters 

                !!! cards col single ""

                    -   N/A
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Hides `wardrobe_panel` via `hide_app()`
                    -   Re-enables `prep_busy` button type
                    
                Used In

                !!! cards col single centered-content ""

                    -   `wardrobe_panel` screen
                        { title="From wardrobe_panel's Dressed button. To closed the wardrobe_panel and end the closet click interaction." }

        #### Call Prep Script :lucide-wrench:

        ??? grid col single "Call Prep Script [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Call Prep Script Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `call_prep_script(label)`
                
                Parameters 

                !!! cards col single ""

                    -   `label` 
                        { title="Prep script label to call in new context" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Disables `prep_busy` 
                    -   Calls `label` in new context via `renpy.call_in_new_context()` 
                    -   Re-enables `prep_busy` after call returns
                    
                Used In

                !!! cards col single centered-content ""

                    -   `bedroom` screen
                        { title="For non-closet click label interactions" }

        #### Call Prep Closet Script :lucide-wrench:

        ??? grid col single "Call Prep Closet Script [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Call Prep Closet Script Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `call_prep_closet_script(label)`
                
                Parameters 

                !!! cards col single ""

                    -   `label` 
                        { title="Closet script label to call in new context" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Disables `closet_busy` 
                    -   Calls `label` in new context via `renpy.call_in_new_context()` 
                    -   Re-enables `closet_busy` after call returns
                    
                Used In

                !!! cards col single centered-content ""

                    -   `wardrobe_panel` screen
                        { title="For closet selection label interactions" }
        
        #### Get Clothing Info :lucide-wrench:

        ??? grid col single "Get Clothing Info [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Get Clothing Info Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `get_clothing_info(sprite_name)`
                
                Parameters 

                !!! cards col single ""

                    -   `sprite_name`
                        { title="Sprite name to look up in clothing_sprites" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Returns a `(category, flag)` tuple for the given sprite
                    -   Returns `(None, None)` if the sprite name isn't present in `clothing_sprites`
                    
                Used In

                !!! cards col single centered-content ""

                    -   `clothing_sprite` screen
                        { title="To fetch the category and flag for the current sprite" }
        
        #### Get Same Category Flags :lucide-wrench:

        ??? grid col single "Get Same Category Flags [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Get Same Category Flags Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `get_same_category_flags(sprite_name)`
                
                Parameters 

                !!! cards col single ""

                    -   `sprite_name`
                        { title="Sprite name whose category siblings to look up" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Returns a list of flags for all sprites in the same category as `sprite_name`
                    -   Excludes `sprite_name`'s own flag
                    -   Returns an empty list if the sprite name isn't present in `clothing_sprites`
                    
                Used In

                !!! cards col single centered-content ""

                    -   `clothing_sprite` screen
                        { title="To clear the flags of sibling sprites before setting the current sprite's flag — ensures only one clothing item per category is selected" }

    === "Statements"

        ### Statements 

        Below all the statements for Monster Silhouette's Game Mode System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
            - Hover over cards for more details
        - **Functionality**
        - Additional **Notes**
            - Hover over cards for more details
        - **Functions Embedded**

        #### Prep Phase 

        ??? grid col single "Prep Phase [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Prep Phase Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `prep_phase "click_script_1" ... "click_script_n"` 

                Arguments 

                !!! cards col single "" 

                    -   `"script_closet_click"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Closet Click label. Suffix: closet_click"}

                    -   `"script_laptop_click"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Laptop Click label. Suffix: laptop_click"}

                    -   `"script_post_closet"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Post Closet Click label. Suffix: post_closet"}
                    
                    -   `"script_key_click"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Key Click label. Suffix: key_click"}
                    
                    -   `"script_top_selected"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Top Selection Click label. Suffixes: dress_shirt_selected or turtle_neck_selected"}
                    
                    -   `"script_bottom_selected"` :octicons-north-star-24:{ .red-icon }
                        { title="Click Script for Bottom Selection Click label. Suffixes: cargo_pants_selected or dress_jeans_selected"}
                    
                    -   `"script_optional_click"` 
                        { title="Click Script for any optional Click labels."}
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Builds `click_map` from label list
                    -   Disables prep busy buttons
                    -   Shows `bedroom` screen with the resulting `click_map`
                    -   Freezes until `prep_done`
                    -   Enables prep busy buttons after freeze is over 
                
                Notes 

                !!! cards col single centered-content ""

                    -   Takes any number of arguments
                        { title="Required click scripts must be included or you will be stuck in a freeze loop" }

                    -   Each argument is a script label name
                        { title="Each label should correspond to a Click Script label" }
                    
                    -   Labels are mapped to click types by naming convention suffix
                        { title="Required Click Types: closet, laptop, dressed, key, and at least 1 Top click type & 1 Bottom click type. Suffixes listed on hover for statement's required arguments." }
                
                Functions Embedded

                !!! cards col single ""

                    -   `prep_phase(clicks)` :lucide-zodiac-libra: 

