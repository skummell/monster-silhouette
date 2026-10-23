# Build Log 

This file is an extensive Build Log and Change Log for Monster Silhouette as a project. 

Includes changes to repo tracked project files, untracked project files, & other game development progress. 

Logs are divided by date ranges then specific dates. 
<br>
If something is under a date range rather than a specific date it means it was worked on multiple days within that date range rather than a specific day corresponding to a single date.

Refer to repo commits for specific dates, times and changes on finalized code edits, fixes & etc on tracked project files mentioned in the logs. 
<br>
Not every commit made as soon as every change is completed.
<br>
(Note: Repo commits only start as of Sep 21, 2026.)

---

**Log relevant files (including those not included in repo):**

(**Note:** not all folders nor all files inside folders are named in trees)

- Project Files: 

  ```
  monster_silhouette/
  ├── game/
  │   ├── audio/
  │   ├── gui/
  │   ├── images/
  │   └── script/
  │   │   └── demo/
  │   │       ├── demo_choices/
  │   │       │   └── demo_choice1.rpy
  │   │       ├── demo_interludes/
  │   │       │   └── demo_choice1.rpy
  │   │       └── demo_intro.rpy
  │   ├── custom_systems.rpy
  │   ├── gui.rpy
  │   ├── options.rpy 
  │   ├── screens.rpy 
  │   └── script.rpy
  ├── LOG.md (CURRENT FILE!)
  └── README.md 

  ```

- Engine Files:  

  ```
  renpy-8.5.3-sdk/
  └── renpy/
      └── common/
          ├── 00gamemenu.rpy
          └── 00action_menu.rpy

  ```

- Game Design Document (GDD) Files 
  
  ```
  Monster Silhouette/
  ├── Characters/
  ├── Concept Art/
  ├── Game Mechanics/
  ├── Locations/
  └── Script/
  ```

## Aug 25-30, 2026

- Brainstorming & Premise 
- Full Demo Script
- Game Warning Categorization 

## Sep 01-04, 2026

- Concept Art 
  - UI Design 
  - Backgrounds (2 Locations, 3 Backgrounds)
  - Prop Sprites
    - Laptop Sprites
    - Wallet Sprite
    - Drink Sprite I
- Minor Script Modifications

### Sep 03, 2026 

- Custom Unified Save & Load Screen 

### Sep 04, 2026 

- Custom Game Screen (In-Game Computer UI)
  - Layout 
    - Using Placeholder UI Elements
  - Functional Meta Buttons 
- New Concept Art 
    - More Background Props
    - Clothing Sprites
    - Profile Pics

## Sep 05-06, 2026

- Meta Screen Bugs & Fixes
  - Content Area Padding & Positioning Fix
  - Scrollbar Formatting Fix
  - Game Menu Key Binding to Custom Game Screen 
  - Game Menu Key Menu Navigation Fixes

- Engine Files Modification (For Full Bug Fix)
  - Files Modified : 
    - 00gamemenu.rpy
    - 00action_menu.rpy
  - Custom Show Callable for Menu version of Computer UI 
    - ShowHome() - Creates a new context between game and meta menus
    - When you ESC inside Meta Menu you opened from the Computer UI menu you correctly return to the Computer UI menu instead of skipping it and returning to the game directly 
  - Screenshot Timing Tweak 
    - Computer UI Menu no longer shows up in the Save Screenshot

## Sep 07, 2026 

- New & Updated Concept Art 
  - UI Design  
    - Player Name Enter Screen
    - Chat Notifications
  - Bedroom Background Update 
    - Sticky Notes Prop 

- Player Name Input
- Script Files Separation / Organization 
- Suppress Overlay Fix for Home Menu Screens (00gamemenu.rpy)

## Sep 08-13, 2026 

- Last New Concept Arts for Demo
  - Background Art
    - Computer UI  
      - Lock Screen 
      - Home Screen
    - Starting Screen
    - Loading Screen
  - Drink Sprite II
  - Character Designs 
    - Victor 
    - Mephisto
    - Sketch Ups (Special Features Conceptualization)
      - Theo 
      - Manager (Larissa)

- Save Delete Key Mapping 

## Sep 14-21, 2026 

- Internal States Initialization

- New Custom Screen(s)
  - App Screen 
    - Template Screen 
    - Sets: 
      - App Window Background
      - App Header 
        - App Title
        - Functional Exit Button
      - App Main Content Area
      - Optional Toolbars
  - Layout for 3 Other Screens (Using Placeholder UI Elements)
    - Profile App Screen 
    - Chat App Screen 
    - Draft App Screen

- Formatting Bugs Fix 
  - Transform & Style Dynamic Implementation for Meta Screens & App Screens

- Project Proposal Presentation Slides

## Sep 22-28, 2026

- Update Meta Screens 
  - Ending Gallery Screen 
    - Locked Endings Version

- New Custom Screen(s)
  - Computer UI Lock Screen (computer_ui_locked)

- Bugs & Fixes 
  - Status Bar Elements & Navigation Dock - Hide & Show Fix
  - Show screens on scene layer during script (show_scene)
  - Show app screens (modal) on scene layer during script (show_app)
  - Intermidant Save_Load Screenshot when called through Computer UI Menu - Prevented
    - Engine File Modified: 00gamemenu.rpy
  - Fix ESC shortcut when App called in Master Scene 
    - Prevent it from hiding App 
    - Let it function like a normal Game Menu Action

- Narrative Script Progression
  - Day 1 - Introduction 
    - In Progress (Just Before First Chat Interaction)

- Usable Bedroom Background Progression 
  - 1 Point Perspective
  - Completed: 
    - Desk Set Up 
  - In Progress: 
    - Bookshelf

- Technical Additions 
  - Tooltips Added 
  - Player Name Validation Added 
  - Key Binding for QuickSave and QuickLoad

- Project Proposal Report 

### Sep 22, 2026

- Status Bar Update 
  - Inner Layout
  - Display Date & Time
    - Time Display functions as textbutton to return to game when inside computer_ui_menu
  - Set as Overlay Screen
- Dynamic Scaling of Window & Elements
  - Stretches Elements
  - Needs modifications when certain elements are added

### Sep 23, 2026

- Layout of Computer UI Locked 
  - Using Placeholder UI Elements
  - Display Date & Time 
  - Display Player Name

## Sep 29-30, 2026 

- New File: `custom_systems.rpy`
  - Custom Statements & Utility Functions to work with Game Systems 
  - Current Statements: 
    - Utility Functions Transfered into Statements
      - `show_scene "screen"`
      - `show_app "screen"` - App Exit Button Functionality Blocked By Default 
        - `show_app_e "screen"` - New! (Enabled App Exit Button Functionality)
      - `hide_app "screen"`
    - New Statements:
      - `chat_start "contact"`
      - `chat_end "contact"`
  - Current Functions: 
    - `show_scene(screen)`
    - `show_app(screen, disable=False)`
    - `hide_app(screen)`
    - `get_chat_entries(contact)`

- Chat App Functionality 
  - Contact Panel
    - Scrollable
    - Contact Item Buttons
      - Set Active Contact 
  - Active Chat Box 
    - Scrollable
    - Activates Chat Box linked to Active Contact 
    - Chat Log 
      - Chat System
        - Store Script lines that correspond to Chat conversation 
          - Custom Statements: `chat_start "contact_name"` & `chat_end "contact_name"` 
            - Track Beginning and End of Chat Conversation inside of Script through Rollback History point ranges (length at start & end)
            - Store History Ranges inside of a List of Chat Ranges linked to a Contact (contact_name)
        - Read Chat History: `get_chat_entries(contact_name)` 
          - Pull from Roll History 
          - Filter by recorded ranges & NVL
      - Display NVL Lines in Chat Box 
    - Chat Bubbles 
      - Display NVL Lines in Chat Bubbles
        - Chat History
        - Live Script 
      - Chat Bubble Background: 
        - Sent Chat Bubbles for Player Character (Right Aligned)
        - Receive Chat Bubbles for other characters (Left Aligned)

### Sep 30, 2026 

- Project Proposal Presentation

- Chat App Bugs & Fixes
  - Bubble Padding & Text Container
  - Scrollable Fixes
    - Auto Scrolls with Script Progression
    - Opens scrolled to the end
  - Seamless switch between Live Script & Updated Chat History Rendering
    - Render Live Chat if NVL Script not Empty 
    - Clear NVL Script 
      - When: 
        - Chat Box is activated again 
        - Or on Chat App Hide 
      - If: 
        - No longer in Chat Block

## Oct 1, 2026

- Narrative Script Progression
  - Script Files (not included in Repo) - `script/demo/`
    - `demo_intro.rpy`
    - `demo_choices/demo_intro.rpy` - New File!
    - `demo_interludes/demo_interlude1.rpy` - New File!
  - Completed Script Dialogue Implementation
    - Day 1 - Introduction
    - Day 1 - First Choice 
  - Not Completed: 
    - Game System Implementations Within Script
    - Day 1 - First Interlude 
      - Stopped Before Prep Phase

## Oct 2-7, 2026 

- Default Scheduled Times of Day Dictionary Variable
  - `clock` variable
  - Format:
    - `occasion`: 
      - default: wake_up, break, lounge_arrival, lounge_closes
      - early time: wake_up, break, lounge_arrival
      - special event: lounge_closes
    - `clock[occasion]` - for default time for `occasion` 
    - `clock["early"][occasion]` - for early time for `occasion`
    - `clock["special"][occasion]` - for special event time for `occasions`
  - Implemented clock variable usage to change time during set periods on script instead of manual assignment

- Bugs & Fixes
  - Window Hiding Bug on a transparent transformed window (`nvl_window`) 
    - Get rid of transform 
    - Overide nvl_window style to be fully transparent & Dialogue + Name text to be transparent
      - No Background 
      - Transparent Text Color (#000000)
  - Accidental use of `||` in if conditions 
    - Changed to `or`
  - New Fix for Date Pushed Left or Right Based on Whether Time is 3 or 4 digits long
    - Text Container with correct sizing and right align on time
  - Return Bug on `demo_intro.rpy` after swapping label orders
    - Add explicit `return` at the end of `demo_intro` label
  - Chat Contact Panel @ Scrollable Error Formatting Content Style Bug
    - Viewpoint Height & Width Setting Parameter Implementation
    - Fix Padding with Test & Try for Height / Width Assignment
  - Chat Auto Scroll Bugs
    - Issues: 
      - Not scrolling past time stamp
      - Lag after first interactable nvl line
    - Fixes: 
      - Assign id to scrollable viewport & let yinitial=1.0 handle the auto scrolling 
      - Fix lag with `ranged` `ui.adjustement` assigned to `adj`

- Major File Update: `custom_systems.rpy`
  - Tweaks to existing functions and statements 
    - `show_app_e` - No longer exists! 
    - `show_app(app_screen)` - No longer takes a `disable` parameter!
      - Button disabling will be handled with the Button Disabler System from now on!
  - New Functions!
    - `button_disabled(button=None, report=True)`
    - `button_disabler_status(global_btn=True, btn_type=True, btn_id=True, disabled=True, enabled=True, inline=False)`
    - `disable_global()`
    - `enable_global()`
    - `disable_all()`
    - `enable_all()`
    - `disable_type(button_type)`
    - `enable_type(button_type)`
    - `disable_all_type(button_type)`
    - `enable_all_type(button_type)`
    - `disable_id(id)`
    - `enable_id(id)`
  - New Statements!
    - All Button Disabler System Custom Statements (Check below ↓)

- Button Disabler System
  - Variables: 
    - `disable_buttons` - Universal (boolean) disabler for all buttons that can be disabled
    - `disabled_button_types` - Universal (boolean) disablers per button type
    - `disabled_button_ids` - List of individual disabled buttons
    - `valid_button_ids` - List of all valid button ids, linked to their button types that can be disabled
  - Custom Statements: 
    - Disable or enable all Buttons
      - `disable_global`, `enable_global`, `disable_all`, `enable_all`
    - Disable or enable all Buttons of button_type
      - `disable_type "button_type"`, `enable_type "button_type"`, `disable_all_type "button_type"`, `enable_all_type "button_type"`
    - Disable or enable Button with button_id
      - `enable_id "button_id"`, `disable_id "button_id"`
  - Debugger Functions:
    - `button_disabled()` - boolean check whether global disabler, button type or button name is currently disabled or not, receive a report in console about where the status is originating from and any inner flag details behind the status, by default
    - `button_disabler_status()` - console function that prints an organized list of button disablers' status
    - Extensive documentation on comments above functions for their usage and optional parameters!

- Usable Bedroom Background Progression 
  - Concept Art 2.0 Completed!
    - Closed: 
      - Position of all elements
      - All props / elements included in background
    - For next Concept Art: 
      - Perspective Fix
      - Settle on a Color Palette

### Oct 4, 2026 

- Player Character Mascot Concept Design

### Oct 5, 2026 

- Chat App Polishes 
  - Chat App Timestamps 
  - Chat App Online Status

### Oct 6, 2026 

- Template Screens for all button types that can be disabled
  - `app_button` - New Template Screen!
  - `app_exit` - New Template Screen!
  - `contact_button` - Name changed! (From contact_item to contact_button)

- Clock Dictionary (`clock`) Variable Update
  - New Occasions added!
    - default: work, mephisto_arrival, mephisto_leaves
    - early time: work

### Oct 7, 2026 

- Partial implementation of Button Disabler System
  - Button sensitivity blocked: 
    - if condition testing button disabled status

## Oct 8, 2026 

- New Button Disabler Variable!
  - `app_to_exit` - Dictionary List Mapping App Buttons IDs to their correspondent App Exit Buttons IDs

- Button Disabler System Implementation
  - In other Game Systems' Statements (`custom_systems.rpy`) d
    - `show_app` - auto-disables corresponding exit button 
    - `hide_app` - auto-enables corresponding exit button
    - `chat_start` - disables all contact buttons then enables corresponding contact button
    - `chat_end` - auto-enables chat exit button
  - In Script Files (`script.rpy` & `script/*.rpy`)
    - Comments updated on disabling actions from other statements called
    - Disable Buttons are all levels then enable app exit buttons at `start` of script 
    - Enable Profile App Button after first time Profile App is shown and hidden in script (`demo_intro`)
    - Enable Chat App Button when Chat Icon is meant to be clickable (`demo_intro`)
    - Disable Chat App Exit Button after Chat Box Activates (`demo_intro`)
      - In preparation for Click Implementations 
    - Enable Draft App Button when Draft App is meant to be clickable (`demo_interlude1`)

- Styled Exit Disabled Warning for Computer UI Menu when you open an app whose exit buton is disabled

- Bugs & Fixes: 
  - `_game_menu_screen` with wrong screen name 
    - Fix: 
      - Switched to `computer_ui_menu`
  - Hover events prevented by `sensitive False`
    - Fix: 
      - Swapped `sensitive False` with `NullAction` for hover events to still work but button do nothing when disabled
  - Stuck in `computer_ui_menu` when exiting with ESC after opening a app
    - Fix: 
      - `game_menu` key on computer_ui_menu now fully exit back to game/scene 
      - `[Return(), Return()]` action instead of a single `Return()`
  - `active_contact` cleared when returning to game during chat block if Chat App opened & exited at least once from computer_ui_menu
    - Fix: 
      - Wrap on hide action in a if for in_chat_block
      - Clears active_contact only if False (not on chat block)
  - Profile App Exit Button disabled by enable Chat exit button inside of hide_app "chat_app" statement 
    - Due to triggering empty set conditional 
      - Which adds all buttons of button type to disabled id except enabled id
    - Fix: 
      - Added additinal if condition
      - Conditional only triggers if button type disabler is on

## Oct 9-13, 2026 

- Moved button disabler variables from `screen.rpy` to `custom_systems.rpy`

- Major File Update: `custom_systems.rpy`
  - Variable Tweaks 
    - Change assignment from default to init python
      - `valid_button_ids`, `app_to_exit`
  - New Functions!
    - `freeze_until(flag_name)`
    - `flag_check(flag_name)`
    - `app_open(app_screen)`
    - `contact_open(contact_name)`
  - New Statements!
    - All Freeze System Custom Statements (Check below ↓)

- Freeze System 
  - Overlay Screen for Freeze Hint (`freeze_hint_display`)
  - Variables: 
    - `flag_conditions` - Dictionary conditions mapped to flag names
    - `freeze_hint` - Dictionary of freeze hints mapped to flag names
    - `_current_hint` - Hint for current Freeze Block
  - Custom Statements: 
    - `freeze_until "flag_name"` - Pause script until condition assigned to flag_name is met

- Add Freeze Conditions dynamically 
  - Based on already logged app screens and contact names (`valid_button_ids`)
    - Use `app_button` and `contact_button` keys' values to dynamically add `[app]` and `[contact]` conditions
- Add Freeze Hints dynamically 
  - Based on already logged app screens, app names, and contact names
    - Use `valid_button_ids`, `contact_button` key values to dynamically add `[contact]` hints
    - use `app_to_exit` keys and values to dynamically add `[app]` hints

- Freeze System Implementation: 
  - Script Implementation: 
    - `demo_intro.rpy`
      - Freeze until Chat is opened 
      - Freeze until And contact is open 
    - `demo_interlude1.rpy`
      - Freeze until Chat is closed 
      - Freeze until Draft is opened
      - Freeze until Draft is closed

## Oct 14-21, 2026 

- Usable Bedroom Background Progression 
  - 1 Point Perspective
  - Elements: 
    - Desk Set Up 
      - Wallet, Key, Laptop Sprites 
    - Wardrobe / Closet 
    - Bookshelf 
    - Bed

- Interactable Bedroom Scene
  - `bedroom` - New screen!
  - `wardrobe_panel` - New screen!

- Narrative Script Progression
  - Script Files (not included in Repo) - `script/demo/`
    - `demo_intro.rpy`
    - `demo_choices/demo_intro.rpy` 
    - `demo_interludes/demo_interlude1.rpy`
    - `demo_prep/` - New Folder!
      - `demo_bed_click.rpy` - New File!
      - `demo_closet_click.rpy` - New File!
      - `demo_key_click.rpy` - New File!
      - `demo_laptop_click.rpy` - New File!
      - `demo_wallet_click.rpy` - New File!
  - Completed Script Dialogue Implementation
    - Day 1 - Introduction
    - Day 1 - First Choice 
    - Day 1 - Bed Click 
    - Day 1 - Wallet Click 
    - Day 1 - Closet Click 
    - Day 1 - Laptop Click 
    - Day 1 - Key Click
    - Game System Partial Implementations Within Script
      - Single Condition Freeze Implemented
      - Expanding Freeze System
  - Not Completed: 
    - Game System Implementations Within Script
      - Prep Phase Freeze 
      - Prep Phase Click System 
      - Closet Click System       
    - Day 1 - First Interlude 
      - Stopped in the middle of Prep Phase
    - Polishes

- Freeze System Update!
  - Integrate Prep Phase into Freeze System 
  - Freeze System now supports dynamic hints 

### Oct 21, 2026 

- Game Mode System 
  - Switch from script progression to other game modes
    - Makes use of the Freeze System
  - Custom Statements: 
    - `prep_phase` - Turns on Prep Phase Game Mode
  - Game Modes: 
    - Prep Phase Game Mode 
      - Variables: 
        - `key_attempted` - Prep Phase Hint gater (Track whether key has been clicked at least once)
        - `closet_clicked` - Freeze sub condition (Track whether closet click has been successfully completed)
        - `laptop_clicked` - Freeze sub condition (Track whether laptop has been clicked)
        - `top_selected` - Gates `closet_clicked`
        - `bottom_selected` - Gates `closet_clicked`

- Scene System Update! 
  - Support for modal screens without correspondant app exit buttons
    - `show_panel` - New Statement!
    - `hide_panel` - New Statement!

## Oct 22, 2026 

- Debugging Prep Phase Game Mode
  - Issues & Fixes
    - Freeze Breaks 
      - Call Scripts in new context 
      - New issue : Closing off `wardrobe_panel` early
        - Open `wardrobe_panel` from button directly instead of calling in script
    - Interaction Overlaps & Incosistencies + Script Loops & Overlaps
      - Fix all variable settings in `bedroom` screen
      - Implement Button Disabler to `bedroom` interactables
      - Implement Button Disabler to `wardrobe_panel` interactables
  - Polishing (`bedroom` and `wardrobe_panel` screens)
    - Add Tooltips 
    - Fix up formatting and styling
  - Additional Prep Phase Testing