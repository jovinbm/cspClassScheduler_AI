import copy

import sys


def startingPointIsUnique(csp, usedStartCoursesInPlans):
    start_course = copy.deepcopy(csp.semesters[0]['courses'][0])
    if start_course not in usedStartCoursesInPlans:
        return True
    else:
        return False


class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

    def length(self):
        "Returns stack length"
        return len(self.list)


class Stack_optimized:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, (csp, course)):
        "Push 'item' onto the stack"
        csp.domain_trim_course_domain()
        csp.domain_trim_no_repetition()
        csp.domain_trim_no_time_conflict()

        zero_domains = csp.get_zero_domains()
        if len(zero_domains) > 0:
            print 'ZERO DOMAINS FOUND, skipping csp', zero_domains
            return True

        if csp.check_constraints_optimized_prerequisites():
            self.list.append((csp, course))

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

    def length(self):
        "Returns stack length"
        return len(self.list)


class Stack_optimized_filtering:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, (csp, course), usedStartCoursesInPlans):
        "Push 'item' onto the stack, check that csp is not in usedStartCoursesInPlans"
        csp.domain_trim_course_domain()
        csp.domain_trim_no_repetition()
        csp.domain_trim_no_time_conflict()

        zero_domains = csp.get_zero_domains()
        if len(zero_domains) > 0:
            print 'ZERO DOMAINS FOUND, skipping csp', zero_domains
            return True

        if not startingPointIsUnique(csp, usedStartCoursesInPlans):
            print 'NON UNIQUE STARTING POINT, skipping csp'
            return True

        if csp.check_constraints_optimized_prerequisites():
            self.list.append((csp, course))

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

    def length(self):
        "Returns stack length"
        return len(self.list)
