---
icon: lucide/messages-circle
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

    If a documentation update is logged in the latest two date-range entries of the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Chat System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

The Chat System is a custom game system in Monster Silhouette that records NVL dialogue lines written in script as 
chat conversation entries and renders them inside the Chat App as persistent, scrollable chat history. 
It handles both live chat — messages appearing in real time as the script progresses — and historical chat — messages retrieved 
from previous conversations and displayed when the player opens a contact's chat box later.

??? info "Components Overview Legend"

    === "Legend"

        <p id="components-overview-legend"></p>

        | :lucide-variable: | :lucide-function-square: | :lucide-square-play: | 
        | ----------------- | ------------------------ | -------------------- |
        | Variable          | Function                 | Statement            |
            
        | :octicons-north-star-24:{ .red-icon } | :lucide-wrench:  | :lucide-bug:      | :lucide-zodiac-libra:            |
        | ------------------------------------- | ---------------- | ----------------- | -------------------------------- |
        | Required argument/parameter           | Utility function | Debugger function | Function equivalent to statement |

    === "Go To Component Overviews"

        !!! cards col single no-row-gap no-margin ""

            !!! grid col single no-pad no-border ""

                !!! cards centered-content ""

                    -   :lucide-variable: **Chat Ranges**
                        [][chat-ranges]{ .card-link }
                    
                    -   :lucide-variable: **Chat Timestamps**
                        [][chat-timestamps]{ .card-link }
                    
                !!! cards centered-content ""

                    -   :lucide-variable: **Chat Start Index**
                        [][chat-start-index]{ .card-link }

                    -   :lucide-variable: **Chat Contact**
                        [][chat-contact]{ .card-link }

                !!! cards col three centered-content ""

                    -   :lucide-variable: **In Chat Block**
                        [][in-chat-block]{ .card-link }
                
                    -   :lucide-variable: **Chat Time Change**
                        [][chat-time-change]{ .card-link }

                    -   :lucide-variable: **Chat Date Change**
                        [][chat-date-change]{ .card-link }

                !!! cards col single centered-content ""

                    -   :lucide-function-square: **Get Chat Entries** 
                        [][get-chat-entries]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-square-play: **Chat Start** 
                        [][chat-start]{ .card-link }
                    
                    -   :lucide-square-play: **Chat End** 
                        [][chat-end]{ .card-link }

=== "How It Works"

    !!! tip "Learn more about Ren'Py's NVL Mode in [Ren'Py Engine Docs][renpy-doc]"

    ## How It Works

    Ren'Py's NVL mode is designed for wall-of-text style dialogue displayed in a full-screen overlay. 
    The Chat System repurposes it entirely — NVL lines are used exclusively as a recording mechanism for chat messages. 
    The NVL window itself is visually transparent and invisible to the player. Chat lines never appear through the NVL screen. 
    They appear in the Chat App instead, rendered as chat bubbles.

    === "Chat History"

        ### Recording via Rollback History

        When a chat block begins, `chat_start` records the current length of `_history_list` — Ren'Py's internal rollback history — as the 
        start index. When the block ends, `chat_end` records the length again as the end index. This start/end pair is stored in 
        `chat_ranges` under the contact's name. Every NVL line spoken between those two indices belongs to that conversation.

        `chat_timestamps` stores a corresponding timestamp entry for each range — the date if it changed since the last conversation with that 
        contact, and the time always. This is what produces the date and time stamps displayed above each conversation in the Chat Box.

        #### Retrieving History

        `get_chat_entries()` reads `chat_ranges` for a given contact, slices `_history_list` for each recorded range, 
        filters to only NVL entries, and interleaves date and time stamp markers from `chat_timestamps`. 
        The result is a flat list of entries the `chat_box` screen iterates over to render the full conversation history.

    === "Live Chat"

        ### Live Chat 

        While a chat block is active, NVL lines accumulate in `nvl_list` — Ren'Py's live NVL buffer. 
        The `chat_box` screen renders this buffer directly as live chat bubbles. When the chat block ends or the Chat Box is reopened, 
        `nvl_list` is cleared. The conversation transitions seamlessly from live rendering to history rendering via `get_chat_entries()`.

    === "Chat Screens"

        !!! tip "Learn more about the Chat App screen in the [App Screens][app-screens] page"

        !!! tip "Learn more about Chat Templates and App Templates screens in the [Template Screens][template-screens] page"

        ### Screens 

        The Chat System's visual output lives across two states and several embedded screens. 

        Screens that make up Chat System UI functionality include: `chat_app`, `contact_button`, `chat_box`, `chat_bubble` and two timestamp 
        screens build on top of the same timestamp template.

        In both an active and non-active chat, the Chat App and Contact Button screens are rendered for the player to see
        — the app itself handles layout through the `app_screen` template screen, within it the contact panel containing the contact 
        buttons and routing to the active Chat Box. 

        For an active chat, three more screens render content for the player to see: the Chat Box, Chat Bubble, and timestamp screens 
        — these are what actually render the conversation entries, live chat, and timestamps. 
        Together they form the complete front end for everything the Chat System records and retrieves.

=== "Chat Ranges & Timestamps"

    ## Chat Ranges & Timestamps

    `chat_ranges` stores conversation history as index ranges into `_history_list`. Each contact maps to a list of 
    `(start_index, end_index)` tuples — one per chat block — in chronological order. When a player opens a contact's chat box, 
    `get_chat_entries()` uses these ranges to slice and filter `_history_list` for that contact's messages only.

    `chat_timestamps` stores a parallel list of `(start_index, date, time)` tuples. The date value is stored as a formatted string 
    only when the in-world date has changed since the last conversation with that contact — otherwise it's stored as an empty string 
    and no date stamp is rendered. The time is always stored. Both are displayed as centered stamp markers above their corresponding 
    conversation segment in the chat box.

=== "Chat Blocks"

    !!! tip "Learn more about the Button Disabler System in the [Button Disabler System][button-disabler-system] page"

    ## Chat Blocks

    A chat block is the span of script between a `chat_start` and `chat_end` statement pair. 
    Only one chat block can be active at a time — `_chat_contact` tracks the current contact and `_in_chat_block` flags the active state.

    Chat Start records the current `_history_list` length as `_chat_start_index`, sets `_chat_contact` and 
    `_in_chat_block`, disables all contact buttons via the Button Disabler System, enables only the current `contact`'s button, and 
    checks whether the date has changed since the last entry for this contact.

    Chat End validates that the contact matches `_chat_contact`, appends the completed `(start_index, end_index)` 
    range to `chat_ranges`, appends the timestamp entry to `chat_timestamps`, clears all temporary states, and re-enables the Chat App 
    exit button if the app is currently open.

=== "Components"

    ??? info "About Chat System Functions"

        The Chat System's functions currently only consist of one singular Utility Function. 

        This is because the Chat System was one of the first Game Systems I made fully, and I was still figuring out how to go about it.

        It's likely that in the future the statements' content will be transformed into functions to manage more easily. 

    ## Components

    Overview of the three components (**variables**, **functions** and **statements**) of the Chat System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Chat System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details (**Init Value** if not Dictionary)
        - **Keys** (for Dictionaries)
            - Hover over cards for **Init Value(s)**
        - **Notes**
        
        === "Index Cordinated Tuples"

            #### Chat Ranges 

            ??? grid col single "Chat Ranges [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Chat Ranges Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `chat_ranges`
                
                    Type 

                    !!! cards col single ""

                        -   Dictionary
                            { title="{str: [(int, int)]}" }
                    
                    Keys 

                    !!! cards col single ""

                        -   N/A
                            { title="Empty dictionary at Init" }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Stores recorded index ranges per contact

            #### Chat Timestamps 

            ??? grid col single "Chat Ranges [:octicons-key-asterisk-24:][components-overview-legend]"

                <!-- tooltip: Chat Timestamps Variable Overview Card -->
                
                !!! grid scrollable ""

                    Variable Name

                    !!! cards col single ""

                        -   `chat_timestamps`
                
                    Type 

                    !!! cards col single ""

                        -   Dictionary
                            { title="{str: [(int, str, str)]}" }
                    
                    Keys 

                    !!! cards col single ""

                        -   N/A
                            { title="Empty dictionary at Init" }

                    Notes 

                    !!! cards col single centered-content ""

                        -   Stores timestamp entries per contact as `(start_index, date, time)`

        === "Temporary Chat Block Flags"

            === "Non-Boolean Flags"

                #### Chat Start Index 

                ??? grid col single "Chat Start Index [:octicons-key-asterisk-24:][components-overview-legend]"

                    <!-- tooltip: Chat Start Index Variable Overview Card -->
                    
                    !!! grid scrollable ""

                        Variable Name

                        !!! cards col single ""

                            -   `_chat_start_index`
                    
                        Type 

                        !!! cards col single ""

                            -   Int | None
                                { title="Init Value: None." }

                        Notes 

                        !!! cards col single centered-content ""

                            -   Temporary storage for the start index of the current chat block
                            -   Cleared back to Init Value on `chat_end`

                #### Chat Contact 

                ??? grid col single "Chat Contact [:octicons-key-asterisk-24:][components-overview-legend]"

                    <!-- tooltip: Chat Contact Variable Overview Card -->
                    
                    !!! grid scrollable ""

                        Variable Name

                        !!! cards col single ""

                            -   `_chat_contact`
                    
                        Type 

                        !!! cards col single ""

                            -   Str | None
                                { title="Init Value: None." }

                        Notes 

                        !!! cards col single centered-content ""

                            -   Name of the Chat Block contact
                            -   Cleared back to Init Value on `chat_end`
            === "Boolean Flags"

                #### In Chat Block 

                ??? grid col single "In Chat Block [:octicons-key-asterisk-24:][components-overview-legend]"

                    <!-- tooltip: In Chat Block Variable Overview Card -->
                    
                    !!! grid scrollable ""

                        Variable Name

                        !!! cards col single ""

                            -   `_in_chat_block`
                    
                        Type 

                        !!! cards col single ""

                            -   Boolean
                                { title="Init Value: False." }

                        Notes 

                        !!! cards col single centered-content ""

                            -   Flags whether a chat block is currently active
                            -   Used by `chat_app` on hide to decide whether to clear `active_contact` and `nvl_list`
                            -   Cleared back to Init Value on `chat_end`

                #### Chat Time Change 

                ??? grid col single "Chat Time Change [:octicons-key-asterisk-24:][components-overview-legend]"

                    <!-- tooltip: Chat Time Change Variable Overview Card -->
                    
                    !!! grid scrollable ""

                        Variable Name

                        !!! cards col single ""

                            -   `_chat_time_change`
                    
                        Type 

                        !!! cards col single ""

                            -   Boolean
                                { title="Init Value: False." }

                        Notes 

                        !!! cards col single centered-content ""

                            -   Flags whether the time should be recorded in the current timestamp
                            -   Always `True` during an active chat block
                            -   Cleared back to Init Value on `chat_end`

                #### Chat Date Change 

                ??? grid col single "Chat Date Change [:octicons-key-asterisk-24:][components-overview-legend]"

                    <!-- tooltip: Chat Date Change Variable Overview Card -->
                    
                    !!! grid scrollable ""

                        Variable Name

                        !!! cards col single ""

                            -   `_chat_date_change`
                    
                        Type 

                        !!! cards col single ""

                            -   Boolean
                                { title="Init Value: True." }

                        Notes 

                        !!! cards col single centered-content ""

                            -   Flags whether the in-world date has changed since the last recorded entry for the current contact
                            -   Determines whether a date stamp is stored and rendered
                            -   Cleared to `False` on `chat_end`

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        ### Functions 

        Below the utility functions for Monster Silhouette's Chat System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - Additional **Notes**
            - Hover over cards for details
        - Other places in code it's **Used In**
            - Hover over cards for details

        #### Get Chat Entries :lucide-wrench:

        ??? grid col single "Get Chat Entries [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Get Chat Entries Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `get_chat_entries(contact)`
                
                Parameters 

                !!! cards col single ""

                    -   `contact`
                        { title="Name of Contact to render chat entries for" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Returns a flat list of entries for contact in script order
                    -   Iterates `chat_ranges[contact]` 
                    -   Slices `_history_list` for each range 
                    -   Filters to `kind == "nvl"`
                
                Notes 
                
                !!! cards col single centered-content ""

                    -   Interleaves date stamp dict and time stamp dict from `chat_timestamps` before each range's messages
                        { title="Date Stamp: {'type': 'date', 'value': date}. Time Stamp: {'type': 'time', 'value': time}" }
                    
                Used In

                !!! cards col single centered-content ""

                    -   `chat_box` screen
                        { title="To render Chat History" }

    === "Statements"

        ### Statements 

        Below all the statements for Monster Silhouette's Chat System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
            - Hover over cards for more details
        - **Functionality**
        - **Functions Embedded**
            - Hover over cards for more details on how they're used in the statement 

        #### Chat Start 

        ??? grid col single "Chat Start [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Chat Start Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `chat_start "contact"` 

                Arguments 

                !!! cards col single "" 

                    -   `"contact"` :octicons-north-star-24:{ .red-icon }
                        { title="Must match a valid contact button ID in valid_button_ids"}
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Records `_chat_start_index`, sets `_chat_contact` and `_in_chat_block`
                    -   Contact Button Disabling / Enabling 
                    -   Checks date change against last recorded timestamp for this contact
                
                Functions Embedded

                !!! cards col single ""

                    -   `disable_all_type(contact_button)` 
                        { title="Disables all Contact Buttons"}

                    -   `enable_id(_chat_contact)`
                        { title="Enables Chat Block contact's Contact Button"}
                    
                    -   `execute_chat_start(contact)` :lucide-zodiac-libra:
                        { title="Called internally by the statement, not exposed as a standalone callable" }

        #### Chat End 

        ??? grid col single "Chat End [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Chat End Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `chat_end "contact"` 

                Arguments 

                !!! cards col single "" 

                    -   `"contact"` :octicons-north-star-24:{ .red-icon }
                        { title="Must match _chat_contact or raises an exception"}
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Appends completed range to `chat_ranges` and timestamp to `chat_timestamps`
                    -   Clears all temporary state variables
                    -   Re-enables Chat App exit button
                
                Functions Embedded

                !!! cards col single ""

                    -   `enable_id("Chat")` 
                        { title="Enables Chat App exit button if chat_app is open"}
                    
                    -   `execute_chat_end(contact)` :lucide-zodiac-libra:
                        { title="Called internally by the statement, not exposed as a standalone callable" }