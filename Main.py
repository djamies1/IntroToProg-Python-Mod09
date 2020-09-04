# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <David Jamieson>,<9/4/2020>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I  # IO classes
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body


# Error catch handling
try:

    # Load data from file into a list of employee objects when script starts
    lstFileData = P.FileProcessor.read_data_from_file("C:\_PythonClass\Assignment09\EmployeeData.txt")
    lstTable = []
    for line in lstFileData:
        lstTable.append(D.Employee(line[0], line[1], line[2].strip()))

    while True:

        # Show user a menu of options
        I.EmployeeIO.print_menu_items()
        # Get user's menu option choice
        strChoice = I.EmployeeIO.input_menu_options()

        # Show user current data in the list of employee objects
        if strChoice.strip() == '1':
            I.EmployeeIO.print_current_list_items(lstTable)
            continue
        # Let user add data to the list of employee objects
        elif strChoice.strip() == '2':
            strEmployee = I.EmployeeIO.input_employee_data()
            lstTable.append(strEmployee)
            continue
        # let user save current data to file
        elif strChoice.strip() == '3':
            P.FileProcessor.save_data_to_file("C:\_PythonClass\Assignment09\EmployeeData.txt", lstTable)
            print('File saved!')
            print('-----------')
            continue
        # Let user exit program
        elif strChoice.strip() == '4':
            print('Exiting Program, thank you!')
            break
        # prompt the user for the correct input type if they enter an input not between 1 to 4
        else:
            print('That is not an accepted input, please enter a number between [1 to 4]')
        continue

# Display error if any of the main body scripting errors out
except Exception as e:
    print("There was an error! Please start the program again")
    print("The error was: ", e)
