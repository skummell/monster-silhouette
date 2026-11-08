---
icon: lucide/layout-grid-circles
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

# App Screens

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview

App Screens are the 3 in-world application screens accessible through the Computer UI's app grid. 

Unlike Meta Screens which serve out-of-game navigation purposes, App Screens are part of the game world — 
their content is tied directly to the story's state and progresses alongside it.

Each App Screen is built on the `app_screen` template and has its own dedicated exit button 
managed by the Button Disabler System.

!!! tip "Learn more about App Screen Template in the [Template Screens][template-screens] page"

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

                    -   :lucide-monitor-play: **Profile App**
                        [][profile-app]{ .card-link }

                    -   :lucide-monitor-cog: **Chat App** 
                        [][chat-app]{ .card-link }

                    -   :lucide-wallpaper: **Draft App** 
                        [][draft-app]{ .card-link }

=== "Narrative Integration"

    !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

    ## Narrative Integration 

    App Screens are not just UI elements — they are in-world objects the Player Character actively uses as part of their daily life. 
    Their content reflects the current state of the story and the choices the player has made.

    Access to each app is gated through the Button Disabler System — app buttons start disabled and become available as 
    the narrative introduces them. 
    <br>
    Each app's exit button is managed independently of its app button and can be disabled during story moments that require 
    the player to interact with the app.

=== "Screens"

    !!! info "About App Parameters"

        App Screens do not have any parameters but feed parameters into the `app_screen` template

    ## Screens 

    Below all the app screens for Monster Silhouette have been organized into overviews containing information on their: 

    - **Screen Name**
    - **Visual Layout**
    - Additional **Notes**
    
    === "Profile App"

        ### Profile App 

        !!! tip "Learn more about Visible Flags in the [Story Mode][story-mode-mechanic] page"

        The Profile App serves as the player's at-a-glance view of their current identity and story state. 

        It displays the player name chosen at the start, the Player Character's pen name, and live tracking of key flags and 
        stats that reflect how the story has unfolded so far. 

        Everything on it is read-only — it observes the state of the game, it has no interactive features that affect the state itself.

        ??? grid col single "Profile App [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Profile App Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `profile_app`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   App Screen Layout Set Up via `app_screen` 
                    -   Profile Info Section (Profile Pic, Player Name, Pen Name, Deadline Widget)
                    -   Stat Tracker Section (Wallet Tracker, Rapport & Suspicion Tracker)
                
                Notes 

                !!! cards col single ""

                    -   Rapport and Suspicion stat values are unavailable until unlocked through story progression
                    -   Wallet location reflects `wallet_on_person` flag
                    -   Deadline countdown reflects `deadline` variable

    === "Chat App"

        ### Chat App 

        !!! tip "Learn more about the Chat System in the [Chat System][chat-system] page"

        The Chat App is the Player Character's primary means of remote communication with other characters throughout the story. 

        Conversations happen through a familiar chat interface, with each contact having their own persistent chat history that 
        accumulates across the game. 

        The app is live during active chat blocks in the script, rendering messages in real time as the narrative progresses, 
        and retains full history when revisited later.

        ??? grid col single "Chat App [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat App Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_app`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   App Screen layout Set Up via `app_screen` 
                    -   Contact Panel with Scrollable Contact List via `contact_button` Template
                    -   Chat Box Area via `chat_box` Template
                
                Notes 

                !!! cards col single ""

                    -   Active contact tracked via `active_contact` variable
                    -   On hide: clears active contact and NVL list if not in a chat block
                    -   Contact buttons are managed by the Button Disabler System — enabled per-contact as the story progresses

    === "Draft App"

        ### Draft App 

        !!! tip "Learn more about the Draft System in the [Draft System][draft-system] page"

        The Draft App gives the player a window into the Player Character's creative process. 

        It displays the book draft the Player Character is actively writing throughout the story, with content that 
        accumulates day by day and shifts in tone and direction based on the route taken. 
        It is the most direct reflection of the player's choices made visible as in-world creative output.

        ??? grid col single "Draft App [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Draft App Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `draft_app`
                    
                Visual Layout

                !!! cards col single centered-content ""

                    -   App Screen Layout Set Up via `app_screen` with `draft_tools` as Toolbar Screen
                    -   Draft File Layout via `draft_file` Template
                
                Notes 

                !!! cards col single ""

                    -   Draft content rendered via `print_transcript()`
                    -   Toolbar and settings bar are currently decorative
                    -   Content reflects the Player Character's Suspicion level through the Draft System