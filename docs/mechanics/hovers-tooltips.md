---
icon: lucide/scan-eye
status: new 
tags: 
    - GDD
    - ㅤLast Updated
    - ㅤㅤNovember 
    - ㅤㅤㅤ8
    - ㅤㅤㅤㅤ2026
---

??? warning "This page may not be up to date"

    Check the page tags for last date it was updated on. 

    If the date matches up with the last date-range entry in the [Build Log][log] you can be certain it's up to date. 

    !!! warning "Zensical's tag feature is not stable and filtering will likely not work as intended"

# Hovers & Tooltips

## Overview 

Hovers & Tooltips is a mechanic in Monster Silhouette that allows players to access additional information about game elements by hovering over them. 

The mechanic provides context-sensitive help without cluttering the main interface.
<br>
It currently extends Ren'Py's native tooltip support to render tooltips consistently across every screen that uses them.

A centralized screen draws the tooltip near its focused element. 
<br>
Screen-aware style families change how it appears depending on the active screen. 
<br>
A content dictionary holds long descriptions that would otherwise bloat inline declarations. 
<br>
Together, they make adding a tooltip to any actionable displayable anywhere in the game a matter of a single line of code.

=== "Ren'Py Built-in Tooltip"

    !!! tip "Learn more about Ren'Py's built-in tooltip attribute in [Ren'Py Engine Docs][renpy-doc]"

    ## Ren'Py Built-in Tooltip

    Ren'Py provides two pieces for tooltips: the `tooltip` attribute on buttons, which declares what the tooltip says, and `GetTooltip()`, which retrieves the 
    tooltip of whichever button currently has focus. 
    Underneath them is Ren'Py's focus tracking — a button gains focus when the mouse enters it and loses focus when the mouse leaves, and `GetTooltip()` 
    follows that focus.

    There is no native tooltip rendering within Ren'Py provided code. 
    No built-in screen to do so, no styling that determines its appearance, and no mechanism that changes that appearance based on the active screen.

=== "Tooltip Display"

    !!! tip "Learn more about the `tooltip_hover` screen in the [Overlay Screens][overlay-screens] page"

    ## Tooltip Display

    The `tooltip_hover` screen takes care of rendering for tooltips.

    It reads `GetTooltip()` on every interaction, and if the result is not `None`, it draws a small frame 
    near the currently focused element showing the tooltip text. 
    
    The screen is registered as an overlay via `config.overlay_screens.append("tooltip_hover")`, which means Ren'Py keeps it active across scene changes 
    and script progression — the same screen renders every tooltip in the game regardless of what else is showing.

    === "Overlay Suppression"

        !!! tip "Learn more about overlay suppression in the [Custom Actions][custom-actions] page"

        ### Overlay Suppression

        Overlays are suppressed while in menu and home contexts, which disables rendering of overlay screens like `tooltip_hover` within those contexts.
        
        The Computer UI Menu shown via `ShowHome()` — and any app screen it opens via `ShowMenu()` — therefore `use tooltip_hover` inline to keep tooltips rendering inside them. 
        
        App screens opened in scene context don't need this; the registered overlay handles them normally. Same screen, same behavior, different mechanism 
        depending on where it's shown.

    === "Tooltip Styles"

        !!! tip "Learn more about the tooltip style families in the [Settings & Options][settings-options] page"

        ### Tooltip Styles

        Once there's a tooltip to display, the screen decides which of four style families to apply by checking the active screen. 
        
        In scene context, it checks `chat_app` first, then `wardrobe_panel`, then `bedroom`, falling through to the default style family if none match. 
        
        In menu context, only `chat_app` triggers a specialized family; every other screen uses the default.  
        
        The check order matters — the most specific match wins.

=== "Tooltip Content"

    ## Tooltip Content

    === "Overview"

        Tooltips come in two forms. Short tooltips are declared inline on the button itself — `tooltip "Wardrobe"`, `tooltip "Return"` — 
        and are appropriate for labels that fit in a few words. Long tooltips need multiple lines of content, and declaring those inline would 
        bloat the button declaration to the point of unreadability.

        Therefore, I use a `tooltip_content` dictionary, which serves to hold those longer strings, keyed by descriptive IDs. 
        
        Buttons look up their tooltip via `tooltip tooltip_content["dress_shirt"]` rather than declaring the full text inline. Content stays reusable — 
        the same string can be used by multiple buttons — and editable in one place, so updating a description is a single dictionary entry rather than 
        a search across every declaration that uses it.

    === "Tooltip Content Variable"

        Below the variable storing long multi-line tooltips for Monster Silhouette's Hovers & Tooltips mechanic has been organized into an overview containing information on its: 

        - **Variable Name**
        - **Type**
            - Hover over cards for more details
        - **Keys**
            - Hover over cards for description
        - **Notes**

        ??? grid col single "Tooltip Content"

            <!-- tooltip: Tooltip Content Variable Overview Card -->
            
            !!! grid scrollable ""

                Variable Name

                !!! cards col single ""

                    -   `tooltip_content`
            
                Type 

                !!! cards col single ""

                    -   Dictionary
                        { title="{str: str}" }
                
                Keys 

                !!! grid col single no-pad no-border ""

                    !!! cards col single centered-content ""

                        -   `"dress_shirt"`
                            { title="Wardrobe tooltip for Dress Shirt sprite" }

                        -   `"thin_turtle_neck"`
                            { title="Wardrobe tooltip for Thin Turtle Neck sprite" }

                        -   `"lightweight_cargo_pants"`
                            { title="Wardrobe tooltip for Lightweight Cargo Pants sprite" }

                        -   `"dress_jeans"`
                            { title="Wardrobe tooltip for Dress Jeans sprite" }

                    !!! cards centered-content ""

                        -   `"chat_t"`
                            { title="Chat contact tooltip for And" }

                        -   `"chat_v"`
                            { title="Chat contact tooltip for At You" }

                        -   `"chat_l"`
                            { title="Chat contact tooltip for Golden Manager" }

                        -   `"chat_c"`
                            { title="Chat contact tooltip for The Abyss Stares Back" }
                    
                    !!! cards col single centered-content ""

                        -   `"chat_m"`
                            { title="Chat contact tooltip for Stare Into The Abyss" }
                
                Notes 

                !!! cards col single centered-content ""

                    -   Content source for long-form tooltips
                    -   Short tooltips use `tooltip "text"` inline instead
