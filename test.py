# # # # # # # # # # myListi = [23,4,1,45,123,46,5433,21]
# # # # # # # # # # print (myListi)

# # # # # # # # # # passWord = input ("please enter password ")
# # # # # # # # # # count = 1 
# # # # # # # # # # while count <3 :
# # # # # # # # # #     print ("incorrenct password please try again ")
# # # # # # # # # #     if count<3:
# # # # # # # # # #         passWord= input("please enter the passwrd ")
# # # # # # # # # #         count +=1

        
        
        
        

        
        
# # # # # # # # # # b= {"brand":"tata",
# # # # # # # # # # "model":"harrier"
# # # # # # # # # # }


# # # # # # # # # # accuracyfCar = [ ]
# # # # # # # # # # choice = 0 
# # # # # # # # # # while choice !=3:
# # # # # # # # # #     choice = input("enter your ")

 










# # # # # # # # # # Function to read JSON file and print name and score
# # # # # # # # # def print_names_and_scores(data):
# # # # # # # # #     # Open and load the JSON data

    
# # # # # # # # #     # Iterate through each entry in the JSON data
# # # # # # # # #     for entry in data:
# # # # # # # # #         name = entry.get('name')
# # # # # # # # #         score = entry.get('score')
# # # # # # # # #         print(f"Name: {name}, Score: {score}")

# # # # # # # # # # File path to the JSON file
# # # # # # # # # json_file = [
# # # # # # # # #     {
# # # # # # # # #         "name": "Alice",
# # # # # # # # #         "score": 95
# # # # # # # # #     },
# # # # # # # # #     {
# # # # # # # # #         "name": "Bob",
# # # # # # # # #         "score": 88
# # # # # # # # #     },
# # # # # # # # #     {
# # # # # # # # #         "name": "Charlie",
# # # # # # # # #         "score": 72
# # # # # # # # #     }
# # # # # # # # # ]


# # # # # # # # # # Call the function
# # # # # # # # # print_names_and_scores(json_file)

















# # # # # # # # cars= [
# # # # # # # #     {"brand":"tata","model":"punch","year":2020 ,"color":"red"},
# # # # # # # #     {"brand":"tata","model":"punch","year":2020, "color":"red"},
# # # # # # # # ]










# # # # # # # def printMany (*v):
# # # # # # #     for a in v :
# # # # # # #         print (f"you provided :{a}")
        
# # # # # # # printMany ("Hello ", 234, True , [3,2,6], 0)
# # # # # # # def printManyPairs (**pairs ):
# # # # # # #     for key,value in pairs.items ():
# # # # # # #         print (f"{key}|value :{value}")
# # # # # # # printManyPairs (name =  "Jayesh ", last_name="raut")


# # # # # # myList = [1,2,34,5,8,12,3,23,2,24,2]
# # # # # # for i in range (len(myList)):
# # # # # #     myList [i]= myList[i]/2

# # # # # # print (myList)



# # # # # # import numpy as np
# # # # # # def generte (a,b ):
# # # # # #     np.random.seed (110)
# # # # # #     return np.random.randint (a,b)

# # # # # # generte(1,10)






# # # # # # # Global variable to hold data
# # # # # # data = None

# # # # # # def getData():
# # # # # #     try:
# # # # # #         if data is None:
# # # # # #             raise ValueError("No data available")
# # # # # #         return data
# # # # # #     except ValueError as e:
# # # # # #         return str(e)

# # # # # # def putData(new_data):
# # # # # #     global data
# # # # # #     try:
# # # # # #         data = new_data
# # # # # #         return "Data stored successfully"
# # # # # #     except Exception as e:
# # # # # #         return f"An error occurred: {str(e)}"

# # # # # # # Store some data
# # # # # # response = putData("Sample Data")
# # # # # # print(response)

# # # # # # # Retrieve and print the data
# # # # # # retrieved_data = getData()
# # # # # # print("Retrieved Data:", retrieved_data)

# # # # # # # Attempt to get data when none is set (to demonstrate error handling)
# # # # # # data = None  # Resetting data to None to force an error
# # # # # # retrieved_data = getData()
# # # # # # print("Retrieved Data after resetting:", retrieved_data)

# # # # # # # Final statement
# # # # # # print("bye! bye!")
















# # # # # # def get_student_data():
# # # # # #     """Prompts the user for student information (name, age, score)
# # # # # #     and stores it in a dictionary.

# # # # # #     Returns:
# # # # # #         A dictionary containing student information or None if user enters 'exit'.
# # # # # #     """
# # # # # #     while True:
# # # # # #         user_input = input("Enter student information (name, age, score) separated by commas, or 'exit' to quit: ")
# # # # # #         if user_input.lower() == 'exit':
# # # # # #             return None

# # # # # #         try:
# # # # # #             student_info = user_input.split(",")
# # # # # #             student = {
# # # # # #                 "name": student_info[0].strip(),
# # # # # #                 "age": int(student_info[1]),
# # # # # #                 "score": int(student_info[2]),
# # # # # #             }

# # # # # #             if student["age"] > 30:
# # # # # #                 raise ValueError("Age cannot be greater than 30")

# # # # # #             return student

# # # # # #         except ValueError as e:
# # # # # #             print(f"Error: {e}. Please enter three comma-separated integers for age and score.")
# # # # # #         except Exception as e:
# # # # # #             print(f"Unexpected error: {e}. Please try again.")


# # # # # # student_data = get_student_data()
# # # # # # if student_data:
# # # # # #     print(f"Student information: {student_data}")













# # # # # students = [] 
# # # # # myInp = input("Enter data (name,age,score) or 'exit' to quit: ")  # Get user input

# # # # # def getData():
# # # # #     if myInp == 'exit':
# # # # #         print("BYE")
# # # # #     else:
# # # # #         student = {}
# # # # #         try:
# # # # #             temp_ = myInp.split(",") 
# # # # #             student["name"] = temp_[0]
# # # # #             student["age"] = int(temp_[1]) 
# # # # #             student["score"] = int(temp_[2]) 

# # # # #             if student["age"] > 30:
# # # # #                 raise Exception("Invalid Age")
# # # # #         except ValueError:
# # # # #             print("Try again (incorrect data format)")
# # # # #         except Exception as e:  
# # # # #             print(f"Invalid: {e}")  
# # # # #         else:
# # # # #             students.append(student)  
# # # # #             with open("file.txt", "a") as file: 
# # # # #                 file.write(f"Student data added: {student}\n")  


# # # # # getData()

# # # # # if students:
# # # # #     print("\nAll student data:")
# # # # #     for student in students:
# # # # #         print(student)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# # # # students = [] 

# # # # def getData():
# # # #     while True:
# # # #         myInp = input("Enter data (name,age,score) or 'save&exit' to quit: ")
# # # #         if myInp == 'save&exit':
# # # #             print("BYE")
# # # #             break
# # # #         else:
# # # #             student = {}
# # # #             try:
# # # #                 temp_ = myInp.split(",") 
# # # #                 student["name"] = temp_[0]
# # # #                 student["age"] = int(temp_[1]) 
# # # #                 student["score"] = int(temp_[2]) 

# # # #                 if student["age"] > 30:
# # # #                     raise Exception("Invalid Age")
# # # #             except ValueError:
# # # #                 print("Try again (incorrect data format)")
# # # #             except Exception as e:  
# # # #                 print(f"Invalid: {e}")  
# # # #             else:
# # # #                 students.append(student)  
# # # #                 with open("file.txt", "a") as file: 
# # # #                     file.write(f"Student data added: {student}\n")

# # # # getData()

# # # # if students:
# # # #     print("\nAll student data:")
# # # #     for student in students:
# # # #         print(student)








# # # # import os 
# # # # print (os.path)
# # # # if os.path.exists ('students.txt'):
# # # #     print ("the file exists")
# # # # else :
# # # #     print ("no succh file ")












# # # a=2
# # # b=4
# # # print( "a is high " if a>b else "b is high ")


# # # myList = ["mango","apple","water","cherry"]
# # # filterList = [ item for item in myList if item != "water"]
# # # print (filterList)
# # # xSet = {True, False , "Jupyter", "Moon", "Sun", 1,2,3,4 }
# # # mySet = {"mango","apple","water","cherry"}
# # # ySet = xSet.union (mySet)
# # # ySet = xSet | mySet
# # # print (xSet)
# # # print (mySet)
# # # print (ySet)






















# # mKeys = ('name', 'age', 'score')

# # data_list = []

# # def get_input(prompt, key):
# #     while True:
# #         try:
# #             value = input(prompt)
# #             if value.lower() == 'save&exit':
# #                 return value
# #             if key == 'age' or key == 'score':
# #                 if value.isnumeric():
# #                     return int(value)
# #                 else:
# #                     raise ValueError("Non-numerical.")
# #             else:
# #                 return value
# #         except ValueError as e:
# #             print(e)

# # def main():
# #     print("Enter data / save&exit")
# #     while True:
# #         data_dict = {}
# #         for key in mKeys:
# #             value = get_input(f"Enter {key}: ", key)
# #             if value == 'save&exit':
# #                 print("\nCollected Data:")
# #                 for entry in data_list:
# #                     print(entry)
# #                 return
# #             data_dict[key] = value
        
# #         data_list.append(data_dict)
# #         print("Data saved. You can continue entering or type 'save&exit' to quit.")
    
# #     print("\nCollected Data:")
# #     for entry in data_list:
# #         print(entry)

# # if __name__ == "__main__":
# #     main()



















# # key = ('name','age', 'score')
# # mdict = dict.fromkeys (key)
# # print(mdict)












# c = 20
# b = f"""
# this is line num 1
# this is line num 2
# this is line num 3
# this is line num 4"""
# print (b)
# myList= [23,45,21,89,67,6,42]
# def myFilter (v):
#     if v>20:
#         return v

# xList = filter (myFilter,myList)
# for i in xList:
#     print (i)
    
    












