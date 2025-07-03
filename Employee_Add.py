employees = []

# Defining Function to take input
def employee_add():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = input("Enter employee salary: ")
    department = input("Enter employee department: ")

# Storing data in dictionaries for temproary use
    employee = {
        "Employee_Name": name,
        "Employee_ID": emp_id,
        "Employee_Salary": salary,
        "Employee_Department": department
    }
#Printing Messages
    employees.append(employee)
    print(f"Employee {name} added successfully!")
