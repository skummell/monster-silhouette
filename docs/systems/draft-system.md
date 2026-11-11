---
icon: lucide/feather
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

    If a documentation update is logged in the latest entry of the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Draft System

!!! tip "Code discussed in this page can be found in [`custom_systems.rpy`][systems]"

## Overview 

The Draft System is a custom game system in Monster Silhouette that records branching book draft content written in script 
as paragraph entries and renders them inside the Draft App as the Player Character's in-progress book. It tracks which draft 
variant was taken on each day through a transcript log, accumulates paragraph content into a persistent Book Transcript, and 
serves that content to the Draft App for display.

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

                    -   :lucide-variable: **Transcript Log**
                        [][transcript-log]{ .card-link }
                    
                    -   :lucide-variable: **Book Transcript**
                        [][book-transcript]{ .card-link }

                !!! cards col single centered-content ""
                    
                    -   :lucide-function-square: **Print Transcript** 
                        [][print-transcript]{ .card-link }
                
                !!! cards centered-content ""

                    -   :lucide-square-play: **Write Draft** 
                        [][write-draft]{ .card-link }
                    
                    -   :lucide-square-play: **Transcript Line** 
                        [][transcript-line]{ .card-link }

=== "How It Works"

    !!! tip "Learn more about the Suspicion level and its effect on Draft contents in the [Story Mode][story-mode-mechanic] page"

    ## How It Works 

    Each day's book draft content is split across two types of labels. 
    A routing label determines which variant of that day's draft to write based on the current Suspicion level, then 
    calls `write_draft` with a single letter suffix. A content label contains only `transcript_line` statements — one 
    per paragraph — and nothing else.

    === "Draft Transcript"

        ### Transcript Handling 

        Write Draft reads the last entry in `transcript_log` for the current chapter, increments the draft number, 
        concatenates the new letter onto the accumulated version string, appends the new tuple to the log, 
        constructs the content label name from the number and version, and calls it in a new context via `renpy.call_in_new_context`.
        The content label runs, its `transcript_line` calls append paragraphs to `_book_transcript`, and control returns.

        Transcript Line is the primitive that all content labels use. 
        It takes a string and appends it directly to `_book_transcript` for the given chapter.

        #### Draft 0 

        Draft0 is handled separately from the routing system. 
        It has no variant — it is always the same opening section. 
        Its content label is called directly in script when the player first opens the Draft App, 
        populating `_book_transcript` with the buffer before any `write_draft` calls have happened.

        #### Transcript Printing 

        `print_transcript` is what the Draft App uses to retrieve content. 

        It simply returns `_book_transcript.get(ch, [])` — the flat accumulated list of paragraphs for the chapter.

    === "Label Naming Convention"

        ### Label Naming Convention 

        Content labels follow the pattern `book_draft{n}_{v}`. 
        <br>
        Where `n` is the draft number and `v` is the accumulated version string. 

        Routing labels follows the pattern `book_draft{n}`. 
        <br>
        Where `n` is the draft number and corresponds to the Game Day. 

        The content label's `v` gains a letter alphabetically based on incrementing Suspicion values. 
        <br>
        The version string (`v`) is always `n` characters long. 

        #### Demo Labels

        Content labels for the Demo in specific follow the pattern `demo_book_draft{n}_{v}`.

        The routing label for Day 1 is `demo_book_draft1`. 

        The content label for a `suspicion == 1` route conditional is `demo_book_draft1_a`. 
        <br>
        Incrementing a letter for each following Suspicion value conditionals 
        (`suspicion ≤ 4`: `b`, `suspicion ≤ 6`: `c`, `suspicion ≤ 9`: `d`, `suspicion == 10`: `e`).

    === "Draft Screens"

        !!! tip "Learn more about the Draft App screen in the [App Screens][app-screens] page"

        !!! tip "Learn more about Draft Templates and App Templates screens in the [Template Screens][template-screens] page"

        ### Screens 

        The Draft System's visual output lives across two states and screens. 

        Screens that make up Draft System UI functionality include: `draft_app` and `draft_file` template.

        In both an empty and filled draft transcript, the Draft App and Draft File screens are rendered for the player to see — the app itself 
        handles layout through the `app_screen` template screen, within it the draft file containing draft layout and routing 
        to the active Draft File. 

        For a filled draft transcript, the Draft File screen calls `print_transcript()` and renders the paragraph list for the specified 
        draft transcript.

=== "Log & Transcript"

    ## Log & Transcript

    ### Logging

    `transcript_log` is keyed by chapter. 

    Each chapter maps to a list of `(draft_number, draft_version)` tuples in order. 
    It is initialized with `(0, "")` so that `draft0` is always represented and the log is never empty. 

    Draft0 has no version letter — it is identified by draft number `0` and an empty string.

    ### Transcripting

    `_book_transcript` is keyed by chapter. 

    Each chapter maps to a flat list of paragraph strings accumulated in order across all `transcript_line` calls. 

    All drafts for a chapter write into the same list — `draft0`'s paragraphs come first, followed by the variant paragraphs 
    from each subsequent day's content label in the order they were called.

=== "Components"

    ??? info "About Draft System Functions"

        The Draft System's functions are all Utility Functions.

    ## Components 

    Overview of the three components (**variables**, **functions** and **statements**) of the Draft System:

    === "Variables"

        ### Variables 

        Below all the variables for Monster Silhouette's Draft System have been organized into overviews containing information on their: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details (**Init Value** if not Dictionary)
        - **Keys** (for Dictionaries)
            - Hover over cards for **Init Value(s)**
        - **Notes**
        
        #### Transcript Log 

        ??? grid col single "Transcript Log [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Transcript Log Variable Overview Card -->
                
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `transcript_log`
                
                Type 

                !!! cards col single ""

                    -   Dictionary
                        { title="{str: [(int, str)]}" }
                    
                Keys 

                !!! cards col single ""

                    -   `"epilogue"`
                        { title="Init Value(s): (0, '')" }

                Notes 

                !!! cards col single centered-content ""

                    -   Stores draft number and version tuples per chapter

        #### Book Transcript

        ??? grid col single "Book Transcript [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Book Transcript Variable Overview Card -->
                
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `_book_transcript`
                
                Type 

                !!! cards col single ""

                    -   Dictionary
                        { title="{str: [str]}" }
                    
                Keys 

                !!! cards col single ""

                    -   `"epilogue"`
                        { title="Empty set at Init" }

                Notes 

                !!! cards col single centered-content ""

                    -   Stores accumulated paragraph strings per chapter

    === "Functions"

        !!! warning "This section does not include internal functions called by statements"

        !!! warning "This section does not include functions directly equivalent to their statements"

        ### Functions 

        Below the utility functions for Monster Silhouette's Draft System have been organized into overviews containing information on their: 

        - **Function Call** — including all parameters
        - **Parameters**
            - Hover over cards for details on what each parameter does
        - **Functionality**
        - Other places in code it's **Used In**
            - Hover over cards for details

        #### Print Transcript :lucide-wrench:

        ??? grid col single "Print Transcript [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Print Transcript Function Overview Card -->
            
            !!! grid scrollable ""

                Function Call

                !!! cards col single ""

                    -   `print_transcript(ch="epilogue")`
                
                Parameters 

                !!! cards col single ""

                    -   `ch`
                        { title="Name of Chapter to fetch Transcript Lines from" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Returns Book Transcript for specified Chapter
                    
                Used In

                !!! cards col single centered-content ""

                    -   `draft_file` screen
                        { title="To render Draft File main content" }

    === "Statements"

        ### Statements 
        
        Below all the statements for Monster Silhouette's Draft System have been organized into overviews containing information on their: 

        - **Statement Usage**
        - **Arguments**
            - Hover over cards for more details
        - **Functionality**
        - Additional **Notes**
            - Hover over cards for more details
        - **Functions Embedded**

        #### Write Draft

        ??? grid col single "Write Draft [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Write Draft Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `write_draft "ver"` 
                    -   Supports the `ch` kwargs: 
                        
                        `write_draft "ver" ch "chapter"`
                    

                Arguments 

                !!! cards "" 

                    -   `"ver"` :octicons-north-star-24:{ .red-icon }
                        { title="Last letter suffix for draft version string"}

                    -   `ch "chapter"`
                        { title="Chapter of Book Transcript to write to" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Reads last tuple from `transcript_log[ch]`
                    -   Increments number, concatenates `ver` onto version
                    -   Appends new tuple
                    -   Constructs and calls content label in new context
                
                Notes 

                !!! cards col single centered-content ""

                    -   `ch` defaults to `"epilogue"` when `None`
                        { title="For both Statement and Function" }
                
                Functions Embedded

                !!! cards col single ""

                    -   `write_draft(ver, ch=None)` :lucide-zodiac-libra: 

        #### Transcript Line

        ??? grid col single "Transcript Line [:octicons-key-asterisk-24:][components-overview-legend]"

            <!-- tooltip: Transcript Line Statement Overview Card -->
            
            !!! grid scrollable ""

                Statement Usage

                !!! cards col single ""

                    -   `transcript_line "text"` 
                    -   Supports the `ch` kwargs: 
                        
                        `transcript_line "ver" ch "chapter"`

                Arguments 

                !!! cards "" 

                    -   `"text"` :octicons-north-star-24:{ .red-icon }
                        { title="Text for one full paragraph in transcript for specified chapter"}

                    -   `ch "chapter"`
                        { title="Chapter of Book Transcript to write to" }
                    
                Functionality

                !!! cards col single centered-content ""

                    -   Appends text to `_book_transcript[ch]`
                
                Notes 

                !!! cards col single centered-content ""

                    -   Used exclusively inside content labels
                    -   `ch` defaults to `"epilogue"` when `None`
                        { title="For both Statement and Function" }
                
                Functions Embedded

                !!! cards col single ""

                    -   `transcript_line(text, ch=None)` :lucide-zodiac-libra: 

*[Day 1]: The only Game Day in the Demo