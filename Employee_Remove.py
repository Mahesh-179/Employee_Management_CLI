from Employee_Add import employees

def remove():
    emp_id = input("Enter ID of employee to remove: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee removed.")
            return
    print("Employee not found.")
