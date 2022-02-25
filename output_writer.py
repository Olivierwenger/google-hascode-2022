

def write_output(plan, file):
    f = open('output/'+file + ".out.txt", "w")
    f.write(str(plan.nprojects) + "\n")
    for planned_project in plan.planned_projects:
        f.write(planned_project.name + "\n")
        contributors_str = ""
        for c in planned_project.contributors:
            contributors_str += (c.name + " ")
        f.write(contributors_str + "\n")
    f.close()