import csv, datetime, os, re


ENTRIES = []


# Feel free to add entries and test them out. 
# If short on time here are a few samples. 

#ENTRIES = [[datetime.datetime(2019, 3, 25, 0, 0), 'Task 1', 10, 'today'], 
           #[datetime.datetime(2019, 3, 29, 0, 0), 'Task', 20, 'tomorrow'],
           #[datetime.datetime(2019, 4, 1, 0, 0), 'April Fools', 40, 'Joke-day'], 
           #[datetime.datetime(2019, 4, 1, 0, 0), 'May fifth month', 40, 'another time']]


def clear_screen():
    """Clears the screen from any previous output."""

    os.system('cls' if os.name == 'nt' else 'clear')


def csv_header():
    """Creates a csv file with the desired header row."""
    
    with open('work_log.csv', 'w') as csvfile:
        fieldnames = [
            "Date",
            "Task Name",
            "Time Spent (Rounded minutes)", 
            "Notes (Optional)"
        ]
        
        t_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        t_writer.writeheader()


def csv_data_gatherer():
    """Gathers data from csv file if it exists. Otherwise it creates one."""
    
    try:
        
        with open('work_log.csv', mode='r', newline='') as csv_file:
            data = csv.DictReader(csv_file)
            rows = list(data)

            data_from_csv = []
            
            for row in rows:
                data_to_list = []
                if row["Date"]:
                    string_date = row["Date"]
                    sds = string_date.split("-")
                    sd_to_obj = datetime.datetime.strptime(
                        "{}/{}/{}".format(
                            sds[0],sds[1],sds[2][:2]), '%Y/%m/%d')
                    
                    data_to_list.append(sd_to_obj)
                    data_to_list.append(row["Task Name"])
                    data_to_list.append(int(row["Time Spent (Rounded minutes)"]))
                    data_to_list.append(row["Notes (Optional)"])
                    data_from_csv.append(data_to_list)

            for x in data_from_csv:
                ENTRIES.append(x)
            
    except FileNotFoundError:
        csv_header()
        

def entry_to_csv():
    """Takes an entry and appends the info to the csv file."""
    
    with open('work_log.csv', 'a') as csvfile:
        fieldnames = [
            "Date",
            "Task Name",
            "Time Spent (Rounded minutes)", 
            "Notes (Optional)"
        ]
        
        t_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        n = 0
        for x in ENTRIES:
            t_writer.writerow({"Date":ENTRIES[n][0],
                               "Task Name":ENTRIES[n][1],
                               "Time Spent (Rounded minutes)":ENTRIES[n][2],
                               "Notes (Optional)":ENTRIES[n][3]})
            n += 1

            
def csv_starter():
    """Checks that a csv file is created once per run of the app."""

    z = 0
    for _ in range(0,1):
        if z == 0:
            csv_data_gatherer()
        z +=1


def main_menu():
    """Displays the main menu of the app."""
    
    csv_starter()
    
    main_menu_options = """
WORK LOG
--------
What Would you like to do?
A) Add new entry
B) Search in existing entries
C) Quit program 
"""

    main_menu_answer = ''

    while (not main_menu_answer == 'a' or 
    not main_menu_answer == 'b' or  
    not main_menu_answer == 'c'):
        
        print(main_menu_options)

        main_menu_answer = input().lower()

        if main_menu_answer == 'a':
            clear_screen()
            add_new_entry()
            
        elif main_menu_answer == 'b':
            clear_screen()
            search_by_menu()
              
        elif main_menu_answer == 'c':
            csv_header()
            entry_to_csv()
            clear_screen()
            break
            
        else:
            print("That's not a valid choice.")
            input("Press enter to try again.")
            clear_screen()
            
    print("Thank you for using Work Log.")
    print("See you later!")


def add_new_entry():
    """Add an entry with a date, title, time spent, and notes."""
    
    new_entry = []

    while True:
        
        print("Date of the task")
        date_of_task = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            validate_date = datetime.datetime.strptime(
                date_of_task, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format.")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
    
    clear_screen()
    dots = date_of_task.split("/")
    obj_dot = datetime.datetime.strptime(
        "{}/{}/{}".format(dots[2],dots[0],dots[1]), '%Y/%m/%d')
    
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


def edit_date_of_entry():
    """creates a date that can then substitute an existing one."""
    
    clear_screen()

    while True:
        
        print("Date of the task")
        edit_date_of_task = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            validate_date = datetime.datetime.strptime(
                edit_date_of_task, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format.")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
    
    edots = edit_date_of_task.split("/")
    obj_edot = datetime.datetime.strptime(
        "{}/{}/{}".format(edots[2],edots[0],edots[1]), '%Y/%m/%d')

    return obj_edot


def edit_title_of_entry():
    """creates a title that can then substitute an existing one."""
    
    clear_screen()
    edit_title_of_the_task = input("Title of the task: ")
    
    return edit_title_of_the_task


def edit_time_spent():
    """creates a time that can then substitute an existing one."""
    
    clear_screen()
    
    while True:
        
        try:
            edit_time_spent = int(input("Time spent (rounded minutes): "))
        
        except:
            print("That's not a number. Try again.")
            input("Press enter to try again.")
            clear_clear_screen()
        
        else:
            break
    
    return edit_time_spent


def edit_task_notes():
    """creates notes that can then substitute an existing one."""
    
    clear_screen()
    edit_task_notes = input("Notes (Optional, you can leave this empty): ")
    
    return edit_task_notes


def display_entries(list):
    """Displays entries and let's you scroll through them. 
    The list parameter needs to hold entries in a format as such
    [date, title, time spent, notes]
    """
    
    n = 0
    while True:
        
        if len(list) >= 1:
            
            if n == -1:
                n += 1
                
            print("Date: {}".format(list[n][0].strftime("%m/%d/%Y")))
            print("Task: {}".format(list[n][1]))
            print("Time To Complete: {} minutes".format(list[n][2]))
            print("Notes: {}".format("".join(list[n][3])))
            print("")
            print("Result {} of {}".format((n+1), len(list)))
            print("")

            choices = ["[N]ext", "[P]revious", "[E]dit",
                       "[D]elete", "[R]eturn to previous menu"]

            if n == 0:
                choices.remove("[P]revious")

            if n == (len(list)-1):
                choices.remove("[N]ext")

            print("{}".format(', '.join(choices)))

            display_entries_selection = input().lower()

            if display_entries_selection == 'p' and n == 0:
                n = n 

            elif display_entries_selection == 'p' and n != 0:
                n -= 1

            if display_entries_selection == 'n' and n == len(list):
                n = n

            elif display_entries_selection == 'n' and n != len(list) - 1:
                n += 1

            if display_entries_selection == 'e':
                list[n][0] = edit_date_of_entry()
                list[n][1] = edit_title_of_entry()
                list[n][2] = edit_time_spent()
                list[n][3] = edit_task_notes()
                clear_screen()
                csv_header()
                entry_to_csv()

            if display_entries_selection == 'd':
                if list[n] in ENTRIES:
                    ENTRIES.remove(list[n])
                    csv_header()
                    entry_to_csv()

                del list[n] 
                n -= 1

            if display_entries_selection == 'r':
                break

            clear_screen()
            
        else:
            break
            
    clear_screen()
    
   
def search_by_menu():
    """Displays the search menu of the app."""
    
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
            
        elif search_by_answer == 'b':
            clear_screen()
            range_of_dates()
            
        elif search_by_answer == 'c':
            clear_screen()
            exact_search()
            
        elif search_by_answer == 'd':
            clear_screen()
            find_by_pattern()
            
        elif search_by_answer == 'e':
            clear_screen()
            exact_time_spent()
            
        elif search_by_answer == 'f':
            clear_screen()
            break
            
        else:
            print("That's not a valid choice.")
            input("Press enter to try again.")
            clear_screen()
            

def exact_date():
    """Searches the list of entries through the date."""
    
    while True:
        
        print("Enter the date")
        exact_date = input("Please use MM/DD/YYYY: ")
        time_format = '%m/%d/%Y'
        
        try:
            test_date = datetime.datetime.strptime(exact_date, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format.")
            input("Press enter to try again.")
            clear_screen()
 
        else:
            break
                   
    eds = exact_date.split("/")
    obj_ed = datetime.datetime.strptime(
        "{}/{}/{}".format(eds[2],eds[0],eds[1]), '%Y/%m/%d')

    real_entries = []
    for x in ENTRIES:
        if obj_ed in x:
            real_entries.append(x)
            clear_screen()
            
    if len(real_entries) >= 1:
        display_entries(real_entries)
  
    if len(real_entries) == 0:
        clear_screen()
        print("There are no entries with the date {}.".format(exact_date))
        print("Press enter to return to the search menu.")
        input()
        clear_screen()
    

def range_of_dates():
    """Searches the list of entries between two dates."""

    while True:
        
        print("Enter two dates. The search will find ")
        print("all the entries between start date and the end date.")
        print()
        
        first_date = input("From: (Please use MM/DD/YYYY) ")
        time_format = '%m/%d/%Y'
        
        try:
            test_date = datetime.datetime.strptime(first_date, time_format)
            
        except ValueError:
            print("That's not a valid date or MM/DD/YYYY format.")
            input("Press enter to try again.")
            clear_screen()
            
        else:
            break
            
    fds = first_date.split("/")
    obj_fd = datetime.datetime.strptime(
        "{}/{}/{}".format(fds[2],fds[0],fds[1]), '%Y/%m/%d')
    
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
    obj_sd = datetime.datetime.strptime(
        "{}/{}/{}".format(sds[2],sds[0],sds[1]), '%Y/%m/%d')
    
    clear_screen()
    
    print("These are all the entries dated between {} and {}.".format(
        first_date, second_date))
    print()
    
    range_of_entries = []
    for x in ENTRIES:
        if ((x[0] >= obj_fd and x[0] < obj_sd
        or x[0] < obj_fd and x[0] >= obj_sd)):
            range_of_entries.append(x)
            
    if len(range_of_entries) >= 1:         
        display_entries(range_of_entries)
            
    if len(range_of_entries) == 0:
        clear_screen()
        print("There are no entries between the dates {} and {}".format(
            first_date, second_date))
        print("Press enter to return to the search menu.")
        input()
    
    clear_screen()

 
def exact_search():
    """Searches the list of entries through words and part of words in
    the title and/or notes.
    """
    
    print("Enter the exact word or part of the word you are searching for.")
    print("That might be found in either the task name or notes.")
    print("REMEMBER: The search is case sensitive.")
    
    print("")
    exact_word_search = input("The search term is: ")
    print("")
    
    clear_screen()
    print("The search term is: {}".format(exact_word_search))
    print("")
    
    entries_with_search_word = []
    for x in ENTRIES:
        if exact_word_search in x[1] or exact_word_search in x[3]:
            entries_with_search_word.append(x)
            
    if len(entries_with_search_word) >= 1:         
        display_entries(entries_with_search_word) 
    
    
    if len(entries_with_search_word) == 0:
        clear_screen()
        print("There are no entries that contain the word {}".format
              (exact_word_search))
        print("Press enter to return to the search menu.")
        input()
        
    clear_screen()


def find_by_pattern():
    """Searches the list of entries with RegEx patterns 
    through characters in the title and/or notes.
    """
    
    print("Use RegEx to find desired information in the task name or notes.")
    print("")
    regex_search = input('Regex Pattern: ')
    print("")
    
    try:
        compiled_search = re.compile(regex_search)
        
    except re.error:
        clear_screen()
        print("No results found.")
    
    else:
        clear_screen()
        print("Regex Pattern: {}".format(regex_search))
        print("")
        
        entries_with_regex = []
        for x in ENTRIES:
            if compiled_search.search(x[1]) or compiled_search.search(x[3]):
                entries_with_regex.append(x)
                
        if len(entries_with_regex) >= 1:         
            display_entries(entries_with_regex)    

    clear_screen()
    print("Press enter to return to the search menu.")
    input()
    clear_screen()


def exact_time_spent():
    """Searches the list of entries through exact time in the time spent
    section of the entry.
    """
    
    while True:
        
        try:
            print("Enter the exact amount of time spent on a task.")
            exact_time_spent = int(input("Time spent (rounded minutes): "))
        
        except:
            print("That's not a number. Try again.")
            clear_screen()
        
        else:
            break
    
    clear_screen()
    
    real_times = []
    for x in ENTRIES:
        if exact_time_spent in x:
            real_times.append(x)
            
    if len(real_times) >= 1:         
        display_entries(real_times)        
            
    if len(real_times) == 0:
        print("An entry with the time spent on a") 
        print("task of {} minutes doesn't exist.".format(exact_time_spent))
    
    print("")
    print("Press enter to return to the search menu.")
    input()
    clear_screen()

  
if __name__ == '__main__':
    main_menu()

