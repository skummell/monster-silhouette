---
icon: lucide/package-plus
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

# Custom Actions

??? info "Code discussed in this page is found in 00gamemenu.rpy and 00action_menu.rpy"

    :   :octicons-alert-24:{ .red-icon } **These modified Engine Files are NOT available in [Monster Silhouette's Public Repo][github-repo]**
        
    :   :octicons-flame-24:{ .blue-icon } **You can find the original, non-modified Engine files in [Ren'Py's Source Code Repo][renpy-repo]**
    

## Overview 

Custom Actions in Monster Silhouette are modifications made to Ren'Py's own game menu infrastructure — specifically to 
`00gamemenu.rpy` and `00action_menu.rpy`, two files in the Ren'Py engine's `common/` folder. Where the Game Systems pages 
document systems built on top of Ren'Py, this page documents changes made inside it.

There is really one conceptual addition to Ren'Py's menu architecture: a third context alongside the game context and Ren'Py's 
existing menu context. Everything else on this page — the `ShowHome` action, the `_home_menu` label, the `_enter_menu` modification, 
the `_home` variable — exists to support that third context and the flow it enables.

The reason for this addition is the Computer UI Menu. Ren'Py's default game menu infrastructure assumes only two states: 
gameplay, or a game menu layered on top of gameplay. Monster Silhouette needs a state where the Computer UI Menu is showing 
— not quite gameplay, not quite a game menu — so that Meta Screens opened from inside it have somewhere to return to. 
Without the home context, opening Save & Load from Computer UI Menu would drop `ESC` back to gameplay instead of back to 
Computer UI Menu.

!!! warning "This Page Covers Engine-Level Modifications"

    This page documents changes made to Ren'Py's source files. 
    Two topics referenced here are documented in full elsewhere — the Computer UI Menu screen and the ShowHome game menu 
    routing set in options.rpy — and are only briefly mentioned here. Links are provided in tips at the relevant sections.

=== "The Three Contexts"

    ## The Three Contexts 

    Ren'Py supports nested contexts via `renpy.call_in_new_context()`. 
    Contexts isolate execution state — each has its own label position, own interaction stack, own values for context-dynamic variables. 
    The game continues to exist underneath; a new context stacks on top and returns control when it ends.

    Monster Silhouette operates with three context types active at different times:

    === "Game Context"

        ### Game Context 

        The default state. Regular script progression, dialogue interactions, screen updates.

        Context flags:

        -   `_menu = False`

        -   `_home = False`

        Every game starts here.

        This is the context that Ren'Py is designed around — the "not in any menu" state.

    === "Menu Context"

        ### Menu Context

        The state introduced by `ShowMenu()` — Ren'Py's standard mechanism for opening screens that live outside gameplay.

        Context flags:

        -   `_menu = True`

        -   `_home = False`

        Entered via Ren'Py's `_game_menu` label, which runs `_enter_game_menu` → `_enter_menu`. 

        `_enter_menu` marks the context with `_menu = True` and sets up the infrastructure that Ren'Py's game menu screens expect.

        This context is Ren'Py's own design. Monster Silhouette uses it unchanged for Meta Screens.

    === "Home Context"

        ### Home Context 

        The state introduced by `ShowHome()` — the custom addition.

        Context flags:

        -   `_menu = False` (intentionally)

        -   `_home = True`

        Entered via the custom `_home_menu` label, which does a lighter setup than `_enter_menu`. 
        Notably, it does not set `_menu = True`.

        The reasoning is structural. Because `_menu` stays `False` in home context, `ShowMenu()` calls made from inside home context 
        take the "not in menu" branch and create a nested menu context rather than showing the screen in the current context. 
        That nesting is what makes `ESC` inside a Meta Screen return the player to Computer UI Menu rather than dropping them back to 
        gameplay — the Menu context returns control to the Home context beneath it, not to the Game context beneath that.

        This is the core insight of the whole design. The home context is a lighter context than a menu context specifically so that 
        menu contexts can nest inside it and return cleanly.

=== "ShowHome Action"

    !!! tip "Learn more about the Computer UI Menu in the [Computer UI Screens][computer-ui-screens] page"

    !!! tip "Learn more about full Game Menu Action routing behavior in the [Settings & Options][settings-options] page"

    ## ShowHome Action 

    `ShowHome` is a custom Action class added to `00action_menu.rpy`. It is the mechanism that enters and exits the home context 
    — the toggle that pressing `ESC` triggers when the player is in gameplay.

    === "Behavior"

        Called with a screen name (defaults to `"computer_ui_menu"`), `ShowHome` checks whether the current context 
        is already in home mode:

        -   **If already in home context** — hide the screen, clear `_home` back to `False`, restart interaction. This is the "exit home menu" path.

        -   **If not in home context** — call `_home_menu` in a new context, passing the screen name. This is the "enter home menu" path.

        The toggle is intentional. 
        The same action both opens and closes the home menu depending on current state 
        — matching how ShowMenu behaves when called from within a menu context.

    === "Signature and Parameters"

        ??? grid col single "Signature and Parameters"

            !!! grid scrollable ""

                Function Call 

                !!! cards col single centered-content ""

                    -   `ShowHome(screen="computer_ui_menu", *args, _transition=config.intra_transition, **kwargs)`
                
                `screen` Parameter

                !!! cards col single centered-content ""

                    -   Target screen name
                    -   Defaults to `computer_ui_menu`
                    -   Must resolve to a defined screen (`renpy.has_screen` is checked; the action returns silently if the screen is not defined)
                    
                `*args` and `**kwargs` Parameters 

                !!! cards col single centered-content ""

                    -   Forwarded to `renpy.show_screen` inside `_home_menu`

                `_transition` Parameter

                !!! cards col single centered-content ""

                    -   Transition used when the screen changes
                    -   Falls back to `config.intra_transition` when not specified

    === "Methods"

        ??? grid col single "Methods"

            !!! grid scrollable ""

                `predict()`

                !!! cards col single centered-content ""

                    -   pre-warms the target screen for caching.
                
                `get_selected()`

                !!! cards col single centered-content ""

                    -   returns whether the target screen is currently showing.
                
                `get_sensitive()`

                !!! cards col single centered-content ""

                    -   always returns `True` (unless screen is `None`).
        
    === "Comparison With ShowMenu"

        `ShowMenu` is Ren'Py's own menu entry action. 
        <br>
        `ShowHome` mirrors its structure but does not go through `_game_menu` and does not call `_enter_menu`. 
        
        Where `ShowMenu` sets up a full menu context, `ShowHome` sets up a lighter home context. 
        
        Both use `call_in_new_context` under the hood.
                
        `ShowHome` is wired as the `ESC` / `game_menu` key trigger through `config.game_menu_action`.

=== "Home Menu Entry Point"

    ## Home Menu Entry Point 

    The `_home_menu` label in `00gamemenu.rpy` is the actual entry point for home context. 

    It is called by `ShowHome.__call__` via `renpy.call_in_new_context`.

    === "What It Does"

        !!! tip "Learn more about Overlay Screens in the [Overlay Screens][overlay-screens] page"

        Its steps in order:

        1. **Screenshot** — takes a screenshot of the current state if not already in a menu context
            - This screenshot becomes the preview thumbnail in save slots
            - Taken before the Computer UI Menu shows, so saves display the gameplay behind the menu, not the menu itself

        2. **Set home flag** — `store._home = True`

        3. **Suppress overlay** — `store.suppress_overlay = True`
            - Hides the Quick Menu, Status Bar, and Freeze Hint Display while home context is active.

        4. **Show the target screen** — `renpy.show_screen(_home_screen, ...)`, standard show behavior (not `_transient`)

        5. **Interact** — `ui.interact()`
            - This is the interaction loop that runs until the player clicks a button that ends the interaction or presses `ESC`

        6. **Clean up** — `store._home = False`

        7. **Return** — ends the context and returns to the game

    === "Why It's Lighter Than Game Menu"

        `_game_menu` calls `_enter_game_menu`, which runs `_enter_menu`, which sets up the full menu context 
        — `context_dynamic` registrations, `_menu = True`, layer clears, and so on. `_home_menu` does none of this.

        The reason: none of that infrastructure is needed for a home context. 
        The Computer UI Menu is a regular screen; it doesn't rely on `_menu` being `True` in its design. 
        By keeping `_menu = False`, `_home_menu` preserves the ability for `ShowMenu` calls made from inside Computer UI Menu to 
        create nested contexts — the behavior that makes `ESC` navigation work correctly.

=== "Supporting Infrastructure"

    ## Supporting Infrastructure 

    === "The Home Variable"

        ### The Home Variable 

        A new store variable, `default _home = False`, that tracks whether a home context is active. 
        Set to `True` when entering `_home_menu`, cleared to `False` on exit.

        Three places read it:

        - `ShowHome.__call__` — toggles home context on/off based on its current value.

        - `_enter_menu` — to suppress the intermediate screenshot when entering a menu from within home context.

        - `_enter_home_menu` — set defensively, though this label isn't currently called.

    === "The Enter Home Menu Label"

        ??? info "Current Usage Implementation"

            This label is not called anywhere in the Engine Files.

            It exists as scaffolding — reserved for future use. 
            
            If the home context ever needs the full `_enter_menu` treatment (`context_dynamic` registrations and so on), 
            `_enter_home_menu` is where that would be wired in. 
            
            As it stands, `_home_menu` does its job without going through `_enter_menu` at all.

        ### The Enter Home Menu Label 

        A parallel to `_enter_game_menu` — same shape, same purpose, but for home context:

        - Sets `suppress_overlay = True`

        - Calls `_enter_menu`

        - Applies `config.enter_transition`

        - Calls an optional `enter_home_menu` hook label if one exists

    === "The Enter Menu Modification"

        !!! tip "Learn more about the Save & Load Screen in the [Meta Screens][meta-screens] page"

        ### The Enter Menu Modification 

        One line changed in the vanilla _enter_menu function:

        ??? file "Code Snippet"
            ```python 
            # Vanilla
            if not renpy.context()._menu:
                renpy.take_screenshot(...)

            # Modified
            if not renpy.context()._menu and not store._home:
                renpy.take_screenshot(...)
            ```

        The addition `and not store._home` prevents a screenshot from being taken when entering a menu context from within home context.

        The reasoning ties back to how screenshots feed save slots. When the player is in gameplay and presses `ESC`, `_home_menu` takes 
        a screenshot before showing Computer UI Menu — that's the correct "gameplay" preview that will appear in save slots. 
        
        Then the player opens Save & Load from Computer UI Menu, which calls: 
        <br>
        `ShowMenu` → `_game_menu` → `_enter_game_menu` → `_enter_menu`. 

        Without the guard, `_enter_menu` would take a second screenshot — but this time, the current screen is Computer UI Menu, 
        not gameplay. Save slots would then show the Computer UI Menu screen as their thumbnail. 
        
        The `and not store._home` guard prevents that second capture when home context is active.

    === "The Invoke Game Menu Flow"

        ### The Invoke Game Menu Flow 

        `_invoke_game_menu` is Ren'Py's handler for the game menu key press. 
        Its else branch checks whether `config.game_menu_action` is set:

        - **If set** — the action runs directly
            - In Monster Silhouette, `config.game_menu_action` is `ShowHome("computer_ui_menu", _zorder=1)`, so ESC triggers `ShowHome`

        - **If not set** — falls back to `renpy.call_in_new_context("_game_menu")`, Ren'Py's standard game menu entry

        This branch is what makes the "press `ESC` to open Computer UI Menu" behavior work — the `game_menu` key press routes through 
        `_invoke_game_menu`, which respects the configured action and defers to `ShowHome` rather than entering Ren'Py's default 
        game menu.



## Modification History 

The current shape of these changes is the product of three rounds of iteration, tracked in [LOG.md][log]:

=== "September 5-6"

    Initial implementation. `ShowHome` created as a callable that opens a new context between game and menu contexts. 
    `_home_menu` label added to support it. 
    The redirect of the game menu key to Computer UI Menu via `config.game_menu_action` also lands here.

    Screenshot timing tweaked in this round — Computer UI Menu no longer shows in the save screenshot. 
    This is the initial screenshot capture fix, handled by `_home_menu` taking the screenshot before showing the screen.

=== "September 7"

    Suppress overlay fix. Added `suppress_overlay = True` handling to hide the Quick Menu during home context. 
    The `_enter_home_menu` label appears to date from this round.

=== "September 22-28"

    Intermediate screenshot fix. 
    Discovered that when opening Save & Load from Computer UI Menu, `_enter_menu` was taking a second screenshot 
    showing Computer UI Menu, which then appeared in save slot thumbnails. 
    Fixed by adding `and not store._home` to the screenshot guard in `_enter_menu` — the modification documented above.

=== "Net Result"

    The current state on this page. 
    Three contexts, one custom action, one custom label, one variable, one modification to a vanilla function, 
    and one branch added to `_invoke_game_menu`.
