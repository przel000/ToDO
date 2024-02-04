def print_tasks():
    task_list.sort(key=lambda x: -int(x[2]))
    for row in task_list:
        print(f"{row}")

def printJobScheduling(arr, t):

	# length of array
	n = len(arr)

	# Sort all jobs according to
	# decreasing order of profit
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# To keep track of free time slots
	result = [False] * t

	# To store result (Sequence of jobs)
	job = ['-1'] * t

	# Iterate through all given jobs
	for i in range(len(arr)):
    
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
  

			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	# print the sequence
	print(job)

task_list = []

while (10):
    
    print("""TODO List Management System
    1: Add
    2: View
    3: Remove
    4: Edit
    5: Exit
    6: optimized task list""")
    w = input()
    if w == '1':
        add = input("What do you want to add: ")
        due = int(input("When it is due: "))
        impo = int(input("Importance(1-10): "))
        row = [add, due, impo]
        task_list.append(row)
    elif w == '2':
        print_tasks()
    elif w == '3':
        rem = input("What do you want to remove: ")
        task_list = [row for row in task_list if row[0] != rem]
    elif w == '4':
        old_task = input("Which task do you want to edit? ")
        for i, row in enumerate(task_list):
            if row[0] == old_task:
                new_task = input("What do you want to change it to: ")
                new_due = input("When it is due: ")
                new_impo = input("Importance(1-4): ")
                task_list[i] = [new_task, new_due, new_impo]
    elif w == '5':
        print("Exiting...")
        break
    
    elif w=='6':
         print(len(task_list))
         printJobScheduling(task_list,len(task_list))
         

    else:
        print("Invalid choice, please choose a number between 1-6.")
        print(task_list)
