# ESPN NFL 2K5 Draft Class Generator by 2k5master

Welcome to the ESPN NFL 2K5 Draft Class Generator!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 1: Setup 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
You need:
1) Mymc: http://www.csclub.uwaterloo.ca:11068/mymc/
2) The Draft Class Generator Tool: You can download that right here!
3) Bad_AL's NFL 2k5 tool: https://forums.operationsports.com/forums/espn-nfl-2k5-football/881901-nfl2k5tool.html

These files will all be packed into the main download with the Draft Class Generator, so don't worry about installing them.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 2: Importing Your File
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
In this section, we're going to get our franchise file onto our computer and ready to edit. First, make sure that your franchise is in the offseason. I haven't tested it for anything other than the offseason, so it may or may not work for other places in the season.

Anyhow, shut down your PCSX2 after saving your file. Then, open mymc and extract your franchise file. Extract it to a place you'll remember; for me I extract it to my saves folder in the NFL 2K23 directory. 

After that, open the NFL2k5Tool. Click File>Load. Don't worry if nothing pops up! Click view, then deselect everything but the List Draft Class option. Then, click list contents. Finally, click file>save text then save it as a .csv in your NFL 2K5 Draft Tool directory. Name it anything you want.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 3: Using The Tool                                        
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is the simplest part. When you open the tool, enter 1, and then all you have to do is enter the name of your csv. Then, let the tool do its magic! Once it is done, you should see a confirmation print-out in the terminal and you'll see a new file that was added to the directory: new.csv. Open that file in a text editor; DO NOT OPEN IT IN EXCEL OR ANOTHER SPREADSHEET EDITOR. You'll need to copy the text from this file.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 4: Exporting
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is the most important section. You'll need two tools for this: Bad_AL's NFL2k5Tool and FlyingFinn's editor. First, open the NFL2k5Tool and click file>load. From there, select your extracted .max. It's a good idea to make a backup, just in case. After the file loads, click view and then deselect everything except for the list draft class option. Then, click list contents and then clear. Finally, paste your text file into the editor, and click File>Save.

You're not done just yet. If you don't do this next step, your file will become corrupted. Open Flying_Finn's NFL 2k5 Gamesave Editor and load your save file. Then, open any player profile and click "accept". Then, save your file and you should be good to go. In the future, I may try to add a way to load the .max directly into my tool, but for now this will have to do.

Finally, open MYMC. Select your franchise file, and then click file>delete. Then, click file>import and open your modified franchise file. When MYMC is done with this process, it should autosave and you're good to go!


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 5: Notes and Debugging
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Essentially, to get good, usable draft classes in this game, you have to use player names that are built into the roster you're using. For 2004 rosters, it works great. But for other rosters, it still tries to generate names based on the 2004 database, and that's what causes the asterisk and blank name issue. So, in order for this tool to work, it has to generate names based on the existing database. Which means that the tool has to use the EXACT name. For example, if the last name was "Stingley Jr" you couldn't make it so that the last name is just "Stingley". Essentially, we're stuck with the existing names in the database. Which is unfortunate, because there's only about 1,700 names. Which means that there will be a lot of repetitive names; it's just how the cookie crumbles. Think about it this way: if you were doing it manually, you would be limited to the same set of names as well. This just automates the process.

To get the names in the database, you'll notice that there's an acceptableNames.txt in the tool's directory. The text file is built on the NFL2k23 Week 0 rosters. It should work fine for other rosters, but you'll have to modify the database slightly. To do this, extract the .txt file from the NFL2k5Tool using only the "List Teams" view option. Nothing else. Then, extract it to a csv. Since I'm lazy and don't want to program any more than I have to, you'll have to open the CSV in a spreadsheet editor and copy the player name columns, and then save it as a txt. Of course, don't forget to replace the existing acceptableNames.txt. I know that's a pain in the ass, so when each official roster update releases I'll do it myself and release an update.

If your file's names look weird, there's the 3 and 4 debug options. Determine if it's an issue with the first names or last names, then print out the first names and or last names to a text file using the appropriate functions. Finally, send the files my way and I'll take a look at it!

One last thing: The source code is released publicaly with this file. I would be nowhere near where I am today without others releasing source code, so this is my way of paying it forward. Feel free to copy/paste/do whatever the hell you want with it. Go crazy.

Thanks for reading and enjoy! -2k5master
