import copy

from objects import PlannedProject


def find_contributors(project, contributors):
    available_contributors = copy.copy(contributors)
    used_contributor = []
    to_increase = []
    for skill in project.skills:
        skill_found = False
        for contributor in available_contributors:
            if not skill_found:
                for s in contributor.skills:
                    if skill.name == s.name:
                        if s.level >= skill.level:
                            used_contributor.append(contributor)
                            if s.level == skill.level:
                                to_increase.append((contributor, skill))
                            available_contributors.remove(contributor)
                            skill_found = True
    if len(used_contributor) < len(project.skills):
        return False, None
    planned_project = PlannedProject(project.name, used_contributor)
    for item in to_increase:
        item[0].level_up(item[1])
    return True, planned_project

