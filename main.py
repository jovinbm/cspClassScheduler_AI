# ===================================================================
# TO RUN, execute > 'python main.py' in root directory
# See courses format in compsci.json
# See Data structures on various optimizations in util.py
# ===================================================================

import copy

import sys
import time

import index
import util

max_stack_size = 0

# these are the used start courses in found plans, used to provide unique plans with diff starting points
usedStartCoursesInPlans = []


def startingPointIsUnique(csp):
    start_course = copy.deepcopy(csp.semesters[0]['courses'][0])
    if start_course not in usedStartCoursesInPlans:
        usedStartCoursesInPlans.append(start_course)
        return True
    else:
        return False


def backtracking_search(csp):
    stack = util.Stack()

    def update_max_stack(stack_size):
        global max_stack_size
        if stack_size > max_stack_size:
            max_stack_size = stack_size

    for course in csp.raw_courses:

        csp_copy = copy.deepcopy(csp)
        csp_copy.add_course(course)
        if csp_copy.no_prerequisite_conflict(csp_copy.semesters) and not csp.level200(course) and not csp.level300(course):
            stack.push((csp_copy, course))

    last_csp = csp
    plans = []

    while not stack.isEmpty():
        current_csp, last_course = stack.pop()
        last_csp = current_csp

        if current_csp.plan_is_complete():

            if csp.startCourseUnique:
                if startingPointIsUnique(current_csp):
                    plans.append(current_csp)

                    if len(plans) == current_csp.noOfPlans:
                        return True, plans
                    else:
                        continue
            else:
                plans.append(current_csp)

                if len(plans) == current_csp.noOfPlans:
                    return True, plans
                else:
                    continue

        successor_courses = current_csp.get_successors(last_course)

        for successor_course in successor_courses:

            csp_copy = copy.deepcopy(current_csp)
            csp_copy.add_course(successor_course)

            if csp_copy.check_constraints():
                stack.push((csp_copy, successor_course))
            update_max_stack(stack.length())
            print 'Stack length', stack.length()

    # if the plans were not found, but did not reach required number, just mark as complete
    if len(plans) > 0:
        return True, plans

    # append the incomplete last best csp, mark plans as incomplete
    plans.append(last_csp)
    return False, plans


def backtracking_search_optimized(csp):
    stack = util.Stack_optimized()

    def update_max_stack(stack_size):
        global max_stack_size
        if stack_size > max_stack_size:
            max_stack_size = stack_size

    # get the start course from the domain of start courses
    for course in csp.semesters_domain[0][3]:
        csp_copy = copy.deepcopy(csp)
        csp_copy.add_course(course)
        if csp_copy.no_prerequisite_conflict(csp_copy.semesters):
            stack.push((csp_copy, course))

    last_csp = csp
    plans = []

    while not stack.isEmpty():
        current_csp, last_course = stack.pop()
        last_csp = current_csp

        if current_csp.plan_is_complete_optimized():
            if csp.startCourseUnique:
                if startingPointIsUnique(current_csp):
                    plans.append(current_csp)

                    if len(plans) == current_csp.noOfPlans:
                        return True, plans
                    else:
                        continue
            else:
                plans.append(current_csp)

                if len(plans) == current_csp.noOfPlans:
                    return True, plans
                else:
                    continue

        successor_courses = current_csp.get_successors_optimized(last_course)

        for successor_course in successor_courses:
            csp_copy = copy.deepcopy(current_csp)
            csp_copy.add_course(successor_course)

            stack.push((csp_copy, successor_course))

            update_max_stack(stack.length())
            print 'Stack length', stack.length()

    # if the plans were not found, but did not reach required number, just mark as complete
    if len(plans) > 0:
        return True, plans

    # append the incomplete last best csp, mark plans as incomplete
    plans.append(last_csp)
    return False, plans


def backtracking_search_optimized_filtering(csp):
    stack = util.Stack_optimized_filtering()

    def update_max_stack(stack_size):
        global max_stack_size
        if stack_size > max_stack_size:
            max_stack_size = stack_size

    # get the start course from the domain of start courses
    for course in csp.semesters_domain[0][3]:
        csp_copy = copy.deepcopy(csp)
        csp_copy.add_course(course)
        if csp_copy.no_prerequisite_conflict(csp_copy.semesters):
            stack.push((csp_copy, course), usedStartCoursesInPlans)

    last_csp = csp
    plans = []

    while not stack.isEmpty():
        current_csp, last_course = stack.pop()
        last_csp = current_csp

        if current_csp.plan_is_complete_optimized():
            if csp.startCourseUnique:
                if startingPointIsUnique(current_csp):
                    plans.append(current_csp)

                    if len(plans) == current_csp.noOfPlans:
                        return True, plans
                    else:
                        continue
            else:
                plans.append(current_csp)

                if len(plans) == current_csp.noOfPlans:
                    return True, plans
                else:
                    continue

        successor_courses = current_csp.get_successors_optimized_filtering(last_course)

        for successor_course in successor_courses:
            csp_copy = copy.deepcopy(current_csp)
            csp_copy.add_course_optimized_filtering(successor_course)

            stack.push((csp_copy, successor_course), usedStartCoursesInPlans)

            update_max_stack(stack.length())
            print 'Stack length', stack.length()

    # if the plans were not found, but did not reach required number, just mark as complete
    if len(plans) > 0:
        return True, plans

    # append the incomplete last best csp, mark plans as incomplete
    plans.append(last_csp)
    return False, plans


# argument_list = sys.argv[1:]
# opts, args = getopt.getopt(argument_list, "o:", ["optimize="])
# print opts
# print args


Classes = index.CLASSES()
start = time.time()
if Classes.optimize and Classes.applyFiltering:
    complete, plans = backtracking_search_optimized_filtering(Classes)
elif Classes.optimize:
    complete, plans = backtracking_search_optimized(Classes)
else:
    complete, plans = backtracking_search(Classes)
print "================================================="
if complete:
    for x in range(0, len(plans)):
        print "PLAN " + str(x + 1)
        plans[x].print_courses()
else:
    print "NO COMPLETE PLANS WERE FOUND: The best we could achieve is the following:"
    for x in range(0, len(plans)):
        print "PLAN " + str(x + 1)
        plans[x].print_courses()

print 'Max stack size', max_stack_size

if Classes.optimize and Classes.applyFiltering:
    print 'Optimized with filtering'
elif Classes.optimize:
    print 'Optimized, no filtering'
else:
    print 'Non optimized'

if Classes.startCourseUnique:
    print 'Start is unique'
else:
    print 'Start not unique'
print "================================================="
end = time.time()
print end - start, 'seconds'
sys.exit()
