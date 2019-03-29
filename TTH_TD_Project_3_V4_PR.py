import csv, datetime, os, re

ENTRIES = []


# Feel free to add entries and test them out. 
# If short on time here are a few samples. 

#ENTRIES = [[datetime.datetime(2019, 3, 25, 0, 0), 'Task 1', 10, 'today'], 
           #[datetime.datetime(2019, 3, 29, 0, 0), 'Task', 20, 'tomorrow'],
           #[datetime.datetime(2019, 4, 1, 0, 0), 'April Fools', 40, 'Joke-day'], 
           #[datetime.datetime(2019, 4, 1, 0, 0), 'May fifth month', 40, 'another time']]
        

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    
    main_menu_options = """
WORK LOG
--------
What Would you like to do?
A) Add new entry
B) Search in existing entries
C) Display entries
D) Quit program 
"""

    main_menu_answer = ''

    while not main_menu_answer == 'a' or not main_menu_answer == 'b' or not main_menu_answer == 'c':
        
        print(main_menu_options)

        main_menu_answer = input().lower()

        if main_menu_answer == 'a':
            clear_screen()
            add_new_entry()
            break
            
        elif main_menu_answer == 'b':
            clear_screen()
            search_by_menu()
            break
            
        elif main_menu_answer == 'c':
            clear_screen()
            display_entries()
            break
            
        elif main_menu_answer == 'd':
            entry_to_csv()
            clear_screen()
            print("Thank you for using Work Log. See you later!")
            break
            
        else:
            print("That's not a valid choice.")
            input("Press enter to try again.")
            clear_screen()


def entry_to_csv():
    
    with open('work_log.csv', 'w') as csvfile:
        fieldnames = ["Date","Task Name","Time Spent (Rounded minutes)", "Notes (Optional)"]
        t_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        t_writer.writeheader()
        
        n = 0
        for x in ENTRIES:
            t_writer.writerow({"Date":ENTRIES[n][0].strftime("%m/%d/%Y"),
                               "Task Name":ENTRIES[n][1],
                               "Time Spent (Rounded minutes)":ENTRIES[n][2],
                               "Notes (Optional)":ENTRIES[n][3]})
            n += 1
            

def add_new_entry():
    
    new_entry = []

    while True:
        
        print("Date of the task")
        date_of_task = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            validate_date = datetime.datetime.strptime(date_of_task, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format. Try again.")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
    
    clear_screen()
    dots = date_of_task.split("/")
    obj_dot = datetime.datetime.strptime("{}/{}/{}".format(dots[2],dots[0],dots[1]), '%Y/%m/%d')
    new_entry.append(obj_dot)

    title_of_the_task = input("Title of the task: ")
    new_entry.append(title_of_the_task)
    clear_screen()
    
    while True:
        
        try:
            time_spent = int(input("Time spent (rounded minutes): "))
        
        except:
            print("That's not a number. Try again.")
        
        else:
            new_entry.append(time_spent)
            clear_screen()
            break
            
    task_notes = input("Notes (Optional, you can leave this empty): ")
    new_entry.append(task_notes)
    
    ENTRIES.append(new_entry)
    
    entry_to_csv()
    
    clear_screen()
    print("The entry has been added. Press enter to return to the menu. ")
    input()
    clear_screen()
    main_menu()
    

def edit_date_of_entry():
    
    clear_screen()

    while True:
        
        print("Date of the task")
        edit_date_of_task = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            validate_date = datetime.datetime.strptime(edit_date_of_task, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format. Try again. ")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
    
    edots = edit_date_of_task.split("/")
    obj_edot = datetime.datetime.strptime("{}/{}/{}".format(edots[2],edots[0],edots[1]), '%Y/%m/%d')

    return obj_edot


def edit_title_of_entry():
    
    clear_screen()
    edit_title_of_the_task = input("Title of the task: ")
    
    return edit_title_of_the_task


def edit_time_spent():
    
    clear_screen()
    
    while True:
        
        try:
            edit_time_spent = int(input("Time spent (rounded minutes): "))
        
        except:
            print("That's not a number. Try again.")
            input("Press enter to try again.")
            clear_screen()
        
        else:
            break
    
    return edit_time_spent


def edit_task_notes():
    
    clear_screen()
    edit_task_notes = input("Notes (Optional, you can leave this empty): ")
    
    return edit_task_notes


def display_entries():
    
    n = 0
    while True:
        
        if len(ENTRIES) >= 1:
            
            if n == -1:
                n += 1
                
            print("Date: {}".format(ENTRIES[n][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(ENTRIES[n][1]))
            print("Time To Complete: {} minutes".format(ENTRIES[n][2]))
            print("Notes: {}".format("".join(ENTRIES[n][3])))
            print("")
            print("Result {} of {}".format((n+1), len(ENTRIES)))
            print("")

            choices = ["[N]ext", "[P]revious", "[E]dit",
                       "[D]elete", "[R]eturn to previous menu"]

            if n == 0:
                choices.remove("[P]revious")

            if n == (len(ENTRIES)-1):
                choices.remove("[N]ext")

            print("{}".format(', '.join(choices)))

            display_entries_selection = input().lower()

            if display_entries_selection == 'p' and n == 0:
                n = n 

            elif display_entries_selection == 'p' and n != 0:
                n -= 1

            if display_entries_selection == 'n' and n == len(ENTRIES):
                n = n

            elif display_entries_selection == 'n' and n != len(ENTRIES) - 1:
                n += 1

            if display_entries_selection == 'e':
                
                ENTRIES[n][0] = edit_date_of_entry()
                ENTRIES[n][1] = edit_title_of_entry()
                ENTRIES[n][2] = edit_time_spent()
                ENTRIES[n][3] = edit_task_notes()
                clear_screen()
                entry_to_csv()

            if display_entries_selection == 'd':
                del ENTRIES[n]
                n -= 1

            if display_entries_selection == 'r':
                break

            clear_screen()
            
        else:
            print("There are no entries.")
            print("Press enter to return to main menu.")
            input()
            break
            
    clear_screen()
    main_menu()
    

def search_by_menu():
    
    search_by_menu = """
Do you want to search by: 
A) Exact Date
B) Range of Dates
C) Exact Search
D) Regex Pattern
E) Exact Time 
F) Return to menu
"""

    search_by_answer = ''
    
    while (not search_by_answer == 'a' or not search_by_answer == 'b' 
           or not search_by_answer == 'c' or not search_by_answer == 'd'
           or not search_by_answer == 'e'):
        
        print(search_by_menu)
        
        search_by_answer = input().lower()

        if search_by_answer == 'a':
            clear_screen()
            exact_date()
            break
            
        elif search_by_answer == 'b':
            clear_screen()
            range_of_dates()
            break
            
        elif search_by_answer == 'c':
            clear_screen()
            exact_search()
            break
            
        elif search_by_answer == 'd':
            clear_screen()
            find_by_pattern()
            break
            
        elif search_by_answer == 'e':
            clear_screen()
            exact_time_spent()
            break
            
        elif search_by_answer == 'f':
            clear_screen()
            main_menu()
            break
            
        else:
            print("That's not a valid choice.")
            input("Press enter to try again.")
            clear_screen()
            

def exact_date():
    
    while True:
        
        print("Enter the date")
        exact_date = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            test_date = datetime.datetime.strptime(exact_date, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format. Try again. ")
            input("Press enter to try again.")
            clear_screen()
 
        else:
            break
                   
    eds = exact_date.split("/")
    obj_ed = datetime.datetime.strptime("{}/{}/{}".format(eds[2],eds[0],eds[1]), '%Y/%m/%d')

    real_entries = []
    for x in ENTRIES:
        if obj_ed in x:
            real_entries.append(x)
            
            clear_screen()
            print("Date: {}".format(real_entries[0][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(real_entries[0][1]))
            print("Time To Complete: {} minutes".format(real_entries[0][2]))
            print("Notes: {}".format(real_entries[0][3]))
            print("")
            print("Press enter to return to the search menu.")
            input()
            clear_screen()
            break
            
    if len(real_entries) == 0:
        clear_screen()
        print("An entry with the date {} doesn't exist.".format(exact_date))
        print("")
        print("Press enter to return to the search menu.")
        input()
        clear_screen()
        
    search_by_menu()
    

def range_of_dates():

    while True:
        
        print("Enter two dates. The search will find ")
        print("all the entries between first date and the end date.")
        print()
        first_date = input("From: (Please use MM/DD/YYYY) ")
        time_format = '%m/%d/%Y'
        
        try:
            test_date = datetime.datetime.strptime(first_date, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format. Try again. ")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
            
    fds = first_date.split("/")
    obj_fd = datetime.datetime.strptime("{}/{}/{}".format(fds[2],fds[0],fds[1]), '%Y/%m/%d')
    clear_screen()
    
    while True:
        
        second_date = input("To: (Please use MM/DD/YYYY) ")
        time_format = '%m/%d/%Y'
        
        try:
            test_date_2 = datetime.datetime.strptime(second_date, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format. Try again.")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
    
    sds = second_date.split("/")
    obj_sd = datetime.datetime.strptime("{}/{}/{}".format(sds[2],sds[0],sds[1]), '%Y/%m/%d')
    clear_screen()
    
    print("These are all the entries dated between {} and {}.".format(first_date, second_date))
    print()
    
    n = 0
    range_of_entries = []
    for x in ENTRIES:
        if ((x[0] > obj_fd and x[0] < obj_sd
        or x[0] < obj_fd and x[0] >= obj_sd)):
            range_of_entries.append(x)
            
            print("----------------")
            print("Date: {}".format(range_of_entries[n][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(range_of_entries[n][1]))
            print("Time To Complete: {} minutes".format(range_of_entries[n][2]))
            print("Notes: {}".format(range_of_entries[n][3]))
            print("")
            n += 1
            
    if len(range_of_entries) == 0:
        clear_screen()
        print("There are no entries with the dates {} and {}".format(first_date, second_date))
    
    print("Press enter to return to the search menu.")
    input()
    clear_screen()
        
    search_by_menu()
    

def exact_time_spent():
    
    while True:
        
        try:
            print("Enter the exact amount of time spent on a task.")
            exact_time_spent = int(input("Time spent (rounded minutes): "))
        
        except:
            print("That's not a number. Try again.")
            input("Press enter to try again.")
            clear_screen()
        
        else:
            break
    
    clear_screen()
    
    n = 0
    real_times = []
    for x in ENTRIES:
        if exact_time_spent in x:
            real_times.append(x)
            
            print("----------------")
            print("Date: {}".format(real_times[n][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(real_times[n][1]))
            print("Time To Complete: {} minutes".format(real_times[n][2]))
            print("Notes: {}".format(real_times[n][3]))
            print("")
            n += 1
            
    if len(real_times) == 0:
        print("An entry with the time spent on a") 
        print("task of {} minutes doesn't exist.".format(exact_time_spent))
    
    print("")
    print("Press enter to return to the search menu.")
    input()
    clear_screen()
        
    search_by_menu()
    

def exact_search():
    
    print("Enter the exact word or part of the word you are searching for.")
    print("That might be found in either the task name or notes.")
    print("REMEMBER: The search is case sensitive.")
    
    print("")
    exact_word_search = input("The search term is: ")
    print("")
    
    clear_screen()
    print("The search term is: {}".format(exact_word_search))
    print("")
    
    n = 0
    entries_with_search_word = []
    for x in ENTRIES:
        if exact_word_search in x[1] or exact_word_search in x[3]:
            entries_with_search_word.append(x)
            
            print("----------------")
            print("Date: {}".format(entries_with_search_word[n][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(entries_with_search_word[n][1]))
            print("Time To Complete: {} minutes".format(entries_with_search_word[n][2]))
            print("Notes: {}".format(entries_with_search_word[n][3]))
            print("")
            n += 1 
            
    print("")
    print("Press enter to return to the search menu.")
    input()
    clear_screen()
        
    search_by_menu()
    

def find_by_pattern():
    
    print("Use RegEx to find desired information in the task name or notes.")
    
    print("")
    regex_search = input('Regex Pattern: ')
    print("")
    
    try:
        compiled_search = re.compile(regex_search)
        
    except re.error:
        clear_screen()
        print("No results found.")
        input("Press enter to try again.")
    
    else:
        clear_screen()
        print("Regex Pattern: {}".format(regex_search))
        print("")
        
        n = 0
        entries_with_regex = []
        
        for x in ENTRIES:
            if compiled_search.search(x[1]) or compiled_search.search(x[3]):
                entries_with_regex.append(x)
                
                print("----------------")
                print("Date: {}".format(entries_with_regex[n][0].strftime("%m/%d/%Y")))
                print("Task: {}".format(entries_with_regex[n][1]))
                print("Time To Complete: {} minutes".format(entries_with_regex[n][2]))
                print("Notes: {}".format(entries_with_regex[n][3]))
                n += 1  

    print("")
    print("Press enter to return to the search menu.")
    input()
    clear_screen()
        
    search_by_menu()
    

if __name__ == '__main__':
    main_menu()
