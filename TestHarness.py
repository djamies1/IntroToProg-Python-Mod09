# ---------------------------------------------------------- #
# Title: Test Harness for supporting .py files
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# David Jamieson, 9/4/2020, edited script
# ---------------------------------------------------------- #

if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I #IO classes
else:
    raise Exception("This file was not created to be imported")

# Test Data Classes Module ---------------------------------------

# Test Person Class
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test Employee Class
objP1 = D.Employee(1, "Bob", "Smith")
objP2 = D.Employee(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test File Processing Module ---------------------------------------

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(D.Employee(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test Input Output Module ---------------------------------------

# Test IO classes
I.EmployeeIO.print_menu_items()

print('Table:')
print(lstTable) #testing to see table output before error
print('End Table')

I.EmployeeIO.print_current_list_items(lstTable)
print(I.EmployeeIO.input_employee_data())
print(I.EmployeeIO.input_menu_options())