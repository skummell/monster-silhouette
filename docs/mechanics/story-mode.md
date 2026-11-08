---
icon: lucide/book-open-text
# status: modified 
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

# Story Mode

## Overview 

Monster Silhouette's Story Mode is a branching narrative where every choice carries weight. 

No choice is purely cosmetic — all of them have consequences, starting from the very first you make, 
even if you don't recognize it as a significant choice initially.

=== "Choices & Branching"
        
    ## Choices & Branching 

    Choices affect narration, available dialogue options, and which scenes play out. 

    Some choices unlock or lock future options entirely. 

    Consequences can be immediate or surface much later in the story.

=== "The Book Draft"

    !!! tip "Learn more about the Draft App screen in the [App Screens][app-screens] page"

    !!! tip "Learn more about Suspicion level's effect on Draft contents in the [Draft System][draft-system] page"

    ## The Book Draft 

    A core narrative premise of Monster Silhouette is that the Player Character is a writer working on a book throughout the story. 

    The Draft App reflects the Player Character's writing progress. 
    <br>
    The content of the draft changes based on the route taken — specifically, the Player Character's Suspicion level at the end of each
    day directly shapes what gets written.

    It serves as both a narrative mirror and a way to experience the story through the Player Character's own creative lens — their interpretation of the events 
    unfolding around them, filtered through their own suspicion and uncertainty, and reflected on their work.

=== "States & Flags"

    ## States & Flags

    States and Flags are what translate choices, interactions and branching from narrative intent into actual in-game behavior. 

    Every decision the player makes — whether visible or invisible — is recorded and tracked through a system of flags and state variables 
    that the game reads continuously to determine what content to show, what options to make available, and how characters respond.

    === "In-Game States"

        The story tracks two categories of states: **Hidden States** and **Visible States**.
        
        #### Hidden States 

        Hidden flags that drive internal game logic.

        The player doesn't see them directly but their effects are felt throughout the narrative in the form of changed scenes, 
        locked or unlocked options, and different character reactions.
        
        #### Visible States
        
        !!! tip "Learn more about the Profile App screen in the [App Screens][app-screens] page"

        !!! tip "Learn more about the Computer UI interface in the [Computer UI][computer-ui-mechanic] page"

        Player-facing representations of visible flags and a select number of hidden flags.

        Live values are accessible through the Profile App and other parts of the Computer UI interface. 

    === "In-Game Flags"

        Flags are individual variables that drive both Hidden and Visible States. 
        <br>
        Some are boolean — on or off — others are numeric. 
        <br>
        Each one tracks a specific aspect of the player's journey through the story.

        Monster Silhouette tracks a large number of these throughout its narrative. A few notable ones include:

        === "Player Name"

            #### Player Name

            The name chosen at the start is the first choice and sets the tone for everything that follows. 

            One specific name choice unlocks additional content and dialogue paths throughout the game. 

            The Profile Screen displays the chosen name throughout the playthrough. 

        === "Rapport & Suspicion"

            #### Rapport & Suspicion

            Rapport and Suspicion are key states the player can track through the Profile App once accessible. 

            Both stats are locked on the Profile App in the beginning of the story and become visible as the story progresses. 
            Unlocking them is itself tied to progressing through story events.
                    
            Both run on a 0-10 scale.

            === "Mephisto's Rapport"

                ##### Rapport

                Reflects the relationship between the Player Character and Mephisto. 

                Affects how Mephisto behaves and what he's willing to say or do in response to the Player Character's 
                own words and actions.

            === "Player Character's Suspicion"

                ##### Suspicion

                Reflects the Player Character's attitude toward Mephisto and the mystery he represents. 
                    
                Affects available dialogue options and how the Player Character interprets events unfolding in the game's 
                story and narrative.

        === "Deadline"

            #### Deadline

            The Deadline tracks the in-game days remaining until the Player Character's book transcript is due. 
            <br>
            This flag is visible on the Profile App throughout playthrough. 
            
            It begins at 7 and decrements at the end of each day. 
            <br>
            Reaching 0 marks the end of the story.

        === "Other Flags"

            #### Other Flags

            Many other flags and variables shape the experience in subtler ways. These include:

            - **Preparation Choice Flags** — whether the player arrived early, brought their wallet, or took a nap before heading out. Each affects scene availability and narration.
            - **Clothing Choice Flags** — the top and bottom garments chosen during the Prep Phase. Certain combinations trigger unique character reactions and additional dialogue.
            - **Relationship Flags** — choices made in conversation that affect how other characters perceive and respond to the Player Character beyond Mephisto's Rapport stat.