---
icon: lucide/sofa
status: new
tags: 
    - GDD
    - ㅤLast Updated
    - ㅤㅤNovember 
    - ㅤㅤㅤ15
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If a documentation update is logged in the latest entry of the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Lounge Modes 

## Overview 

The Lounge Modes encompass the gameplay and narrative sequences that take place at Victor's Tea Lounge (also known as Kiri Rêve Tea Lounge in-game). 
These modes move the game into the lounge's public, interactive environment, governing arrival flows and event-driven interactable states.

The sequence is made up of two modes — Lounge Arrival and Lounge Event — each running on one of the two interactable lounge scenes.

=== "Interactable Scene"
    
    !!! tip "Learn more about the Lounge screens in the [Game Mode Screens][game-mode-screens] page"
    
    ## Interactable Scene 

    The lounge modes feature two distinct interactable scenes that structure the player's experience within the tea lounge environment. 

    Each scene serves as the visual and functional backdrop for the mode running on it. 
    Sprite placement, ambient states, and interactive hotspots are handled within the scene, shaping the public space the player navigates.

    ??? grid col single "Lounge - Looking In"

        <!-- tooltip: Lounge Looking In Scene Overview. Provides a brief overview of the looking in scene, including: Screen Name, Visual Components, Functionality, and Extra Notes -->

        !!! grid scrollable ""

            Screen Name

            !!! cards col single ""

                -   `lounge_look`
                
            Visual Components 

            !!! cards col single centered-content ""

                -   Lounge Backdrop (Looking In Perspective)
                -   Counter & Bonsai Assembly
                -   Table & Chairs (Interactive Sit Down Spot)

            Functionality 

            !!! cards col single centered-content ""

                -   All Lounge Arrival Functionality 
            
            Extra Notes 

            !!! cards col single centered-content "" 

                -   The interactable functionality for Lounge Arrival inside of this screen is locked until the game mode is triggered

    ??? grid col single "Lounge - Seating Down"

        <!-- tooltip: Lounge Seating Down Scene Overview. Provides a brief overview of the seating down scene, including: Screen Name, Visual Components, Functionality, and Extra Notes -->

        !!! grid scrollable ""

            Screen Name

            !!! cards col single ""

                -   `lounge_sit`
                
            Visual Components 

            !!! cards col single centered-content ""

                -   Lounge Backdrop (Seating Down Perspective)
                -   Wind Chime
                -   Table & Chairs Assembly
                -   Laptop Sprite

            Functionality 

            !!! cards col single centered-content ""

                -   All Lounge Event Functionality 
            
            Extra Notes 

            !!! cards col single centered-content "" 

                -   The interactable functionality for Lounge Event inside of this screen is locked until the game mode is triggered

=== "Lounge Arrival"

    !!! tip "Learn more about the Lounge Arrival Mode in the [Game Mode System][game-mode-system] page"

    ## Lounge Arrival

    The Lounge Arrival mode handles the transition of the game state as the Player Character arrives at the Kiri Rêve Tea Lounge. 
    This mode serves as the operational entry point into the lounge sequence.

    It manages the initial setup of the scene's interactive version, bringing up the tea lounge background with its designated interactive layer enabled. 
    At the end of the mode it shows the second lounge scene.

    Required interaction must be completed before the story can continue the narrative.

=== "Lounge Event"

    !!! tip "Learn more about the Lounge Event Mode in the [Game Mode System][game-mode-system] page"

    ## Lounge Event 

    The Lounge Event mode governs the narrative encounters and social interactions that take place once the player is seated inside the tea lounge. 

    This mode takes over script progression at points in the story when the second lounge scene environment needs to become interactable. 
    It re-displays the scene with its interactive layer enabled, determines the appropriate interactive event to trigger, and runs that event's 
    freeze sequences and more.

    Required interaction must be completed before the story can continue the narrative.


