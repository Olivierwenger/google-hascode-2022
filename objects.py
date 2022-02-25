class Contributor:

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def level_up(self, skill):
        for s in self.skills:
            if s.name == skill.name:
                s.level += 1


class Skill:

    def __init__(self, name, level):
        self.name = name
        self.level = int(level)

class Project:

    def __init__(self, name, ndays, score, deadline, skills):
        self.name = name
        self.ndays = ndays
        self.score = score
        self.deadline = deadline
        self.skills = skills

class Plan:

    def __init__(self, nprojects, planned_projects):
        self.nprojects = nprojects
        self.planned_projects = planned_projects

class PlannedProject:

    def __init__(self, name, contributors):
        self.name = name
        self.contributors = contributors
