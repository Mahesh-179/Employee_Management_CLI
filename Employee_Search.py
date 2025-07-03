from Employee_Add import employees

def search_emp():
    emp_id = input("Enter ID to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee Found:")
            print(emp)
            return
    print(" Employee not found.")
