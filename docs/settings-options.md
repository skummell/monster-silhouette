---
icon: lucide/settings-2
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

# Settings & Options

!!! tip "Code discussed in this page can be found in [`gui.rpy`][gui] and [`options.rpy`][options]"

## Overview 

Settings & Options in Monster Silhouette are the configuration values that shape the game's presentation — 
how large it renders, what it looks and sounds like, how menus behave, and what identity the project carries into a build. 
They are split across two files: `gui.rpy`, which governs visual styling and interface defaults, and `options.rpy`, 
which governs behavior, metadata, and build configuration.

Nothing here introduces new logic. Every entry on this page is a value being set, a default being overridden, or a routing being 
redirected. But configuration does a lot of quiet work — the most structurally significant change in either file is the one that 
replaces Ren'Py's entire game menu system with the Computer UI, and several others shape how the game feels before a single line 
of script runs.

??? warning "This Page Covers Configuration Only"

    For anything that introduces new logic or systems, refer to the Game Systems pages. 
    Two topics that come up here — the Save & Load screen and the `ShowHome()` game menu callable — 
    are documented on other pages and only briefly referenced here. Links are provided in tips at the relevant sections.

=== "Game Menu Replacement"

    ## Game Menu Replacement 

    !!! tip "Learn more about the ShowHome Custom Action in the [Custom Actions][custom-actions] page"

    !!! tip "Learn more about the Computer UI Menu in the [Computer UI Screens][computer-ui-screens] page"

    === "Game Menu Replacement Overview"

        By default, pressing ESC or right-clicking in a Ren'Py game opens the save screen. 
        Monster Silhouette replaces both the screen that opens and the action that opens it. 
        The entire game menu infrastructure is redirected to the Computer UI Menu — the in-world computer doubles as the 
        game's out-of-game menu system, blurring the line between navigating the game and navigating the computer the 
        Player Character uses.

        Two settings work together to accomplish this. The first assigns the screen; the second assigns the action.
        Both must be set for the redirect to work cleanly across all the different places Ren'Py can trigger a game menu.

    === "Screen & Action Assignment"

        ??? grid col single "Screen Assignment"

            <!-- tooltip: Screen Assignment Overview Card -->
                        
            !!! grid scrollable ""

                Variable 

                !!! cards col single centered-content ""

                    -   `_game_menu_screen` 

                Value 

                !!! cards col single centered-content ""

                    -   `"computer_ui_menu"`
                
                Notes 

                !!! cards col single ""

                    -   Replaces the screen Ren'Py opens when the game menu action fires
                    -   Any Ren'Py infrastructure that reads this variable — return actions, quit actions, save screen access — now routes through Computer UI Menu instead

        ??? grid col single "Action Assignment"

            <!-- tooltip: Action Assignment Overview Card -->
                        
            !!! grid scrollable ""

                Variable 

                !!! cards col single ""

                    -   `config.game_menu_action` 

                Value 

                !!! cards col single ""

                    -   `ShowHome("computer_ui_menu", _zorder=1)`
                
                Notes 

                !!! cards col single ""

                    -   Replaces the action triggered by ESC and right-click
                    -   `ShowHome()` is not a stock Ren'Py action; it's a custom callable implemented at the engine level to preserve context when opening and closing the game menu from inside the Computer UI.

=== "Screen & Resolution"

    ## Screen & Resolution 

    Monster Silhouette renders at 1280x720, smaller than Ren'Py's default 1920x1080. 
    The choice is driven by the game's web build target. Browser rendering hits a much friendlier performance ceiling at 720p, 
    and scaling up to fill larger displays reads cleanly with the pixel-adjacent aesthetic the game leans into. The resolution 
    also sets the base measurements that every layout in the game is built against.

    ### Screen Configuration

    === "Screen Configuration Details"

        Window resizing is enabled. A custom `adjust_view_size` function is wired into `config.adjust_view_size` as a pass-through — 
        currently returning the given width and height unchanged. The hook exists to eventually support element-specific scaling rules 
        as more UI is introduced, at which point the function can branch on incoming dimensions rather than returning them untouched. 
        Right now it does nothing beyond letting the window resize without disturbing the base layout.

        Screen/style conflict checking is enabled. This tells Ren'Py to raise an error when a screen or style definition assigns the same 
        property twice — a bug class that's easy to introduce during heavy UI work and hard to debug once it's buried in a stack of 
        inherited styles. It was turned on during the intensive screen development in September as a safety net and has remained on since.

    === "Overview Card"

        ??? grid col single "Screen Configuration"

            <!-- tooltip: Screen Configuration Overview Card -->
                        
            !!! grid scrollable ""

                Base Resolution

                !!! cards col single ""

                    -   `gui.init(1280, 720)` 

                Window Resizing Enabled 

                !!! cards col single ""

                    -   `config.gl_resize`
                    -   `config.adjust_view_size` — assigned to custom `adjust_view_size(width, height)` function
                
                Property Conflict Checking Enabled 

                !!! cards col single ""

                    -   `config.check_conflicting_properties`

=== "Visual Theme"

    ## Visual Theme

    === "Color Palette"

        ### Colors

        The palette is dominated by teal-blues against low-saturation grays and near-blacks. 

        The choice works on two levels: in practice and within Monster Silhouette's narrative.

        Practically, blue is the dominant color of operating system interfaces across every platform players are likely to have 
        used — Windows, macOS, and most Linux desktop environments all carry the visual weight of blue somewhere in their UI. 
        Leaning into teal-blue gives the Computer UI an immediate familiarity, reading as "a computer" before the player has 
        processed any specific element.

        Narratively, blue is also Mephisto's character color. His presence in the game is defined by a silhouette that only the player 
        character can see as one — everyone else sees a normal person. Tying the UI's accent palette to the same color family as his 
        character quietly mirrors the connection between the player character, their computer, and the mystery the story builds around. 
        The exact shades are kept distinct from his own — the UI reads as its own thing — but the family relationship is deliberate.

        === "Color Declaration"

            Most colors are declared once in `gui.rpy` and referenced throughout screens via `gui.*` variables. That said, several literal hex 
            values still live directly in `screens.rpy` and script rather than pulling from these variables.
            These are noted in-code as future cleanup — replacing them with `gui.*` references once the final visual pass lands.

        === "Color Palette Roles"

            ??? grid col single "Palette Roles"

                <!-- tooltip: Palette Roles Table -->

                | Roles             | Color Family                                                                            |
                | :---------------: | :-------------------------------------------------------------------------------------: |
                | Primary accent    | Teal-blue — used for labels, highlights, and active states                              |
                | Hover state       | Brighter teal-blue — the accent's "pressed forward" version                             |
                | Idle text         | Mid-gray — the default for text that isn't interactive                                  |
                | Small idle text   | Lighter gray — the default for small interface text that needs slightly more lift       |
                | Selected text     | Gray — matched to idle_small; the game doesn't strongly distinguish selected from idle  |
                | Insensitive text  | Mid-gray at partial alpha — the same family as idle, dimmed                             |
                | Muted UI bars     | Deep desaturated teal — bar backgrounds                                                 |
                | Hover muted bars  | Slightly lighter version of the muted bar                                               |
                | Dialogue text     | Off-white gray — dialogue reads at low contrast to reduce eye strain over long sessions |
                | Interface text    | Black — the interface uses dark-on-light contrast where possible                        |
                | Fourth wall break | Muted red family — a custom addition reserved for narrative breaking moments            |

            The two fourth-wall colors are a Monster Silhouette-specific addition with no Ren'Py equivalent. 
            They exist to visually mark moments where the narrative breaks frame. The specific shade used for the background is noted 
            in-code as possibly being adjusted later to a muted red closer to the game's overall palette.

    === "Font Families"

        ### Fonts 

        Every string in the game — dialogue, interface, character names, notifications — renders in PT Mono, a monospace typeface. 
        The choice reinforces the game's identity around a writer working at their computer. A proportional font would feel more 
        "visual novel" and less "person staring at a document editor at three in the morning." The consistency across the interface 
        and the narrative text also makes the Computer UI feel coherent — the game's own text and the character's digital environment 
        share a visual language.

        There's one subtle piece of engineering behind the font setup. When Ren'Py renders bold text on a font without a bold file, it 
        synthesizes the bolding by smearing the glyphs — a technique called faux-bold. At small sizes in a monospace font, faux-bold 
        reads as blurry and slightly wrong. The game maps bold requests on the regular font file to the actual bold font file instead, 
        so any text asked to be bold renders with real bold glyphs.

        ??? grid col single "Font Assignments"

            !!! grid scrollable ""

                Dialogue font 
                    
                !!! cards col single centered-content ""

                    -   PT Mono Regular

                Bold dialogue font 
                    
                !!! cards col single centered-content ""
                        
                    -   PT Mono Bold

                Character name font 

                !!! cards col single centered-content ""
                        
                    -   PT Mono Regular

                Interface font 

                !!! cards col single centered-content ""
                        
                    -   PT Mono Regular

                Bold-request replacement 
                    
                !!! cards col single centered-content ""
                        
                    -   regular requests for bold map to the bold file
        
    === "Font Sizes"

        ### Font Sizes 

        The size scale is tuned for the 720p base. Dialogue and interface text sit at the same size, 
        which reinforces the shared visual language between narrative and UI. 
        Character names render noticeably larger than dialogue — they serve as the visual anchor for who's speaking. 
        The label size sits just above dialogue to mark section headings in menus without overreaching. 
        The notify size is significantly smaller, sitting as a background element. 
        The title size is the largest — it's reserved for the game's title and any headers of comparable weight.

        The relative scale matters more than the exact numbers, which may shift as the final visual pass lands.
        What's important is that dialogue and interface sit together, that names stand out, and that titles carry the most weight.

    === "Screen Styles"

        !!! tip "Learn more about Ren'Py's built-in styles feature in [Ren'Py Engine Docs][renpy-doc]"

        !!! tip "Code for screen styles discussed in this section can be found in [screens.rpy][screens]"

        ### Screen Styles

        Screen styles in Monster Silhouette give every screen in the game shared conventions for consistency — from the properties 
        applied to elements to the dimensions that position them.

        Below you'll find: standardization rules that keep screen styles organized, and tooltip styling which 
        varies based on the active screen will be covered.
    
        === "Screen Style Standardization"

            #### Screen Style Standardization 

            Screen Style Standardization is the set of rules that keeps every screen's styles organized and consistent. 
            Without them, each screen would re-declare the same property blocks inline and position elements using unnamed literal values — 
            properties scattered across the file, values that have to be found by scrolling rather than by name, and no easy way to change 
            something that appears on multiple screens without searching each one individually.

            It deals with the reusable helper styles that screens inherit from, the grouping pattern that keeps each screen's styles findable, 
            and the rule for where dimension values live between shared config and inline declarations will be covered.

            === "Helper Styles"

                ##### Helper Styles

                Four helper styles exist in `screens.rpy` — `clipped`, `zeroed_frame`, `bolded`, and `full_screen`. 
                Each captures a repeated property block that many screens otherwise declare on their own.

                Style inheritance through Ren'Py's `style X is Y` syntax applies them. 
                Instead of every screen that needs clipping writing `clipping True` for each element that needs to be clipped — 
                it writes `style some_element is clipped`. 
                The property block lives once in the helper style, and every screen that needs it points at the same definition.

            === "Per-Screen Grouping"

                ##### Per-Screen Grouping 

                Styles for a given screen are grouped under a comment header naming that screen — `# Status Bar Styles`, `# Chat Box Styles`, 
                `# Profile App Styles`, and so on.

                Each style group sits directly after the screen it describes. A reader scrolling through `screens.rpy` sees a screen definition, 
                then immediately sees the styles that screen uses. There's no jumping between distant parts of the file to find the style governing 
                a property they're looking at.
            
            === "Dimension Scoping"

                ##### Dimension Scoping 

                Dimension values live in two places, split by scope. Shared values and values that compose from shared ones live in `gui.rpy` under 
                "Positioning & Sizing Shared Config for Screen Styles." Values that exist only to make one screen's internal layout readable stay as inline 
                `$` variables at the top of that screen.

                A value like `app_grid_top_pad` doesn't live in `gui.rpy` only because it's used across multiple screens — it lives there because 
                it's built from `status_bar_height`, which is itself shared. Changing `status_bar_height` cascades correctly through every value composed 
                from it.

                Values that only make one screen's layout readable stay inline. They're never referenced from outside their screen, so putting them in 
                `gui.rpy` would force naming prefixes to avoid collisions with other screens' variables, and would push the reader into a separate 
                file to understand how one screen lays out.

                The rule is straightforward: if a value is used by more than one screen, or built from something that is, it lives in `gui.rpy`. 
                Otherwise it stays inline.

                Three conventions follow the same principle. `config.screen_width` is used for horizontal positioning wherever the layout should adapt 
                to the base resolution rather than assume a fixed width. `align` and `anchor` are preferred over absolute coordinates so positioning survives 
                window resize. Composite values compose from smaller defines, so a single change cascades through every value built from it.
        
        === "Dynamic Tooltip Styles"

            !!! tip "Learn more about how tooltip styles are selected in the [Hovers & Tooltips][hovers-tooltips-mechanic] page"

            #### Dynamic Tooltip Styles 

            Tooltips in Monster Silhouette are styled based on the screen context they appear in. Four style families exist to serve the different 
            kinds of content that hover contexts produce.

            The `tooltip` family is the default. It renders a small, self-contained frame for brief labels — the kind used for interface buttons 
            like a return-to-game control.

            Three specialized families replace it in specific contexts. `profile_preview` is compact and tinted, sized for the multi-line tag lines 
            shown above chat contacts. `wardrobe_select` is wider, sized for clothing descriptions that can run several lines. 
            `bedroom_tooltip` uses a muted color matching the game's UI, keeping bedroom prop labels visually quiet so they don't compete with the scene.

            All four follow the same naming convention: `[family]_frame` for the container and `[family]_text` for the text inside it. 
            The `tooltip_hover` screen combines them at render time via `style_prefix + "_frame"` and `style_prefix + "_text"`. 
            Adding a new family means defining both styles under a new prefix — no changes to the rendering screen are required.



=== "Dialogue & Text Layout"

    ## Dialogue & Text Layout 

    The layout of the say window, choice buttons, and quick menu are currently Ren'Py defaults. 
    None of them have been styled yet. They will be adjusted at a later stage to match the final visuals and assets 
    of Monster Silhouette — the default layouts are functional placeholders that let the game be written and tested while the 
    visual design catches up.

    The NVL configuration is a different case entirely. The NVL screen has been repurposed by the Chat System and rendered 
    fully transparent — its layout doesn't matter visually because nothing renders to it. NVL lines are used as a recording 
    mechanism, not a display format. The `gui.nvl_*` values still govern how NVL entries size and space within the invisible buffer, 
    but nothing on that buffer is ever seen by the player. Aside from what's required for the Chat System to function, NVL settings 
    follow Ren'Py's default.

    === "Layouts That Will Be Styled"

        These layouts currently use Ren'Py defaults and will receive a styling pass when the final visual assets are ready.

        ### Say Window

        The dialogue box, name box, and text positioning currently all sit at Ren'Py's defaults. 
        No custom geometry, no custom name box styling, no changes to the dialogue or name text positions.

        When this gets styled, it will be built to match the game's final look and feel — 
        the current layout is functional but doesn't yet carry the visual weight of a completed Monster Silhouette dialogue box.

        ### Quick Menu

        The in-game Quick Menu at the bottom of the screen also sits at Ren'Py defaults — the default button set, 
        the default spacing, the default hover states. It will be styled alongside the say window as part of the same visual pass.

    === "Ren'Py Default Layouts"

        These layouts follow Ren'Py defaults and will remain close to them.

        ### Choice Buttons

        Menu choice buttons use Ren'Py's default layout and styling. Nothing has been customized here yet, and there's currently no 
        plan to restyle them beyond what the base template already provides.

        ### NVL Configuration

        The `gui.nvl_*` values govern NVL entry sizing and spacing, but none of it is visible to the player because the NVL screen 
        itself is transparent. The values exist so that the Chat System's recording mechanism has consistent geometry to work with. 
        Everything visible about NVL behavior is documented on the Chat System page.

=== "Save & Load Configuration"

    ## Save & Load Configuration 

    !!! tip "Learn more about the Save & Load screen in the [Meta Screens][meta-screens] page"

    The unified Save & Load screen itself is documented on the Meta Screens page. What lives here are the 
    configuration values that shape how saves behave — how much dialogue history the game holds, what key deletes saves, 
    and whether cloud sync is active.

    Save slot layout has not been customized. Slot dimensions, thumbnail sizes, slot grid dimensions, and spacing all use 
    Ren'Py defaults. This may change in the future if the game's save presentation needs to differ from what the engine provides, 
    but at present there's no reason to deviate from a layout that works.

    === "History Buffer"

        !!! tip "Learn more about the Chat System in the [Chat System][chat-system] page"

        ### History Buffer 

        The dialogue history buffer has been expanded dramatically from Ren'Py's default of 250 entries to 10000. 
        This was driven by the Chat System more than anything else — the Chat App relies on the history buffer to construct 
        extended chat histories per contact, since every NVL line that appears in a chat block needs to be retrievable for the 
        history rendering. With a 250 entry limit, long conversations or multiple conversations in sequence would evict earlier 
        chat messages from history entirely. Raising the ceiling eliminates that problem and lets chat history accumulate across an 
        entire playthrough.

        Beyond the Chat System, there just wasn't a reason for the history to be short. Players in a mystery visual novel are likely 
        to want to look back — even hundreds of entries back — to catch details they might have missed. Setting the ceiling high enough 
        to feel effectively unbounded serves that.

    === "Key Binding"

        ### Key Binding

        Monster Silhouette provides several key bindings on top of Ren'Py's defaults for save management.

        The delete key for removing individual save slots on hover, and the quick 
        save & load shortcuts for saving and loading without opening the save menu.

        === "Delete Key Binding"

            #### Delete Key Binding 

            The delete key for save slots has been remapped to `D`. In save and load screens, pressing `D` while hovering over a save slot 
            triggers a confirm message and deletes the save. This gives the player a dedicated one-key binding rather than requiring them 
            to interact with a context menu, making save management less disruptive to the flow of playing.

        === "Quick Save & Load Key Binding"

            #### Quick Save & Load Key Binding

            `F5` triggers a quick save and `F6` triggers a quick load, both bound directly on the `say` screen. 
            Because the `say` screen displays whenever dialogue is on screen, the two keys are available throughout normal gameplay without 
            opening the save menu first.

            The bindings call `QuickSave()` and `QuickLoad()` directly as key actions rather than routing through the quick save slot page — 
            pressing `F5` saves to the current quick save slot, and `F6` loads from it. This keeps save access available in the moment rather 
            than requiring the player to interrupt play to save.

    === "Cloud Sync"

        ### Cloud Sync

        Ren'Py's cloud sync feature is disabled. The primary reason is that Monster Silhouette is currently in demo — syncing demo 
        saves to a cloud account doesn't serve the player, and having sync enabled means players could end up with demo saves mixed 
        into their cloud storage for a game whose full release may not be compatible with them. Sync will likely be revisited when 
        the full game ships.

        The Save & Load screen renders the sync buttons conditionally based on the `config.has_sync` variable, so re-enabling this 
        is a one-line change if the decision changes.

=== "Audio Configuration"

    ## Audio Configuration 

    The voice mixer has been disabled. Monster Silhouette doesn't have voice acting and has no plans to add it at this stage 
    in its development — turning off the channel removes an audio setting that would otherwise sit in Preferences as a permanently 
    empty option. Sound and music remain enabled.

    There's no main menu background music assigned yet, though the slot exists in `options.rpy` for when one is added.

    ??? grid col single "Audio Channels"

        !!! grid scrollable ""

            Sound

            !!! cards col single centered-content ""

                -   enabled

            Music 

            !!! cards col single centered-content ""

                -   enabled

            Voice

            !!! cards col single centered-content ""

                -   disabled

=== "Window & Transitions"

    ## Window & Transitions 

    Transitions across the game are currently restrained. The game opens, closes, and moves between menu screens via a dissolve; 
    nothing else is set. This is a placeholder register, not a final state — Monster Silhouette will gain additional transitions in 
    the future as part of the visual polishing pass. Scene changes, chapter breaks, and narrative moments that call for more expressive 
    transitions will be given proper treatments once the visual design settles.

    The after-load and end-game transitions are at Ren'Py defaults. They have not been explicitly disabled. When the game gains more 
    transitions, these will likely be given treatments alongside the rest.

    === "Window Management"

        ??? grid col single "Window Management"

            !!! grid scrollable ""

                Window mode 

                !!! cards col single centered-content ""

                    -   `"auto"`
                    -   — the dialogue box hides before scene statements and reappears when dialogue resumes

                Show transition

                !!! cards col single centered-content ""
                    -   short dissolve

                Hide transition

                !!! cards col single centered-content ""
                    -   short dissolve

    === "Screen Transitions"

        ??? grid col single "Screen Transitions"

            !!! grid scrollable ""

                Enter 

                !!! cards col single centered-content ""

                    -   Ren'Py default

                Exit 

                !!! cards col single centered-content ""

                    -   Ren'Py default

                Intra 

                !!! cards col single centered-content ""

                    -   Ren'Py default

                After load 

                !!! cards col single centered-content ""

                    -   Ren'Py default

                End game 

                !!! cards col single centered-content ""

                    -   Ren'Py default

=== "Game Metadata & Build"

    ## Game Metadata & Build 

    === "Metadata"

        ### Metadata 

        These values assemble the project's public-facing identity — the name that appears in the window title, 
        the version shown on the About screen, the icon that appears in taskbar and dock presentations, the save directory name, 
        and the About text itself.

        The game title is hidden on the Main Menu — `gui.show_name` is set to `False`. This is a deliberate design choice: 
        the Main Menu's identity is carried by its visuals rather than a text title, letting the title screen read as a 
        composed image rather than a header plus navigation. The project name still appears in the window title and on the About screen.

        ??? grid col single "Project Metadata"

            !!! grid scrollable ""

                Name 

                !!! cards col single centered-content ""

                    -   Monster Silhouette 
                
                Version 

                !!! cards col single centered-content ""

                    -   0.1-beta
                
                Show name on main menu 
                
                !!! cards col single centered-content ""

                    -   disabled
                
                Window Icon

                !!! cards col single centered-content ""

                    -   `gui/window_icon.png` — Default Ren'Py Window Icon
                
                Save directory 

                !!! cards col single centered-content ""

                    -   versioned project identifier
                    
    === "About Text"

        !!! tip "Learn more about the About screen in the [Meta Screens][meta-screens] page"

        ### About Text 

        The About screen pulls its content from gui.about, a rich text string containing the project's premise blurb, 
        a credits line, and a set of official source links. The string supports Ren'Py's markup — bold, sizing, and 
        hyperlinks — all of which render on the About screen itself.


    === "Build Configuration"

        ??? info "About itch.io Project Link"

            The itch.io project link is present in `options.rpy` but remains commented out — it will be enabled once the project page 
            goes live.

        ### Build Configuration 

        Build configuration uses Ren'Py defaults for file classification and exclusion. 
        There's no custom archive layout, no custom file exclusions beyond what the engine provides, 
        and no additional documentation handling beyond the standard patterns. Standard build behavior applies.

## Closing Note 

Each of these settings is a single line somewhere in a configuration file. None of them do anything on their own.
 Together they determine the resolution the game renders at, the language its interface speaks in, how it sounds, 
 what pressing ESC does, and what the game calls itself when it introduces itself. That's a lot of surface area from two 
 files worth of configuration.