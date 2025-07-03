from Employee_Add import employees
def update():
    emp_id = input("Enter ID of employee to update: ")
    for emp in employees:
        if emp["id"] == emp_id:
            new_name = input("Enter new name: ")
            emp["name"] = new_name
            print(" Employee updated.")
            return
    print(" Employee not found.")
