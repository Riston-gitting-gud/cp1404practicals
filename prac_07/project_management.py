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

