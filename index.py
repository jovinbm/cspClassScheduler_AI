import copy
import json

import datetime
import sys


def logger(data):
    print data
    return


def hourMin(timeString):
    # timestring format e.g "10:00:00"
    hour = None
    minute = None

    if timeString[0]:
        hour = int(str(timeString[0]) + str(timeString[1]))
    else:
        hour = int(timeString[1])

    if timeString[3]:
        minute = int(str(timeString[3]) + str(timeString[4]))
    else:
        minute = int(timeString[4])

    assert not hour == True
    assert not minute == True

    return hour, minute


def getTimeTuples(schedule):
    "gets time tuples for courses in a pecific day"
    time_tuples = []

    if schedule['day'] and schedule['begin_time'] and schedule['end_time']:
        startHour, startMin = hourMin(schedule['begin_time'])
        endHour, endMin = hourMin(schedule['end_time'])
        time_tuples.append((startHour, startMin, 0, endHour, endMin, 0))

    return time_tuples


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def get_user_input_int(question_string, start_inclusive, end_inclusive, default):
    try:
        user_input = int(raw_input(question_string))
    except:
        user_input = default

    if start_inclusive <= user_input <= end_inclusive:
        return user_input
    else:
        return default


def get_user_input_str(question_string, default):
    try:
        user_input = str(raw_input(question_string))
    except:
        user_input = default
    return user_input


class CLASSES:
    def __init__(self):
        self.raw_courses = []

        with open('compsci.json') as data_file:
            self.raw_courses = json.load(data_file)

        self.optimize = [False, True][get_user_input_int(
            "Optimize (1)YES or (0)NO? (0 or 1 only, Default = 1(YES) for None or non-int): ",
            0,
            1,
            1)]

        if self.optimize:
            print 'Optimize: True'
        else:
            print 'Optimize: False'

        self.applyFiltering = False

        if self.optimize:
            self.applyFiltering = [False, True][get_user_input_int(
                "Apply filtering? (1)YES or (0)NO? (0 or 1 only, Default = 1(YES) for None or non-int): ",
                0,
                1,
                1)]

            if self.applyFiltering:
                print 'Filtering: True'
            else:
                print 'Filtering: False'

        while 1:
            self.noOfCourses = get_user_input_int(
                "What is the total number of courses you want to take? (1 to 100, Default = 16 for None or non-int): ",
                1,
                100,
                16)
            print self.noOfCourses, 'courses'

            self.noOfSemesters = get_user_input_int(
                "What is the total number of semesters left? (1 to 100, Default = 8 for None or non-int): ",
                1,
                100,
                8)
            print self.noOfSemesters, 'semesters'

            self.coursesPerSemester = None
            while self.coursesPerSemester is None:
                self.coursesPerSemester = get_user_input_int(
                    "Courses per semester? (1 to 10000, Default = 2 for None or non-int): ",
                    1,
                    10000,
                    2)
            print self.coursesPerSemester, 'courses/semester'

            # check if data makes sense
            if self.noOfSemesters * self.coursesPerSemester < self.noOfCourses:
                print "You have too few semesters to finish the required number of courses. Check data and try again"
            else:
                break

        # terms
        self.terms = ['FALL', 'SPRING']
        self.startTerm = None
        while self.startTerm is None:
            self.startTerm = self.terms[get_user_input_int(
                "Start in (0)FALL or (1)SPRING?  (0 or 1 only, Default = 0 for None or non-int): ",
                0,
                1,
                0)]
            print 'Start term:', self.startTerm

        # semesters
        self.semesters = {}
        self.semesters_domain = []  # format (semester, term, index of course in courses, domain)
        start_term_index = self.terms.index(self.startTerm)  # 0 or 1
        for semester in range(0, self.noOfSemesters):
            self.semesters[semester] = {
                'term': self.terms[start_term_index],
                'courses': []
            }

            for x in range(0, self.coursesPerSemester):
                raw_courses_copy = copy.deepcopy(self.raw_courses)
                self.semesters_domain.append(
                    [semester,
                     self.terms[start_term_index],
                     x,
                     raw_courses_copy]
                )

            if start_term_index == 0:
                start_term_index = 1
            else:
                start_term_index = 0

        # no of plans to generate
        self.noOfPlans = None
        self.plans = []
        while self.noOfPlans is None:
            self.noOfPlans = get_user_input_int(
                "Number of plans to generate?  (1 to 100000 only, Default = 1 for None or non-int): ",
                1,
                100000,
                1)
            print self.noOfPlans, 'plans'

        self.startCourseUnique = [False, True][get_user_input_int(
            "Unique start course for every plan? (1)YES or (0)NO? (0 or 1 only, Default = 0(NO) for None or non-int): ",
            0,
            1,
            0)]
        if self.startCourseUnique:
            print 'Unique start course: True'
        else:
            print 'Unique start course: False'

        self.usedStartCourses = []

        # ================================INITIAL: TRIMMING THE DOMAINS===============================
        self.domain_trim_level_200()
        self.domain_trim_level_300()
        self.domain_trim_no_fall_spring_conflict()

    def domain_trim_level_200(self):
        "trims domains to remove courses above level 200, e.g. returns True if there were changes"
        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        for x in range(0, self.noOfCourses):

            d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain[x])

            # loop into every removing courses that their times don't work with the current course
            for current_course_in_domain in d_domain:
                if self.level200(current_course_in_domain):
                    self.semesters_domain[x][3].remove(current_course_in_domain)

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: LEVEL 200 trim, before', before_trimming
            print 'Domains length: LEVEL 200 trim, after ', after_trimming
            return True

    def domain_trim_level_300(self):
        "trims domains to remove courses above level 300, e.g. returns True if there were changes"
        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        for x in range(0, self.noOfCourses):

            d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain[x])

            # loop into every removing courses that their times don't work with the current course
            for current_course_in_domain in d_domain:
                if self.level300(current_course_in_domain):
                    self.semesters_domain[x][3].remove(current_course_in_domain)

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: LEVEL 300 trim, before', before_trimming
            print 'Domains length: LEVEL 300 trim, after ', after_trimming
            return True

    def domain_trim_no_fall_spring_conflict(self):
        "trims domains to avoid time conflicts, e.g. returns True if there were changes"

        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        # should only consider courses in the same semester
        terms = self.terms
        start_term = self.startTerm  # 'FALL OR SPRING'
        start_term_index = terms.index(start_term)  # 0 or 1

        if not len(terms) or not start_term:
            sys.exit('terms or start term is not defined')

        for x in range(0, self.noOfCourses, self.coursesPerSemester):

            # remove the course from all other domains
            for y in range(x, x + self.coursesPerSemester):
                this_term = terms[start_term_index]

                d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain)[y]

                # loop into every removing courses that their times don't work with the current course
                for current_course_in_domain in d_domain:
                    if not self.courses_fit_fall_spring(this_term, [current_course_in_domain]):
                        self.semesters_domain[y][3].remove(current_course_in_domain)
            if start_term_index == 0:
                start_term_index = 1
            else:
                start_term_index = 0

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: FALL SPRING trim, before', before_trimming
            print 'Domains length: FALL SPRING trim, after ', after_trimming
            return True

    def domain_trim_course_domain(self):
        "trims domains of all assigned courses to one, e.g. returns True if there were changes"
        course_list = self.get_courses_list()
        if len([course for course in course_list if course is not None]) == 0:
            return False

        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        for x in range(0, len(course_list)):
            if course_list[x] is None:
                continue
            current_course = course_list[x]
            # set the domain of the this course to it's position only
            self.semesters_domain[x][3] = [current_course]

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: COURSE DOMAIN trim, before', before_trimming
            print 'Domains length: COURSE DOMAIN trim, after ', after_trimming
            return True

    def domain_trim_no_repetition(self):
        "trims domains to avoid repetition of a course, e.g. returns True if there were changes"
        course_list = self.get_courses_list()
        if len([course for course in course_list if course is not None]) == 0:
            return False

        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        for x in range(0, len(course_list)):
            if course_list[x] is None:
                continue
            current_course = course_list[x]

            # remove the course from all other domains
            for y in range(0, len(self.semesters_domain)):
                d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain[y])
                if x == y:
                    continue  # avoid removing itself
                if current_course in d_domain:
                    self.semesters_domain[y][3].remove(current_course)

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: No repetition trim, before', before_trimming
            print 'Domains length: No repetition trim, after ', after_trimming
            return True

    def domain_trim_no_time_conflict(self):
        "trims domains to avoid time conflicts, e.g. returns True if there were changes"
        course_list = self.get_courses_list()
        if len([course for course in course_list if course is not None]) == 0:
            return False

        before_trimming = [len(domain[3]) for domain in self.semesters_domain]

        # should only consider courses in the same semester
        for x in range(0, len(course_list), self.coursesPerSemester):
            start_at_index = x

            current_course = course_list[start_at_index]

            # get the position of the non-None course in domain
            if current_course is None:
                for xd in range(start_at_index + 1, x + self.coursesPerSemester):
                    if course_list[xd] is not None:
                        start_at_index = xd
                        current_course = course_list[start_at_index]
                        break
            # if still None, skip this semester
            if current_course is None:
                continue

            # remove the course from all other domains
            # for y in range(start_at_index + 1, start_at_index + self.coursesPerSemester):
            for y in range(x, x + self.coursesPerSemester):
                if y == start_at_index:
                    continue  # avoid removing itself

                d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain[y])

                # loop into every removing courses that their times don't work with the current course
                for current_course_in_domain in d_domain:
                    temp_course_list = [current_course, current_course_in_domain]
                    if not self.checkTimeConflict(temp_course_list):
                        self.semesters_domain[y][3].remove(current_course_in_domain)

        after_trimming = [len(domain[3]) for domain in self.semesters_domain]
        if before_trimming == after_trimming:
            return False
        else:
            print 'Domains length: Time conflict trim, before', before_trimming
            print 'Domains length: Time conflict trim, after ', after_trimming
            return True

    def get_zero_domains(self):
        "returns the positions list of lists [d_semester, d_term, d_course_index, d_domain] of the zero domains or []"

        zero_domains = []

        for y in range(0, len(self.semesters_domain)):
            d_semester, d_term, d_course_index, d_domain = self.semesters_domain[y]
            if len(d_domain) == 0:
                zero_domains.append(copy.deepcopy(self.semesters_domain[y]))

        return zero_domains

    def plan_is_complete(self):

        all_courses = self.get_courses_list()

        if len([course for course in all_courses if course is not None]) < self.noOfCourses:
            return False

        if not self.check_constraints():
            return False

        return True

    def plan_is_complete_optimized(self):

        all_courses = self.get_courses_list()

        if len([course for course in all_courses if course is not None]) < self.noOfCourses:
            return False

        if not self.check_constraints_optimized():
            return False

        return True

    def get_successors(self, parent):

        all_courses = [course for course in self.raw_courses]

        successors = []
        for course in all_courses:

            if self.level200(course):
                continue

            if self.level300(course):
                continue

            if course['number'] == parent['number']:
                continue

            successors.append(copy.deepcopy(course))

        return successors

    def add_course(self, course):

        for semester in self.semesters:
            if len(self.semesters[semester]['courses']) < self.coursesPerSemester:
                self.semesters[semester]['courses'].append(copy.deepcopy(course))
                return self.semesters

        return self.semesters

    def get_successors_optimized(self, parent):

        # if all courses are filled, then just return []
        all_courses = self.get_courses_list()
        if len([course for course in all_courses if course is not None]) == self.noOfCourses:
            return []

        n_semester, n_term, n_course_index, n_position_in_course_list = self.get_next_course_position_in_order()
        return self.semesters_domain[n_position_in_course_list][3]

    def get_successors_optimized_filtering(self, parent):

        # if all courses are filled, then just return []
        all_courses = self.get_courses_list()
        if len([course for course in all_courses if course is not None]) == self.noOfCourses:
            return []

        # find the domain with the minimum remaining values
        mrv_domain = self.get_next_mrv_domain()
        if mrv_domain:
            d_semester, d_term, d_course_index, d_domain = mrv_domain
            return d_domain

        n_semester, n_term, n_course_index, n_position_in_course_list = self.get_next_course_position_in_order()
        return self.semesters_domain[n_position_in_course_list][3]

    def add_course_optimized_filtering(self, course):

        mrv_domain = self.get_next_mrv_domain()
        if mrv_domain:
            d_semester, d_term, d_course_index, d_domain = mrv_domain
            self.semesters[d_semester]['courses'].append(course)
            return self.semesters

        for semester in self.semesters:
            if len(self.semesters[semester]['courses']) < self.coursesPerSemester:
                self.semesters[semester]['courses'].append(copy.deepcopy(course))
                return self.semesters

        return self.semesters

    def get_next_mrv_domain(self):
        'returns domain with minimum remaining values, skips domains with len = 1 since already assigned'

        all_courses = self.get_courses_list()
        if len([course for course in all_courses if course is not None]) == self.noOfCourses:
            return False

        size = float("inf")
        lowest = None
        for y in range(len(self.semesters_domain) - 1, 0, -1):
            d_semester, d_term, d_course_index, d_domain = copy.deepcopy(self.semesters_domain[y])
            if len(d_domain) < size and len(d_domain) != 1:
                size = len(d_domain)
                lowest = [d_semester, d_term, d_course_index, d_domain]
        if lowest:
            return lowest

    def remove_course(self, course):

        for semester in self.semesters:
            if course in self.semesters[semester]['courses']:
                if course is None:
                    continue
                self.semesters[semester]['courses'].remove(course)
                return self.semesters

        return self.semesters

    def check_constraints(self):

        if not self.no_repetition(self.semesters):
            return False

        if not self.no_prerequisite_conflict(self.semesters):
            return False

        if not self.fits_fall_spring(self.semesters):
            return False

        if not self.no_time_conflict(self.semesters):
            return False
        return True

    def check_constraints_optimized_prerequisites(self):
        'breaks if it finds any constraints not satisified'

        if not self.no_prerequisite_conflict(self.semesters):
            return False

        return True

    def check_constraints_optimized(self):
        'breaks if it finds any constraints not satisifed'

        if not self.no_repetition(self.semesters):
            sys.exit('Constraint violation not allowed here')
            # return False

        if not self.no_prerequisite_conflict(self.semesters):
            return False

        if not self.fits_fall_spring(self.semesters):
            sys.exit('Constraint violation not allowed here')
            # return False

        if not self.no_time_conflict(self.semesters):
            sys.exit('Constraint violation not allowed here')
            # return False
        return True

    def no_repetition(self, semesters):
        # get course catalogs from the whole plan of study
        chosen_course_catalogs = []

        for semester in semesters:
            for course in semesters[semester]['courses']:
                if course is None:
                    continue
                chosen_course_catalogs.append(copy.deepcopy(course['cat_num']))

        if len(chosen_course_catalogs) != len(set(chosen_course_catalogs)):
            logger("repetition conflict")
            return False

        return True

    def fits_fall_spring(self, semesters):

        # checks if courses fit fall and spring schedules

        for semester in semesters:
            for course in semesters[semester]['courses']:
                if course is None:
                    continue

                if course['term'] == "":
                    continue

                if semesters[semester]['term'].lower() != course['term'].lower():
                    logger("Fall spring conflict")
                    return False

        return True

    def courses_fit_fall_spring(self, term, courses):

        # checks if courses fit fall and spring schedules
        # term has to be either 'FALL' or 'SPRING

        if term != 'FALL' and term != 'SPRING':
            sys.exit('term not equal to FALL or SPRING')

        for course in courses:
            if course is None:
                continue

            if course['term'] == "":
                continue

            if course['term'].lower() != term.lower():
                return False

        return True

    def no_time_conflict(self, semesters):

        for semester in semesters:
            if not self.checkTimeConflict(semesters[semester]['courses']):
                logger("Time conflict")
                return False

        return True

    def checkTimeConflict(self, course_list):
        # checks if there is a time conflict btn courses in a given list

        # days carries the course schedule dicts
        days = {
            1: [],  # monday
            2: [],  # tuesday
            3: [],  # wednesday
            4: [],  # thursday
            5: [],  # friday
            6: [],  # saturday
            7: []  # sunday
        }

        # put courses into their respective days
        for course in course_list:
            if course is None:
                continue
            if len(course['schedule']) > 0:
                for schedule in course['schedule']:
                    if schedule['day'] and schedule['begin_time'] and schedule['end_time']:
                        days[int(schedule['day'])].append(copy.deepcopy(schedule))

        # for each day, check that no course conflicts
        for day in days:
            day_schedules = days[day]
            time_tuples = []

            for schedule in day_schedules:
                time_tuples += getTimeTuples(schedule)

            # check for conflicts
            index = 0
            for startHour, startMin, startSec, endHour, endMin, endSec in time_tuples:
                start = datetime.time(startHour, startMin, startSec)
                end = datetime.time(endHour, endMin, endSec)

                # check all except itself
                for x in range(0, len(time_tuples)):
                    if index != x:

                        if time_in_range(start, end, datetime.time(time_tuples[x][0],
                                                                   time_tuples[x][1],
                                                                   time_tuples[x][2])) \
                                or time_in_range(start, end, datetime.time(time_tuples[x][3],
                                                                           time_tuples[x][4],
                                                                           time_tuples[x][5])):
                            return False

                index += 1

        return True

    def no_prerequisite_conflict(self, semesters):
        currentCourses = []

        def requirementIsFullFilled(requirement_code, currentCourseIndex):

            # directly allow permissions from instructor
            if requirement_code == 'perm':
                return True

            for x in range(0, currentCourseIndex - 1):
                if currentCourses[x] is None:
                    continue
                if self.get_course_code(currentCourses[x]) == requirement_code:
                    return True

            return False

        def and_requirementIsFullFilled(requirements_codes, currentCourseIndex):
            for x in range(0, len(requirements_codes)):
                if not requirementIsFullFilled(requirements_codes[x], currentCourseIndex):
                    return False
            return True

        currentCourses = self.get_courses_list()

        if len([course for course in currentCourses if course is not None]) == 0:
            return True

        for course_x in range(0, len(currentCourses)):
            if currentCourses[course_x] is None:
                continue

            requirements = currentCourses[course_x]['requirements']
            if bool(requirements):
                option_or_list = []
                for option in requirements:
                    if and_requirementIsFullFilled(requirements[option], course_x):
                        option_or_list.append(True)
                    else:
                        option_or_list.append(False)

                if True in option_or_list:
                    continue
                else:
                    logger("Prerequisite conflict")
                    return False
        return True

    def get_catalog_number_from_cust_code(self, code):
        # code format e.g COMPSCI50, perm

        if code == 'perm':
            return 'perm'

        for course in self.raw_courses:

            if course['cat_num']:
                course_code = course['field'].upper() + str(course['number'])
                if course_code == code:
                    return course['cat_num']

        if code[0] == "C":
            logger("Failed to locate " + code)
        return False

    def get_course_code(self, course):
        # code format e.g COMPSCI50, perm

        if not course['field']:
            return False

        if not course['number']:
            return False

        return course['field'] + course['number']

    def level200(self, course):

        course_string = str(course['number'])

        if len(course_string) < 3:
            return False
        if course_string[0] != str(2):
            return False
        return True

    def level300(self, course):
        course_string = str(course['number'])
        if len(course_string) < 3:
            return False
        if course_string[0] != str(3):
            return False
        return True

    def get_courses_list(self):
        # returns a list of courses in order from the semesters, [course, course, None, course, course, None]
        courses = []
        for semester in self.semesters:
            semester_courses = self.semesters[semester]['courses']
            for c in semester_courses:
                courses.append(c)
            if len(semester_courses) < self.coursesPerSemester:
                for d in range(0, self.coursesPerSemester - len(semester_courses)):
                    courses.append(None)
                    # courses += self.semesters[semester]['courses']
        return courses

    def get_course_position(self, course):
        "returns [semester, term, index of course in its courses, position_in_course_list]"
        for semester in self.semesters:
            if course in self.semesters[semester]['courses']:
                return [
                    semester
                    , self.semesters[semester]['term']
                    , self.semesters[semester]['courses'].index(course)
                    , (semester * self.coursesPerSemester) + self.semesters[semester]['courses'].index(course)
                ]
        return None

    def get_next_course_position_in_order(self):
        "returns next course in order [semester, term, index of course in it's courses,position_in_course_list ]"

        all_courses = self.get_courses_list()

        if len([course for course in all_courses if course is not None]) == 0:
            return None

        counter = 0
        for semester in self.semesters:
            courses = self.semesters[semester]['courses']
            counter += len(courses)

            # should equate to the index of next non-None course, since that's the one we consider next
            if counter == all_courses.index(None):
                return [
                    semester
                    , self.semesters[semester]['term']
                    , len(courses)
                    , counter
                ]

    def print_course_codes(self, semesters=None):
        if semesters is None:
            semesters = self.semesters
        courses = []
        for semester in semesters:
            for course in self.semesters[semester]['courses']:
                courses.append(course['field'] + " " + course['number'])
        logger(courses)

    def print_courses(self):
        for semester in self.semesters:
            courses = []

            for course in self.semesters[semester]['courses']:
                courses.append(course['field'] + " " + course['number'])

            logger(courses)
