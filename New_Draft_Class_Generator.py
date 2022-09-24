# Imports
import csv
import random
import webbrowser
import sys
import time

# Monke :)
# This comment keeps the program working. Whenever I remove it, it breaks. Don't ask questions.

# Variables
debug_devmode = False
debug = False
total = 0
fnames_list = []
lnames_list = []
new_numbers_list = []
new_position_list = []
acceptable_fnames_list = []
acceptable_lnames_list = []

# Main Menu
print("ESPN NFL 2K5 Draft Class Generator by 2k5master")
print("")
print('1 - Proceed and enter the name of your CSV')
print("2 - Generate New acceptableNames.txt based on roster file (RESTART REQUIRED AFTER FILE IS GENERATED)")
print("3 - Disable the removal of unique/recognizable names when generating draft class")
print("4 - Enable the removal of unique/recognizable names when generating draft class")
print("5 - Open the documentation")
print("6 - Exit the application")
print("debug - Enter debug mode")

global first_names
global last_names
# Reads the acceptableNames.txt
with open('acceptableNames.txt', 'r') as text_raw:
    text = text_raw.read()

edited_text = text.split("\n")

# Gets the first and last names out of that text file; weeds out non-names.
first_names = []
last_names = []
for element in edited_text:
    temp_name = element
    element_total = 0
    element_length = len(element)
    new_last_name_total = 0
    for i in temp_name:
        if not i == ',':
            element_total+=1
        else:
            final_total = element_total

    for x in range(0, element_length):
        new_last_name_total += 1

    last_name_total_temp = new_last_name_total - final_total
    last_name_total = -last_name_total_temp + 1

    last_name = temp_name[last_name_total::1]

    if not temp_name == ',':
        first_names.append(temp_name[0:final_total:1])
        last_names.append(last_name)
    

length_first_names = len(first_names)
for i in range(0, length_first_names):
    try:
        if first_names[i] == ',':
            first_names.pop(i)
    except:
        continue

length_last_names = len(last_names)
for i in range(0, length_last_names):
    try:
        if last_names[i] == ',':
            last_names.pop(i)
    except:
        continue

for element in last_names:
    if len(element) < 4:
        last_names.remove(element)

for element in first_names:
    if len(element) < 4:
        first_names.remove(element)

last_names.pop(-1)
first_names.pop(-1)

# Main Function. This is what generates the draft class. If you're lost here, let me give you some words of wisdom: I was once in your shoes, looking at programs that I thought I could never make.
# But keep working on it. You'll never be as good as me, but you can keep trying anyways.

def main_function(first_names, last_names, total):
    csv_name = input("Please enter the name of your CSV (Please add .csv to the end of the file name). Input: ")
    try:
        with open(csv_name, newline='') as csvfile:
            filecsv = csv.reader(csvfile, delimiter=' ', quotechar='|')
            global position_list
            global number_list
            position_list = []
            number_list = []

            for row in filecsv:
                total+=1
                position = str(row)
                temp_position = position.split(',')
                new_number = str(position[-5:-3:1])
                new_position = str(position[2:5:])
                if new_position[1:2:1] == ',':
                    position_temp = new_position[0:1:1]
                    position_list.append(position_temp)
                elif new_position[2:3:1] == ',':
                    position_temp = new_position[0:2:1]
                    position_list.append(position_temp)
                elif not new_position[2:3:1] == ',':
                    position_temp = new_position[0:3:1]
                    position_list.append(position_temp)

                if new_number[0:1:] == ',':
                    number_temp = new_number[1]

                else:
                    number_temp = new_number

                if number_temp[0:1:] == '0':
                    number_temp = number_temp[1::1]

                number_list.append(number_temp)
    except:
        print("Not a valid file name!")
        main_menu(first_names, last_names, total)

    for i in range(1, 4):
        number_list.pop(0)

    for i in range(1, 4):
        position_list.pop(0)

    with open('config.txt', 'r') as h:
        config = h.read()

    temp_total = 0
    if config == "True":
        for element in last_names:
            for i in range(0, len(element)):
                if element[i] == '-':
                    last_names.remove(element)
                    temp_total+=1
            if temp_total == 0:
                if element[-2::1] == "Jr":
                    last_names.remove(element)
                elif element[-2::1] == "Sr":
                    last_names.remove(element)
                elif element[-2::1] == "IV":
                    last_names.remove(element)
                elif element[-3::1] == "III":
                    last_names.remove(element)
                elif element[-1::1] == "V":
                    last_names.remove(element)
                elif element[-2::1] == "II":
                    last_names.remove(element)
                elif element[-3::1] == "Jr.0":
                    last_names.remove(element)
            temp_total = 0

    length_first = len(first_names)
    length_last = len(last_names)
    print(length_last)

    animation_num = 0
    with open("new.csv", 'w', newline='') as csvwriter:
        animation = [".", "..", "..."]
        global fnames_list
        global lnames_list
        global new_position_list
        global new_numbers_list
        fnames_list = []
        lnames_list = []
        classWriter = csv.writer(csvwriter)
        classWriter.writerow(["#Position", "fname", "lname", "JerseyNumber"])
        classWriter.writerow('')
        classWriter.writerow(["Team = DraftClass    Players:380"])
        output_total = 0
        for i in range(0, 380):
            random_number_first = (random.randint(1, length_first)) - 1
            random_number_last = (random.randint(1, length_last)) - 1
            try:
                first_name = first_names[random_number_first-1]
                last_name = last_names[random_number_last-1]
                fnames_list.append(first_name)
                lnames_list.append(last_name)
                classWriter.writerow([position_list[0], first_name, last_name, number_list[0]])
                new_numbers_list.append(number_list[0])
                new_position_list.append(position_list[0])
                number_list.pop(0)
                position_list.pop(0)
                sys.stdout.write("\r" + "Generating Draft Class" + animation[animation_num])
                time.sleep(0.03)
                sys.stdout.flush()
                if animation_num < 2:
                    animation_num+=1
                else:
                    animation_num = 0             

            except:
                if output_total == 0:
                    print("Draft Class Written to new.csv")
                    output_total+=1
                else:
                    continue
    sys.stdout.write(".Completed!")
    print("")
    print("Draft Class written to new.csv")

# Debug features - To access these use the term "debug_devmode" in the terminal
def debug_list_names(fnames_list, lnames_list):
    print(fnames_list)
    print(lnames_list)

def debug_list_others(position_list, number_list):
    print(position_list)
    print(number_list)

def generate_names(textName, acceptable_fnames_list, acceptable_lnames_list):
    try:
        with open(textName, 'r') as b:
            names_data = b.read()

        names_lines = names_data.split('\n')
        
        for element in names_lines:
            temp = element.split(',')
            if not temp == ['']:
                if len(temp) >= 4:
                    acceptable_fnames_list.append(temp[1])
                    acceptable_lnames_list.append(temp[2])
        acceptable_fnames_list.pop(0)
        acceptable_lnames_list.pop(0)
        g = open('acceptableNames.txt', 'w')
        for i in range(0, len(acceptable_fnames_list)):
            g.write(acceptable_fnames_list[i] + ',' + acceptable_lnames_list[i] + '\n')
        g.close()

    except:
        print("Not a valid file name!")
        main_menu(debug_devmode, new_numbers_list, new_position_list)

def disable_uniquenames():
    with open('config.txt', 'w') as z:
        z.write("False")

def enable_uniquenames():
    with open('config.txt', 'w') as y:
        y.write("True")

# Main menu function
def main_menu(debug_devmode, new_numbers_list, new_position_list):
    global textName

    if debug_devmode == True:
        print("Developer Debug Menu")
        print("1 - Print out the list of player first names (Debug)")
        print("2 - Print out the list of player last names (Debug)")
        print("3 - Print out the list of generated player first and last names (Debug)")
        print("4 - Print out the list of generated player positions and numbers (Debug)")
        print("5 - Exit debug mode.")

    main_menu_input = input("Input: ")

    if main_menu_input == "1" and debug_devmode == False:
        main_function(first_names, last_names, total)
    elif main_menu_input == "2" and debug_devmode == False:
        textName = input("Input the name of the roster file that you'd like to convert to acceptableNames.txt: ")
        generate_names(textName, acceptable_fnames_list, acceptable_lnames_list)
        print("New acceptableNames.txt generated! Restart the program to use the file.")
    elif main_menu_input == "3" and debug_devmode == False:
        disable_uniquenames()
    elif main_menu_input == "4" and debug_devmode == False:
        enable_uniquenames()
    elif main_menu_input == "5" and debug_devmode == False:
        webbrowser.open('https://github.com/2k5master/ESPN-NFL-2K5-Draft-Class-Generator')
    elif main_menu_input == "1" and debug_devmode == True:
        print(first_names)
    elif main_menu_input == "2" and debug_devmode == True:
        print(last_names)
    elif main_menu_input == "6" and debug_devmode == False:
        quit()
    elif main_menu_input == "4" and debug_devmode == True:
        debug_list_others(new_position_list, new_numbers_list)
    elif main_menu_input == "3" and debug_devmode == True:
        debug_list_names(fnames_list, lnames_list)
    elif main_menu_input == "5" and debug_devmode == True:
        debug_devmode = False
        print("Main Menu")
        print("")
        print('1 - Proceed and enter the name of your CSV')
        print("2 - Generate New acceptableNames.txt based on roster file")
        print("3 - Disable the removal of unique/recognizable names when generating draft class")
        print("4 - Enable the removal of unique/recognizable names when generating draft class")
        print("5 - Open the documentation")
        print("6 - Exit the application")
        print("debug - Enter debug mode")
    elif main_menu_input == "debug":
        debug_devmode = True
    else:
        print("Not a valid input!")

    main_menu(debug_devmode, new_numbers_list, new_position_list)
    
# Calls the main menu function
main_menu(debug_devmode, new_numbers_list, new_position_list)