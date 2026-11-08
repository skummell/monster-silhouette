---
icon: lucide/blend
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

# Overlay Screens 

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview 

Overlay screens are screens that display on top of the game at all times while active. 

They are registered as overlay screens in Ren'Py's config, meaning they persist across scene
changes and script progression without needing to be explicitly shown each time.

??? info "Screen Overview Legend"

    === "Legend"

        <p id="screen-overview-legend"></p>
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-letters:          | :lucide-lock-open:           |
        | ------------------------------------- | ------------------------- | ---------------------------- |
        | Required parameters                   | Fixed set of valid values | NO fixed set of valid values |

    === "Go To Screen Overviews"

        !!! cards col single no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards col centered-content ""

                    -   :lucide-refresh-ccw: **Status Bar**
                        [][status-bar]{ .card-link }

                    -   :lucide-astroid: **Freeze Hint Display** 
                        [][freeze-hint-display]{ .card-link }

                    -   :lucide-triangle-alert: **Exit Disabled Warning** 
                        [][exit-disabled-warning]{ .card-link }
                
                    -   :lucide-message-square-dot: **Chat App Notification**
                        [][chat-app-notification]{ .card-link }

                !!! cards col single centered-content ""
                    
                    -   :lucide-square-dashed-mouse-pointer: **Tooltip Hover** 
                        [][tooltip-hover]{ .card-link }

=== "Visibility & Registration"

    !!! tip "Overlay screens are registered through `config.overlay_screens` in [screens.rpy][screens]."

    ## Visibility & Registration

    Unlike regular screens that need to be explicitly shown and hidden through script or screen actions, 
    registered overlay screens are managed automatically by Ren'Py — they stay active as long as their internal 
    display conditions are met, regardless of what else is happening in the game.

    Each overlay screen defines its own conditions for when it should be visible, rather than relying on external show and hide calls.

=== "Screens"

    ## Screens

    Below all the original overlay screens for Monster Silhouette have been organized into overviews containing information on their: 

    - **Screen Name**
    - **Parameters**
        - Hover over cards for details (purpose, type, valid values, other notes)
    - **Visual Layout**
    - Additional **Notes**

    === "Status Bar"

        !!! tip "Learn more about the Computer UI screens in the [Computer UI Screens][computer-ui-screens] page"

        ### Status Bar 

        Displays the in-world date and time persistently throughout the game. 
        Also displays Computer UI-specific icons when inside the Computer UI. 
            
        Active whenever `status_bar = True` or when inside Computer UI Menu. 

        ??? grid col single "Status Bar [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Status Bar Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `status_bar`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Top Bar Background 
                    -   Computer UI Icons 
                    -   Date Text 
                    -   Time Text Button 
                
                Notes 

                !!! cards col single ""

                    -   Computer UI icons only visible when inside Computer UI screen (`computer_ui` & `computer_ui_menu`)
                    -   Time display doubles as a return-to-game button when inside Computer UI Menu
                    -   In-game visibility controlled by `status_bar` boolean variable

    === "Freeze Hint Display"

        !!! tip "Learn more about the Freeze System in the [Freeze System][freeze-system] page"

        ### Freeze Hint Display 

        Displays a hint to the player during a Freeze block, guiding them toward the action needed to continue the story. 

        Only shows when `_current_hint` is not `None` and the player is not inside the Computer UI Menu.

        ??? grid col single "Freeze Hint Display [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Freeze Hint Display Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `freeze_hint_display`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Hint Frame Wrapper
                    -   Hint Text
                
                Notes 

                !!! cards col single ""

                    -   Content driven by `_current_hint` variable, set and cleared by the Freeze System
                    -   Hidden during Computer UI Menu to avoid cluttering the menu

    === "Exit Disabled Warning"

        !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

        ### Exit Disabled Warning 

        Displays a warning message when a player opens an app whose exit button is currently disabled, 
        informing them to use the ESC shortcut instead.

        ??? grid col single "Exit Disabled Warning [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Exit Disabled Warning Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `exit_disabled_warning`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `app` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Display name of the app shown in the warning message. String." }
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Warning Frame Wrapper
                    -   Warning Text
                
                Notes 

                !!! cards col single ""

                    -   Only shown when inside Computer UI Menu and the relevant app exit button is disabled
                    -   Called directly in app screen definitions conditionally
                    
    === "Chat App Notification"

        !!! tip "Learn more about the Chat App in the [App Screens][app-screens] page"

        ### Chat App Notification 

        A notification popup that appears when new chat messages arrive during script progression. 

        Doubles as a button to open the Chat App directly.

        ??? grid col single "Chat App Notification [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat App Notification Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_app_notification`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   `msg` :lucide-lock-open:
                        { title="Number of new messages to display. Int. Default: 1." }
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Notification Button layout via `notif_button` template
                    -   Notification Detail Text
                
                Notes 

                !!! cards col single ""

                    -   Uses `notif_button` template
                    -   On click: opens Chat App and hides itself
                    -   When disabled via Button Disabler System: does nothing
                    -   Shown via `show_notif` statement in script
    
    === "Tooltip Hover"

        !!! tip "Learn more about the Hovers & Tooltips mechanic in the [Hovers & Tooltips][hovers-tooltips-mechanic] page"

        ### Tooltip Hover

        Renders the tooltip for whichever interactive element currently has focus. 

        Style varies based on the active screen — the screen selects from four style families to match the context it's rendering in.

        ??? grid col single "Tooltip Hover [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Tooltip Hover Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `tooltip_hover`
                    
                Parameters 

                !!! cards col single centered-content ""

                    -   N/A
                    
                Visual Layout

                !!! cards centered-content ""

                    -   Tooltip Frame 
                    -   Tooltip Text
                
                Notes 

                !!! cards col single ""

                    -   Applies one of four style families based on active screen
                    -   Uses inline `use tooltip_hover` in Computer UI Menu and app screens opened from it, where overlays are suppressed
                    -   Content comes from `tooltip` inline `"text"` declarations or `tooltip_content` dictionary lookups



