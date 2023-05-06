# Project Management Program

import datetime
from project import Project


def main():
    projects = []
    user_input = ''

    while user_input.lower() != 'q':
        print(f'- (L)oad projects \n'
              '- (S)ave projects \n'
              '- (D)isplay projects \n'
              '- (F)ilter projects by date \n'
              '- (A)dd new project \n'
              '- (U)pdate project \n'
              '- (Q)uit')
        user_input = input(">>> ")

        if user_input.lower() == 'l':
            file_name = input('Please type in the file to be loaded: ')
            projects = load_projects(file_name)

        if user_input.lower() == 'd':
            display_all_projects(projects)

        if user_input.lower() == 'u':
            update_project(projects)

        if user_input.lower() == 'f':
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            display_filtered_projects(projects, date)

        if user_input.lower() == 'a':
            print("Lets add a new project")
            add_new_project(projects)

        if user_input.lower() == 's':
            file_name = input('Please type in the file name to save project data to: ')
            save_projects(projects, file_name)

    print("Thank you for using custom-built project management software.")


def sort_by_priority(projects, to_reverse):
    result = sorted(projects, key=lambda x: x.priority, reverse=to_reverse)
    return result


def load_projects(file_name):
    projects = []
    with open(file_name, 'r', newline='') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]), len(projects))
            else:
                print(f'\nInvalid row detected.\n"{line}"\n Ignoring....\n')
            projects.append(project)

        print(projects)
        return projects


def update_project(projects):
    projects_str = ''
    for i, project in enumerate(projects):
        projects_str = projects_str + str(i) + ' ' + repr(project) + '\n'
    print(projects_str)
    project_choice = int(input('Project choice: '))
    print(repr(projects[project_choice]))
    new_percentage = input('New Percentage: ')
    new_priority = input('New Priority: ')
    if new_percentage != '':
        projects[project_choice].completion_estimate = int(new_percentage)
    if new_priority != '':
        projects[project_choice].priority = int(new_priority)


def display_all_projects(projects):
    incomplete_projects = 'Incomplete projects: \n'
    complete_projects = 'Completed projects: \n'
    sorted_projects = sort_by_priority(projects, False)

    for project in sorted_projects:
        if project.completion_estimate < 100:
            incomplete_projects = incomplete_projects + '\t' + repr(project) + '\n'
        else:
            complete_projects = complete_projects + '\t' + repr(project) + '\n'
    display = incomplete_projects + complete_projects
    display = display.strip()
    print(display)


def display_filtered_projects(projects, start_date):
    projects_str = ''
    displayed_project_list = []

    for project in projects:
        project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if start_date <= project_date:
            displayed_project_list.append(project)
    displayed_project_list.sort(key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y").date())

    for project in displayed_project_list:
        projects_str = projects_str + repr(project) + '\n'

    projects_str = projects_str.strip()
    print(projects_str)


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_estimate = input("Percent complete: ")
    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_estimate), len(projects))
    projects.append(project)


def save_projects(projects, file_name):
    with open(file_name, 'w', newline='') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                           f"\t{project.cost_estimate}\t{project.completion_estimate}\n")
        return True


if __name__ == "__main__":
    main()
