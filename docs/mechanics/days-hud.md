---
icon: lucide/calendar
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

# Screen HUD & In-Game Dates

## Overview 

The Screen HUD and the In-Game Dates are two systems that together define the temporal structure of Monster Silhouette's story narrative. 

The In-Game Day system governs how the story is paced and structured across time, while the Screen HUD keeps the player anchored to that structure at all times.

=== "Screen HUD"

    !!! tip "Learn more about Status Bar screen containing Screen HUD in [Overlay Screens][overlay-screens] page"

    !!! tip "Learn more about Screen HUD in Computer UI in [Computer UI Screens][computer-ui-screens] page"

    ## Screen HUD 

    A persistent overlay that displays throughout the game whenever enabled. Its primary elements are the current 
    in-world date and the current in-world time.

    Neither the date nor the time reflect real time — both are in-world values that advance at scripted story beats. 
    Time in particular jumps forward at key narrative moments rather than ticking continuously.

    The HUD is disabled in specific contexts — the Lock Screen being one example — and its visual elements on screen change 
    depending on where the player is in the game.

=== "In-Game Dates"

    ??? info "Demo & Full Game"
        The Demo covers Day 1 only.

        The full game is planned to span 7 days, from September 26th to October 2nd. 
        <br>
        Concluding the story at the start of Day 8 on October 3rd.
        
        Finished product of the game will likely expand on Day 1 of Demo and be released episodically.

    ## In-Game Dates 

    === "Overview"

        !!! tip "Learn more about the Deadline countdown on the Profile App in the [App Screens][app-screens] page"

        The story is structured across a fixed sequence of in-game days, each locked to a specific real calendar date and day of the week 
        — September 26th through October 3rd. 
        <br>
        These dates are strictly bound to the game's narrative and have nothing to do with real time.

        A day advances through story progression and player action, ending only once the Wrap Phase is completed.

        Each day is self-contained with its own unique narrative events, but the state the player carries out of one day directly shapes what is available in the next. 
        The Deadline countdown on the Profile App decrements at the end of each day and stays in sync with day progression.

        Day 8, October 3rd, is the story's endpoint. The story concludes at its start rather than playing through it.

    === "Structure of a Day"

        !!! tip "Learn more about the Wrap & Prep Phases in the [Prep & Wrap Modes][prep-wrap-mechanic] page"

        ### Structure of a Day

        Most in-game days are structured similarly narratively, including the following parts of a day:

        - **Introduction** — narrative setup, establishes the day's context
        - **Prep Phase** — interactable bedroom scene before the main events
        - **Main Narrative** — primary story events, character interactions
        - **Conclusion & Wrap Phase** — interactable bedroom scene to close out the day