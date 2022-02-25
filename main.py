import output_writer
from input_reader import read_file
from solvers.basic_solver import solve

file_names = [
    'd_dense_schedule',
    'e_exceptional_skills',
    'f_find_great_mentors',
]

for file_name in file_names:
    contributors, projects = read_file(file_name)

    plan = solve(contributors, projects)

    output_writer.write_output(plan, file_name)


