from helpers import find_contributors
from objects import Plan


def solve(contributors, projects):

    sorted_project = {}

    for project in projects:
        min_skill = min([ skill.level for skill in project.skills ])

        sorted_project[project.name] = min_skill

    sorted_list = sorted((value, key) for (key, value) in sorted_project.items())
    sorted_dict = [k for _,k in sorted_list]
    print(sorted_list)
    doable_projects = []
    for p in sorted_dict:
        project = [ p1 for p1 in projects if p1.name == p][0]
        doable, doable_project = find_contributors(project, contributors)
        if doable:
            doable_projects.append(doable_project)

    print(doable_projects)

    plan = Plan(len(doable_projects), doable_projects)

    return plan
