"""
To-Do List Application (Command-Line Version)
------------------------------------------------
A simple, dependency-free CLI task manager. Uses the same tasks.json
file format as todo_app.py, so both versions can share data.

Run with:  python todo_cli.py
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")
PRIORITIES = ["Low", "Medium", "High"]


def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def print_menu():
    print("\n" + "=" * 40)
    print(" TO-DO LIST")
    print("=" * 40)
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task complete/incomplete")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Clear completed tasks")
    print("7. Exit")
    print("=" * 40)


def view_tasks(tasks, filter_mode="All"):
    if not tasks:
        print("\n(No tasks yet — add one!)")
        return

    print()
    for i, t in enumerate(tasks, start=1):
        if filter_mode == "Active" and t["done"]:
            continue
        if filter_mode == "Completed" and not t["done"]:
            continue
        status = "[x]" if t["done"] else "[ ]"
        due = f" (due {t['due_date']})" if t.get("due_date") else ""
        print(f"{i:>2}. {status} {t['title']}  <{t['priority']}>{due}")


def prompt_int(prompt, max_value):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= max_value:
            return int(raw) - 1
        print(f"Please enter a number between 1 and {max_value}.")


def valid_date(text):
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_task(tasks):
    title = input("Task description: ").strip()
    if not title:
        print("Task description cannot be empty.")
        return

    due = input("Due date (YYYY-MM-DD, or leave blank): ").strip()
    if due and not valid_date(due):
        print("Invalid date format — saving without a due date.")
        due = ""

    print(f"Priority options: {', '.join(PRIORITIES)}")
    priority = input("Priority (default Medium): ").strip().title() or "Medium"
    if priority not in PRIORITIES:
        priority = "Medium"

    tasks.append({
        "title": title,
        "due_date": due,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_tasks(tasks)
    print("Task added.")


def toggle_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    view_tasks(tasks)
    idx = prompt_int("Task number to toggle: ", len(tasks))
    tasks[idx]["done"] = not tasks[idx]["done"]
    save_tasks(tasks)
    print("Updated.")


def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    view_tasks(tasks)
    idx = prompt_int("Task number to edit: ", len(tasks))
    task = tasks[idx]

    new_title = input(f"New description [{task['title']}]: ").strip()
    if new_title:
        task["title"] = new_title

    new_due = input(f"New due date [{task.get('due_date', '')}]: ").strip()
    if new_due:
        if valid_date(new_due):
            task["due_date"] = new_due
        else:
            print("Invalid date — keeping previous value.")

    new_priority = input(f"New priority [{task['priority']}]: ").strip().title()
    if new_priority in PRIORITIES:
        task["priority"] = new_priority

    save_tasks(tasks)
    print("Task updated.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    idx = prompt_int("Task number to delete: ", len(tasks))
    removed = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Deleted '{removed['title']}'.")


def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    print(f"Removed {before - len(tasks)} completed task(s).")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            print("\nFilter: (a)ll / (act)ive / (c)ompleted [default all]")
            f = input("> ").strip().lower()
            mode = "Active" if f.startswith("act") else "Completed" if f.startswith("c") else "All"
            view_tasks(tasks, mode)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            clear_completed(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-7.")


if __name__ == "__main__":
    main()