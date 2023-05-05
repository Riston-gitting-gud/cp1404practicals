# Project Management Program

import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    class ProjectList:
        def __init__(self):
            self.projects = []

        def load_projects(self, filename):
            with open(filename, 'r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                    self.projects.append(project)

        def save_projects(self, filename):
            with open(filename, 'w') as file:
                file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for project in self.projects:
                    file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}"
                               f"\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")

        def display_projects(self):
            incomplete = sorted([p for p in self.projects if p.completion_percentage < 100])
            complete = sorted([p for p in self.projects if p.completion_percentage == 100])
            print("Incomplete projects:")
            for project in incomplete:
                print(f"  {project}")
            print("Completed projects:")
            for project in complete:
                print(f"  {project}")


