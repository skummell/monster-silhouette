---
icon: lucide/image
status: new 
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

# Scene System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

The Scene System is a custom game system in Monster Silhouette that allows Ren'Py screens to be used in place of 
traditional image scenes. It provides a set of custom statements and underlying functions that show and hide screens 
directly on Ren'Py's master layer, giving them the same visual position as a background scene while retaining all the 
interactivity and dynamic rendering that screens offer.

The system also manages the relationship between app screens and their exit buttons, and provides a validated channel 
for showing notification screens.

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

                !!! cards col single centered-content ""

                    -   :lucide-variable: **Valid Notif Screens**
                        [][valid-notif-screens]{ .card-link }

                !!! cards col four centered-content ""

                    -   :lucide-function-square: **Show Scene** 
                        [][show-scene-function]{ .card-link }
                    
                    -   :lucide-function-square: **Show App** 
                        [][show-app-function]{ .card-link }
                    
                    -   :lucide-function-square: **Hide App** 
                        [][hide-app-function]{ .card-link }
                    
                    -   :lucide-function-square: **Show Notif** 
                        [][show-notif-function]{ .card-link }
                
                !!! cards col four centered-content ""

                    -   :lucide-square-play: **Show Scene** 
                        [][show-scene-statement]{ .card-link }
                    
                    -   :lucide-square-play: **Show App** 
                        [][show-app-statement]{ .card-link }

                    -   :lucide-square-play: **Show Panel**
                        [][show-panel]{ .card-link }

                    -   :lucide-square-play: **Show Notif** 
                        [][show-notif-statement]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-square-play: **Hide App** 
                        [][hide-app-statement]{ .card-link }
                    
                    -   :lucide-square-play: **Hide Panel**
                        [][hide-panel]{ .card-link }

=== "Layer Architecture"
    
    ## Layer Architecture 

    In Ren'Py, visuals are rendered across multiple named layers stacked on top of each other. 

    The master layer — also called the scene layer — sits at the bottom of this stack and is where traditional background scenes live. 
    Above it sit layers for sprites, effects, and finally the interface layer where screens like the dialogue box and menus render.

    By default, Ren'Py only allows image files to be shown on the master layer via the `scene` statement. 
    The Scene System works around this by using `renpy.show_screen()` with `_layer="master"` to place screens 
    directly onto that layer. 

    This means screens shown through the Scene System appear behind dialogue and UI elements, 
    exactly where a background image would sit, but with full screen functionality including dynamic content, interactable 
    elements and conditional rendering.

=== "How It Works"

    ## How It Works

    The Scene System currently manages four distinct types of screens, each with slightly different behavior and dedicated statements:

    === "Scene Screens"

        !!! tip "Learn more about these screens in the [Computer UI Screens][computer-ui-screens] and [Game Mode Screens][game-mode-screens] pages"

        ### Scene Screens 

        Full replacements for the current scene. 

        When `show_scene` is called it clears the master layer entirely before placing the new screen, ensuring only one scene is 
        ever active at a time. Replicating the functionality of the standard Ren'Py scene statement with screens.
        These are used for backgrounds like the bedroom and the Computer UI.

        Scene Screens in Monster Silhouette currently include: 
        
        - `computer_ui`
        - `computer_ui_locked`
        - `bedroom`

    === "App Screens"

        !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

        !!! tip "Learn more about these screens in the [App Screens][app-screens] page"

        ### App Screens 

        Shown on top of the current scene without replacing it. 

        `show_app` places the app screen on the master layer above whatever scene is currently showing. 
        When an app screen is shown, its corresponding exit button is automatically disabled by the system — the button is re-enabled 
        automatically when `hide_app` is called. This ensures the exit button state always reflects whether the app is actually open, 
        without needing manual management in the script.

        App Screens in Monster Silhouette currently include: 

        - `profile_app`
        - `chat_app`
        - `draft_app`

    === "Panel Screens"

        !!! tip "Learn more about these screens in the [Game Mode Screens][game-mode-screens] page"

        ### Panel Screens 

        Behave identically to app screens in terms of rendering — they sit on top of the current scene on the master layer. 

        The difference is that panel screens have no corresponding app exit button, so `show_panel` and `hide_panel` skip the button disabler 
        logic entirely. Used for modal overlays like `wardrobe_panel`.

        Panel Screens in Monster Silhouette currently include: 

        - `wardrobe_panel`

    === "Notification Screens"

        !!! tip "Learn more about these screens in the [Overlay Screens][overlay-screens] page"

        ### Notification Screens 

        Shown on top of the current scene via `show_notif`. 

        Before showing, the function validates the screen name against `valid_notif_screens` and refuses to show anything not in that set. 
        If the notification screen is already showing, it is hidden first before being shown again — preventing duplicate notifications 
        from stacking. Supports kwargs for passing data to the notification screen at show time.

        Notification Screens in Monster Silhouette currently include: 

        - `chat_app_notification`

=== "Components"

    ??? info "About Scene System Functions"

        The Scene System's functions are all Utility Functions.

    ## Components

    Overview of the three components (**variables**, **functions** and **statements**) of the Scene System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Scene System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Values**
        - **Purpose**
        - Additional **Notes**
        
        #### Valid Notif Screens

        ??? grid col single "Valid Notif Screens [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Valid Notif Screens Variable Overview Card -->
            
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `valid_notif_screens`
            
                Values 

                !!! cards col single ""

                    -   `chat_app_notification`
                
                Purpose 

                !!! cards col single centered-content ""

                    -   Stores the names of screens that are permitted to be shown via `show_notif`
                    -   Acts as a whitelist — any screen name not in this set will be rejected with a console printed error

                Notes 

                !!! cards col single ""

                    -   New notification screens must be registered here before they can be used with `show_notif`

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        ### Functions 

        Below all the utility functions for Monster Silhouette's Scene System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - Other places in code it's **Used In**
        
        #### Show Scene :lucide-wrench: { #show-scene-function }

        ??? grid col single "Show Scene [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Show Scene Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `show_scene(screen_name, **kwargs)`
                
                Parameters 

                !!! cards ""

                    -   `screen_name` :octicons-north-star-24:{ .red-icon }
                        { title="Name of screen to be shown" }
                    -   `**kwargs`
                        { title="Supports all renpy.show_screen kwargs" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Clears master layer via `renpy.scene(layer="master")`
                    -   Shows screen on master layer via `renpy.show_screen(screen_name, _layer="master", **kwargs)`
                
                Used In

                !!! cards col single ""

                    -   `show_scene` statement
        
        #### Show App :lucide-wrench: { #show-app-function } 

        ??? grid col single "Show App [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Show App Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `show_app(screen_name, **kwargs)`
                
                Parameters 

                !!! cards ""

                    -   `screen_name` :octicons-north-star-24:{ .red-icon }
                        { title="Name of screen to be shown" }
                    -   `**kwargs`
                        { title="Supports all renpy.show_screen kwargs" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Shows screen on master layer via `renpy.show_screen(screen_name, _layer="master", **kwargs)`
                    -   Does not clear the layer — stacks above current scene
                
                Used In

                !!! cards col single ""

                    -   `show_app` statement
                    -   `show_panel` statement
                    -   `open_wardrobe()` in Game Mode System
        
        #### Hide App :lucide-wrench: { #hide-app-function}

        ??? grid col single "Hide App [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Hide App Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `hide_app(screen_name)`
                
                Parameters 

                !!! cards ""

                    -   `screen_name` :octicons-north-star-24:{ .red-icon }
                        { title="Name of screen to be hidden" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Hides screen from master layer via `renpy.hide_screen(screen_name, layer="master")`
                
                Used In

                !!! cards col single ""

                    -   `hide_app` statement
                    -   `hide_panel` statement
                    -   `close_wardrobe()` in Game Mode System

        #### Show Notif :lucide-wrench: { #show-notif-function }

        ??? grid col single "Show Notif [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Show Notif Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `show_notif(screen_name, **kwargs)`
                
                Parameters 

                !!! cards ""

                    -   `screen_name` :octicons-north-star-24:{ .red-icon }
                        { title="Name of screen to be shown" }
                    -   `**kwargs`
                        { title="Supports all renpy.show_screen kwargs" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Validates screen name against `valid_notif_screens` — prints error and returns if invalid
                    -   Hides existing instance if already showing
                    -   Shows screen on master layer via `renpy.show_screen(screen_name, _layer="master", **kwargs)`
                
                Used In

                !!! cards col single ""

                    -   `show_notif` statement

    === "Statements"

        ### Statements 

        Below all the statements for Monster Silhouette's Scene System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
        - **Functionality**
        - **Functions Embedded**
        
        === "Showing Scenes"
        
            #### Show Scene { #show-scene-statement }

            ??? grid col single "Show Scene [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Show Scene Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `show_scene "screen"` 

                    Arguments 

                    !!! cards col single "" 

                        -    `"screen"` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Shows a screen on the master layer as the current scene
                        -   Clears the master layer before showing — replaces any existing scene
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `show_scene(screen)` :lucide-zodiac-libra:
                    
            #### Show App { #show-app-statement }

            ??? grid col single "Show App [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Show App Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `show_app "app_screen"` 
                    
                    Arguments 

                    !!! cards col single ""

                        -   `"app_screen"` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Shows an app screen on the master layer above the current scene
                        -   Automatically disables the corresponding app exit button via `disable_id`
                    
                    Functions Embedded 

                    !!! cards col single ""

                        -   `show_app(app_screen)` 
                        -   `disable_id(app_exit_button)`
                    
            #### Show Panel 

            ??? grid col single "Show Panel [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Show Panel Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `show_panel "panel_screen"` 
                        
                    Arguments 

                    !!! cards col single ""

                        -   `"panel_screen"` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Shows a panel screen on the master layer above the current scene
                        -   No exit button management
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `show_app(panel_screen)` :lucide-zodiac-libra:
                
            #### Show Notif { #show-notif-statement }

            ??? grid col single "Show Notif [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Hide Panel Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `show_notif "notif_screen"` 
                        -   Supports kwargs: 
                        
                            `show_notif "notif_screen" kwarg "value"`
                        
                    Arguments 

                    !!! cards ""

                        -   `"notif_screen"` :octicons-north-star-24:{ .red-icon }
                        -   `kwargs "value"`
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Shows a notification screen on the master layer above the current scene
                        -   Validates screen name against `valid_notif_screens` before showing
                        -   Hides existing instance first if already showing
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `show_notif(screen_name, **kwargs)` :lucide-zodiac-libra:
        
        === "Hiding Scenes"

            #### Hide App { #hide-app-statement }

            ??? grid col single "Hide App [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Hide App Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `hide_app "app_screen"` 
                    
                    Arguments 

                    !!! cards col single ""

                        -   `"app_screen"` :octicons-north-star-24:{ .red-icon }
                        
                    Functionality

                    !!! cards col single centered-content ""

                        -   Hides an app screen from the master layer
                        -   Automatically re-enables the corresponding app exit button via `enable_id`
                    
                    Functions Embedded

                    !!! cards col single ""

                        - `hide_app(app_screen)`
                        - `enable_id(app_exit_button)`
            
            #### Hide Panel

            ??? grid col single "Hide Panel [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Hide Panel Statement Overview Card -->
                
                !!! grid scrollable ""

                    Statement Usage

                    !!! cards col single ""

                        -   `hide_panel "panel_screen"` 
                    
                    Arguments 

                    !!! cards col single ""

                        -   `"panel_screen"` :octicons-north-star-24:{ .red-icon }

                    Functionality

                    !!! cards col single centered-content ""

                        -   Hides a panel screen from the master layer
                        -   No exit button management
                    
                    Functions Embedded

                    !!! cards col single ""

                        -   `hide_app(panel_screen)` :lucide-zodiac-libra:
