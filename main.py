import requests


def get_user_projects():
    response = requests.get(f"https://gitlab.com/api/v4/users/{user_name}/projects")
    my_projects = response.json()
    try:
        for project in my_projects:
            print(f"Project name: {project['name']} \nProject URL: {project['web_url']}\n")
    except:
        print(my_projects['message'])


user_name =input("Enter user name to get projects name and URL from gitlab\n")
get_user_projects()