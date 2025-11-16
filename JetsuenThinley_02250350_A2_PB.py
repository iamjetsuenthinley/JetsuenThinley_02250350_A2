#Bubble sort function
def bubble_sort(arr):
    a = arr[:] 
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

#Insertion Sort function
def insertion_sort(arr):
    a = arr[:]  
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


recursion_counter = {"count": 0}
#Quick Sort function
def quick_sort(arr):
    recursion_counter["count"] = 0
    sorted_arr = _quick_sort(arr[:])
    return sorted_arr, recursion_counter["count"]

def _quick_sort(a):
    recursion_counter["count"] += 1
    if len(a) <= 1:
        return a
    pivot = a[-1]
    left = [x for x in a[:-1] if x <= pivot]
    right = [x for x in a[:-1] if x > pivot]
    return _quick_sort(left) + [pivot] + _quick_sort(right)

running=True
while running:
    print("\n Sorting Algorithms Menu")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit program")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        names = ["Letho", "Pema", "chimi", "Jigme", "Tsheting", "Tashi", "Pema", "Dorji",
            "Sangay", "Karma", "Sonam", "Ugyen", "Passang", "Yugyel", "Phurba"]
        print("Original:", names)
        sorted_names = bubble_sort(names)
        print("Sorted:", sorted_names)

    elif choice == "2":
        scores = [96, 55, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 60]
        print("Original scores:", scores)
        sorted_scores = insertion_sort(scores)
        print("Sorted scores:", sorted_scores)
        top_five = sorted_scores[::-1][:5]
        print("Top 5 Scores:")
        for i, s in enumerate(top_five, 1):
            print(f"{i}. {s}")

    elif choice == "3":
        prices = [680, 330, 676, 124, 790, 320, 410, 235, 699, 150, 275, 620, 540, 485, 999]
        print("Original prices:", prices)
        sorted_prices, rec_calls = quick_sort(prices)
        print("Sorted prices:", sorted_prices)
        print(f"Recursive calls: {rec_calls}")

    elif choice == "4":
        print("Thank you for using the sorting program!")
        break
    else:
        print("Invalid choice. Enter 1, 2, 3 or 4.")

    #Continue or exit choice
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


