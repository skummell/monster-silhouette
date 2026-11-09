## Monster Silhouette © 2026 SkumMell
## Licensed under GPL v3 — see LICENSE

################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2
define _game_menu_screen = "computer_ui_menu"

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1280, 720)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True

init python:
    config.gl_resize = True
    
    def adjust_view_size(width, height):
        return width, height
    
    config.adjust_view_size = adjust_view_size

################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#5BA3C9'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#888888'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#33B5D4'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#aaaaaa'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#C8C8C8'
define gui.interface_text_color = '#000'

## Fourth Wall break colors 
define gui.fourth_wall_color = "#FF0000" # Change this to a matching background muted red or something 
define gui.fourth_wall_text = "#8B1A1A"

# Note: Change arbritary colors "####" to use gui. defined colors in screens and script later.

## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "fonts/PT_Mono/PTMono-Regular.ttf"
define gui.text_font_bold = "fonts/PT_Mono/PTMono-Bold.ttf"

## The font used for character names.
define gui.name_text_font = "fonts/PT_Mono/PTMono-Regular.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "fonts/PT_Mono/PTMono-Regular.ttf"

## The bold version of font.
init python:
    # When bold is requested on the regular font, use the bold font file.
    config.font_replacement_map[("fonts/PT_Mono/PTMono-Regular.ttf", True, False)] = ("fonts/PT_Mono/PTMono-Bold.ttf", False, False)

## The size of normal dialogue text.
define gui.text_size = 22

## The size of character names.
define gui.name_text_size = 30

## The size of text in the game's user interface.
define gui.interface_text_size = 22

## The size of labels in the game's user interface.
define gui.label_text_size = 24

## The size of text on the notify screen.
define gui.notify_text_size = 16

## The size of the game's title.
define gui.title_text_size = 50


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 185

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 240
define gui.name_ypos = 0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 744

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 15
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = 10

## The vertical position of the notify screen.
define gui.notify_ypos = 45

## The spacing between menu choices.
define gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 10

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 10000

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 140

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 240
define gui.history_name_ypos = 0
define gui.history_name_width = 200
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 320
define gui.history_text_ypos = 2
define gui.history_text_width = 820
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 115

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 10

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"

################################################################################
## Positioning & Sizing Shared Config for Screen Styles
################################################################################

# status_bar : height, logo left padding, gap between right elements 

define status_bar_height = 38
define status_bar_details_gap = 20
define ui_logo_left_pad = 20

# navigation_dock : spacing between icons, bottom padding 

define dock_icons_spacing = 30 
define dock_bottom_pad = 20

# app_grid : gap between grid and status, top padding, spacing between grid elements

define app_grid_status_gap = 112
define app_grid_top_pad = status_bar_height + app_grid_status_gap
define app_grid_spacing = 40

# app_screen : gap between content

define app_header_content_gap = 20

# app_header : header height 

define app_header_height = 35

# app_exit : button width & height 

define app_exit_width = 60
define app_exit_height = app_header_height - 4

# meta_screen : header height, exit button width & height, content bottom padding 

define meta_header_height = 58
define meta_exit_button_width = 68
define meta_exit_button_height = meta_header_height - 6
define meta_content_bottom_pad = 12

# help : right padding for label, label width, label icon width & height 

define label_right_pad = 20
define label_width = 250
define label_icon_width = 24 
define label_icon_height = 24

# ending_gallery : grid entry/element width & height 

define ending_grid_entry_width = 590 
define ending_grid_entry_height = 130

# profile_app : sections, trackers, deadline widget, wallet tracker content, stat tracker content

# Profile App Sections
define profile_section_width = 620

# Profile Info
define profile_info_height = 280
define profile_info_top_pad = 13

# Profile content
define profile_content_left_pad = 55

# Tracker Height
define profile_trackers_height = 200

# Profile Pic
define profile_pic_top_pad = 95
define profile_pic_height = 100

# Wallet Tracker
define wallet_tracker_width = 260

# Stat Tracker
define stat_tracker_width = 340
define stat_tracker_left_pad = wallet_tracker_width + 18

# Deadline Widget
define widget_width = 210
define widget_height = 75

# Deadline Widget Content 
define widget_content_width = 190
define widget_content_height = 55

# Deadline Widget Text 
define widget_text_width = 105
define widget_label_height = 20
define widget_label_top_pad = 5
define widget_detail_height = 25
define widget_in_size = 20

# Wallet Tracker Content
define wallet_tracker_pad = 10
define wallet_tracker_content_width = wallet_tracker_width - wallet_tracker_pad * 2
define wallet_tracker_content_height = profile_trackers_height - wallet_tracker_pad * 2

# Wallet Tracker Content Title
define wallet_tracker_title_height = 30
define wallet_tracker_title_gap = 5

# Wallet Tracker Map 
define wallet_tracker_map_width = wallet_tracker_content_width
define wallet_tracker_map_height = wallet_tracker_content_height - wallet_tracker_title_height - wallet_tracker_title_gap

# Wallet Tracker Location Pin 
define wallet_tracker_spotter_size = 25

# Stat Tracker Content
define stat_tracker_pad = 15
define stat_tracker_content_width = stat_tracker_width - stat_tracker_pad * 2
define stat_tracker_content_height = profile_trackers_height - stat_tracker_pad * 2

# Stat Tracker Row
define stat_tracker_row_gap = 10
define stat_tracker_row_height = (stat_tracker_content_height - stat_tracker_row_gap) // 2

# Stat Tracker Icons
define stat_tracker_row_icon_size = 40
define stat_tracker_row_icon_gap = 10
define stat_tracker_row_lock_size = 20

# Stat Tracker Bars
define stat_tracker_row_bar_height = 20
define stat_tracker_row_bar_gap = 0

# Stat Tracker Label 
define stat_tracker_row_label_height = 22

# Stat Tracker Bar Values
define stat_tracker_row_value_width = stat_tracker_row_lock_size * 2
define stat_tracker_row_value_height = stat_tracker_row_lock_size

# Stat Tracker Row Body 
define stat_tracker_row_body_width = stat_tracker_content_width - stat_tracker_row_icon_size - stat_tracker_row_value_width - (stat_tracker_row_icon_gap * 2)
define stat_tracker_row_body_height = stat_tracker_row_label_height + stat_tracker_row_bar_gap + stat_tracker_row_bar_height

# Stat Tracker Icon Bottom Pad
define stat_tracker_icon_bottom = (stat_tracker_row_height + stat_tracker_row_body_height) // 2

# chat_app : container, contact panel container, chat box container  

# Chat App Container
define chat_app_pad = 15

# Contact Panel Container 
define contact_panel_width = 230
define contact_panel_height = 500
define contact_panel_gap = 10 

# Chat Box Container 
define chat_box_width = 570
define chat_box_height = contact_panel_height

# contact_button : button, online status

# Button 
define contact_button_width = 205
define contact_button_height = 87

# Status 
define contact_status_width = 60 
define contact_status_height = 15
define contact_status_xpad = 4

# chat_box : header, content, chat bubble, keyboard field

# Chat Box Header
define chat_box_header_width = chat_box_width
define chat_box_header_height = 40 

# Chat Box Comtent
define chat_box_content_width = chat_box_width
define chat_box_content_height = 410
define chat_box_content_top_pad = 40

# Chat Bubble 
define chat_box_bubble_content_width = chat_box_content_width - chat_box_content_top_pad
define chat_box_bubble_content_height = chat_box_content_height - chat_box_content_top_pad

# Chat Box Keyboard
define chat_box_key_width = 500
define chat_box_key_height = 40

# chat_bubble : width & text height 

define chat_bubble_width = 240 
define chat_bubble_text_height = chat_bubble_width - 40 

# draft app : window, scrollable area, frame 

# Draft App Window
define draft_window_width = 700
define draft_window_height = 650 

# Scrollable Area 
define draft_scroll_width = draft_window_width - 30
define draft_scroll_height = draft_window_height - 75

# Draft Frame
define draft_frame_width = draft_scroll_width - 20

# draft_file : auto scroll buttons, header, content 

# Auto Scroll Buttons
define scroll_button_width = 20
define scroll_button_height = 20 

# Draft File Header 
define draft_header_width = draft_frame_width
define draft_header_height = 35

# Draft File Content 
define draft_content_width = draft_frame_width
define draft_content_height = 480

# draft_tool : toolbar & settings bar 

# Draft Toolbar
define draft_toolbar_width = draft_window_width
define draft_toolbar_height = 50  # CHANGE TO 30 Later when placeholder is replaced

# Draft Toolbar Content 
define draft_toolbar_content_width = 680
define draft_toolbar_content_height = 30

# Draft Settings Bar
define draft_settings_bar_width = draft_window_width
define draft_settings_bar_height = 50

# Draft Settings Bar Content 
define draft_settings_bar_content_width = 670
define draft_settings_bar_content_height = 50

# notif_button : button height & width 

define notif_button_width = 315
define notif_button_height = 74

# timespamp_for_chat : frame padding, content height, frame height

define stamp_frame_pad = 10
define stamp_content_height = 15
define stamp_frame_height = stamp_content_height + (stamp_frame_pad * 2)

# bedroom : width & height for containers

# Bookshelf Assemble
define bookshelf_assemble_width = 342
define bookshelf_assemble_height = 508 

# Desk Setup
define desk_setup_width = 546 
define desk_setup_height = 432

# Chair in Bedroom 
define bedroom_chair_width = 142
define bedroom_chair_height = 323

# wardrobe_panel : panel height & width & spacing 

define wardrobe_panel_width = 420 
define wardrobe_panel_height = 320
define wardrobe_panel_spacing = 20 

# lounge_look : width & height for containers

# Counter Assemble 
define lounge_look_counter_width = 1182
define lounge_look_counter_height = 421

################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20