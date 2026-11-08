---
icon: lucide/gamepad-2
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

# Game Mode Screens

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview

Game mode screens are interactable scene screens that take over from normal script progression during specific game modes. 

Unlike regular scenes that serve as static backgrounds, these screens are fully interactive — the player clicks elements 
within them to drive the story forward.

They are the only screens in Monster Silhouette where the player has direct physical agency over the environment rather 
than making choices through dialogue menus or chat.

??? info "Screen Overview Legend"

    === "Legend"

        <p id="screen-overview-legend"></p>
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-letters:          | :lucide-lock-open:           |
        | ------------------------------------- | ------------------------- | ---------------------------- |
        | Required parameters                   | Fixed set of valid values | NO fixed set of valid values |

    === "Go To Screen Overviews"

        !!! cards col single no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards centered-content ""

                    -   :lucide-bed-double: **Bedroom**
                        [][bedroom]{ .card-link }

                    -   :lucide-hat-glasses: **Wardrobe Panel** 
                        [][wardrobe-panel]{ .card-link }

=== "Interactable Scenes"

    !!! tip "Learn more about the Scene System in the [Scene System][scene-system] page"

    !!! tip "Learn more about the Freeze System in the [Freeze System][freeze-system] page"

    !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

    ## Interactable Scenes 

    Game mode screens are shown via the Scene System and remain active until the game mode's completion conditions are 
    met through the Freeze System. Script progression is suspended for the duration — the story does not move forward 
    until the player has satisfied all required interactions.

    The screens themselves are not passive displays. They maintain their own internal state, respond to player clicks in real time, 
    and feed the results of those clicks back into the story through script labels called in new contexts. 
    This keeps the interactable scene and the narrative script cleanly separated while still allowing each click to have narrative 
    consequences.

    Interactable elements are managed by the Button Disabler System — specific button types are toggled on and off to control which 
    elements are clickable at any given moment, preventing conflicts between active script execution and player input.

=== "Screens"

    !!! tip "Learn more about the Game Mode System in the [Game Mode System][game-mode-system] page"

    !!! tip "Learn more about the Game Mode Templates use in the [Template Screens][template-screens] page"

    ## Screens

    Below all the game mode screens for Monster Silhouette have been organized into overviews containing information on their: 

    - **Screen Name**
    - **Parameters**
        - Hover over cards for details (purpose, type, valid values, other notes)
    - **Visual Layout**
    - Additional **Notes**

    === "Bedroom"

        ### Bedroom 

        The Bedroom is the Player Character's home base — the space they start and end every day in. 

        As an interactable scene it becomes the stage for both the Prep Phase at the start of the day and the Wrap Phase at the end. 

        The props scattered around the room are not just decoration — each one is a potential interaction point that can affect the 
        narrative going forward.

        ??? grid col single "Bedroom [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Bedroom Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `bedroom`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `click_map` :lucide-letters:
                        { title="Click type keys mapping to script label names. Dictionary. Default: empty dict" }
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   Bedroom Background Layers (Walls, Bookshelf, Wardrobe, Desk Setup, Chair, Bed)
                    -   Buttons for Each Interactable Prop Sprite
                
                Notes 

                !!! cards col single ""

                    -   Uses `prep_busy` button type disabler for Prep Phase bedroom interactables
                    -   Wallet and laptop sprites conditionally hidden when picked up
                    -   Wardrobe opens `wardrobe_panel` on click
                    -   Key click is the exit gate — exit is only active when required interactions have been completed
                    -   Script labels for each click are fed in via `click_map` by the `prep_phase` statement
                    -   Interactable prop buttons are rendered via the `bedroom_interactable` template.

    === "Wardrobe Panel"

        ### Wardrobe Panel

        The Wardrobe Panel is a focused selection interface that opens within the Bedroom scene when the player interacts with the wardrobe. 
        It temporarily takes over the bedroom scene, presenting the available clothing options for the day. 

        The player must make a complete outfit choice — both a top and a bottom — before they can confirm and return to the bedroom. 

        The selections made here feed directly into the story as clothing flags that trigger unique character reactions and additional 
        dialogue throughout the day.

        ??? grid col single "Wardrobe Panel [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Wardrobe Panel Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `wardrobe_panel`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `click_map` :lucide-letters:
                        { title="Clothing selection keys mapping to script label names. Dictionary. Default: empty dict" }
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   Wardrobe Panel Background 
                    -   Two Columns of Clothing Option Sprite Buttons (Tops on the Left, Bottoms on the Right)
                    -   Dressed Confirm Button
                
                Notes 

                !!! cards col single ""

                    -   Modal — bedroom interactables are disabled while this is open via `closet_busy` button type disabler
                    -   Clothing buttons use selected state to highlight current selection
                    -   Dressed button only becomes sensitive when both a top and bottom have been selected
                    -   Opens via `open_wardrobe()` function inside `bedroom` screen 
                    -   Closes via `close_wardrobe()` function
                    -   Sprite Buttons are rendered through the `clothing_sprite` template

