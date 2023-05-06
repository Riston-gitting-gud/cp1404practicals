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
    display = display.strip()  # do not display the last newline
    print(display)


def update_project(projects):
    projects_str = ''
    for i, project in enumerate(projects):
        projects_str = projects_str + str(i) + ' ' + repr(project) + '\n'
    # # do not display the last newline
    # print(display[:len(display) - 2])
    print(projects_str)
    project_choice = int(input('Project choice: '))
    print(repr(projects[project_choice]))
    new_percentage = input('New Percentage: ')
    new_priority = input('New Priority: ')
    if new_percentage != '':
        projects[project_choice].completion_estimate = int(new_percentage)
    if new_priority != '':
        projects[project_choice].priority = int(new_priority)
