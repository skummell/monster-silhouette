---
icon: lucide/monitor
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

# Computer UI Screens 

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview 

The Computer UI screens make up the visual and functional infrastructure of the Computer UI mechanic. 
These screens are all original to Monster Silhouette.

They range from the primary navigation screen to cosmetic display screens that serve the Computer UI system's narrative presentation.

??? info "Screen Overview Legend"

    === "Legend"

        <p id="screen-overview-legend"></p>
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-letters:          | :lucide-lock-open:           |
        | ------------------------------------- | ------------------------- | ---------------------------- |
        | Required parameters                   | Fixed set of valid values | NO fixed set of valid values |

    === "Go To Screen Overviews"

        !!! cards col single no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards col three centered-content ""

                    -   :lucide-monitor-play: **Computer UI**
                        [][computer-ui]{ .card-link }

                    -   :lucide-monitor-cog: **Computer UI Menu** 
                        [][computer-ui-menu]{ .card-link }

                    -   :lucide-wallpaper: **Computer UI Locked** 
                        [][computer-ui-locked]{ .card-link }

                !!! cards centered-content ""
                
                    -   :lucide-dock: **Navigation Dock**
                        [][navigation-dock]{ .card-link }
                    
                    -   :lucide-layout-grid: **App Grid**
                        [][app-grid]{ .card-link }

=== "Context & Behavior"

    !!! tip "Learn more about Ren'Py Special Screens in [Ren'Py Source Code Docs][renpy-doc-special-screens]"

    !!! tip "Learn more about Monster Silhouette's Game Menu Action in the [Settings & Options][settings-options] page"

    ## Context & Behavior

    The Computer UI screens operate across two distinct contexts that affect how they behave 
    — in-game scene context and menu context.

    In scene context, the Computer UI appears as part of the narrative. 
    <br>
    The player interacts with it as they would any in-world object. 
    <br>
    App buttons open their respective apps on top of the scene, just below the Ren'Py special screen `say` (which displays 
    normal script dialogue), and the navigation dock is hidden entirely.

    In menu context, accessed through the Game Menu Action, the full Computer UI is available including 
    the navigation dock and thereby all meta screen access. 
    <br> 
    App screens opened from here behave the same as in scene context, but the app screens' show action is handled 
    differently to ensure that ESC navigation correctly returns to the Computer UI Menu rather than the game directly.

=== "Screens"

    !!! info "About Computer UI Parameters"

        Computer UI Screens do not have any parameters

    ## Screens 

    Below all the Computer UI Screens for Monster Silhouette have been organized into overviews containing information on their: 

    - **Screen Name**
    - **Visual Layout**
    - Additional **Notes**

    === "Computer UI"

        !!! tip "Learn more about Status Bar screen in the [Overlay Screens][overlay-screens] page"
        
        ### Computer UI 

        The primary Computer UI screen. Serves as the in-game home screen the player navigates through. 

        Contains the app grid with app icon buttons and the navigation dock. 
        The navigation dock is only accessible from the menu version.

        ??? grid col single "Computer UI [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Computer UI Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `computer_ui`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   Computer UI Background
                    -   App Grid via `app_grid`
                    -   Navigation Dock via `navigation_dock` 
                
                Notes 

                !!! cards col single ""

                    -   Navigation dock only renders when Quick Menu is not present
                    -   App buttons become active progressively through story events

    === "Computer UI Menu"

        ### Computer UI Menu

        The menu version of the Computer UI screen. Wraps computer_ui and status_bar together and adds game menu key behavior. 

        This is what opens when the player uses the Game Menu Action.

        ??? grid col single "Computer UI Menu [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Computer UI Menu Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `computer_ui_menu`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   All of Computer UI Components 
                    -   Status Bar (unconditionally)
                
                Notes 

                !!! cards col single ""

                    -   Replaces Ren'Py's default game menu screen
                    -   ESC key returns to game via `[Return(), Return()]`
                    -   Uses `menu` tag (like Main Menu and all the Meta Screens)
                    -   Clicking `ESC` from a Meta Screen or App Screen opened from Computer UI Menu returns you to Computer UI Menu

    === "Computer UI Locked"

        ### Computer UI Locked 

        A cosmetic screen displayed narratively before the main Computer UI. 

        Shows the in-world date, time, player name and a profile picture (currently a placeholder) — styled as a computer lock screen.

        ??? grid col single "Computer UI Locked [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Computer UI Locked Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `computer_ui_locked`
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Computer UI Lock Screen Background
                    -   Date and Time Display
                    -   Player Character Profile Pic & Player Name 
                    -   Lock Icon
                
                Notes 

                !!! cards col single ""

                    -   Purely cosmetic, no interaction
                    -   Shown and dismissed through script

    === "Navigation Dock"

        !!! tip "Learn more about Meta Screens trigged by dock buttons in the [Meta Screens][meta-screens] page"

        !!! tip "Learn more about the Dock Button Template in [Template Screens][template-screens] page"

        ### Navigation Dock 

        The dock at the bottom of the Computer UI that houses the Meta Screen navigation buttons and the main menu return button.

        In-game menu navigation has been moved here from where it originally was inside the Ren'Py special screen `navigation`. 

        ??? grid col single "Navigation Dock [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Navigation Dock Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `navigation_dock`
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Grid of Dock Icon Buttons
                    -   Power Off Icon Button
                
                Notes 

                !!! cards col single ""

                    -   Only visually and functionally accessible inside `computer_ui_menu`
                    -   Grid Icon Buttons open their designated Meta Screens
                    -   Power off button returns to Main Menu
                    -   Grid icon buttons are rendered via the `dock_button` template
            
    === "App Grid"

        !!! tip "Learn more about App Button Template in [Template Screens][template-screens] page"

        !!! tip "Learn more about App Screens triggered by App Buttons in [App Screens][app-screens] page"

        ### App Grid 

        The grid of app icon buttons inside the Computer UI home screen. 

        Currently contains three active app buttons and placeholder icon slots for *possible* future apps.

        ??? grid col single "App Grid [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: App Grid Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `app_grid`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   6x3 Grid of Icons
                    -   App Buttons for App Screens
                    -   Placeholder Icons for Remaining Slots 
                
                Notes 

                !!! cards col single ""

                    -   Detects scene context automatically via `in_scene` check
                    -   Uses `app_button` template for active button slots

