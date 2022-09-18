# Imports
import names
import csv
import random
import webbrowser

total = 0

print("ESPN NFL 2K5 Draft Class Generator by 2k5master")
print("Main Menu")
print("1 - Proceed and enter the name of your CSV")
print("2 - Open the documentation")
print("3 - Print out the list of player first names (Debug)")
print("4 - Print out the list of player last names (Debug)")
print("5 - Exit the application")

with open('acceptableNames.txt', 'r') as text_raw:
    text = text_raw.read()

edited_text = text.split("\n")

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

def main_menu():
    main_menu_input = input("Input:")

    if main_menu_input == "1":
        csv_name = input("Please enter the name of your CSV (Please add .csv to the end of the file name). Input: ")
        with open(csv_name, newline='') as csvfile:
        filecsv = csv.reader(csvfile, delimiter=' ', quotechar='|')
        position_list = []
        number_list = []

        for row in filecsv:
            total+=1
            position = str(row)
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

        for i in range(1, 4):
            number_list.pop(0)

        for i in range(1, 4):
            position_list.pop(0)

        length_first = len(first_names)
        length_last = len(last_names)

        with open("new.csv", 'w', newline='') as csvwriter:
            classWriter = csv.writer(csvwriter)
            classWriter.writerow(["#Position", "fname", "lname", "JerseyNumber"])
            classWriter.writerow('')
            classWriter.writerow(["Team = DraftClass    Players:380"])
            output_total = 0
            for i in range(0, 380):
                names_list = []
                random_number_first = (random.randint(1, length_first)) - 1
                random_number_last = (random.randint(1, length_last)) - 1
                new_first_names = names.get_first_name(gender='male')
                new_last_names = names.get_last_name()
                try:
                    classWriter.writerow([position_list[0], first_names[random_number_first-1], last_names[random_number_last-1], number_list[0]])
                    number_list.pop(0)
                    position_list.pop(0)
                except:
                    if output_total == 0:
                        print("Draft Class Written to new.csv")
                        output_total+=1
                    else:
                        continue

        print("Draft Class written to new.csv")
        if main_menu_input == "2":
            webbrowser.open("https://github.com/2k5master/ESPN-NFL-2K5-Draft-Class-Generator")
        if main_menu_input == "3":
            with open("debug_fnames.txt", "w") as f:
                for element in first_names:
                    f.appened(element)

    main_menu()

main_menu()



    


                
            




        





