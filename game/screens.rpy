## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE   

################################################################################
## Initialization
################################################################################

init offset = -1
default player_endings = 0 # Track How Many Endings Have Been Reached By The Player
default total_endings = 0 # Number Of Endings Currently Available 
default active_contact = None # Track which Chat Contact is Open / Active

# Tooltip Content Dictionary for Long Tooltips
define tooltip_content = { 
    # Wardrobe Clothing Tooltips
    "dress_shirt": "{b}Dress Shirt{/b}\n\nA slightly fancy, semi-formal dress shirt you got from Victor a few years ago. You don't know how pricy it was but it was probably pricier than 90% of your closet. Victor never gifted things at a normal price range.",
    "thin_turtle_neck": "{b}Thin Turtle Neck{/b}\n\nA turtle neck of good quality fabric. You're quite fond of it. Traps heat when the sun is strong but is otherwise fine by itself, even in warmer weather.",
    "lightweight_cargo_pants": "{b}Lightweight Cargo Pants{/b}\n\nYour favorite cargo pants. It's got lots of pockets. You could probably fit a surprise or two in them.",
    "dress_jeans": "{b}Dress Jeans{/b}\n\nSlightly formal jeans you've had since college. Somehow it still looks new. A good pair with a more semi-formal top.",

    # Chat Profile Preview Tooltips
    "chat_t": "World Explorer!\nThe great Theo is here!",
    "chat_v": "Owner of Kiri Rêve Tea Lounge.\nLocation: Lucius Ave & Blackwood Rd, Ombra Town.",
    "chat_l": "Head Pub. Manager @ King Yellow.\nEditor of Best-Selling Horror Writer: The Abyss Stares Back.",
    "chat_c": "Mystery Horror Writer.\nAuthor of Into The Depths, To Die To Sleep, and many more.",
    "chat_m": "Horror Connoisseur and #1 Faithful Fan of The Abyss Stares Back's book sagas."
}

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

# Set Clipping to True
style clipped: 
    clipping True

# Set Frame with no background, padding nor margin
style zeroed_frame: 
    background None
    padding(0, 0)
    margin(0, 0)

# Set to bold 
style bolded: 
    bold True 

style full_screen: 
    xysize(config.screen_width, config.screen_height)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    key "K_F5" action QuickSave()
    key "K_F6" action QuickLoad()

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save & Load") action ShowMenu('save_load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu (status_bar & freeze_hint_display) screen(s) is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("status_bar")
    config.overlay_screens.append("freeze_hint_display")
    config.overlay_screens.append("tooltip_hover")

default quick_menu = True
default status_bar = False

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Status Bar screen ###########################################################
## This screen is only included in-game and provides you with the
## In-game Date and Time

screen status_bar(): 

    zorder 100

    # Computer UI Status Bar Logo Dimensions
    $ ui_logo_height = 20 
    $ ui_logo_width = 35

    # Computer UI Status Bar Icon Dimensions 
    $ status_bar_icon_width = 40
    $ status_bar_icon_height = 20

    if status_bar or renpy.get_screen("computer_ui_menu"):

        # Content
        frame: 
            at fill_width(status_bar_height)
            style "status_bar_frame"

            add "gui/placeholders/status_bar_placeholder.svg": 
                at fill_width(status_bar_height)
            
            if renpy.get_screen("computer_ui") or renpy.get_screen("computer_ui_menu") or renpy.get_screen("computer_ui", "master"): 

                # Logo 
                add "#000": 
                    xysize(ui_logo_width, ui_logo_height)
                    yalign 0.5
                    xpos ui_logo_left_pad

            # Icons & Details
            hbox: 
                style "status_bar_hbox"

                # Computer UI Icons
                if renpy.get_screen("computer_ui") or renpy.get_screen("computer_ui_menu") or renpy.get_screen("computer_ui", "master"): 
                    # Battery
                    add "#000": 
                        xysize(status_bar_icon_width, status_bar_icon_height)
                        yalign 0.5 

                    # WiFi 
                    add "#000":
                        xysize(status_bar_icon_width, status_bar_icon_height)
                        yalign 0.5 

                    # Spotlight
                    add "#000":
                        xysize(status_bar_icon_width, status_bar_icon_height)
                        yalign 0.5 

                else: # Placeholder space for layout consistency 

                    null width status_bar_icon_width height status_bar_icon_height
                    null width status_bar_icon_width height status_bar_icon_height
                    null width status_bar_icon_width height status_bar_icon_height

                # Date Text 
                fixed: 
                    style "date_text_container"

                    text _(abyss_date.strftime("%a %b %d")): 
                        style "date_text"

                # Time Text Container 
                fixed: 
                    style "time_text_container"

                    textbutton (abyss_time): 
                        style "time_text"
                        text_hover_color gui.hover_color
                        text_size 20

                        action If(renpy.get_screen("computer_ui_menu"), Return(), None)

                        tooltip "Return"

# Status Bar Styles

# Status Bar Content Frame 
style status_bar_frame is clipped: 
    background None
    padding(0, 0)
    margin(0, 0)

# Status Bar Icons & Details Container
style status_bar_hbox is clipped
style status_bar_hbox: 

    # Same pad to the right as the logo has to the left
    xanchor 1.0
    xpos int(config.screen_width - ui_logo_left_pad)
    # Length of one third of Status Bar
    xsize int(config.screen_width / 3)
    # Center Vertically
    yalign 0.5 
    # Spacing between Hbox Elements
    spacing status_bar_details_gap 

# Status Bar Text Containers
style status_bar_text_container: 

    # Text Container Height 
    ysize 25
    # Center Vertically 
    yalign 0.5 

# Status Bar Date Text Container 
style date_text_container is status_bar_text_container
style date_text_container: 

    # Date Text Container Width
    xsize 120

# Status Bar Time Text Container
style time_text_container is status_bar_text_container
style time_text_container: 

    # Time Text Container Width 
    xsize 100

# Status Bar Text
style status_bar_text: 

    # Align to the Left
    xalign 1.0
    # Text Size 
    size 20

# Status Bar Date Text 
style date_text is status_bar_text 

# Status Bar Time Text
style time_text is status_bar_text

# Fill Screen Transform
transform fill_screen: 
    xysize(config.screen_width, config.screen_height)
    fit "fill"

# Fill Width Transform
transform fill_width(height=38): 
    xysize(config.screen_width, height)
    fit "fill"

## Tooltip Hover screen ###############################################################
##
## This screen is used to display tooltips when hovering over buttons and other elements 
## that have tooltips defined.

screen tooltip_hover():

    zorder 200

    # Tooltip
    $ tooltip = GetTooltip()

    # Tooltip Style
    if not renpy.get_screen("computer_ui_menu"):
        if renpy.get_screen("chat_app", "master") or renpy.get_screen("chat_app"):
            $ style_prefix = "profile_preview"
        elif renpy.get_screen("wardrobe_panel", "master"):
            $ style_prefix = "wardrobe_select"
        elif renpy.get_screen("bedroom", "master"):
            $ style_prefix = "bedroom_tooltip"
        else:
            $ style_prefix = "tooltip"
    else:
        if renpy.get_screen("chat_app"):
            $ style_prefix = "profile_preview"
        else:
            $ style_prefix = "tooltip"
    
    if tooltip: 

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                style style_prefix + "_frame"
                    
                text tooltip style style_prefix + "_text"

# Tooltip Hover Styles 

# Default Styles 

# Tooltip Frame (Default Style)
style tooltip_frame: 
    background "#5E5E5E"
    # Horizontal Padding 
    xpadding 12 
    # Vertical Padding
    ypadding 4
    # Center Horizontally 
    xalign 0.5
    # Height 
    ysize 45
    # Vertical Margin
    ymargin 10

# Tooltip Text (Default Style)
style tooltip_text: 
    size 14 
    color "#C8C8C8"
    # Center Horizontally
    xalign 0.5
    textalign 0.5

# Profile Preview Tooltip (Contact Button Hover)
style profile_preview_frame:
    background "#00bfffa4"
    xpadding 8
    ypadding 6
    xsize 200

style profile_preview_text:
    size 10
    color "#000000"
    xalign 0.0
    textalign 0.0
    layout "tex"

# Bedroom Interactable Tooltip
style bedroom_tooltip_frame is tooltip_frame:
    background gui.muted_color

style bedroom_tooltip_text is tooltip_text

# Wardrobe Selection Tooltip
style wardrobe_select_frame:
    background "#5E5E5E"
    xpadding 12
    ypadding 4
    xalign 0.5
    ymargin 10
    xsize 300

style wardrobe_select_text is tooltip_text:
    xalign 0.0
    yalign 1.0
    textalign 0.0
    layout "tex"

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Start") action [Start(), Hide("computer_ui")]
        textbutton _("Save & Load") action ShowMenu("save_load")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=True)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

## Navigation Dock screen ######################################################
## Similar to the Navigation Screen, this screen provides navigation
## to other menus.

screen navigation_dock(): 

    zorder 2

    fixed: 
    
        # Dock Icons (6 icons)
        grid 6 1: 
            style "navigation_dock"

            # History - Icon Button 
            use dock_button("history", "History")

            # Save & Load - Icon Button
            use dock_button("save_load", "Save & Load")

            # Preferences - Icon Button 
            use dock_button("preferences", "Preferences")

            # Ending Gallery - Icon Button 
            use dock_button("ending_gallery", "Endings")

            # About - Icon Button 
            use dock_button("about", "About")

            # Help - Icon Button 
            if renpy.variant("pc") or renpy.variant("web") and not renpy.variant("mobile"): 
                ## Help isn't necessary or relevant to mobile devices. 
                use dock_button("help", "Help")
    
    if _in_replay: 
        
        textbutton _("End Replay") action EndReplay(confirm=True)

    # Main Menu Return - Power Off Icon Button
    if not main_menu: 
        imagebutton: 

            style "power_off_button"

            idle "gui/placeholders/power_off_placeholder.svg"

            action MainMenu()

            tooltip "Start Screen"

# Navigation Dock Styles 

# Docks at the bottom of the screen 
style bottom_dock: 
    # Push to the bottom of screen
    yalign 1.0
    # Raise up a little
    yoffset -(dock_bottom_pad)

# Navigation Dock
style navigation_dock is bottom_dock

style navigation_dock: 
    # Center Horizontally 
    xalign 0.5 
    # Navigation Dock Icons Spacing 
    spacing dock_icons_spacing 

# Power Off Button
style power_off_button is bottom_dock 

style power_off_button: 
    # Push to the right corner of the screen
    xalign 0.95

## Dock Button Template ########################################################
##
## Template for Dock Buttons (History, Save & Load, Preferences, Endings, About, Help)

screen dock_button(page_name, tooltip, dock_icon="gui/placeholders/dock_icon_placeholder.svg"):

    imagebutton:

        idle dock_icon

        action ShowMenu(page_name)

        tooltip tooltip

## App Grid screen #############################################################
## This screen display in-game apps inside the Computer UI 

screen app_grid():

    $ in_scene = False

    if not renpy.get_screen("computer_ui_menu") and renpy.get_screen("computer_ui", layer="master"): 
        $ in_scene = True

    fixed: 
        # Grid Icons (6 columns x 3 rows)  
        grid 6 3: 
            style "app_grid"

            # Row 1 

            # Profile App
            use app_button("profile_app", "Profile", in_scene)
                
            # Chat App 
            use app_button("chat_app", "Chat", in_scene)

            # Draft App 
            use app_button("draft_app", "Draft", in_scene)

            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"

            # Row 2
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"

            # Row 3
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"
            add "gui/placeholders/grid_icon_placeholder.svg"

# App Grid Styles

# App Grid 
style app_grid: 
    # Horizontal centering 
    xalign 0.5 
    # Top Padding
    ypos app_grid_top_pad
    # Grid Spacing
    spacing app_grid_spacing

## App Open Button Template ####################################################
##
## Template for app buttons 
## Shows app screens through appropriate method
## (profile_app, chat_app, draft_app)

screen app_button(app_name, tooltip, in_scene=False, app_icon="gui/placeholders/grid_icon_placeholder.svg"): 

    imagebutton: 

        id app_name

        idle app_icon

        # Disable Button if disablers are on and screen is not Computer UI Menu
        if button_disabled(app_name):
            
            action NullAction()

        else: 
            
            action If(in_scene, Function(show_app, app_name), Show(app_name))

        tooltip tooltip


## App Screen Template #########################################################
##
## Template for app screens
## (Profile App, Chat App, Draft App)
## For Design consistency

screen app_screen(window_width, window_height, content_width, content_height, screen_title, tool_screen=None): 
    
    tag app

    if renpy.get_screen("app", "master") and not renpy.get_screen("computer_ui_menu"):
        key "game_menu" action config.game_menu_action
    else: 
        key "game_menu" action Hide()

    window id "app": 

        style "app_window"
        xysize (window_width, window_height)

        fixed: 
            style "app_window_content"
            xysize (window_width, window_height)

            add "#000000":
                xysize (window_width, window_height)

            # Title Bar 
            use app_header(window_width, screen_title)

            # Main Content Area
            frame: 
                style "app_main_content"
                at app_main_content(content_width, content_height)
                
                add "#C8C8C8": 
                    xysize(content_width, content_height)

                transclude

            if tool_screen != None: 
                use expression tool_screen
    
    if renpy.get_screen("computer_ui_menu"): 
        use tooltip_hover

# App Screen Styles

# App Screen Window
style app_window is clipped: 
    background None
    padding(0, 0)
    margin(0, 0)
    xalign 0.5
    yalign 0.5

# App Screen Window Content 
style app_window_content is clipped

# App Main Content Frame Transform & Style 
transform app_main_content(content_width, content_height): 
    xysize(content_width, content_height)
    xalign 0.5
    ypos app_header_height + app_header_content_gap

style app_main_content is clipped:
    background None
    padding(0, 0)
    margin(0, 0)

## App Header screen ###########################################################
##
## Displays App Header with App Name and the closing button inside of 
## App Screens

screen app_header(window_width, screen_title): 

    frame: 

        style "app_header_frame"

        xysize(window_width, app_header_height)

        add "gui/placeholders/App Title Bar Placeholder.svg": 
            xysize(config.screen_width, app_header_height)

        fixed: 
        
            style "app_header_content"

            xysize(window_width, app_header_height)

            # Exit Button - Hides Screen 
            use app_exit(screen_title)

            # Title Text 
            text screen_title: 

                style "app_header_title"

# App Header Styles

# App Header Frame
style app_header_frame is zeroed_frame 
style app_header_frame is clipped: 
    background None
    padding(0, 0)
    margin(0, 0)

# App Header Content Container
style app_header_content is clipped

style app_header_content: 
    yalign 0.5 

# App Header Title
style app_header_title is bolded

style app_header_title: 
    # Center Title 
    xalign 0.5 
    yalign 0.5 

## App Exit Button #############################################################
##
## App Exit Button Screen for reusable purposes 
## Hides app screens or does nothing if disabled
## (Profile, Chat, Draft)

screen app_exit(id_name): 

    imagebutton: 

        style "app_exit_button"
        
        id id_name

        idle "#0026ff"

        # Disable Button if disablers are on and screen is not Computer UI Menu
        if button_disabled(id_name):

            action NullAction()

        else: 
        
            action Hide()

# App Exit Styles

# App Exit Button
style app_exit_button: 
    xysize(app_exit_width, app_exit_height)
    xpos 10 # Left padding


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    zorder 2

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

## Computer UI Menu screen #####################################################
##
## A version of Computer UI that can be called on at any time in point as
## the primary game menu

screen computer_ui_menu(): 

    tag menu

    modal True

    key "game_menu" action [Return(), Return()]
    
    use computer_ui
    use status_bar
    use tooltip_hover

## Computer UI screen (Custom Game Screen) #####################################
##
## A screen that serves as a menu center from which the player can access
## meta screens and special gameplay screens

screen computer_ui(): 

    tag game

    fixed: 

        at fill_screen

        style "clipped"

        # Background
        add "gui/placeholders/gray_background.svg": 
            at fill_screen

        use app_grid  

        if not renpy.get_screen("quick_menu"): # Only when Quick Menu is not Available
            use navigation_dock 

## Scrollable Content screen ###################################################
##
## A screen that provides scroll support depending on the scroll type

screen scrollable_content(scroll=None, yinitial=0.0, spacing=0, scrollbars="vertical", left_pad=0, top_pad=0, right_pad=0, bottom_pad=0, yadjustment=None, vp_width=0, vp_height=0): 

    # Content with scroll support
    if scroll == "viewport":
        viewport id "vp_static":
            if vp_width: 
                xsize vp_width
            else: 
                xfill True

            if vp_height: 
                ysize vp_height
            else: 
                yfill True
            yinitial yinitial
            yadjustment yadjustment
            scrollbars scrollbars
            vscrollbar_unscrollable "hide"
            mousewheel True
            draggable True
            pagekeys True

            frame: 
                background None 

                padding (left_pad, top_pad, right_pad, bottom_pad)

                
                vbox:

                    spacing spacing
                    xfill True

                    transclude

    elif scroll == "vpgrid":
        vpgrid:
            if vp_width: 
                xsize vp_width
            else: 
                xfill True
            if vp_height: 
                ysize vp_height
            else: 
                yfill True
            side_xfill True
            cols 1
            yinitial yinitial 
            scrollbars scrollbars
            vscrollbar_unscrollable "hide"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            spacing spacing
            transclude

    else:
        transclude

init python:

    def _on_adj_ranged(adj):
        adj.value = adj.range

    adj = ui.adjustment(ranged=_on_adj_ranged)

    def scroll_top(adj_var): 
        adj_var.change(0)

    def scroll_bottom(adj_var): 
        adj_var.change(adj_var.range)


## Meta Screen Template ########################################################
## 
## Template for all meta screens 
## (About, Save & Load, History, Preferences, Help, Ending Gallery)
## For Design consistency

screen meta_screen(title, scroll=None, yinitial=0.0, spacing=0, **kwargs): 

    tag menu 

    key "game_menu" action Return()

    # Meta Screen Dimensions 
    $ content_width = 1240
    $ content_height = 640

    fixed: 

        style "clipped"

        at fill_screen

        # Background 
        add "#000000"

        # Header Bar
        fixed: 

            at fill_width(meta_header_height)

            style "clipped"

            add "gui/placeholders/meta_screen_header.svg": 
                at fill_width(meta_header_height)
                
            # Header Title 
            text title: 
                style "meta_header_title"

            # Close Button - Returns to previous screen
            imagebutton: 

                idle "gui/placeholders/meta_screen_exit_placeholder.svg"
                at meta_close_button
                style "meta_close_button"

                action Return()

        # Main Content Area 
        fixed: 
            
            style "meta_main_content"

            xysize (content_width, content_height)
            
            add "gui/placeholders/meta_screen_content_background.svg": 
                xysize (content_width, content_height)

            frame:

                style "meta_main_content_frame"

                use scrollable_content(scroll, yinitial, spacing, **kwargs): 
                    transclude

# Meta Screen Styles

# Meta Screen Header Title 
style meta_header_title is bolded 

style meta_header_title: 
    # Left Padding 
    xpos 20 
    # Top Padding
    yalign 0.5
    # Text Color
    color "#d6d6d6"
    # Text Size
    size 30 

# Meta Screen Exit Button
style meta_close_button: 
    # Left Padding 
    xpos int(config.screen_width - meta_exit_button_width - 12)
    # Center vertically 
    yalign 0.5 

transform meta_close_button: 
    xysize (meta_exit_button_width, meta_exit_button_height)

# Meta Screen Main Content Container 
style meta_main_content is clipped

style meta_main_content: 
    # Center Horizontally
    xalign 0.5 
    # Enforce Lower Padding
    yanchor 1.0 
    ypos (config.screen_height - meta_content_bottom_pad)
    
# Meta Screen Main Content Container Frame 
style meta_main_content_frame is zeroed_frame 

style meta_main_content_frame: 
    padding (20, 20, 20, 20)

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu
    zorder 2

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use meta_screen(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            # text _("Version [config.version!t]\n")
            text _("by {b}SkumMell{/b}\n")
            

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n" style "about_text"

            add Solid("#000000") xysize (config.screen_width, 2)

            text _("\nYou are currently playing {b}Monster Silhouette Demo{/b} ([config.version!t]).\n")

            text _("\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_text: 
    size 20
    line_spacing -5


## Load and Save screen #######################################################
##
## This screen is responsible for letting the player save and load the game
##
## The default Load and Save screen in ren'py are separate screens. 
## https://www.renpy.org/doc/html/screen_special.html#save 
## https://www.renpy.org/doc/html/screen_special.html#load

# Custom Unified Save & Load Menu
screen save_load(): 
    
    tag menu 
    zorder 2

    if main_menu: 
        # In main menu - only load
        use file_slots("load")

        # Game Menu Key
    else: 
        # In-game - save & load 
        use file_slots()


screen file_slots(context=None):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use meta_screen("Save & Load"):

        fixed:

            style "file_slots_fixed"

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                style "slot_grid"

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        # Context dependent actions

                        # Main Menu - Load immediately
                        if context == "load": 
                            action FileLoad(slot, confirm=True)

                        # In-game behavior
                        else: 
                            
                            # Slot Empty - Save immediately 
                            if not FileLoadable(slot):
                                action FileAction(slot)

                            # Slot Occupied - Ask Whether to Save or Load
                            else: 
                                action ShowMenu("save_load_choice", slot)

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                style "page_vbox"

                hbox:
                    style "page_hbox"

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save_load" and not main_menu:
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 4
    xalign 0.5

style page_label_text:
    size 28
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    size 26
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

style file_slots_fixed: 
    # Center things 
    xfill True
    yfill True

style slot_grid: 
    xalign 0.5
    yalign 0.5
    spacing gui.slot_spacing

style page_vbox:
    xalign 0.5
    yalign 1.0
    yoffset -5

style page_hbox: 
    xalign 0.5
    spacing gui.page_spacing

# Save or Load Choice Screen - Unified Save & Load Screen Handler
screen save_load_choice(slot): 

    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame: 
        vbox: 
            style "confirm_save_load_vbox"

            hbox: 
                style "confirm_save_load_hbox"

                textbutton _("Save") action [Hide("save_load_choice"), FileAction(slot)]
                textbutton _("Load") action [Hide("save_load_choice"), FileLoad(slot)]

    key "game_menu" action Hide("save_load_choice")

style confirm_save_load: 
    xalign 0.5 

style confirm_save_load_vbox is confirm_save_load 

style confirm_save_load_vbox: 
    yalign 0.5
    spacing 30 

style confirm_save_load_hbox is confirm_save_load 

style confirm_save_load_hbox: 
    spacing 100

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    zorder 2

    use meta_screen(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0
    bold True 

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    zorder 2

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use meta_screen(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu
    zorder 2

    default device = "controls"

    use meta_screen(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("MS-Controls") action SetScreenVariable("device", "controls")

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
            elif device == "controls":
                use controls_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

screen controls_help():

    hbox: 
        label _("F5")
        text _("Quick Save.")
    
    hbox: 
        label _("F6")
        text _("Quick Load.")

    hbox: 
        label _("D")
        text _("Delete save slot on hover.")
    
    hbox: 
        label _("ESC")
        text _("Access Computer UI Menu and exit game menus and apps.")
    
    hbox: 
        
        fixed: 
            style "help_icon"

            add "#000" xysize(label_icon_width, label_icon_height) yalign 0.5 xalign 1.0

        text _("Click for a hint when available.")

# Help Styles

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize label_width

style help_hbox: 
    spacing label_right_pad

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

style help_icon:
    xsize label_width
    ysize label_icon_height

## Ending Gallery screen #######################################################
## 
## This screen serves as a gallery for endings the Player has achieved. 

screen ending_gallery(): 

    tag menu 
    zorder 2

    $ screen_name = "Ending Gallery"

    $ ending_lock_icon_width = 300 
    $ ending_lock_icon_height = 350

    if player_endings == 0: # Zero Endings Unlcoked
        use meta_screen(_(screen_name)): 

            fixed:
                style "ending_gallery"

                vbox: 
                    style "ending_gallery_zero_vbox"

                    add "#000": 
                        xysize(ending_lock_icon_width, ending_lock_icon_height)
                        xalign 0.5

                    text "Currently no Available Endings": 
                        style "ending_gallery_zero_text"

    else: # At Least One Ending Unlocked 
        
        use meta_screen(_(screen_name), "viewport", scrollbars=None, top_pad=50): 

            fixed: 
                style "ending_gallery_endings"

                # Ending Grid Placeholder 
                grid 2 3: 
                    style "ending_gallery_grid"

                    fixed: 
                        style "ending_gallery_grid_entry"
                        add "#a71f1f": 
                            xysize(ending_grid_entry_width, ending_grid_entry_height)

                    fixed: 
                        style "ending_gallery_grid_entry"
                        add "#000": 
                            xysize(ending_grid_entry_width, ending_grid_entry_height)

                    fixed: 
                        style "ending_gallery_grid_entry"
                        add "#000": 
                            xysize(ending_grid_entry_width, ending_grid_entry_height)
                    
                    fixed: 
                        style "ending_gallery_grid_entry"
                        add "#000": 
                            xysize(ending_grid_entry_width, ending_grid_entry_height)
                    
                    fixed: 
                        style "ending_gallery_grid_entry"
                        add "#000": 
                            xysize(ending_grid_entry_width, ending_grid_entry_height)


# Ending Gallery Styles 

style ending_gallery is clipped

# Ending Gallery Zero Endings Main Content Container 
style ending_gallery_zero_vbox is clipped
style ending_gallery_zero_vbox: 
    xysize(655, 415)
    xalign 0.5
    yalign 0.5
    spacing 40 

style ending_gallery_zero_text is label_text
style ending_gallery_zero_text:
    xalign 0.5
    color "#000"

style ending_gallery_endings: 
    xysize (1200, 430)
    xalign 0.5
    yalign 0.5

style ending_gallery_grid:
    spacing 20
    xalign 0.5
    yalign 0.5

style ending_gallery_grid_entry:
    xysize(ending_grid_entry_width, ending_grid_entry_height)


################################################################################
## Special Gameplay screens
################################################################################

## Exit Disabled Warning Screen ################################################
##
## This screen warns the player that the exit button for the app is currently unavailable.

screen exit_disabled_warning(app):

    zorder 20

    frame: 

        style "exit_disabled_warning_frame"

        text "{b}Note:{/b} [app] App exit button is currently unavailable. Use ESC shortcut to close out of app.":
            style "exit_disabled_warning_text"

# Exit Disabled Warning Styles

# Exit Disabled Warning Frame
style exit_disabled_warning_frame:

    background gui.muted_color
    # Center Horizontally 
    xalign 0.5 
    # Top Padding
    ypos 10

# Exit Disabled Warning Text
style exit_disabled_warning_text:

    size 16 
    color gui.hover_color
    # Center Horizontally 
    xalign 0.5
    textalign 0.5

## Freeze Hint Display Screen ##################################################
##
## This screen displays a hint for the player in order to end a freeze and 
## move on with the story

screen freeze_hint_display():

    zorder 150 

    if not renpy.get_screen("computer_ui_menu") and _current_hint is not None: 
        
        frame: 
            style "freeze_hint_display_frame"

            text "{b}Hint:{/b} [_current_hint]": 
                style "freeze_hint_display_text"

# Freeze Hint Display Styles 

# Freeze Hint Display Frame
style freeze_hint_display_frame: 

    background gui.muted_color
    # Left Padding
    xpos 40
    # Top Padding 
    ypos status_bar_height + 2 

# Freeze Hint Display Text
style freeze_hint_display_text: 

    size 16
    color gui.hover_color
    xalign 0.5
    textalign 0.5

## Notif Button Template #######################################################
##
## This is a template for Notification Buttons 

screen notif_button(app_screen, app_prefix, notif_bg="gui/placeholders/light_gray_background.svg", notif_icon="gui/placeholders/grid_icon_placeholder.svg"): 

    $ icon_width = 58
    $ icon_height = 52

    button: 

        style "notif_button"

        if button_disabled(app_screen): 

            action NullAction()

        else: 

            action (Function(show_app, app_screen), Function(hide_app, app_screen + "_notification"))

        add notif_bg: 
            xysize(notif_button_width, notif_button_height)

        frame: 

            style "notif_button_frame"

            hbox: 
                style "notif_button_hbox"

                add notif_icon: 
                    xysize(icon_width, icon_height)

                vbox: 

                    style "notif_button_vbox"

                    text "[app_prefix] Notification": 
                        style "notif_button_title"
                    
                    transclude 

# Notif Button Styles 

# Notif Button 
style notif_button is clipped
style notif_button: 

    xysize(notif_button_width, notif_button_height)
    xcenter 0.86
    ypos 40

# Notif Button Frame 
style notif_button_frame is clipped
style notif_button_frame: 

    # Fill to Contents
    xfill True 
    yfill True 
    # Remove Frame Background
    background None
    # Padding 
    padding(15, 10, 15, 10)
    # Center 
    xalign 0.5
    yalign 0.5

# Notif Button Content Container
style notif_button_hbox: 

    # Fill to Contents
    xfill True 
    yfill True 
    # Center Horizontally 
    xalign 0.5

# Notif Button Text Container
style notif_button_vbox: 
    # Center Horizontally 
    xalign 0.5 
    # Gap Between notif button text 
    spacing 10 

# Notif Button Text
style notif_button_text: 
    color "#000"
    size 15
    textalign 0.5
    # Center Horizontally 
    xalign 0.5

# Notif Button Title Text 
style notif_button_title is notif_button_text: 
    size 18
    bold True 

## Chat Notification Screen ####################################################
##
## This screen displays a chat notification pop up that doubles as 
## a button to open chat app

screen chat_app_notification(msg=1): 

    zorder 100

    use notif_button("chat_app", "Chat"):

        $ notif_det = ""

        if msg == 1: 

            $ notif_det = "1 New Message"

        else: 

            $ notif_det = "[msg] New Messages"

        text [notif_det] style "notif_button_text"

## Profile App screen ##########################################################
## 
## A screen that gives information about the player's current Player Name, 
## Wallet Location, as well as Rapport & Suspicion Stats

screen profile_app(): 

    tag app
    zorder 10
    modal True

    # App Screen Dimensions 
    $ window_width = 700
    $ window_height = 600
    $ content_width = 650
    $ content_height = 525

    # Profile Pic
    $ profile_pic_width = 100
    $ profile_pic_height = 100
    $ profile_pic_top_pad = 95

    $ app_title = "Profile"

    # Exit button unavailble warning. 
    # If on computer_ui_menu and Profile App exit button is disabled
    if renpy.get_screen("computer_ui_menu") and button_disabled(app_title): 
        use exit_disabled_warning(app_title)
    
    use app_screen(window_width, window_height, content_width, content_height, app_title):
                
        # Profile Info
        fixed: 
            style "profile_info"

            # Info Content Area
            add "gui/placeholders/Profile App Info Backdrop 1.svg":
                xysize(profile_section_width, profile_info_height)

            add "gui/placeholders/Profile App Info Backdrop 2.svg": 
                xysize(profile_section_width, 120)
                ypos 160 

            # Profile Pic
            add "gui/placeholders/Profile App Profile Pic Placeholder.svg":
                xysize(profile_pic_width, profile_pic_height)
                xpos profile_content_left_pad
                ypos profile_pic_top_pad

            # Profile ID
            vbox: 
                style "profile_id"

                text "[player_name]": 
                    style "profile_player_name_text"

                text "The Abyss Stares Back": 
                    style "profile_pen_name_text"

            # Deadline Reminder Widget
            fixed: 
                style "deadline_widget"

                add "gui/placeholders/Profile App Deadline Widget Placeholder.svg":
                    xysize(widget_width, widget_height)

                # Widget Content
                fixed:
                    style "deadline_widget_content"

                    # Calendar Icon Placeholder
                    add "#5E5E5E":
                        xysize(widget_content_height, widget_content_height)

                    # Text Column
                    fixed: 
                        style "deadline_widget_text"

                        # Label
                        fixed: 
                            style "deadline_widget_label"

                            text "Book Deadline":
                                style "deadline_widget_label_text"

                        # Detail
                        fixed:
                            style "deadline_widget_detail"

                            # In Badge
                            fixed: 
                                style "deadline_widget_in"

                                text "in":
                                    style "deadline_widget_in_text"

                            # Days Badge
                            fixed:
                                style "deadline_widget_days"

                                add "#000"

                                text "[deadline] days":
                                    style "deadline_widget_days_text"

        # Trackers
        fixed: 
            style "profile_trackers"

            # Wallet Tracker 
            fixed: 
                style "wallet_tracker"

                add "gui/placeholders/Profile App Wallet Tracker Background Placeholder.svg":
                    xysize(wallet_tracker_width, profile_trackers_height)

                # Wallet Tracker Content
                vbox: 
                    style "wallet_tracker_content"

                    # Title
                    text "Wallet":
                        style "wallet_tracker_title"

                    # Map Sprite
                    fixed: 
                        style "wallet_tracker_map"

                        add "#555":
                            xysize(wallet_tracker_map_width, wallet_tracker_map_height)

                        vbox: 
                            style "wallet_tracker_map_spotter"

                            add "#C8C8C8":
                                xysize(wallet_tracker_spotter_size, wallet_tracker_spotter_size)
                                xalign 0.5

                            text ("Nearby" if wallet_on_person else "Home"):
                                style "wallet_tracker_location_text"

            # Stat Tracker
            fixed: 
                style "stat_tracker"

                add "gui/placeholders/Profile App Stat Tracker Background Placeholder.svg":
                    xysize(stat_tracker_width, profile_trackers_height)

                # Stat Tracker Content
                vbox: 
                    style "stat_tracker_content"

                    # Suspicion Row
                    fixed: 
                        style "stat_tracker_row"

                        # Icon + Body
                        hbox:
                            style "stat_tracker_body"

                            add "#5E5E5E":
                                xysize(stat_tracker_row_icon_size, stat_tracker_row_icon_size)
                                yalign 1.0

                            vbox:
                                style "stat_tracker_row_body"

                                text "Suspicion":
                                    style "stat_tracker_row_label"

                                if suspicion is not None:
                                    bar:
                                        style "stat_tracker_row_bar"
                                        value StaticValue(suspicion, 10)
                                else:
                                    bar:
                                        style "stat_tracker_row_bar_locked"
                                        value StaticValue(0, 10)

                        # Value / Lock
                        fixed:
                            style "stat_tracker_row_value_container"

                            if suspicion is not None:
                                text "[suspicion]":
                                    style "stat_tracker_row_value"
                            else:
                                add "#666":
                                    xysize(stat_tracker_row_lock_size, stat_tracker_row_lock_size)
                                    xalign 1.0
                                    yalign 0.5

                    # Rapport Row
                    fixed: 
                        style "stat_tracker_row"

                        # Icon + Body
                        hbox:
                            style "stat_tracker_body"

                            add "#5E5E5E":
                                xysize(stat_tracker_row_icon_size, stat_tracker_row_icon_size)
                                yalign 1.0

                            vbox:
                                style "stat_tracker_row_body"

                                text "Rapport":
                                    style "stat_tracker_row_label"

                                if rapport is not None:
                                    bar:
                                        style "stat_tracker_row_bar"
                                        value StaticValue(rapport, 10)
                                else:
                                    bar:
                                        style "stat_tracker_row_bar_locked"
                                        value StaticValue(0, 10)

                        # Value / Lock
                        fixed:
                            style "stat_tracker_row_value_container"

                            if rapport is not None:
                                text "[rapport]":
                                    style "stat_tracker_row_value"
                            else:
                                add "#666":
                                    xysize(stat_tracker_row_lock_size, stat_tracker_row_lock_size)
                                    xalign 1.0
                                    yalign 0.5

# Profile App Styles 

# Profile Info Section
style profile_info is clipped

style profile_info: 
    xysize(profile_section_width, profile_info_height)
    xalign 0.5
    ypos profile_info_top_pad

# Profile ID Container
style profile_id is clipped

style profile_id: 
    xpos profile_content_left_pad
    ypos (profile_pic_top_pad + profile_pic_height)
    spacing 10

# Profile ID Texts
style profile_player_name_text is bolded

style profile_player_name_text: 
    size 20

style profile_pen_name_text: 
    size 18

# Deadline Widget
style deadline_widget is clipped

style deadline_widget: 
    xysize(widget_width, widget_height)
    xpos 365
    ypos 30

# Deadline Widget Content
style deadline_widget_content is clipped

style deadline_widget_content: 
    xysize(widget_content_width, widget_content_height)
    xpos 8
    yalign 0.5

# Deadline Widget Text Column
style deadline_widget_text is clipped

style deadline_widget_text: 
    xysize(widget_text_width, widget_content_height)
    xpos (widget_content_height + 10)

# Deadline Widget Label
style deadline_widget_label is clipped

style deadline_widget_label: 
    xysize(widget_text_width, widget_label_height)
    ypos widget_label_top_pad

style deadline_widget_label_text is bolded

style deadline_widget_label_text: 
    size 14
    color "#000000"
    xalign 0.5
    yalign 0.5

# Deadline Widget Detail
style deadline_widget_detail is clipped

style deadline_widget_detail: 
    xysize(widget_text_width, widget_detail_height)
    ypos (widget_label_top_pad + widget_label_height)
    xpos 15

# Deadline Widget In Badge
style deadline_widget_in is clipped

style deadline_widget_in: 
    xysize(widget_in_size, widget_in_size)

style deadline_widget_in_text: 
    size 12
    color "#000000"
    yalign 0.5
    xalign 0.5

# Deadline Widget Days Badge
style deadline_widget_days is clipped

style deadline_widget_days: 
    xysize(60, 20)
    xpos (widget_in_size + 5)

style deadline_widget_days_text: 
    size 12
    color "#C8C8C8"
    yalign 0.5
    xalign 0.5

# Trackers Section
style profile_trackers is clipped

style profile_trackers: 
    xysize(profile_section_width, profile_trackers_height)
    xalign 0.5
    ypos (profile_info_top_pad + profile_info_height + 19)

# Wallet Tracker
style wallet_tracker is clipped

style wallet_tracker: 
    xysize(wallet_tracker_width, profile_trackers_height)

# Wallet Tracker Content
style wallet_tracker_content is clipped

style wallet_tracker_content:
    xysize(wallet_tracker_content_width, wallet_tracker_content_height)
    xalign 0.5
    yalign 0.5
    spacing wallet_tracker_title_gap

# Wallet Tracker Title
style wallet_tracker_title is bolded
style wallet_tracker_title:
    xsize(wallet_tracker_content_width)
    ysize(wallet_tracker_title_height)
    textalign 0.5
    xalign 0.5
    size 20
    color "#C8C8C8"

# Wallet Tracker Map
style wallet_tracker_map is clipped
style wallet_tracker_map:
    xysize(wallet_tracker_map_width, wallet_tracker_map_height)

style wallet_tracker_map_spotter is clipped: 
    # Center Horizontally
    xalign 0.5
    # Push to the right about half way to the corner
    yalign 0.7
    # Spacing between spotter and Text
    spacing 4

# Wallet Tracker Location Text
style wallet_tracker_location_text is bolded
style wallet_tracker_location_text:
    size 14
    color "#C8C8C8"
    textalign 0.5
    xalign 0.5

# Stat Tracker
style stat_tracker is clipped
style stat_tracker: 
    xysize(stat_tracker_width, profile_trackers_height)
    xpos stat_tracker_left_pad

# Stat Tracker Content
style stat_tracker_content is clipped
style stat_tracker_content:
    xysize(stat_tracker_content_width, stat_tracker_content_height)
    xalign 0.5
    yalign 0.5
    spacing stat_tracker_row_gap

# Stat Tracker Row
style stat_tracker_row is clipped
style stat_tracker_row:
    xysize(stat_tracker_content_width, stat_tracker_row_height)

style stat_tracker_body:
    # Push to the right 
    yanchor 1.0
    # Match the bottom padding of icon 
    ypos stat_tracker_icon_bottom
    # Gap between rows
    spacing stat_tracker_row_icon_gap

# Stat Tracker Row Body
style stat_tracker_row_body is clipped
style stat_tracker_row_body:
    xsize(stat_tracker_row_body_width)
    yfit True
    # Spacing between Label and Bar
    spacing 2

# Stat Tracker Row Label
style stat_tracker_row_label is bolded
style stat_tracker_row_label:
    xsize(stat_tracker_row_body_width)
    size 16
    color "#C8C8C8"

# Stat Tracker Row Bar
style stat_tracker_row_bar:
    xsize(stat_tracker_row_body_width)
    ysize(stat_tracker_row_bar_height)
    left_bar gui.accent_color
    right_bar "#C8C8C8"

style stat_tracker_row_bar_locked is stat_tracker_row_bar:
    right_bar "#666"

# Stat Tracker Row Value Container
style stat_tracker_row_value_container is clipped
style stat_tracker_row_value_container:
    xysize(stat_tracker_row_value_width, stat_tracker_row_value_height)
    xalign 1.0
    yanchor 1.0
    ypos stat_tracker_icon_bottom

# Stat Tracker Row Value
style stat_tracker_row_value is bolded
style stat_tracker_row_value:
    xalign 1.0
    yalign 0.5
    size 16
    color "#C8C8C8"

## Chat App screen ####################################################################
## 
## A screen that stores away Chats between the Player Character & other 
## Characters which serve as a part of the narrative

screen chat_app(): 

    tag app 
    zorder 10 
    modal True 

    on "hide" action If(_in_chat_block, false=SetVariable("active_contact", None)), If(_in_chat_block, false=Function(nvl_clear))

    # App Screen Dimensions 
    $ window_width = 900
    $ window_height = 600
    $ content_width = 850
    $ content_height = 525
    $ contact_panel_content_bot_pad = contact_panel_gap
    $ contact_panel_content_top_pad = contact_panel_gap
    $ contact_panel_content_width = contact_button_width
    $ contact_panel_content_height = contact_panel_height - contact_panel_content_bot_pad - contact_panel_content_top_pad

    $ app_title = "Chat"

    # Exit button unavailble warning. 
    # If on computer_ui_menu and Profile App exit button is disabled
    if renpy.get_screen("computer_ui_menu") and button_disabled(app_title): 
        use exit_disabled_warning(app_title)

    use app_screen(window_width, window_height, content_width, content_height, app_title):

        fixed: 

            style "chat_app"

            # Contact Panel 
            fixed: 
                style "contact_panel"
            
                add "gui/placeholders/Contact Panel Background Placeholder.svg":
                    xysize(contact_panel_width, contact_panel_height)

                fixed: 
                    xysize(contact_panel_content_width, contact_panel_content_height)
                    xalign 0.5
                    yalign 0.5

                    # Contact List
                    use scrollable_content("vpgrid", spacing=contact_panel_gap, scrollbars=None, vp_width=contact_panel_content_width, vp_height=contact_panel_content_height): 

                        # And (Theo) - Contact Button 
                        use contact_button("And", tooltip=tooltip_content["chat_t"])

                        # At You (Victor) - Contact Button 
                        use contact_button("At You", tooltip=tooltip_content["chat_v"])

                        # Golden Manager - Contact Button 
                        use contact_button("Golden Manager", tooltip=tooltip_content["chat_l"])

                        # The Abyss Stares Back (Player) - Contact Button 
                        use contact_button("The Abyss Stares Back", tooltip=tooltip_content["chat_c"])

                        # Stare Into The Abyss - Contact Button
                        use contact_button("Stare Into The Abyss", tooltip=tooltip_content["chat_m"])

            # Chat Box
            fixed: 
                style "chat_box"

                add "gui/placeholders/Chat Box Background Placeholder.svg":
                    xysize(chat_box_width, chat_box_height)

                if active_contact: 
                    use chat_box(active_contact)

# Chat App Styles 

# Chat App Main Content Container
style chat_app is clipped

style chat_app: 
    xysize(contact_panel_width + chat_box_width + contact_panel_gap, contact_panel_height)
    # Left Padding
    xpos chat_app_pad
    # Top Padding 
    ypos chat_app_pad

# Chat Contact Panel Container 
style contact_panel is clipped

style contact_panel: 
    xysize(contact_panel_width, contact_panel_height)

# Chat Box Container 
style chat_box is clipped 

style chat_box: 
    xysize(chat_box_width, chat_box_height)
    # Left Padding 
    xpos (contact_panel_width + contact_panel_gap)

## Contact Button Template ############################################################
## 
## A template screen for contact buttons, which will activate the chat box for contact

screen contact_button(name, avatar="#808080", tooltip=None): 

    $ online = False # Implement Disabler / Enabler later

    $ contact_profile_width = 60 
    $ contact_profile_height = contact_profile_width
    $ contact_profile_top_pad = 5
    $ online_status_dot_width = 6 
    $ online_status_dot_height = online_status_dot_width

    button: 

        id name

        style "contact_button"

        if tooltip: 
            tooltip tooltip

        # Disable Button if disablers are on and screen is not Computer UI Menu
        if button_disabled(name):

            action NullAction()
            
        else: 

            action SetVariable("active_contact", name), If(_in_chat_block, false=Function(nvl_clear))

        add "gui/placeholders/Contact Item Background.svg": 
            xysize(contact_button_width, contact_button_height)

        # Contact Button Content 
        hbox: 
            style_prefix "chat_contact"
            style "chat_contact_profile_name"

            # Contact Profile
            add avatar: 
                ypos contact_profile_top_pad
                xysize(contact_profile_width, contact_profile_height)

            # Contact Name
            fixed: 

                text name

        if online: 
            $ online_status = "online"
            $ color = gui.accent_color
        else: 
            $ online_status = "offline"
            $ color = gui.idle_color

        # Online Status Text Container 
        fixed: 
            style "chat_online_status"

            add "#000": 
                xysize (contact_status_width, contact_status_height)

            add "gui/placeholders/Profile App Profile Pic Placeholder.svg": # Make dot color based on 'color' with final asset
                xysize(online_status_dot_width, online_status_dot_height)
                yalign 0.5
                xpos contact_status_xpad

            text online_status: 
                style "chat_online_status_text"
                color color

# Contact Button Styles

style chat_online_status_text is bolded 

style chat_online_status_text: 
    # Push to the right of container 
    xalign 1.0
    # Right Padding 
    xoffset -(contact_status_xpad)
    # Center vertically 
    yalign 0.5 
    # Text size 
    size 10 

# Contact Button Container 
style contact_button is clipped 

style contact_button: 
    xysize(contact_button_width, contact_button_height)
    xalign 0.5 

# Chat Contact Button Container 
style chat_contact is clipped
style chat_contact: 
    # Left Padding 
    xpos 15
    # Center Vertically
    yalign 0.5 
    # Gap Between Contact Avatar & Name
    spacing 15

# Chat Contact Button Text 
style chat_contact_text is bolded 
style chat_contact_text: 
    xalign 0.5
    size 16
    color "#000"
    textalign 0.5

# Chat Contact Contact Name Container 
style chat_contact_fixed is clipped
style chat_contact_fixed: 

    xysize (100, 70)

style chat_contact_profile_name is chat_contact

style chat_online_status is chat_contact 

style chat_online_status: 
    xysize (contact_status_width, contact_status_height)
    xalign 0.95
    yalign 0.95

## Chat Box Template ###########################################################
##
## Screen Template for an active Chat Box inside Chat App. 

screen chat_box(contact):

    ## Chat Box Header 
    fixed: 

        style "chat_box_header"

        add "gui/placeholders/Chat Box Header.svg": 
            xysize(chat_box_header_width, chat_box_header_height)

        text contact: 
            style "chat_box_header_text"

    ## Main Content Area
    fixed: 

        style "chat_box_content"

        fixed: 
            style "chat_box_bubble_content"

            # Chat Content 
            use scrollable_content("viewport", spacing=15, scrollbars=None, yinitial=1.0, yadjustment=adj):
                
                # Chat Buffer ? 

                # Chat History 
                for entry in get_chat_entries(contact): 

                    # Timestamp marker
                    if isinstance(entry, dict): 
                        if entry["type"] == "date": 
                            use chat_date_stamp(entry["value"])
                        else: 
                            use chat_time_stamp(entry["value"])

                    # Messages
                    else: 
                    
                        use chat_bubble(entry.who, entry.what)

                # Live Chat
                if nvl_list:
                    
                    # Print Chat Date
                    if _chat_date_change: 
                        use chat_date_stamp(abyss_date.strftime("%a %b %d"))

                    # Print Chat Time 
                    use chat_time_stamp(abyss_time)
                    
                    # Print Chat Bubbles
                    for entry in nvl_list: 
                        use chat_bubble(entry[0], entry[1])
                    
    # Keyboard Field

    fixed: 
        style "chat_box_keyboard"
        clipping True

        
        add "gui/placeholders/Keyboard Bubble.svg":
            ypos 5
            xysize(chat_box_key_width, chat_box_key_height)

# Chat Box Styles 

style chat_box_header is clipped
style chat_box_header:
    xysize(chat_box_header_width, chat_box_header_height)

style chat_box_header_text is bolded
style chat_box_header_text: 
    # Center
    xalign 0.5 
    yalign 0.5 
    # Text Size
    size 25

style chat_box_content is clipped
style chat_box_content: 
    xysize(chat_box_content_width, chat_box_content_height)
    ypos chat_box_content_top_pad

style chat_box_bubble_content: 
    xysize(chat_box_bubble_content_width, chat_box_bubble_content_height)
    xalign 0.5 
    yalign 0.5 

style chat_box_keyboard: 
    xysize(chat_box_key_width, chat_box_key_height)
    xalign 0.5
    yanchor 1.0 
    ypos (chat_box_height - 15)


## Chat Bubble screen ##########################################################
##
## A screen that displays a script line tied to a nvl type character 

screen chat_bubble(who, what): 

    $ is_sent = (who == chat_c.name)
    $ bubble = "gui/placeholders/Chat Bubble (Sent).svg" if is_sent else "gui/placeholders/Chat Bubble (Receive).svg"
    $ bubble_text_color = "#000" if is_sent else "#C8C8C8"
    $ xalign = 1.0 if is_sent else 0


    frame: 

        style "chat_bubble_frame"

        xalign xalign

        background Frame(bubble, 4, 4, 4, 4)

        # Chat Bubble Text Container
        fixed: 
            style "chat_bubble_content"

            text what: 
                style "chat_bubble_text"
                color bubble_text_color

# Chat Bubble Styles

style chat_bubble_frame is clipped 
style chat_bubble_frame: 
    xsize chat_bubble_width
    padding (20, 10, 20, 10)

style chat_bubble_content is clipped 
style chat_bubble_content:
    xsize chat_bubble_text_height
    yfit True

style chat_bubble_text: 
    xsize chat_bubble_text_height
    size 16 

## Chat Timestamp template for chat ############################################
##
## A screen that displays a date stamp

screen timestamp_for_chat(stamp): 

    frame: 

        style "chat_stamp_frame"

        # Timestamp Text Container
        fixed: 
            
            style "chat_stamp_fixed"

            text stamp: 
                style "chat_stamp_text"

# Timestamp Styles 

# Chat Stamp Frame
style chat_stamp_frame is clipped
style chat_stamp_frame: 
    # Height of stamp 
    ysize stamp_frame_height 
    # Center
    xalign 0.5
    yalign 0.5
    # Padding 
    padding (stamp_frame_pad, stamp_frame_pad, stamp_frame_pad, stamp_frame_pad)

    background "#C8C8C8" 

# Chat Stamp Content Container 
style chat_stamp_fixed is clipped
style chat_stamp_fixed:
    # Height of Content Container
    ysize stamp_content_height
    # Fill Content Width
    xfit True
    # Center 
    xalign 0.5
    yalign 0.5

# Chat Stamp Text
style chat_stamp_text is bolded 
style chat_stamp_text: 

    # Match to stamp content container 
    ysize stamp_content_height
    # Align Text
    textalign 0.5
    size 14
    color "#000"

## Chat Datestamp screen #######################################################
##
## A screen that displays a date stamp for chat

screen chat_date_stamp(date): 

    use timestamp_for_chat(date)

## Chat Timestamp screen #######################################################
## 
## A screen that displays a time stamp for chat

screen chat_time_stamp(time): 

    use timestamp_for_chat(time)

# Draft Scroll
default draft_adj = ui.adjustment()

## Draft App screen ############################################################
## 
## A screen that lets the player view the progress of the Epilogue Draft 
## the Player Character is writing on throughout the game

screen draft_app(): 

    tag app 
    zorder 10 
    modal True 

    $ app_title = "Draft"

    # Exit button unavailble warning. 
    # If on computer_ui_menu and Profile App exit button is disabled
    if renpy.get_screen("computer_ui_menu") and button_disabled(app_title): 
        use exit_disabled_warning(app_title)

    use app_screen(draft_window_width, draft_window_height, draft_scroll_width, draft_scroll_height, app_title, "draft_tools"): 

        frame: 
            style "draft_app_frame"

            # Fake sense that there is something to scroll up to but don't make it actually scroll 
                # Maybe make the scroll bar look like it's already somewhat scrolled ? 
                # Or instead of scroll do something like make it look like chapters have been drafted in different files 
                    # Only file you (player) has access to is the epilogue 
                    # But all the other chapters are there you just can't click 
                    # could be implemented into tool bar for draft_app 
                        # Needs a little concept redesigning to work though 
                        # or maybe not too much... maybe can just add a related icon with implication
                            # maybe like hover on the icon will show other files ...

            use draft_file()

# Draft App Styles

style draft_app_frame is clipped 

style draft_app_frame: 
    xsize draft_frame_width
    ysize (draft_header_height + draft_content_height)
    background None 
    padding (10, 9, 10, 9)

## Draft File Template #########################################################
##
## Screen Template for an active Draft File inside Draft App.

screen draft_file(log_name="epilogue", book_title="To Be Or Not To Be", book_abrv="tbontb"): 

    # Chapter Title from log_name
    # ex. (default log_name) 
    #   chapter_title = "Epilogue"
    $ chapter_title = log_name[0].upper() + log_name[1:]

    # File Name from book_abrv and log_name 
    # ex. (default book_abrv and default log_name) 
    #   file_name = "tbontb_epilogue_transcript"
    $ file_name = book_abrv + "_" + log_name + "_transcript"

    $ paragraph_gap = 20 
    $ content_top_pad = 15
    $ content_bot_pad = content_top_pad
    $ content_left_pad = 10
    $ content_right_pad = content_left_pad

    # Display Fixed Chapter Title Header
    fixed: 
        style "draft_file_header"

        # Book Chapter Title 
        # ex. (default book_title & default chapter_title) 
        #   "To Be Or Not To Be - Epilogue"
        text (book_title + " - " + chapter_title): 
            style "draft_title_text"

        # Auto Scroll
        hbox:
            style "auto_scroll_hbox"

            # Scroll to top 
            imagebutton: 

                idle "#000"
                style "scroll_button"

                action Function(scroll_top, draft_adj)

                tooltip "Scroll to top"

            # Scroll to bottom 
            imagebutton: 

                idle "#000"
                style "scroll_button"

                action Function(scroll_bottom, draft_adj)

                tooltip "Scroll to bottom"

    # Scrollable Content 
    fixed: 
        style "draft_file_content" 

        if _book_transcript.get(log_name, []): 

            # Book Transcript 
            $ transcript = print_transcript(log_name)
            
            use scrollable_content("viewport", spacing=paragraph_gap, top_pad=content_top_pad, bottom_pad=content_bot_pad, left_pad=content_left_pad, right_pad=content_right_pad, yinitial=1.0, yadjustment=draft_adj): 

                for paragraph in transcript: 

                    text paragraph: 
                        style "draft_file_paragraph"


style draft_file_header is clipped
style draft_file_header: 
    xysize(draft_header_width, draft_header_height)

style draft_title_text is bolded
style draft_title_text: 
    # Center
    xalign 0.5 
    yalign 0.5 
    color "#000"
    size 22

style auto_scroll_hbox: 
    # Scooch to the right 
    xalign 1.0 
    # Center vertically 
    yalign 0.5 
    # Spacing between auto scroll buttons 
    spacing 2

style scroll_button: 
    xysize(scroll_button_width, scroll_button_height)

style draft_file_content is clipped
style draft_file_content: 
    xysize(draft_content_width, draft_content_height)
    # Top Padding
    ypos draft_header_height

style draft_file_paragraph: 
    color "#000"
    size 18
    xfill True 

## Draft Tools screen ##########################################################
## 
## A screen that displays Draft App Tools
## Decorative (for now)

screen draft_tools(): 

    tag tools

    fixed: 
        xysize(draft_window_width, draft_window_height - app_header_height)
        ypos app_header_height
        clipping True

        # Top Toolbar
        fixed: 
            style "toolbar"

            add "gui/placeholders/Draft Toolbar Placeholder.svg": 
                xysize (draft_toolbar_width, draft_toolbar_height)

            frame: 
                style "toolbar_frame"

                fixed: 
                    xysize(draft_toolbar_content_width, draft_toolbar_content_height)
                
                    # Mode Switch Icons
                    hbox: 
                        style "mode_switch_icons"

                        # Edit Icon
                        imagebutton: 
                            idle "#000"
                            style "edit_icon"

                            action NullAction()

                            tooltip "Edit Mode"
                            
                        # Read Icon
                        imagebutton: 
                            idle "#000"
                            style "read_icon"

                            action NullAction()

                            tooltip "View Mode"

                    # Misc Icons
                    hbox: 
                        style "misc_icons"

                        # Clipboard Icon
                        imagebutton: 
                            idle "#000"
                            style "cp_icon"

                            action NullAction()

                            tooltip "Copy & Paste"
                        
                        # Scissor Icon 
                        imagebutton:
                            idle "#000"
                            style "cut_icon"

                            action NullAction()

                            tooltip "Cut"

                        # Microphone Icon 
                        imagebutton:
                            idle "#000"
                            style "mic_icon"

                            action NullAction()

                            tooltip "Voice Recordings"

                        # Printer Icon 
                        imagebutton:
                            idle "#000"
                            style "print_icon"

                            action NullAction()

                            tooltip "Print"

                        # Airplane Icon
                        imagebutton: 
                            idle "#000"
                            style "share_icon"

                            action NullAction()

                            tooltip "Share"

                        # Three Dots Icon 
                        imagebutton: 
                            idle "#000"
                            style "more_icon"

                            action NullAction()

                            tooltip "Expand Toolbar Options"
                        
                    # Open Files Icons
                    hbox: 
                        style "open_files_icons"

                        # Folder Icon 
                        imagebutton: 
                            idle "#000"
                            style "folder_icon"

                            action NullAction()

                            tooltip "Choose Folder"

                        # File Icon 
                        imagebutton: 
                            idle "#000"
                            style "file_icon"

                            action NullAction()

                            tooltip "Choose File"
                        

        # Bottom Settings Bar
        fixed: 
            style "settings_bar"

            add "gui/placeholders/Draft Settings Bar Placeholder.svg": 
                xysize (draft_settings_bar_width, draft_settings_bar_height)

            frame: 
                style "settings_bar_frame"

                fixed: 
                    xysize(draft_settings_bar_content_width, draft_settings_bar_content_height)

                    # Save Icons 
                    hbox: 
                        style "save_icons"

                        # Save Mode Icon
                        imagebutton: 
                            idle "#c8c8c8"
                            style "save_mode_icon"

                            action NullAction()

                            tooltip "Save Mode"

                        # Save Status Icon 
                        imagebutton: 
                            idle "#c8c8c8"
                            style "save_status_icon"

                            action NullAction()

                            tooltip "Save Status"

                    # Star Icons
                    hbox: 
                        style "star_icons"

                        # Star Icon 
                        imagebutton: 
                            idle "#c8c8c8"
                            style "starred_icon"

                            action NullAction()

                            tooltip "Bookmark"

                    # Settings Icons
                    hbox: 
                        style "option_icons"

                        # Gear Icon
                        imagebutton: 
                            idle "#c8c8c8"
                            style "gear_icon"

                            action NullAction()

                            tooltip "Settings"

# Draft Tools Styles 

# Toolbar Styles 
style toolbar is clipped
style toolbar: 
    xsize draft_toolbar_width
    ysize 30 # Change to draft_toolbar_height once placeholder is gone and value is fixed in variable

style settings_bar is toolbar: 
    ysize draft_settings_bar_height 
    yalign 1.0

style toolbar_frame is clipped
style toolbar_frame: 

    xysize(draft_toolbar_content_width, draft_toolbar_content_height)
    padding (0, 0, 0, 0)
    xalign 0.5
    background None

style settings_bar_frame is toolbar_frame
style settings_bar_frame: 

    xysize(draft_settings_bar_content_width, draft_settings_bar_content_height)

# Toolbar Icons 
style toolbar_icon: 
    xsize 18
    ysize 20

style edit_icon is toolbar_icon

style read_icon is toolbar_icon
style read_icon: 
    xsize 30

style cp_icon is toolbar_icon

style cut_icon is toolbar_icon
style cut_icon: 
    xsize 25

style mic_icon is toolbar_icon
style mic_icon: 
    xsize 16

style print_icon is toolbar_icon
style print_icon: 
    xsize 27

style share_icon is toolbar_icon
style share_icon: 
    xsize 22

style more_icon is toolbar_icon
style more_icon: 
    xsize 20

style folder_icon is toolbar_icon

style file_icon is toolbar_icon
style file_icon: 
    xsize 60

# Settings Icons 
style settings_icon: 
    xsize 20
    ysize 20

style save_mode_icon is settings_icon
style save_mode_icon: 
    xsize 80

style save_status_icon is settings_icon

style starred_icon is settings_icon
style starred_icon: 
    xysize(22, 22)

style gear_icon is settings_icon
style gear_icon: 
    xysize(30, 30)

# Toolbar Icon Tuples
style toolbar_icon_tuple: 
    ysize 20
    spacing 10
    xfit True
    yalign 0.5

style mode_switch_icons is toolbar_icon_tuple

style misc_icons is toolbar_icon_tuple
style misc_icons: 
    # Edit Icon (18) + Spacing (10) + Read Icon (30) + Gap Between Tuple [mode_switch_icons & misc_icons] (80)
    xpos (18 + 10 + 30 + 80)

style open_files_icons is toolbar_icon_tuple
style open_files_icons: 
    xalign 1.0

# Setting Icons Tuples
style settings_icon_tuple: 
    ysize 30
    spacing 10 
    xfit True 
    yalign 0.5

style save_icons is settings_icon_tuple
style save_icons: 
    ysize 20

style star_icons is settings_icon_tuple
style star_icons: 

    ysize 22
    # Save Mode Icon (80) + Spacing (10) + Save Status Icon (20) + Gap Between Tuple [save_icons & star_icons] (40)
    xpos (80 + 10 + 20 + 40)

style option_icons is settings_icon_tuple
style option_icons: 
    xalign 1.0

################################################################################
## Special Game Mode screens
################################################################################

## Bedroom Screen ##############################################################
## 
## Interactable Background / Scene for Prep Phase Game Mode

screen bedroom(click_map={}): 
    
    tag game 

    fixed:
        style "bedroom"

        # Walls - Backdrop
        add "images/placeholders/bedroom_walls_v1.png":
            xysize(config.screen_width, config.screen_height)

        # Bookshelf
        add "images/placeholders/bedroom_bookshelf_v1.png":
            xysize(342, 508)
            # Horizontal Positioning
            xpos 928
            # Vertical Positioning
            ypos 17

        # Wardrobe - Closet Click
        if "closet" in click_map: 
            $ closet_script = click_map["closet"]
            $ closet_interact = Function(open_wardrobe, click_map)
        else: 
            $ closet_script = None
            $ closet_interact = None
        
        use bedroom_interactable(sprite="images/placeholders/bedroom_wardrobe_v1.png", xsize=294, ysize=470, xpos=114, ypos=62, tooltip="Wardrobe", script=closet_script, interact=closet_interact, closet_prep=True)

        # Desk + Items
        fixed:
            # Horizontal Positioning
            xpos 397
            # Vertical Positioning
            ypos 117

            add "images/placeholders/bedroom_desk_v1.png":
                xysize(546, 432)

            # Wallet - Wallet Click
            if not wallet_on_person:
                if "wallet" in click_map:
                    $ wallet_script = click_map["wallet"]
                else: 
                    $ wallet_script = None

                use bedroom_interactable(sprite="images/placeholders/bedroom_wallet_v1.png", xsize=37, ysize=19, xpos=67, ypos=183, tooltip="Wallet", script=wallet_script)

            # Key - Key Click
            if "key" in click_map:
                $ key_script = click_map["key"]
            else: 
                $ key_script = None

            use bedroom_interactable(sprite="images/placeholders/bedroom_key_v1.png", xsize=12, ysize=14, xpos=103, ypos=212, tooltip="Key", script=key_script)

            # Laptop - Laptop Click
            if not laptop_clicked:
                if "laptop" in click_map:
                    $ laptop_script = click_map["laptop"]
                    $ laptop_interact = SetVariable("laptop_clicked", True)
                else: 
                    $ laptop_script = None
                    $ laptop_interact = None
            
                use bedroom_interactable(sprite="images/placeholders/bedroom_laptop_v1.png", xsize=142, ysize=102, xpos=369, ypos=106, tooltip="Laptop", script=laptop_script, interact=laptop_interact)

        # Chair
        add "images/placeholders/bedroom_chair_v1.png":
            xysize(142, 323)
            # Horizontal Positioning
            xpos 600
            # Vertical Positioning
            ypos 283

        # Bed - Bed Click
        if "bed" in click_map:
            $ bed_script = click_map["bed"]
        else:
            $ bed_script = None

        use bedroom_interactable(sprite="images/placeholders/bedroom_bed_v1.png", xsize=964, ysize=173, xpos=88, ypos=740, yanchor=1.0, tooltip="Bed", script=bed_script)

# Bedroom Styles 

style bedroom is full_screen

## Bedroom Interactable Template ###############################################
##
## A screen template for interactable objects in the bedroom scene.

screen bedroom_interactable(sprite, xsize, ysize, xpos, ypos, xanchor=0.0, yanchor=0.0, tooltip=None, script=None, interact=None, closet_prep=False):

    if script: 

        if closet_prep: 
            $ call_script = call_prep_closet_script
        else:
            $ call_script = call_prep_script

        if interact: 

            $ action = (interact, Function(call_script, script))

        else: 

            $ action = Function(call_script, script)

    imagebutton: 

        idle sprite 

        xysize(xsize, ysize)

        # Horizontal Positioning Anchor
        xanchor xanchor

        # Horizontal Positioning
        xpos xpos

        # Vertical Positioning Anchor
        yanchor yanchor

        # Vertical Positioning
        ypos ypos

        if tooltip:
            tooltip tooltip

        if script is None:
            sensitive False 

        if button_disabled("prep_busy"): 

            action NullAction() 
        
        else: 

            if script: 

                action action 

# Delete later
image wardrobe_option = Transform("gui/placeholders/Chat Bubble (Receive).svg", xsize=180, ysize=120)
image wardrobe_option_selected = Transform("gui/placeholders/Chat Bubble (Sent).svg", xsize=180, ysize=120)

## Wardrobe Panel ##############################################################
##
## Panel Screen for Closet Click in Bedroom Prep Phase 

screen wardrobe_panel(click_map={}): 

    modal True 

    # Change into hover img for each button later (with each buttons selected variable conditional)
    $ hover_dress_shirt = "wardrobe_option" if not semiformal_top else "wardrobe_option_selected"
    $ hover_turtle_neck = "wardrobe_option" if not contour_top else "wardrobe_option_selected"
    $ hover_cargo_pants = "wardrobe_option" if not many_pockets else "wardrobe_option_selected"
    $ hover_dress_jeans = "wardrobe_option" if not heavy_pants else "wardrobe_option_selected"

    frame: 
        style "wardrobe_panel_frame"

        # Background 
        add "#C8C8C8":
            xysize(wardrobe_panel_width, wardrobe_panel_height)
            xalign 0.5 
            yalign 0.5

        vbox: 

            hbox:
                style "wardrobe_panel_hbox"

                ## Tops (Left Column)
                vbox:
                    style "wardrobe_panel_vbox"

                    ## Top Option 1 - Dress Shirt (Semiformal)
                    if "dress_shirt" in click_map:
                        $ dress_shirt_script = click_map["dress_shirt"]
                    else: 
                        $ dress_shirt_script = None

                    use clothing_sprite("dress_shirt", "wardrobe_option", hover_dress_shirt, "wardrobe_option_selected", dress_shirt_script, tooltip_content["dress_shirt"])

                    ## Top Option 2 - Turtle Neck (Contour)
                    imagebutton:
                        idle "wardrobe_option"
                        hover hover_turtle_neck
                        selected_idle "wardrobe_option_selected"

                        selected contour_top
                        
                        tooltip tooltip_content["thin_turtle_neck"]

                        if button_disabled("closet_busy"): 
                            action NullAction()

                        else: 

                            if "turtle_neck" in click_map: 

                                action (If(semiformal_top, SetVariable("semiformal_top", False)), SetVariable("contour_top", True), SetVariable("top_selected", True), Function(call_prep_closet_script, click_map["turtle_neck"]))

                ## Bottoms (Right Column)
                vbox:
                    style "wardrobe_panel_vbox"

                    ## Bottom Option 1 - Cargo Pants (Many Pockets)
                    imagebutton:
                        idle "wardrobe_option"
                        hover hover_cargo_pants
                        selected_idle "wardrobe_option_selected"

                        selected many_pockets

                        tooltip tooltip_content["lightweight_cargo_pants"]
                        
                        if button_disabled("closet_busy"): 
                            action NullAction()

                        else: 
                            if "cargo_pants" in click_map:
                                action (If(heavy_pants, SetVariable("heavy_pants", False)), SetVariable("many_pockets", True), SetVariable("bottom_selected", True), Function(call_prep_closet_script, click_map["cargo_pants"]))

                    ## Bottom Option 2 - Dress Jeans (Heavy Pants)
                    imagebutton:
                        idle "wardrobe_option"
                        hover hover_dress_jeans
                        selected_idle "wardrobe_option_selected"

                        selected heavy_pants

                        tooltip tooltip_content["dress_jeans"]

                        if button_disabled("closet_busy"): 
                            action NullAction()

                        else: 
                            if "dress_jeans" in click_map:
                                action (If(many_pockets, SetVariable("many_pockets", False)), SetVariable("heavy_pants", True), SetVariable("bottom_selected", True), Function(call_prep_closet_script, click_map["dress_jeans"]))

            ## Done Button
            textbutton "Dressed":
                style "wardrobe_panel_dressed_button"
                sensitive (top_selected and bottom_selected)

                if button_disabled("closet_busy"): 
                    action NullAction()
                
                else:
                    if "dressed" in click_map:
                        action (SetVariable("closet_clicked", True), Function(close_wardrobe), Function(call_prep_script, click_map["dressed"]))

# Wardrobe Panel Styles 

# Wardrobe Panel Container 
style wardrobe_panel_frame is clipped
style wardrobe_panel_frame: 
    xysize(wardrobe_panel_width, wardrobe_panel_height)
    # Center 
    xalign 0.5
    yalign 0.5
    padding(wardrobe_panel_spacing, wardrobe_panel_spacing)
    background None

# Wardrobe Panel Content Container 
style wardrobe_panel_hbox is clipped
style wardrobe_panel_hbox: 
    xysize(380, 260)
    # Spacing between Columns
    spacing wardrobe_panel_spacing

# Wardrobe Panel Column 
style wardrobe_panel_vbox: 
    spacing wardrobe_panel_spacing

# Wradrobe Panel Dressed Button
style wardrobe_panel_dressed_button: 
    # Push to bottom
    yalign 1.0


## Clothing Sprite #############################################################
##
## A screen that displays the wardrobe clothing sprite as a button for the player 
## to click on in the bedroom scene.

screen clothing_sprite(sprite_name, idle_sprite, hover_sprite, selected_sprite, script, tooltip=None):

    $ category, flag = get_clothing_info(sprite_name)

    if script:
        $ other_flags = get_same_category_flags(sprite_name)
        $ disable_flags = [SetVariable(f, False) for f in other_flags]

        $ flag_selected = SetVariable(flag, True)

        $ selected_category = SetVariable(category + "_selected", True)

        $ call_script = Function(call_prep_closet_script, script)

        $ action = (disable_flags, flag_selected, selected_category, call_script)

    imagebutton: 
        idle idle_sprite
        hover hover_sprite
        selected_idle selected_sprite

        selected eval(flag)

        if tooltip:
            tooltip tooltip
        
        if script is None: 
            sensitive False

        if button_disabled("closet_busy"):

            action NullAction()
        else:

            if script: 

                action action

################################################################################
## Cosmetic Screens
################################################################################

## Computer UI - Lock screen ###################################################
##
## A screen that displays in-game date & in-game time a step before the 
## Computer UI (Main Screen) within game narrative. 

screen computer_ui_locked(): 

    tag cosmetic 

    $ content_width = 430
    $ content_height = 600
    $ date_time_container_width = 160
    $ profile_lock_container_width = 270 
    $ profile_lock_container_height = 270 
    $ profile_lock_inner_width = 160 
    $ profile_lock_inner_height = 160
    $ locked_icon_width = 30
    $ locked_icon_height = 35

    fixed: 

        style "computer_ui_locked"

        add "#797979"

        # Screen Content
        vbox: 

            style "computer_ui_locked_vbox"
            xysize(content_width, content_height)

            # Date & Time
            fixed:
                style "computer_lock_datetime_container"

                xysize(content_width, date_time_container_width)

                add "#C8C8C8": 
                    xysize(content_width, date_time_container_width)

                vbox: 
                    style "computer_lock_datetime_vbox"

                    text abyss_date.strftime("%A, %B %d"): 
                        style "computer_lock_date"
                        
                    text abyss_time: 
                        style "computer_lock_time"
                        

            # Profile & Lock
            fixed: 

                style "computer_ui_locked_profile_container"

                xysize(profile_lock_container_width, profile_lock_container_height)

                vbox: 

                    style "computer_ui_locked_profile_vbox"

                    xysize(profile_lock_container_width, profile_lock_container_height)

                    # Profile
                    vbox: 

                        style "computer_ui_locked_profile"

                        xysize(profile_lock_container_width, profile_lock_inner_height)

                        # Profile Pic
                        add "#000":
                            xysize(profile_lock_inner_width, profile_lock_inner_height)
                            xalign 0.5
                            

                        text "[player_name]":
                            style "computer_ui_locked_name"
                            
                    # Lock
                    add "#000": 
                        xysize(locked_icon_width, locked_icon_height)
                        xalign 0.5

# Computer UI Locked Styles

# Computer UI Lock Screen
style computer_ui_locked is full_screen: 
    clipping True

# Computer UI Lock Screen Main Content
style computer_ui_locked_vbox is clipped
style computer_ui_locked_vbox: 
    # Center Horizontally
    xalign 0.5
    # Spacing between Date-Time and Profile-Lock
    spacing 120
    # Top Padding 
    ypos 95

# Computer UI Lock Screen Date & Time Container 
style computer_lock_datetime_container is clipped
style computer_lock_datetime_vbox: 
    # Center
    xalign 0.5 
    yalign 0.5 
    spacing 10 # Spacing between Date & Time 

# Computer UI Lock Screen Text
style computer_lock_text: 
    color "#000"
    size 30
    xalign 0.5 

# Computer UI Lock Screen Date Text
style computer_lock_date is computer_lock_text

# Computer UI Lock Screen Time Text
style computer_lock_time is computer_lock_text

style computer_lock_time: 
    size 60

# Computer UI Lock Screen Profile Container
style computer_ui_locked_profile_container is clipped 

style computer_ui_locked_profile_container: 
    xalign 0.5 

# Computer UI Lock Screen Profile Inner Container 
style computer_ui_locked_profile_vbox is clipped

style computer_ui_locked_profile_vbox: 
    # Spacing between Profile & Lock 
    spacing 30

# Computer UI Lock Screen Profile
style computer_ui_locked_profile is clipped

style computer_ui_locked_profile: 
    # Spacing between Profile Pic and Player Name
    spacing 10 

# Computer UI Lock Screen Lock
style computer_ui_locked_name is computer_lock_text

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#C8C8C8"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

## NVL is used exclusively for Chat in this project. 
## Visually Hidden with nvl_dialogue kept for required Text object by Ren'Py

screen nvl(dialogue, items=None):


    window:
        style "nvl_window"
        background None
        

        has vbox: 
            spacing gui.nvl_spacing 

        use nvl_dialogue(dialogue) 

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background None
    padding (0, 0, 0, 0)

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    color "#00000000"
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 870

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    top_margin 20 
    bottom_margin 20

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600