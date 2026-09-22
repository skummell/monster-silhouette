## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE   

################################################################################
## Initialization
################################################################################

init offset = -1

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


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

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

## Status Bar (Custom Screen) ##################################################
## This screen is only included in-game and provides you with the
## in-game date and time
screen status_bar(): 

    frame: 
        at fill_width(38)
        background None
        padding(0, 0)
        margin(0, 0)

        clipping True

        add "gui/placeholders/status_bar_placeholder.svg": 
            at fill_width(38)

# Fill Screen Transform
transform fill_screen: 
    xysize (config.screen_width, config.screen_height)
    fit "fill"

# Fill Width Transform
transform fill_width(height=38): 
    xysize (config.screen_width, height)
    fit "fill"

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

## Navigation Dock - Custom In-Game Navigation Screen ##########################
## Similar to the Navigation Screen, this screen provides navigation
## to other menus.

screen navigation_dock(): 

    zorder 2
    
    # Dock Icons (6 icons)
    grid 6 1: 
        xalign 0.5
        ypos 640
        spacing 30 

        # History - Icon Button 
        imagebutton:
            idle "gui/placeholders/dock_icon_placeholder.svg"

            action ShowMenu("history")

        # Save & Load - Icon Button
        imagebutton: 
            idle "gui/placeholders/dock_icon_placeholder.svg"

            action ShowMenu("save_load")
            

        # Preferences - Icon Button 
        imagebutton: 
            idle "gui/placeholders/dock_icon_placeholder.svg"

            action ShowMenu("preferences")

        # Endings - Icon Button 
        imagebutton: 
            idle "gui/placeholders/dock_icon_placeholder.svg"

            action ShowMenu("ending_gallery")

        # About - Icon Button 
        imagebutton: 
            idle "gui/placeholders/dock_icon_placeholder.svg"

            action ShowMenu("about")

        # Help - Icon Button 
        if renpy.variant("pc") or renpy.variant("web") and not renpy.variant("mobile"): 
            ## Help isn't necessary or relevant to mobile devices. 
            imagebutton: 
                idle "gui/placeholders/dock_icon_placeholder.svg"

                action ShowMenu("help")
    
    if _in_replay: 
        
        textbutton _("End Replay") action EndReplay(confirm=True)

    # Main Menu Return - Power Off Icon Button
    if not main_menu: 
        imagebutton: 
            idle "gui/placeholders/power_off_placeholder.svg"
            xalign 0.95
            ypos 660

            action MainMenu()

## App Grid Screen #############################################################
## This screen display in-game apps inside the Computer UI 

screen app_grid():

    # Grid Icons (6 columns x 3 rows) 
        grid 6 3: 
            xalign 0.5
            ypos 150
            spacing 40 

            # Row 1 

            # Profile App
            imagebutton: 
                idle "gui/placeholders/grid_icon_placeholder.svg"

                action Show("profile_app")
            
            # Chat App 
            imagebutton: 
                idle "gui/placeholders/grid_icon_placeholder.svg"

                action Show("chat_app")

            # Draft App 
            imagebutton:
                idle  "gui/placeholders/grid_icon_placeholder.svg"

                action Show("draft_app")

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

## App Screen Template #########################################################
## Template for app screens
## 
## For Design consistency

screen app_screen(window_width, window_height, content_width, content_height, screen_title, tool_screen=None): 
    
    tag app

    key "game_menu" action Hide()

    window id "app": 

        xysize (window_width, window_height)
        style "app_window"

        fixed: 
            xysize (window_width, window_height)
            clipping True

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

style app_window: 
    xalign 0.5
    yalign 0.5
    background None 
    clipping True 

define app_header_height = 35

screen app_header(window_width, screen_title): 

    frame: 

        xysize(window_width, app_header_height)
        background None 
        padding (0, 0)
        margin (0, 0)

        clipping True 

        add "gui/placeholders/App Title Bar Placeholder.svg": 
            xysize(config.screen_width, app_header_height)

        fixed: 

            xysize(window_width, app_header_height)

            clipping True 

            # Exit Button - Hides Screen 
            imagebutton: 
                idle "gui/placeholders/App Exit Button Placeholder.svg"
                at app_exit_button

                action Hide()

            # Title Text 
            text screen_title: 
                xalign 0.5
                ypos 4
                bold True
            
    
transform app_exit_button: 
    xysize(60, 25)
    xpos 10
    ypos 4

# App Main Content Frame Transform & Style 
transform app_main_content(content_width, content_height): 
    xysize(content_width, content_height)
    xalign 0.5
    ypos app_header_height + 20 

style app_main_content:
    background None
    padding(0, 0)
    margin(0, 0)

    clipping True 

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

## Computer UI - Call as Menu
screen computer_ui_menu(): 

    tag menu

    key "game_menu" action Return()
    
    use computer_ui

## Computer UI screen (Custom Game Screen)
screen computer_ui(): 

    tag game

    fixed: 

        at fill_screen

        clipping True

        # Background
        add "gui/placeholders/gray_background.svg": 
            at fill_screen

        use status_bar
        use app_grid
        use navigation_dock

## Scrollable Content 
screen scrollable_content(scroll=None, yinitial=0.0, spacing=0): 
    # Content with scroll support
    if scroll == "viewport":
        viewport:
            xfill True
            yfill True
            yinitial yinitial
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            mousewheel True
            draggable True
            pagekeys True
                        

            vbox:
                spacing spacing
                xfill True
                transclude

    elif scroll == "vpgrid":
        vpgrid:
            xfill True
            yfill True
            cols 1
            yinitial yinitial
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            spacing spacing
            transclude

    else:
        transclude

## Meta Screen Template ########################################################
## Template for all meta screens 
## (About, Save & Load, History, Preferences, Help, Endings)
## For Design consistency

screen meta_screen(title, scroll=None, yinitial=0.0, spacing=0): 

    tag menu 

    key "game_menu" action Return()

    # Meta Screen Dimensions 
    $ button_width = 56 
    $ button_height = 48
    $ meta_header_height = 58
    $ content_width = 1240
    $ content_height = 640

    fixed: 

        at fill_screen

        clipping True 

        # Background 
        add "#000000"

        # Header Bar
        fixed: 

            at fill_width(meta_header_height)

            clipping True 

            add "gui/placeholders/meta_screen_header.svg": 
                at fill_width(meta_header_height)
                
            # Header Title 
            text title: 
                xpos 20
                ypos 15
                color "#d6d6d6"
                size 24
                bold True

            # Close Button - Returns to previous screen
            imagebutton: 
                idle "gui/placeholders/meta_screen_exit_placeholder.svg"
                at meta_close_button
                xpos config.screen_width - button_width - 12
                ypos 5
                action Return()

        # Main Content Area 
        fixed: 
            xysize (content_width, content_height)
            xalign 0.5
            ypos config.screen_height - content_height - 12

            clipping True
            
            add "gui/placeholders/meta_screen_content_background.svg": 
                xysize (content_width, content_height)

            frame:

                background None 
                padding (20, 20, 20, 20)

                use scrollable_content(scroll, yinitial, spacing): 
                    transclude

transform meta_close_button: 
    xysize (56, 48)

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
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


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

            # Center things 
            xfill True
            yfill True

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

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

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

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

# Save or Load Choice Screen - Unified Save & Load Screen Handler
screen save_load_choice(slot): 
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame: 
        vbox: 
            xalign 0.5
            yalign 0.5
            spacing 30 

            hbox: 
                xalign 0.5
                spacing 100

                textbutton _("Save") action [Hide("save_load_choice"), FileAction(slot)]
                textbutton _("Load") action [Hide("save_load_choice"), FileLoad(slot)]

    key "game_menu" action Hide("save_load_choice")

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
    ypadding 3
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


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

    default device = "keyboard"

    use meta_screen(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

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
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

## Endings Screen ##############################################################
## This screen serves as a gallery for endings the Player has played through.

screen ending_gallery(): 

    tag menu 
    zorder 2

    use meta_screen(_("Endings")): 
        vbox: 
            text "Endings Gallery" style "game_menu_label"
            text "Coming soon..." style "game_menu_label"

################################################################################
## Special Gameplay screens
################################################################################

## Profile App Screen ##########################################################
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
    
    use app_screen(window_width, window_height, content_width, content_height, "Profile"):
                
        # Profile Info
        fixed: 
            xysize(620, 280)
            xalign 0.5
            ypos 13

            clipping True

            # Info Content Area
            add "gui/placeholders/Profile App Info Backdrop 1.svg":
                xysize(620, 280)

            add "gui/placeholders/Profile App Info Backdrop 2.svg": 
                xysize(620, 120)
                ypos 160 

            # Profile Pic
            add "gui/placeholders/Profile App Profile Pic Placeholder.svg":
                xysize(100, 100)
                xpos 55
                ypos 95

            # Profile ID
            vbox: 
                xpos 55
                ypos 195
                spacing 10

                # Player Name 
                text "[player_name]": 
                    size 20
                    bold True

                # Profile Name
                text "The Abyss Stares Back": 
                    size 18

            # Deadline Reminder Widget
            fixed: 

                xysize(210, 75)
                xpos 365
                ypos 30
                            
                clipping True

                add "gui/placeholders/Profile App Deadline Widget Placeholder.svg":
                    xysize(210, 75)

        # Trackers
        fixed: 
            xysize(620, 200)
            xpos 15
            ypos 13 + 280 + 19

            clipping True

            # Wallet Tracker 
            fixed: 

                xysize(260, 200)

                clipping True 

                add "gui/placeholders/Profile App Wallet Tracker Background Placeholder.svg":
                    xysize(260, 200)                

            # Stat Tracker
            fixed: 
                        
                xysize(340, 200)
                xpos 260 + 18

                clipping True

                add "gui/placeholders/Profile App Stat Tracker Background Placeholder.svg":
                    xysize(340, 200)

## Chat App ####################################################################
## 
## A screen that stores away Chats between the Player Character & other 
## Characters which serve as a part of the narrative

screen chat_app(): 

    tag app 
    zorder 10 
    modal True 

    # App Screen Dimensions 
    $ window_width = 900
    $ window_height = 600
    $ content_width = 850
    $ content_height = 525

    use app_screen(window_width, window_height, content_width, content_height, "Chat"):

        fixed: 
            xysize(230 + 570 + 20, 500)
            xpos 15
            ypos 15

            clipping True 

            # Contact Panel 
            fixed: 
                xysize(230, 500)
                
                clipping True
            
                add "gui/placeholders/Contact Panel Background Placeholder.svg":
                    xysize(230, 500)

            # Chat Box
            fixed: 
                xysize(570, 500)
                xpos 230 + 20

                clipping True

                add "gui/placeholders/Chat Box Background Placeholder.svg":
                    xysize(570, 500)
            
## Draft App ###################################################################
## A screen that lets the player view the progress of the Epilogue Draft 
## the Player Character is writing on throughout the game

screen draft_app(): 

    tag app 
    zorder 10 
    modal True 

    # App Screen Dimensions 
    $ window_width = 700
    $ window_height = 650
    $ content_width = 670
    $ content_height = 575

    use app_screen(window_width, window_height, content_width, content_height, "Draft", "draft_tools"): 

        frame: 
            xysize(650, 515)
            background None 
            padding (10, 9, 10, 9)
            
            clipping True

            text "Text Here": 
                color "#000"
    
screen draft_tools(): 

    tag tools

    fixed: 

        fixed: 
            xysize (700, 30)
            ypos 35

            clipping True 

            add "gui/placeholders/Draft Toolbar Placeholder.svg": 
                xysize (700, 30)

        fixed: 
            xysize (700, 50)
            ypos 700 - 100

            clipping True

            add "gui/placeholders/Draft Settings Bar Placeholder.svg": 
                xysize (700, 50)

################################################################################

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


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


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

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

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
