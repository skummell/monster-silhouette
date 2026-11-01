*[UML]: Unified Modeling Language 
*[FSM]: Finite State Machine
*[VS]: Visual Novel
*[RPG]: A Role-Playing Game (RPG) is a game in which players assume and play out the roles of characters in a fictional setting. Players guide narrative & character development through a process of structured decision-making.
*[N/A]: Not Applicable

*[UML State Machine]: An ULM extension of the traditional FSM designed to handle more complex, event-driven systems. The system responds to events based on its current internal state, which can trigger actions and state transitions.
*[Finite State Machine]: A FSM is a mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one state to another in response to some inputs (this is called a transition).
*[Visual Novel]: A VS is a type of interactive, narrative-driven video game, that tells a story primarily through text combined with static or sprite-based artwork, background music and sound effects

*[Ren'Py Engine]: An open-source visual novel engine built on Python, used to develop Monster Silhouette. Provides the core scripting language, rendering, audio, save system and built-in screen infrastructure the game is built on top of.
*[Gameplay Mechanics]: The systems and rules that define how the player interacts with and experiences Monster Silhouette beyond passive reading. Includes choices, state tracking, game modes, UI systems and other interactive elements.
*[Game Menu Action]: A built-in Ren’Py action that opens the game menu. In Monster Silhouette this has been overridden to open the Computer UI Menu (which serves as Monster Silhouette's custom Game Menu) instead of the default Ren’Py game menu.
*[Main Menu]: An essential part of the Start Screen, and where its primary functionality lives.
*[Quick Menu]: Ren'Py's in-game menu bar, usually at the bottom of the screen. Provides quick access to Back, History, Skip, Auto, Save & Load, and Preferences.
*[Game Day]: An in-game day of the narrative. Each Game Day corresponds to a specific date in the game's calendar.
*[Game Date]: The in-game calendar date shown in the Screen HUD.
*[Game Time]: The in-game time shown in the Screen HUD.
*[args]: Positional arguments. Additional values passed to a function or statement by position rather than by name. Distinct from kwargs.
*[kwargs]: Keyword arguments. Optional named parameters passed to a function or statement using the format `key "value"` and `key=value`. With the key matching the exact name of the parameter being assigned. Allows additional data to be passed without being positionally required.

*[Game Screens]: The game screens created or modified for Monster Silhouette beyond what Ren'Py provides. Includes Template Screens, Meta Screens, Overlay Screens, Computer UI Screens, App Screens, Game Mode Screens
*[Meta Screens]: History, Save & Load, Preferences, Ending Gallery, About, Help
*[App Screens]: Profile App, Chat App, Draft App
*[Computer UI Screens]: Computer UI, Computer UI Menu, Computer UI Locked, Navigation Dock, App Grid
*[Template Screens]: Meta Screen, App Screen, App Header, App Exit, App Button, Contact Button, Chat Box, Chat Bubble, Timestamp For Chat, Chat Date Stamp, Chat Time Stamp, Draft File, Scrollable Content, Notif Button
*[Overlay Screens]: Status Bar, Freeze Hint Display, Exit Disabled Warning, Chat App Notification 
*[Game Mode Screens]: Bedroom, Wardrobe Panel

*[Ren'Py Special Screens]: Screens built into Ren'Py that the engine itself displays under specific conditions. Includes say, choice, input, nvl, bubble, quick_menu, main_menu, game_menu, save, load, preferences, history, about, help, confirm, skip_indicator, notify, and file_slots.

*[Game Systems]: The custom systems created for Monster Silhouette beyond what Ren'Py provides. Includes Scene System, Button Disabler System, Chat System, Draft System, Freeze System, and Game Mode System.
*[Scene System]: Custom system that allows Ren'Py screens to be used in place of traditional image scenes.
*[Button Disabler System]: Custom system that controls button interactivity across the game through three independent disabler levels — Global, Type, and ID.
*[Chat System]: Custom system that records NVL dialogue lines as chat conversation entries and renders them inside the Chat App.
*[Draft System]: Custom system that records branching book draft content and renders it inside the Draft App.
*[Freeze System]: Custom system that pauses script progression until a specific condition is met by the player.
*[Game Mode System]: Custom system that switches script progression into interactive game modes with their own rules, screens, and completion conditions.

*[Utility Functions]: Game System functions intended for use in screens, other parts of code, or the developer console. Distinct from statements, which are for script files.
*[Debugger Functions]: Game System functions intended for use in the developer console for debugging purposes.

*[Mephisto]: A mysterious recent arrival to town whom the Player Character meets in the main narrative of Day 1 of the Demo — and who appears to the Player Character as a silhouette.
*[Player Character]: The protagonist of Monster Silhouette. A successful mystery horror writer working on the epilogue of their latest book. Name chosen by the player at the start of the game.
*[Theo]: The Player Character's best friend. Outgoing, cheerful, and always busy. Away on a trip during Day 1 of the Demo.
*[Victor]: The Player Character and Theo's close childhood friend. Owner of Kiri Rêve Tea Lounge, the main location of Day 1.
*[Larissa]: The Player Character's publishing manager and editor at King Yellow Publishing. Appears as "Golden Manager" in the Chat App during the Demo.

*[SkumMell]: Solo developer, writer, artist, and coder of Monster Silhouette. Also known as Mel.

*[Contact]: An in-game character the Player Character can communicate with through the Chat App.
*[Chat Block]: The span of script between a chat_start and chat_end statement pair.
*[Context]: Ren'Py's isolated execution state. Monster Silhouette operates with three context types: Game Context, Menu Context, and Home Context.
*[NVL Mode]: Ren'Py's wall-of-text dialogue mode. Repurposed by Monster Silhouette's Chat System as a recording mechanism for chat messages.
*[Master Layer]: Ren'Py's bottommost visual layer where traditional background scenes live. Also called the scene layer.
*[Statement]: A custom Ren'Py command defined via renpy.register_statement for use in script files.
*[Flag]: A variable that tracks a specific aspect of the player's journey through the story.

*[this Documentation]: Any documentation page found on this source code documentation site (Monster Silhouette - Source Code Docs)