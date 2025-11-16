#Linear Search fucntion
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i + 1   
    return None

#Binary Search function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

running = True
while running:
    print("\nSearch Menu")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        student_ids = [2250001, 2250002, 2250003, 2250004, 2250005,2250006, 2250007, 2250008, 2250009, 2250010,
            2250011, 2250012, 2250013, 2250014, 2250015,2250016, 2250017, 2250018, 2250019, 2250020]
        
        print("Student ID list:", student_ids)
        try:
            target = int(input("Enter the Student ID you want to search: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        pos = linear_search(student_ids, target)
        if pos:
            print(f"Student ID {target} found at position {pos}.")
        else:
            print(f"Student ID {target} was not found.")

    elif choice == "2":
        sorted_scores = [45, 48, 52, 55, 58, 61, 64, 67, 70, 73,76, 79, 82, 85, 88, 90, 92, 95, 97, 100]

        print("Score list:", sorted_scores)
        try:
            target = int(input("Enter the score to search: "))
        except ValueError:
            print("Please enter a valid score.")
            continue

        pos = binary_search(sorted_scores, target)
        if pos:
            print(f"Score {target} found at position {pos}.")
        else:
            print(f"Score {target} not found.")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
        continue

    #Continue or Exit function
    while True:
        cont = input("\nWould you like to perform another search? (y/n): ").lower()
        if cont == 'n':
            print("Thank you for using the search program!")
            running=False
            break
        elif cont == 'y':
            break
        else:
            print("Please enter y or n")
