---
icon: lucide/cpu
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

# Meta Screens 

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview 

!!! tip "Learn more about Meta Screen template in [Template Screens][template-screens] page"

!!! tip "Learn more about Navigation Dock & Computer UI Menu screens in [Computer UI Screens][computer-ui-screens] page"

Meta Screens are the out-of-game navigation screens accessible through the Quick Menu or the Navigation Dock in the Computer UI Menu.

Most are built on top of Ren'Py special screens, with the primary modification being the adoption of the `meta_screen` template
as their shared layout foundation. A few have additional customization beyond that.

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

                    -   :lucide-save: **Save & Load**
                        [][save-load]{ .card-link }

                    -   :lucide-arrow-down-up: **Save & Load Choice** 
                        [][save-load-choice]{ .card-link }

                    -   :lucide-between-horizonal-start: **File Slots** 
                        [][file-slots]{ .card-link }

                !!! cards col single centered-content ""
                
                    -   :lucide-aperture: **Ending Gallery**
                        [][ending-gallery]{ .card-link }
                    
                    -   :lucide-badge-question-mark: **Controls Help**
                        [][controls-help]{ .card-link }

Below the meta screens for Monster Silhouette that have been modified beyond their layout have been organized into overviews containing information on their: 

- **Screen Name**
- **Parameters**
    - Hover over cards for details (purpose, type, valid values, other notes)
- **Visual Layout** (for Original Screens)
- Additional **Notes**

=== "Ren'Py Provided Screens"

    !!! tip "Visit [Ren'Py Docs][renpy-doc-special-screens] to learn out more about Ren'Py special screens"

    !!! tip "Learn more about Monster Silhouette's `gui.about` in the [Settings & Options][settings-options] page"

    ## Ren'Py-Provided Screens 

    The following screens exist in Ren'Py's default infrastructure and have only been restyled to use the `meta_screen` [template][template-screens] for visual consistency:

    - `about` — content defined in [`options.rpy`][options] via `gui.about`
    - `history` — no content changes, layout only
    - `preferences` — no content changes, layout only
    - `help` — layout only; gained an original MS-Controls tab (see Original Meta Screens tab)

=== "Unified Save & Load Screen" 

    ## Unified Save & Load Screen 

    Ren'Py provides Save and Load as two separate special screens (`save` and `load`) by default. 

    I have repurposed their functionality into a single unified `save_load` screen for Monster Silhouette. 

    When accessed from the Main Menu only loading is available. 
    When accessed in-game both saving and loading functionality are available on the same screen. 

    An additional `save_load_choice` screen handles the case where a player clicks an occupied save slot, prompting them to choose between saving over it or loading from it.

    === "Save Load"

        ### Save Load 

        Save Load is a unified version of the special Ren'Py screens `save` and `load` which: 

        - Conditionally renders load-only (main menu) or save & load (in-game) 
        - Delegates slot rendering to `file_slots`

        ??? grid col single "Save Load [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Save Load Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `save_load`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                    
                Notes 

                !!! cards col single ""

                    -   Replaces Ren'Py's separate `save` and `load` screens

    === "Save Load Choice"

        ### Save Load Choice 

        Save Load Choice is a modal prompt screen that asks the player whether they wish to save or load on an occupied slot.

        ??? grid col single "Save Load Choice [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Save Load Choice Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `save_load_choice`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `slot` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="Save File Identifier. Valid values: valid save file slot number." }
                    
                Notes 

                !!! cards col single ""

                    -   Original screen, no Ren'Py provided equivalent
                    -   Modal with `zorder 200`
                    -   Uses Ren'Py `confirm` screen's GUI Style

    === "File Slots"

        ### File Slots

        File Slots is a screen that renders the grid of save file slots with context-appropriate actions, page navigation, and sync buttons.

        ??? grid col single "File Slots [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: File Slots Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `file_slots`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `context` :lucide-letters:
                        { title="Save & Load Screen Context. Load Context triggers main menu behavior: loading saves immediately. Other or no context triggers in-game behavior: saves immediately on empty slots, and passes through save_load_choice on occupied slots. String. Valid values: 'load', None. All other values will be treated the same as None." }
                    
                Notes 

                !!! cards col single ""

                    -   modified from Ren'Py's original `file_slots` screen — slot actions are now context-dependent rather than fixed

=== "Original Meta Screens"

    ## Original Meta Screens 

    Monster Silhouette currently has 2 original screens in the meta screen ecosystem — one standalone, one nested inside a Ren'Py-provided meta screen.

    === "Ending Gallery"

        ### Ending Gallery 

        An entirely original screen built for Monster Silhouette. Displays endings the player has achieved. 

        Shows a locked placeholder state when no endings have been reached. 
        
        Once at least one ending is unlocked, it switches to a grid layout of ending entries — currently filled with a work in progress placeholder content 
        until real endings are implemented.

        ??? grid col single "Ending Gallery [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Ending Gallery Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `ending_gallery`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                
                Visual Layout 

                !!! cards col single centered-content ""

                    -   Locked State (No Endings)
                    -   Ending Grid (At Least One Ending)
                    
                Notes 

                !!! cards col single ""

                    -   Tracks `player_endings` and `total_endings` variables
                    -   Locked state shown when `player_endings == 0`
                    -   Grid layout shown when `player_endings > 0`; entries are placeholders until real ending content lands
    
    === "Controls Help"

        ### Controls Help

        Provides a reference guide for Monster Silhouette-specific controls — the key bindings and interaction cues that go beyond Ren'Py's defaults. 
        
        It appears as an additional tab (MS-Controls) inside the Help meta screen, alongside Ren'Py's Keyboard, Mouse, and Gamepad tabs.

        ??? grid col single "Controls Help [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Controls Help Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `controls_help`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                    
                Visual Layout

                !!! cards centered-content ""

                    - Key Binding List
                    - Hint Icon Reference
                
                Notes 

                !!! cards col single ""

                    -   Rendered inside Help's tabbed navigation
                    -   Default tab when Help opens
                    -   Sits alongside Ren'Py's Keyboard, Mouse, and Gamepad help tabs