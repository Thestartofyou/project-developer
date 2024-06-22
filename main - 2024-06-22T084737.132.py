import json

# File to store project data
DATA_FILE = "projects.json"

def load_data():
    """Load project data from a JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    """Save project data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_project(projects):
    """Add a new project to the list."""
    project = {
        "name": input("Project Name: "),
        "client": input("Client Name: "),
        "deadline": input("Deadline (YYYY-MM-DD): "),
        "status": input("Status: "),
        "details": input("Details: ")
    }
    projects.append(project)
    save_data(projects)
    print("Project added successfully!")

def view_projects(projects):
    """View all projects."""
    for i, project in enumerate(projects, start=1):
        print(f"\nProject {i}")
        for key, value in project.items():
            print(f"{key.capitalize()}: {value}")

def update_project(projects):
    """Update an existing project."""
    view_projects(projects)
    project_number = int(input("\nEnter project number to update: ")) - 1
    if 0 <= project_number < len(projects):
        project = projects[project_number]
        print("\nLeave field empty to keep current value.")
        project["name"] = input(f"Project Name ({project['name']}): ") or project["name"]
        project["client"] = input(f"Client Name ({project['client']}): ") or project["client"]
        project["deadline"] = input(f"Deadline ({project['deadline']}): ") or project["deadline"]
        project["status"] = input(f"Status ({project['status']}): ") or project["status"]
        project["details"] = input(f"Details ({project['details']}): ") or project["details"]
        save_data(projects)
        print("Project updated successfully!")
    else:
        print("Invalid project number!")

def main():
    """Main function to handle user choices."""
    projects = load_data()
    while True:
        print("\nProject Management System")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Update Project")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_project(projects)
        elif choice == "2":
            view_projects(projects)
        elif choice == "3":
            update_project(projects)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
