from inputhdl import userinput
import os


"""
Defined the function to accept inputs 
and store them in a Dictionary and later append to a list 
"""
students = []
dKeys = ('name','age','score')

def getData():
    print("Enter 1 for 'Add Entry'")
    print("Enter 2 for 'Save Data'")
    print("Enter 3 for 'Load Data'")
    print("Enter 4 for 'Delete All Data'")
    print("Enter 0 to 'Exit'")
    myInp = userinput.getInt("Enter your Option from above: ")

    if myInp==0:
        print('BYE!')
    elif myInp==1:
        student = {}
        try:
            student["name"]=userinput.getString("Enter your Name: ")
            student["age"]=userinput.getInt("Enter your Age: ")
            student["score"]=userinput.getInt("Enter your Score: ")
            if student["age"] > 30:
                raise Exception("Invalid Age!")
        except ValueError:
            print("Error! Need 3 inputs sepereted by a ',', Please try again")
        except:
            print("Invalid Age, Please try again")
        else:
            students.append(student)
        finally:
            print("\n\n***Data Saved!!!***\n\n\n")
            getData()
    elif myInp==2:
        try:
            theFile = open("students.txt",'w')
            theFile.write(str(students))
        except:
            print("error saving file")
        finally:
            theFile.close()
    elif myInp==3:
        try:
            theFile = open("students.txt",'r')
            students = eval(theFile.read())
        except:
            print("error saving file")
        finally:
            for stdt in students:
                print(f"Name: {stdt["name"]}, Score: {stdt["score"]}")
            theFile.close()
    
    elif myInp==4:
        try:
            os.remove('students.txt')
        except FileNotFoundError:
            print("The file does not exist")
        else:
            print("File deleted successfully!")
    
    
        

#called the function
getData()

#for loop for printing formatted table


for stdt in students:
    print(f"Name: {stdt["name"]}, Score: {stdt["score"]}")