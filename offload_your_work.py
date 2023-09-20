# Offload Your Work

"""
You are the best freelancer in the city. Everybody knows you, but what they don't know, is that you are actually offloading your work to other freelancers and and you rarely need to do any work. You're living the life!

To make this process easier you need to write a method called workNeeded to figure out how much time you need to contribute to a project.

Giving the amount of time in minutes needed to complete the project and an array of pair values representing other freelancers' time in [Hours, Minutes] format ie. [[2, 33], [3, 44]] calculate how much time you will need to contribute to the project (if at all) and return a string depending on the case.

If we need to contribute time to the project then return "I need to work x hour(s) and y minute(s)"
If we don't have to contribute any time to the project then return "Easy Money!"
"""

# My Solution

def work_needed(project_minutes, free_lancers):
    time_left = project_minutes
    for h,m in free_lancers:
        time_left -= (h * 60 + m)
        
    if time_left <= 0:
        return "Easy Money!"
    
    else:
        return f"I need to work {time_left//60} hour(s) and {time_left - (time_left//60 * 60)} minute(s)"
    
# Other Solutions

def work_needed(project_minutes, freelancers):
    available_minutes = sum(hours * 60 + minutes for hours, minutes in freelancers)
    workload_minutes = project_minutes - available_minutes
    if workload_minutes <= 0:
        return 'Easy Money!'
    else:
        hours, minutes = divmod(workload_minutes, 60)
        return 'I need to work {} hour(s) and {} minute(s)'.format(hours, minutes)