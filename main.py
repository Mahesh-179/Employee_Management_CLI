from Employee_Add import employee_add
from Employee_Update import update
from Employee_Remove import remove
from Employee_Search import search_emp

def main():
    print("=================== EMPLOYEE MANAGEMENT SYSTEM ====================")

    while True:
        print("\n 1. Add Employee\n 2. Update Employee\n 3. Remove Employee\n 4. Search Employee\n 5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                employee_add()
            elif choice == 2:
                update()
            elif choice == 3:
                remove()
            elif choice == 4:
                search_emp()
            elif choice == 5:
                print("👋 Exiting Program...")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
