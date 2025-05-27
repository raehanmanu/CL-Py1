
# 18
def quiz():
    questions = {
        "Capital of Hungary?": "Budapest",
        "22 + 22 = ?": "44",
        "What is the closest planet to the sun?": "Venus"
    }
    score = 0
    for q, a in questions.items():
        ans = input(q + " ")
        if ans.strip().lower() == a.lower():
            score += 1
    print(f"Your score: {score}/{len(questions)}")

# 19
def expense_tracker():
    expenses = {}

    for day in range(7):
        amount = float(input(f"Enter expense for day {day+1}: "))
        expenses[f"Day {day+1}"] = amount

    print("\nWeekly Summary:")
    total = 0
    for day, amt in expenses.items():
        print(f"{day}: {amt}")
        total += amt

    print(f"Total Weekly Expenses: {total}")


# 20
def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add\n2. Remove\n3. Mark Complete\n4. Show\n5. Exit")
        choice = input("Choice: ")
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
        elif choice == '3':
            task = input("Enter task to mark complete: ")
            if task in tasks:
                idx = tasks.index(task)
                tasks[idx] += " (done)"
        elif choice == '4':
            for t in tasks:
                print(t)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
        save_tasks(tasks)
