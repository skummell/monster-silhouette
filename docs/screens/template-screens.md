---
icon: lucide/layout-template
status: new 
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

# Template Screens

!!! tip "Code discussed in this page can be found in [`screens.rpy`][screens]"

## Overview

Template screens are reusable screen definitions that other screens are built on top of or make use of. 
Rather than duplicating layout and logic across multiple screens, common patterns are abstracted into templates that accept parameters to customize their output.

Below all the template screens for Monster Silhouette have been organized into overviews containing information on their: 

- **Screen Name**
- **Parameters**
- **Layout Components**
- Additional **Notes**
- A list of screens the templates are **Used By**.

??? info "Screen Overview Legend"

    === "Legend"

        <p id="screen-overview-legend"></p>
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-letters:          | :lucide-lock-open:           |
        | ------------------------------------- | ------------------------- | ---------------------------- |
        | Required parameters                   | Fixed set of valid values | NO fixed set of valid values |

    === "Go To Screen Overviews"

        !!! cards no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards col single centered-content ""

                    -   :lucide-binary: **Meta Screen**
                        [][meta-screen]{ .card-link }

            !!! grid col single no-pad no-border ""

                !!! cards centered-content ""

                    -   :lucide-app-window: **App Screen**
                        [][app-screen]{ .card-link }
                    
                    -   :lucide-hash: **App Header**
                    [][app-header]{ .card-link }

                    -   :lucide-x: **App Exit**
                        [][app-exit]{ .card-link }

                    -   :lucide-squircle: **App Button**
                        [][app-button]{ .card-link }

            !!! grid col single no-pad no-border ""

                !!! cards centered-content ""
                    -   :lucide-contact-round: **Contact Button**
                        [][contact-button]{ .card-link }
                    
                    -   :lucide-message-square-dashed: **Chat Box**
                        [][chat-box]{ .card-link }

                    -   :lucide-message-square-text: **Chat Bubble**
                        [][chat-bubble]{ .card-link }

                    -   :lucide-stamp: **Timestamp For Chat**
                        [][timestamp-for-chat]{ .card-link }

                    -   :lucide-calendar-1: **Chat Date Stamp**
                        [][chat-date-stamp]{ .card-link }

                    -   :lucide-clock-1: **Chat Time Stamp**
                        [][chat-time-stamp]{ .card-link }

            !!! grid col single no-pad no-border ""

                !!! cards col single centered-content ""
                    -   :lucide-notepad-text-dashed: **Draft File**
                        [][draft-file]{ .card-link }

        !!! cards centered-content ""

            -   :lucide-mouse: **Scrollable Content**
                [][scrollable-content]{ .card-link }
                
            -   :lucide-monitor-dot: **Notif Button**
                [][notif-button]{ .card-link }

!!! tip 
    
    Hover over parameter cards for a brief description of: 

    - what they're used for
    - what type their values should be
    - what are the valid values (if they apply)
    - any other note worthy nuances

=== "Meta Templates"

    !!! tip "Learn more about Meta Screens in the [Meta Screens][meta-screens] page"

    ## Meta Templates 

    The Meta Screen Templates set up the basic layout for Meta Screen components.

    ### Meta Screen

    The Meta Screen Template sets up the basic layout all Meta Screens share.

    ??? grid col single "Meta Screen [:octicons-key-asterisk-24:][screen-overview-legend]"

        <!-- tooltip: Meta Screen Overview Card -->

        !!! grid scrollable ""

            Screen Name 

            !!! cards col single ""

                -   `meta_screen`
            
            Parameters 

            !!! cards ""

                -   `title` :octicons-north-star-24:{ .red-icon } :lucide-lock-open: 
                    { title="Display title shown in the header bar. String." }
                -   `scroll` :lucide-letters:
                    { title="Scroll mode for the content area. String. Valid values: 'viewport', 'vpgrid'. Default: None (no scroll)." }
                -   `yinitial` :lucide-lock-open: 
                    { title="Initial vertical scroll position. Int or Float. 0.0 = top, 1.0 = bottom. Default: 0.0." }
                -   `spacing` :lucide-lock-open: 
                    { title="Spacing between content items in pixels. Int. Default: 0." }
                
            Layout Components

            !!! cards col single centered-content ""

                -   Background
                -   Header Bar with Title & Close Button
                -   Main Content Area
            
            Notes 

            !!! cards col single ""

                -   Content area supports optional scrolling via `scrollable_content`
                -   Close button returns to previous screen
                -   All six Meta Screens are built on this template
            
            Used By

            !!! cards ""

                -   `about`
                -   `save_load`
                -   `history` 
                -   `preferences` 
                -   `help` 
                -   `ending_gallery`

=== "App Templates"

    !!! tip "Learn more about App Screens in the [App Screens][app-screens] page"

    ## App Templates 

    The App Screen Templates set up the basic layout for App components.

    === "App Screen"

        ### App Screen 

        The App Screen Template sets up the basic layout all App Screens share.

        ??? grid col single "App Screen [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: App Screen Template Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `app_screen`
                        
                Parameters 

                !!! cards ""

                    -   `window_width` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Width of the app window in pixels. Int." } 
                    -   `window_height` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Height of the app window in pixels. Int." }
                    -   `content_width` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Width of the main content area in pixels. Int." }
                    -   `content_height` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Height of the main content area in pixels. Int." }
                    -   `screen_title` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Display title shown in the app header bar. String." }
                    -   `tool_screen` :lucide-letters:
                        { title="Name of an optional toolbar screen to render alongside the content area. String. Valid values: any registered tool screen name. Default: None." }
                    
                Layout Components 

                !!! cards col single ""

                    -   Background
                    -   Header bar via `app_header`
                    -   Main Content Area
                    
                Notes 

                !!! cards col single ""

                    -   Accepts an optional `tool_screen` parameter to render an additional toolbar screen alongside the main content
                    -   Content is passed via `transclude` — each app fills it with its own content

                Used By 

                !!! cards col single ""

                    -   `profile_app`
                    -   `chat_app`
                    -   `draft_app`
    
    === "App Header" 

        ### App Header 

        The App Header Template renders the title bar and places an exit button inside an app window.

        ??? grid col single "App Header [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: App Header Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `app_header`
                    
                Parameters    
                        
                !!! cards ""

                    -   `window_width` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Width of the header bar in pixels. Int. Should match the app's window width." }
                    -   `screen_title` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Display title shown centered in the header bar. String." }

                Layout Components 

                !!! cards col single ""
                        
                    -   App Title Text centered 
                    -   Exit Button via `app exit` on the left
                    
                Used By
                    
                !!! cards col single ""

                    -   `app_screen`
    
    === "App Exit"

        ### App Exit 

        The App Exit Template renders an exit button with a unique linked id on app screens. 

        ??? grid col single "App Exit [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: App Exit Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `app_exit` 
                    
                Parameters    
                        
                !!! cards col single ""

                    -   `id_name` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="Button ID used by the Button Disabler System. String. Valid values: app exit IDs registered in valid_button_ids." }

                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   App Exit Icon Idle
                    
                Notes 

                !!! cards col single ""

                    -   When enabled: hides the current screen
                    -   When disabled via Button Disabler System: does nothing but remains visible
                    
                Used By
                    
                !!! cards col single ""

                    -   `app_header`
                    
    === "App Button" 

        ### App Button 

        The App Button Template renders an app icon button with linked functionality to open the app its dedicated to in the Computer UI app grid.

        ??? grid col single "App Button [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: App Button Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `app_button`
                    
                Parameters    
                        
                !!! cards ""

                    -   `app_name` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="App screen name this button opens. String. Valid value: app button IDs registered in valid_button_ids." }
                    -   `tooltip` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Tooltip text displayed on hover. String." }
                    -   `in_scene` :lucide-letters:
                        { title="Whether the button is being used inside a scene context. Boolean. Valid values: True, False. Default: False. Checked in app_grid and automatically passed as True when rendered inside a scene." }
                    -   `app_icon` :lucide-lock-open:
                        { title="Path to the icon image displayed on the button. String. Valid values: Color or Image Path. Default: placeholder icon." }

                Layout Components 

                !!! cards centered-content ""
                        
                    -   App Icon Idle
                    -   App Icon Tooltip
                    
                Notes 

                !!! cards col single ""

                    -   When in scene context: opens app via `show_app()` function
                    -   When in menu context: opens app via `Show()` action
                    -   When disabled via Button Disabler System: does nothing
                    
                Used By
                    
                !!! cards col single ""

                    -   `app_grid`

=== "Chat Templates"

    !!! tip "Learn more about the Chat System in the [Chat System][chat-system] page"

    ## Chat Templates

    The Chat Templates set up the basic layout for Chat App components.

    === "Contact Button"

        ### Contact Button

        The Contact Button Template renders a contact item button with linked functionality to set a contact to active in Chat App's contact panel.

        ??? grid col single "Contact Button [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Contact Button Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `contact_button`
                    
                Parameters    
                        
                !!! cards ""

                    -   `name` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="Contact name. String. Valid values: contact button IDs registered in valid_button_ids." }
                    -   `avatar` :lucide-lock-open:
                        { title="Contact's avatar / profile pic. String. Valid values: Color or Image Path. Default: '#808080'" }

                Layout Components 

                !!! cards centered-content ""
                    
                    -   Button Background
                    -   Contact Name 
                    -   Profile Pic
                    -   Online Status Indicator
                    
                Notes 

                !!! cards col single ""

                    -   When clicked: sets the active contact to open their chat box
                    -   When disabled via Button Disabler System: does nothing
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_app`
    === "Chat Box"

        ### Chat Box

        The Chat Box Template renders the active chat box for a given contact in Chat App, linked up to the currently active contact.

        ??? grid col single "Chat Box [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat Box Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_box`
                    
                Parameters    
                        
                !!! cards col single ""

                    -   `contact` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="Contact name whose chat history and live messages to render. String. Valid values: contact button IDs registered in valid_button_ids." }

                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   Chat Box Header with contact name
                    -   Scrollable Content Area with Chat History & Live Chat 
                    -   Keyboard field at the bottom
                    
                Notes 

                !!! cards col single ""

                    -   Chat history is pulled via `get_chat_entries(contact)`
                    -   Live chat renders from `nvl_list` when a chat block is active
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_app`
    
    === "Chat Bubble"

        ### Chat Bubble

        The Chat Bubble Template renders a single chat message into a bubble-like container from a nvl dialogue line in Chat App's Chat Box.

        ??? grid col single "Chat Bubble [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat Bubble Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_bubble`
                    
                Parameters    
                        
                !!! cards ""

                    -   `who` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="Speaker name. Determines bubble alignment and style. Sent if matches Player Character's chat name, received otherwise. String. Pulls from rollback history with get_chat_entries(contact)." }
                    -   `what` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Message text to display inside the bubble. String. Pulls from rollback history with get_chat_entries(contact)." }

                Layout Components 

                !!! cards centered-content ""
                        
                    -   Bubble Background 
                    -   Chat Message Text 
                    
                Notes 

                !!! cards col single ""

                    -   Sent messages (Player Character) are right-aligned with a sent bubble background
                    -   Received messages are left-aligned with a received bubble background
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_box`
        
    === "Timestamps For Chat"

        ### Timestamp For Chat

        The Timestamp For Chat Template sets up a basic layout for chat timestamp display in Chat Box.

        ??? grid col single "Timestamp For Chat [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Timestamp For Chat Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `timestamp_for_chat` 
                    
                Parameters    
                        
                !!! cards col single ""

                    -   `stamp` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Text to display as the timestamp. String." }

                Layout Components 

                !!! cards centered-content ""
                        
                    -   Timestamp Background  
                    -   Centered Stamp Text
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_date_stamp`
                    -   `chat_time_stamp`
    
    === "Chat Date Stamp"

        ### Chat Date Stamp

        The Chat Date Stamp Template renders the date stamp for the chat timestamp display in Chat Box.

        ??? grid col single "Chat Date Stamp [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat Date Stamp Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_date_stamp`
                    
                Parameters    
                        
                !!! cards col single ""

                    -   `date` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Date string to display. String. Pulls from 'abyss_date' when using during live chat and when using 'chat_start' and 'chat_end'. Passed directly to timestamp_for_chat." }

                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   Thin Chat Stamp Wrapper for date stamp
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_box`
    
    === "Chat Time Stamp"

        ### Chat Time Stamp

        The Chat Time Stamp Template renders the time stamp for the chat timestamp display in Chat Box.

        ??? grid col single "Chat Time Stamp [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Chat Time Stamp Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `chat_time_stamp`
                    
                Parameters    
                        
                !!! cards col single ""

                    -   `time` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Time string to display. String. Pulls from 'abyss_time' when using during live chat and 'chat_end'. Passed directly to timestamp_for_chat."}

                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   Thin Chat Stamp Wrapper for time stamp
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_box`

=== "Draft Templates"

    !!! tip "Learn more about the Draft System in the [Draft System][draft-system] page"

    ## Draft Templates 

    The Draft Templates set up the basic layout for Draft App components.

    ### Draft File

    The Draft File Template renders the main content area of the Draft App.

    ??? grid col single "Draft File [:octicons-key-asterisk-24:][screen-overview-legend]"

        <!-- tooltip: Draft File Overview Card -->

        !!! grid scrollable ""

            Screen Name 

            !!! cards col single ""

                -   `draft_file`
                
            Parameters    
                    
            !!! cards col single ""

                -   `log_name` :lucide-letters:
                    { title="Chapter key used to look up transcript log and book transcript. String. Valid value: a key in transcript_log and _book_transcript. Default: 'epilogue'." }
                -   `book_title` :lucide-lock-open:
                    { title="Full book title displayed in the chapter header. String. Default: 'To Be Or Not To Be'." }
                -   `book_abrv` :lucide-lock-open:
                    { title="Book title abbreviation used to construct the internal file name. String. Default: 'tbontb'." }

            Layout Components 

            !!! cards col single centered-content ""
                    
                -   Book Title & Chapter Title display in Header
                -   Auto Scroll Buttons in Header
                -   Scrollable Content Area 
                
            Notes 

            !!! cards col single ""

                -   Book Title & Chapter Title is derived from `log_name`
                -   Content area renders book transcript via `print_transcript(log_name)`
                -   Header contains two auto scroll buttons: a scroll-to-top & a scroll-to-bottom button
                
            Used By
                
            !!! cards col single ""

                -   `draft_app`
    
=== "Utility Templates"

    ## Utility Templates 

    The Shared Utility Templates set up the basic layout for shared utility components.

    === "Scrollable Content"

        ### Scrollable Content

        The Scrollable Content Template sets up a scrollable viewport wrapper. 

        ??? grid col single "Scrollable Content [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Scrollable Content Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `scrollable_content`
                    
                Parameters    
                        
                !!! cards ""

                    -   `scroll` :lucide-letters:
                        { title="Scroll mode. String. Valid values: 'viewport', 'vpgrid'. Default: None (no scroll)." }
                    -   `yinitial` :lucide-lock-open:
                        { title="Initial vertical scroll position. Int or Float. 0.0 = top, 1.0 = bottom. Default: 0.0." }
                    -   `spacing` :lucide-lock-open:
                        { title="Spacing between content items in pixels. Int. Default: 0." }
                    -   `scrollbars` :lucide-letters:
                        { title="Scrollbar visibility. String. Valid values: 'vertical', 'horizontal', None. Default: 'vertical'." }
                    -   `left_pad` :lucide-lock-open:
                        { title="Left padding of content area in pixels. Int. Default: 0." }
                    -   `top_pad` :lucide-lock-open:
                        { title="Top padding of content area in pixels. Int. Default: 0." }
                    -   `right_pad` :lucide-lock-open:
                        { title="Right padding of content area in pixels. Int. Default: 0." }
                    -   `bottom_pad` :lucide-lock-open:
                        { title="Bottom padding of content area in pixels. Int. Default: 0." }
                    -   `yadjustment` :lucide-letters:
                        { title="Scroll adjustment object for programmatic scroll control. Enables a smooth scroll alongside scrollable id which provides the necessary refresh for auto scrolling. Ren'Py ui.adjustment() instance. Valid values: Any declared ui.adjustment() instance. Default: None." }
                    -   `vp_width` :lucide-lock-open:
                        { title="Explicit viewport width in pixels. Int. Default: 0 (fills available width)." }
                    -   `vp_height` :lucide-lock-open:
                        { title="Explicit viewport height in pixels. Int. Default: 0 (fills available height)." }
                    
                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   Scrollbar 
                    -   Scrollable Content Padding, Spacing, Height & Width for Viewport
                    
                Notes 

                !!! cards col single ""

                    -   Supports `viewport` and `vpgrid` scroll modes, or no scroll at all
                    -   Content is passed via `transclude`
                    -   Optional scroll settings:
                        - scroll initial position with `yinitial` 
                        - auto scroll with refresh using `id` and `yadjustment`
                    
                Used By
                    
                !!! cards ""

                    -   `meta_screen`
                    -   `chat_app` 
                    -   `chat_box` 
                    -   `draft_file`

    === "Notif Button"

        ### Notif Button

        The Notif Button Template sets up the basic layout for notification popup buttons. 

        ??? grid col single "Notif Button [:octicons-key-asterisk-24:][screen-overview-legend]"

            <!-- tooltip: Notif Button Overview Card -->

            !!! grid scrollable ""

                Screen Name 

                !!! cards col single ""

                    -   `notif_button`
                    
                Parameters    
                        
                !!! cards ""

                    -   `app_screen` :octicons-north-star-24:{ .red-icon } :lucide-letters:
                        { title="App screen name this notification opens on click. String. Valid values: valid app button ID registered in valid_button_ids." } 
                    -   `app_prefix` :octicons-north-star-24:{ .red-icon } :lucide-lock-open:
                        { title="Display prefix shown in the notification title. String." } 
                    -   `notif_bg` :lucide-lock-open:
                        { title="Path to the notification background image. String. Valid values: Color or Image Path. Default: placeholder light gray background." } 
                    -   `notif_icon` :lucide-lock-open:
                        { title="Path to the notification icon image. String. Valid values: Color or Image Path. Default: placeholder grid icon." } 

                Layout Components 

                !!! cards col single centered-content ""
                        
                    -   Button Background 
                    -   Icon to Match App
                    -   Notification Title Text
                    -   Notification Detail Text Container 
                    
                Notes 

                !!! cards col single ""

                    -   On click: opens the linked app screen and hides itself
                    -   When disabled via Button Disabler System: does nothing
                    -   Content is passed via `transclude` for the notification detail text
                    
                Used By
                    
                !!! cards col single ""

                    -   `chat_app_notification`