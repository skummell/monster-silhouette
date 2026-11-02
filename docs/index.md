---
icon: lucide/rocket
status: new 
tags: 
    - Index
    - ㅤLast Updated
    - ㅤㅤNovember
    - ㅤㅤㅤ1
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If the date matches up with the last date-range entry in the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Introduction

??? info "Ren'Py Engine Version"

    Monster Silhouette is made using [Ren'Py Engine 8.5.3][renpy-8.5.3] (currently the latest Release)

## Overview

Monster Silhouette is a Visual Novel RPG made by SkumMell (me) with [Ren'Py Visual Novel Engine][renpy-web]. 

The Documentation in this site primarily provides details on unique source code features implemented and coded into Monster 
Silhouette by me beyond what [Ren'Py Engine][renpy-doc] already provides.

=== "Brief Description"

    ### Brief Description

    All choices matter, starting from the name you choose.
    <br>
    All choices have consequences, most of which will be long term.

    Demo being built as a semester long project.
    <br>
    The demo's initial premise, script draft and narrative conceptualization were done in 5 days. 
    <br>
    The final game will *likely* see considerable changes from the demo. 


    ??? grid centered "Categorization Card"
        <!-- tooltip: Monster Silhouette's Categorization Card -->

        **TITLE**

        !!! cards col single ""

            -   Monster Silhouette

        **RATING**

        !!! cards col single ""

            -   16+ Mature

        **TAGS**

        !!! cards col three bordered "" 

            -   Visual Novel
            -   RPG
            -   Indie
            -   Single Player
            -   Multiple Endings
            -   Choices Matter

        **GENRES**

        !!! cards col three bordered ""

            -   Horror
            -   Slice of Life
            -   Mystery
             
        **DEMO RELEASE DATE (EST)**

        !!! cards col single ""

            -   Late December, 2026

=== "Narrative Premise"

    ### Narrative Premise 

    *You* are a mystery horror writer.

    The deadline to *your* latest sequel is approaching but because *you* didn't have the identity of *your* 
    culprit planned beforehand, *you* have to come up with it now. 

    *You've* been holed up in *your* room working on it for the last few months, living off take out, 
    when *you* receive a message from *your* best friend. 

    *Your* best friend, Theo is an outgoing, cheerful guy who's always busy. 
    He usually comes around to check on *you*, but hasn't done so in a few days because he's traveling. 
    The message tells *you* to get out of the house once and visit *your* mutual friend, Victor in his niche tea-lounge. 
    Telling *you* that changing scenery will be good for *your* progress. 

    Unable to refuse his request *you* decide to go the next day early afternoon. 

    There *you* meet *your* new inspiration. 

    A new guy in town who *you* can only see the silhouette of, despite everyone else acting as
    if there's nothing wrong with him. Often commenting on his physical appearance which *you* can see none of. 
    Strangely this silhouette has something not so usual, that catches *your* attention even more. 

## Official Channels

Monster Silhouette's official links and pages.
<br>
Any pages not linked or discussed below are not to be considered Official Channels.

!!! tip "More official channels will be added as game development continues."

### Links

=== "Creator's Social Media" 

    !!! cards col three ""

        -   :octicons-mark-github-24: GitHub
            [][skummell-github]{ .card-link }

        -   :simple-instagram: Instagram
            [][skummell-insta]{ .card-link }
        
        -   :simple-tumblr: Tumblr
            [][skummell-tumblr]{ .card-link }

=== "Project Source Code"

    !!! cards ""

        -   :octicons-repo-24: Source Code
            [][github-repo]{ .card-link }

        -   :octicons-code-square-24: Source Code Doc
            [][source-doc]{ .card-link }

### Brief Overviews

#### :octicons-repo-24: GitHub Repository 

The [Monster Silhouette GitHub Repository][github-repo] serves as a partial source code showcase that includes the 
non-narrative portions of the game's [project files][project-files-heading]. 

It provides access to the git commit history of these files to be viewed freely throughout build progression and keeps 
track of a detailed project build log.

!!! cards col single ""

    -   :octicons-book-24: **`README`** - Repository & Project Overview [:octicons-view-files-24:][readme-preview]{ .hover-preview }
        [][readme]{ .card-link }

    -   :octicons-law-24: **`LICENSE`** - Source Code License [:octicons-view-files-24:][license-preview]{ .hover-preview }
        [][license]{ .card-link }

    -   :octicons-history-24: **`COMMITS`** - Public Commit History
        [][commits]{ .card-link }

    -   :octicons-log-24: **`LOG`** - Project Build Log [:octicons-view-files-24:][log-preview]{ .hover-preview }
        [][log]{ .card-link }


## Source Code Files & Folders

Overviews and File Trees for Files & Folders relevant to Monster Silhouette's source code and features. 

This section contains a mention of every source code file that has been modified by me at some point, 
including both [Monster Silhouette Project Files][project-files-heading] and [Ren'Py Engine Files][engine-files-heading].

??? info "File Tree Legend"

    === "Legend"

        <p id="file-tree-legend"></p>

        | :octicons-file-directory-fill-24: | :octicons-file-24: | :octicons-eye-24:     | :octicons-eye-closed-24:  | :octicons-copy-24: | :octicons-compose-24: |
        | --------------------------------- | ------------------ | --------------------- | ------------------------- | ------------------ | --------------------- |
        | Folder                            | File               | In Public GitHub Repo | NOT in Public GitHub Repo | Provided by Ren'Py | Created by me         |
        
        | :lucide-circle-ellipsis: | :lucide-circle-dashed: |
        | ------------------------ | ---------------------- |
        | NOT empty when provided  | Empty when provided    |

    === "Go To File Trees"

        !!! cards ""

            -   :lucide-square-kanban: Project File Tree
                [][project-file-tree]{ .card-link }

            -   :lucide-cog: Engine File Tree
                [][engine-file-tree]{ .card-link }

=== "Project Files"


    !!! tip "For Limited Access to Monster Silhouette's Project Files"

        Check out [Monster Silhouette's Public GitHub][github-repo] Repository
    
    ### Project Files 

    The core of a Ren'Py project is generated into a `game/` directory inside the designated Project File Directory by Ren'Py Visual Novel Engine.

    This core project directory contains all editable script files (`.rpy`), images, audio and compiled bytecode (`rpyc`).

    !!! warning "In this Documentation we will only discuss `.rpy` Project Files in detail" 

    #### Relevant Project Files & Folders 

    !!! tip "Check [File Tree][project-file-tree] for file content inside of folders"

    === "Folders & Files generated by Ren'Py Engine"

        **Folders & Files generated by Ren'Py Engine**

        - `game/`: Core Project Files.
        - `images/`: For background and character sprites. 
        - `audio/`: For music and sound effects. 
        - `gui/`: For interface graphics like buttons and other UI elements. 
        - `tl/`: For translation files. 
        - `cache/` and `saves/`: Generated directories for performance and user progress
        - `script.rpy`: Main dialogue and logic 
        -  `options.rpy`: Configuration settings. 
        - `screens.rpy`: UI Screen definitions. 
        - `gui.rpy`: Visual styling settings and tracked variables.

    === "Folders & Files created by me"

        **Folders & Files created by me**

        - `monster-silhouette/`: Project Directory.
        - `fonts/`: For fonts used in game. 
        - `script/`: For organized script files containing game narrative content.
        - `gui/placeholders/`: For Monster Silhouette's unique GUI graphics placeholder assets. 
        - `images/placeholders/`: For Monster Silhoueete's Sprite and Background graphics placeholder assets.
        - `custom_systems.rpy`: For custom game systems and statements.

    #### File Tree [:octicons-key-asterisk-24:][tree-legend] { #project-file-tree } 

    ??? folder "`monster-silhouette/` :octicons-eye-24:  :octicons-compose-24:" 
        ??? folder "`game/` :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:"
            !!! folder "`audio/` :octicons-eye-closed-24: :octicons-copy-24: :lucide-circle-dashed:"
            !!! folder "`fonts/` :octicons-eye-closed-24: :octicons-compose-24:"

            ??? folder "`gui/` :octicons-eye-closed-24: :octicons-copy-24: :lucide-circle-ellipsis:"

                !!! folder "`placeholders/` :octicons-eye-closed-24: :octicons-compose-24:"

            ??? folder "`images/` :octicons-eye-closed-24: :octicons-copy-24: :lucide-circle-dashed:"

                !!! folder "`placeholders/` :octicons-eye-closed-24: :octicons-compose-24:"

            ??? folder "`libs/` :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:"
                [:octicons-file-24: `libs.txt`][libs] :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:

            ??? folder "`script/` :octicons-eye-closed-24: :octicons-compose-24:"

                ??? folder "`demo/` :octicons-eye-closed-24: :octicons-compose-24:"
                    ??? folder "`demo_book_drafts/` :octicons-eye-closed-24: :octicons-compose-24:"
                        
                        :octicons-file-24: `demo_book_draft0.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                        :octicons-file-24: `demo_book_draft1.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                    ??? folder "`demo_choices/` :octicons-eye-closed-24: :octicons-compose-24:"

                        :octicons-file-24: `demo_choice1.rpy` :octicons-eye-closed-24: :octicons-compose-24:
                        
                    ??? folder "`demo_interludes/` :octicons-eye-closed-24: :octicons-compose-24:"

                        :octicons-file-24: `demo_interlude1.rpy` :octicons-eye-closed-24: :octicons-compose-24:
                        
                    ??? folder "`demo_prep/` :octicons-eye-closed-24: :octicons-compose-24:"

                        :octicons-file-24: `demo_bed_click.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                        :octicons-file-24: `demo_closet_click.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                        :octicons-file-24: `demo_key_click.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                        :octicons-file-24: `demo_laptop_click.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                        :octicons-file-24: `demo_wallet_click.rpy` :octicons-eye-closed-24: :octicons-compose-24:

                    :octicons-file-24: `demo_intro.rpy` :octicons-eye-closed-24: :octicons-compose-24:

            ??? folder "`tl/` :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:"

                ??? folder "`None/` :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:"

                    [:octicons-file-24: `common.rpym`][common] :octicons-eye-24: :octicons-copy-24: :lucide-circle-ellipsis:

                
            [:octicons-file-24: `custom_systems.rpy`][systems]   :octicons-eye-24:  :octicons-compose-24:

            [:octicons-file-24:  `gui.rpy`][gui]                  :octicons-eye-24:       :octicons-copy-24: :lucide-circle-ellipsis:

            [:octicons-file-24:  `options.rpy`][options]          :octicons-eye-24:       :octicons-copy-24: :lucide-circle-ellipsis:

            [:octicons-file-24:  `screens.rpy`][screens]          :octicons-eye-24:       :octicons-copy-24: :lucide-circle-ellipsis:

            [:octicons-file-24:  `script.rpy`][script]            :octicons-eye-24:       :octicons-copy-24: :lucide-circle-ellipsis:

=== "Engine Files"

    !!! tip "For Full Access to Ren'Py's Engine Files"

        Check out [Ren'Py's Source Code][renpy-repo] or download [Ren'Py Visual Novel Engine][renpy-latest] for yourself

    ### Engine Files 

    When you download Ren'Py Visual Novel Engine from the [Ren'Py Website][renpy-web], you obtain a folder whose name is 
    conventionally formatted as `renpy-ver-sdk`, where `ver` is the engine's version number (#.#.#).

    Inside it contains the Ren'Py Engine Launcher alongside the engine files.

    !!! warning "In this Documentation we will only discuss Engine Files I have modified"

    #### Relevant Engine Files & Folders 

    !!! tip "Check [File Tree][engine-file-tree] for file content inside of folders"

    - `renpy-8.5.3-sdk/` - Engine File Directory.
    - `renpy/` - Python engine source.
    - `common/` - Built in `.rpy` scripts Ren'Py ships with.
    - `00gamemenu.rpy` - Defines game menu infrastructure.
    - `00action_menu.rpy` - Defines built-in actions for navigating and controlling the game menu.

    #### File Tree [:octicons-key-asterisk-24:][tree-legend] { #engine-file-tree } 

    ??? folder "`renpy-8.5.3-sdk/` :octicons-eye-closed-24:  :octicons-copy-24: :lucide-circle-ellipsis:" 

        ??? folder "`renpy/` :octicons-eye-closed-24:  :octicons-copy-24: :lucide-circle-ellipsis:" 

            ??? folder "`common/` :octicons-eye-closed-24:  :octicons-copy-24: :lucide-circle-ellipsis:" 

                :octicons-file-24: `00gamemenu.rpy` :octicons-eye-closed-24:  :octicons-copy-24: :lucide-circle-ellipsis:

                :octicons-file-24: `00action_menu.rpy` :octicons-eye-closed-24:  :octicons-copy-24: :lucide-circle-ellipsis:

## Interactive Mechanics & Documentation Categories

In this Documentation, besides this introductory page informing you of basics, you will be able to find
pages on Monster Silhouette's Interactive Mechanics and several Documentation Categories.

=== "Interactive Mechanics"

    ??? tip "Check out the Gameplay Mechanics pages for more details:"

        !!! cards col four centered-content ""

            -   :lucide-book-open-text: **Story Mode**
                [][story-mode-mechanic]{ .card-link }
            
            -   :lucide-laptop-minimal: **Computer UI** 
                [][computer-ui-mechanic]{ .card-link }
            
            -   :lucide-sun-moon: **Prep & Wrap Modes** 
                [][prep-wrap-mechanic]{ .card-link }
            
            -   :lucide-calendar: **Screen HUD & In-Game Dates** 
                [][days-hud-mechanic]{ .card-link }

    ### Gameplay Mechanics 

    Monster Silhouette has and uses multiple game mechanics besides the built-in Ren'Py script statements and coded features.

    These Gameplay Mechanics are built around several unique Game Systems and can be split into the following categories:

    === "Story Mode"

        **Story Mode**

        The story mode of the game is a branching narrative affected by player choices. 

        Game logic is designed and organized on top of a UML State Machine Model, with patterns abstracted and represented as multiple Finite State Machine Models. 

        The UML serves to manage the complex, branch narratives, while the FSM defines complex character behavior and narrative paths through a 
        series of states, events and actions. 

    === "Computer UI"

        **Computer UI**

        The game includes a Computer UI mode separated into two flavors: in-world operational prop and game navigation menu. 

        The Computer UI serves as a custom game system that blends the in-world use of a computer with meta game functionalities by allowing the player 
        to access Meta Screens and other in-world systems through the same screen. 

    === "Prep & Wrap Modes"

        **Prep & Wrap Modes**

        During every in-game day at the beginning and the end of day the player will get to experience the Prep Phase and Wrap Phase game modes which allows 
        them to prepare or wrap up the day, respectively.

        These game modes both take place in the Bedroom of the Player Character. 
        <br>
        With the player being able to freely click around interactive parts of the Player Character's Bedroom.

    === "Screen HUD & In-Game Dates"

        **Screen HUD**

        The game includes a permanent HUD element that displays in-game at all times as long as its enabled.

        The primary elements in it are the in-world Date and Time. 

        **In-Game Dates**

        The in-world date goes from **September 26th** to **October 3rd**. 

        Each date will have their own unique fixed events apart from each other, with exception of the Prep and Wrap Phases that are fixed 
        throughout all of the dates. Though the phases themselves will also have narrative changes from one day to the other.

=== "Documentation Categories"

    ### Documentation

    Source Code Documentation in this site has been separated into several categories for organization: 

    === "Game Screens"

        ??? tip "Check out the Game Screens pages for more details:"

            !!! cards col three centered-content ""

                -   :lucide-layout-template: **Template Screens**
                    [][template-screens]{ .card-link }

                -   :lucide-cpu: **Meta Screens**
                    [][meta-screens]{ .card-link }

                -   :lucide-blend: **Overlay Screens**
                    [][overlay-screens]{ .card-link }

                -   :lucide-monitor: **Computer UI Screens**
                    [][computer-ui-screens]{ .card-link }

                -   :lucide-layout-grid-circles: **App Screens**
                    [][app-screens]{ .card-link }

                -   :lucide-gamepad-2: **Game Mode Screens**
                    [][game-mode-screens]{ .card-link }

        **Game Screens** 

        Game Screen Documentation provides an overview of any custom screens or modifications I've made to Ren'Py special screens for Monster Silhouette.

        Game Screens are primarily defined in [`screens.rpy`][screens] file.
        <br>
        Where you'll be able to find all the screen definitions. 

    === "Game Systems"

        ??? tip "Check out the Game Systems pages for more details:"

            !!! cards col three centered-content ""

                -   :lucide-image: **Scene System**
                    [][scene-system]{ .card-link }
                
                -   :lucide-mouse-pointer-2-off: **Button Disabler System** 
                    [][button-disabler-system]{ .card-link }
                
                -   :lucide-messages-circle: **Chat System** 
                    [][chat-system]{ .card-link }
                
                -   :lucide-feather: **Draft System** 
                    [][draft-system]{ .card-link }
                
                -   :lucide-pause: **Freeze System**
                    [][freeze-system]{ .card-link }
                
                -   :lucide-gamepad-directional: **Game Mode System** 
                    [][game-mode-system]{ .card-link }

        **Game Systems** 

        Game System Documentation provides an overview of the custom game systems I've created to manage the unique mechanics in Monster Silhouette. 

        Game Systems are primarily defined in [`custom_systems.rpy`][systems] file. 
        <br>
        Where you'll be able to find the different game systems' variables, functions and statements.
        <br>
        These game systems serve to make the interaction between script labels and files and other parts of the game's code easy and clean.

    === "Settings & Options"

        !!! tip "Check out the [Settings & Options][settings-options] page for more details"

        **Settings & Options**

        Settings & Options Documentation provides an overview of minor setting and option adjustments and additions I've made for Monster Silhouette. 

        Settings & Options are primarily defined in [`gui.rpy`][gui] and [`options.rpy`][options] files. 
        <br>
        Where you'll be able to find GUI Configurations and Customization Options for the game. 

    === "Custom Actions"

        !!! tip "Check out the [Custom Actions][custom-actions] page for more details"

        **Custom Actions**

        Custom Actions Documentation provides an overview of custom engine actions I have defined. 

        Custom Actions touch engine files, and in this case are primarily defined in `00gamemenu.rpy` and `00action_menu.rpy` files. 
        <br>
        Where you'll be able to find Game Menu Definition and Actions. 