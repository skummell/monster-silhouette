# Build Log 

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
    - `show_app(screen, disabled)`
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

# Oct 2-3, 2026 

- Default Scheduled Times of Day Dictionary Variable
  - Format:
    - `occasion`: 
      - default: wake_up, break, lounge_arrival, lounge_closes
      - early time: wake_up, break, lounge_arrival
      - special event: lounge_closes
    - `clock[occasion]` - for default time for `occasion` 
    - `clock["early"][occasion]` - for early time for `occasion`
    - `clock["special"][occasion]` - for special event time for `occasions`
  - Implement clock variable usage to change time during set periods on script instead of manual assignment