from inputhdl import userinput
import os
import json

# Dictionary for question bank
question_bank = {
    "menu": """
Enter 1 for 'Add Entry'         
Enter 2 for 'Save Data'         
Enter 3 for 'Load Data'         
Enter 4 for 'Delete All Data'   
Enter 5 for 'Search'            
Enter 0 to 'Exit'               
""",
    "option_prompt": "Enter your Option from above: ",
    "name_prompt": "Enter your Name: ",
    "age_prompt": "Enter your Age: ",
    "score_prompt": "Enter your Score: ",
    "search_prompt": "Enter name of student: ",
    "invalid_age": "Invalid Age, Please try again",
    "invalid_input": "Error! Need 3 inputs separated by a ',', Please try again",
    "bye": "BYE!",
    "data_saved": "\n\n**Data Saved!!!**\n\n\n",
    "error_saving_file": "Error saving file",
    "error_loading_file": "Error loading file",
    "file_deleted": "File deleted successfully!",
    "file_not_exist": "The file does not exist"
}

students = []

def print_list(students):
    for stdt in students:
        print(f"Name: {stdt['name']}, Score: {stdt['score']}")

def add_entry():
    student = {}
    try:
        student["name"] = userinput.getString(question_bank["name_prompt"])
        student["age"] = userinput.getInt(question_bank["age_prompt"])
        student["score"] = userinput.getInt(question_bank["score_prompt"])
        if student["age"] > 30:
            raise Exception("Invalid Age!")
    except ValueError:
        print(question_bank["invalid_input"])
    except Exception as e:
        print(str(e))
    else:
        students.append(student)
    finally:
        print(question_bank["data_saved"])

def save_data():
    try:
        with open("students.txt", 'w') as the_file:
            json.dump(students, the_file)
    except Exception as e:
        print(f"{question_bank['error_saving_file']}: {str(e)}")

def load_data():
    global students
    try:
        with open("students.txt", 'r') as the_file:
            students = json.load(the_file)
    except Exception as e:
        print(f"{question_bank['error_loading_file']}: {str(e)}")
    else:
        print_list(students)

def delete_data():
    try:
        os.remove('students.txt')
    except FileNotFoundError:
        print(question_bank["file_not_exist"])
    else:
        print(question_bank["file_deleted"])

def search_student():
    s_name = userinput.getString(question_bank["search_prompt"])
    filtlist = list(filter(lambda listItem: listItem["name"] == s_name, students))
    print_list(filtlist)

def get_data():
    while True:
        print(question_bank["menu"])
        my_inp = userinput.getInt(question_bank["option_prompt"])

        if my_inp == 0:
            print(question_bank["bye"])
            break
        elif my_inp == 1:
            add_entry()
        elif my_inp == 2:
            save_data()
        elif my_inp == 3:
            load_data()
        elif my_inp == 4:
            delete_data()
        elif my_inp == 5:
            search_student()
        else:
            print("Invalid option, please try again.")

# Call the function to start the program
get_data()
