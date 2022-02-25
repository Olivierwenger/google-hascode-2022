from objects import Contributor, Skill, Project


def read_file(name: str) :
    file = open("input/"+name + ".in.txt")
    # lines = file.readlines()

    contributors_count, projects_count = file.readline().strip().split()

    contributors = []
    projects = []

    for i in range(int(contributors_count)):
        name, skill_count = file.readline().strip().split()
        skills = []
        for j in range(int(skill_count)):
            skill_name, level = file.readline().strip().split()
            skills.append(Skill(skill_name, level))

        contributors.append(Contributor(name, skills))

    for i in range(int(projects_count)):
        name, duration, score, deadline, role_count = file.readline().strip().split()
        skills = []

        for j in range(int(role_count)):
            skill_name, level = file.readline().strip().split()
            skills.append(Skill(skill_name, level))

        projects.append(Project(name, duration, score, deadline, skills))

    return contributors, projects


