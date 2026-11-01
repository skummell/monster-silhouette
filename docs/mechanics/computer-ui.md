---
icon: lucide/laptop-minimal
status: new 
tags: 
    - GDD
    - ㅤLast Updated
    - ㅤㅤOctober 
    - ㅤㅤㅤ31
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If the date matches up with the last date-range entry in the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"


# Computer UI

## Overview 

The Computer UI mechanic is where in-game meta functionality and Monster Silhouette's unique in-world computer navigation system live. 

In this section, we will briefly explore what this mechanic looks like in game.

=== "Computer UI System Screens"

    !!! tip "Learn more about Computer UI Screens in the [Computer UI Screens][computer-ui-screens] page"

    ## Computer UI System Screens 

    The Computer UI mechanic is made up of several different screens. 

    This includes the main Computer UI Screen, as well as several others, both those directly used inside the Computer UI Screen as well as other separate screens that serve the Computer UI System all the same.

    === "Computer UI Screens"

        !!! tip "Learn more about Meta Screens in the [Meta Screens][meta-screens] page"

        ### Computer UI Screens

        Computer UI System's core functionality is attached to the primary Computer UI Screen. 

        The Computer UI Menu is a version of the Computer UI Screen that can be called on as a menu. Through which you have access to all meta screens.

        ??? grid col single "Computer UI Screen"

            !!! grid scrollable ""

                Screen Name

                !!! cards col single ""

                    -   `computer_ui`
                
                Visual Components 

                !!! cards col centered-content ""

                    -   App Grid 

                    -   App Icons
                    
                    -   Navigation Dock
                    
                    -   Button Tooltips
                
                Functionality 

                !!! cards col single centered-content ""

                    -   Access to App Screens
                    
                    -   Access to Meta Screens
                            
                Extra Notes 

                !!! cards col single ""

                    -   Meta Screen Access is restricted in Computer UI when Quick Menu is present.
                    -   Navigation Dock is where Meta Screen Access lives.
                    -   Navigation Dock is fully inaccessible both visually and functionally outside of Computer UI's Menu version.
                    -   The App Grid's App Buttons become active in-game at Day 1 - Introduction.
                    
                        They are inactive if you access Computer UI before the introduction enables the respective buttons.

        ??? grid col single "Computer UI Menu Screen"

            !!! grid scrollable ""

                Screen Name

                !!! cards col single ""

                    -   `computer_ui_menu`
                
                Visual Components 

                !!! cards col single ""

                    -   All of Computer UI's visuals 
                    
                        Including Navigation Dock

                Functionality 

                !!! cards col single ""

                    -   All of Computer UI's functionality 
                    
                        Including Access to Meta Screens 

    === "Cosmetic Screens"

        ### Cosmetic Screens

        The Computer UI System has several cosmetic screens which have almost no interactability and serve primarily to display visual elements. 

        Aside from the following, several other imbedded screens are cosmetic in functionality.

        ??? grid col single "Computer UI Lock Screen"

            !!! grid scrollable ""

                Screen Name

                !!! cards col single ""

                    -   `computer_ui_locked`
                
                Visual Components 

                !!! cards col single centered-content ""

                    - In-World Time & Date 
                    - Player Name
                    - Player Character Profile Pic
            
        ??? grid col single "Status Bar Screen"

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `status_bar`
                    
                Visual Components 

                !!! cards centered-content ""

                    -   Computer Top Bar Icons 
                    
                    -   In-World Time & Date 
                    
                Extra Notes

                !!! cards centered-content col single ""

                    -   Overlay Screen
                    
                    -   Computer Top Bar Icons only show up when inside of Computer UI

                    -   Time is a return to game button if on Menu version of Computer UI

    === "Embedded Systems"

        !!! tip "Learn more about App Screens in the [App Screens][app-screens] page"

        ### Embedded Systems

        The Computer UI System itself is an access and navigation channel to other Gameplay Mechanics and Systems. 

        Aside from the game menus that are already mostly built into Ren'Py Engine, the Computer UI Screen provides access to the screens containing Monster Silhouette's unique Gameplay Mechanics through the app icon buttons that live inside the Computer UI's app grid.

        The three app icons in the Computer UI grid each open an embedded in-world system. 
        <br>
        These App Screens are distinct from Meta Screens — they are part of the game world rather than game navigation.

        ??? grid col single "Profile App Screen"

            !!! grid scrollable ""

                Screen Name

                !!! cards col single ""

                    -   `profile_app`
                    
                Visual Components 

                !!! cards centered-content ""

                    -   App Header & Exit Button
                    -   Player Name & Pen Name
                    -   Profile Pic
                    -   Wallet Location
                    -   Book Deadline Countdown
                    -   Rapport & Suspicion Stat Tracker
                
                Functionality 

                !!! cards col single centered-content ""

                    -   Displays player identity (as reflected through the Player Character) and live game stats
                    
                Extra Notes 

                !!! cards col single centered-content ""

                    -   Read-only, no interaction beyond viewing

        ??? grid col single "Chat App Screen"

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_app`
                    
                Visual Components

                !!! cards col single centered-content ""

                    -   App Header & Exit Button
                    -   Chat Contact Panel 
                    -   Chat Box
                
                Functionality 

                !!! cards col single centered-content ""

                    -   Primary remote communication channel between the Player Character and other characters
                    -   Conversations through a Chat-like Interface
                    -   Persistent & accumulative Chat History
                    -   Contact Buttons become active throughout the story
                    -   Contacts themselves become active on their own during story progression

        ??? grid col single "Draft App Screen"

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `draft_app`
                    
                Visual Components 

                !!! cards col single centered-content ""

                    -   App Header & Exit Button
                    -   Toolbar & Settings Bar
                    -   Draft File
                
                Functionality 

                !!! cards col single centered-content ""

                    -   Displays the Player Character's draft-in-progress
                    -   Read-only from player perspective 
                    
                Extra Notes 

                !!! cards col single centered-content ""

                    -   Content updates as the story progresses and reflects the route taken
                    -   Player Character's Suspicion level directly influences what gets written

=== "Access to Computer UI"

    !!! tip "Learn more about Monster Silhouette's Game Menu Action in the [Settings & Options][settings-options] page"

    ## Access to Computer UI 

    There are two access points to the Computer UI System inside the game:

    ### Game Menu 

    Computer UI's Menu version can be accessed through the the Game Menu Action. 

    ### Script and Narrative 

    Computer UI can also be accessed through the story and progression of its narrative script. 

    At different points in the game, Computer UI will be present as a part of the narrative and the player will interact with it directly to move the story forward.


*[in-game meta functionality]: out-of-game meta functionality is handled by Main Menu.