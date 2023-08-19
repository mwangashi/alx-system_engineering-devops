import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee info
    employee_info_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_info = employee_info_response.json()
    
    # Fetch employee's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_list = todo_response.json()
    
    # Calculate TODO progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])
    
    # Display progress
    print(f"Employee {employee_info['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Display completed task titles
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
