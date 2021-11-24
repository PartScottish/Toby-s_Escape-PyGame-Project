Instillation and general instructions, TO-DO and Future Features.


Instillation instructions ~ Game has been tested following these instructions to work on Windows and Mac:
1) Ensure PyGame 2.0 is installed - via operating system command shell
2) Ensure Python version is 3.8 or newer - I recommend using Sublime
3) Unzip the game folder "pygame"  
4) Launch main.py from within the "pygame" folder within your IDE of choice - Again, I recommend Sublime as it was built and tested on this software.
5) Run / build the file and follow the in-game instructions
6) Do not rename or move any files, folders or assets - including variables within the code

General instructions:
1) Read the Game_Description.txt for the story setting for the game
2) Delete high_score.txt to reset the highscore within the game
3) Game music volume is set relatively low to avoid varying volume levels per OS - you may need to turn this up more than you think; or down

TO-DO / Features to add ~ Many or most of these were axed in development due to working on this game solo and not in a group:
1) Remove all hard-coding of numbers, especially those pertaining to coordinates and refactor with named variables from utils.py
2) Redesign the platforms to be objects and not sprites. This will allow for better collision checking and spawn manipulation. 
2.1) Fix platform y axis spawn to require a minimum value to fix the "stuck between platforms bug"
2.2) Fix playform y (and x) axis spawns to eliminate any "impossible" scenarios
3) Add new backgrounds/levels when reaching certain scores 
4) I toyed with a "win-condition" but it essentially would require a rework of the scoring system ~ see 5)
5) Add lives and score objects. 3 lives, one lost each time you fall. Coins and life pick-ups to help modulate score gain and enable a win-condition. Currently a win-condition renders the highscore effectively redundant
6) Screen dimensions were deliberately chosen to fit with the theme of the game. The sounds and style of the game are deliberately in the theme of the late 80's and 90's arcade-style games and i felt like this resolution was the middle-ground between maintaining that but also making it a bit more hi-res for modern computers. With this in mind, modifying the resolution of all assets to enable the use of ", RESIZABLE" to allow users to play in a size of their choosing.


