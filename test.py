import json


class CLASSES:
    def __init__(self):
        self.raw_courses = []

        with open('compsci.json') as data_file:
            self.raw_courses = json.load(data_file)

        # self.courses = []
        # for course in self.raw_courses:
        #     if not self.level200(course) or not self.level300(course):
        #         self.courses.append(course)
        #
        # print len(self.courses)

        # self.semesters = {
        #     0: {
        #         'term': 'FALL',
        #         'courses': []
        #     },
        #     1: {
        #         'term': 'SPRING',
        #         'courses': []
        #     },
        #     2: {
        #         'term': 'FALL',
        #         'courses': []
        #     },
        #     3: {
        #         'term': 'SPRING',
        #         'courses': []
        #     },
        #     4: {
        #         'term': 'FALL',
        #         'courses': []
        #     },
        #     5: {
        #         'term': 'SPRING',
        #         'courses': []
        #     },
        #     6: {
        #         'term': 'FALL',
        #         'courses': []
        #     },
        #     7: {
        #         'term': 'SPRING',
        #         'courses': []
        #     }
        # }

        # self.semesters = test.CLASSES().semesters

        self.semesters = {
            0: {
                'term': 'FALL',
                'courses': [
                    {
                        "cat_num": "49491",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "50",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "49492",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "51",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            1: {
                'term': 'SPRING',
                'courses': [
                    {
                        "cat_num": "49493",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "52",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                            "1": [
                                "COMPSCI50",
                            ],
                            "2": [
                                "COMPSCI51",
                            ]
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "49494",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "53",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            2: {
                'term': 'FALL',
                'courses': [
                    {
                        "cat_num": "49495",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "54",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "49496",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "55",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            3: {
                'term': 'SPRING',
                'courses': [
                    {
                        "cat_num": "49497",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "56",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "49498",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "57",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            4: {
                'term': 'FALL',
                'courses': [
                    {
                        "cat_num": "49499",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "58",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "494910",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "59",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            5: {
                'term': 'SPRING',
                'courses': [
                    {
                        "cat_num": "494911",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "60",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "494912",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "61",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            6: {
                'term': 'FALL',
                'courses': [
                    {
                        "cat_num": "494913",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "62",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "494914",
                        "term": "FALL",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "63",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            },
            7: {
                'term': 'SPRING',
                'courses': [
                    {
                        "cat_num": "494915",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "64",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "13:00:00",
                                "end_time": "14:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    },
                    {
                        "cat_num": "494916",
                        "term": "SPRING",
                        "bracketed": False,
                        "field": "COMPSCI",
                        "number": "65",
                        "title": "Introduction to Computer Science I",
                        "faculty": [
                            {
                                "id": "F98d2c536d93571eff451df8bd44823d8",
                                "first": "David",
                                "middle": "J.",
                                "last": "Malan",
                                "suffix": ""
                            }
                        ],
                        "schedule": [
                            {
                                "day": "1",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            },
                            {
                                "day": "3",
                                "type": "Lecture",
                                "optional": False,
                                "begin_time": "10:00:00",
                                "end_time": "11:30:00"
                            }
                        ],
                        "locations": [
                            {
                                "type": "Lecture",
                                "building": "Memorial Hall",
                                "room": "Sanders Theatre"
                            }
                        ],
                        "description": "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience.",
                        "prerequisites": "",
                        "requirements": {
                        },
                        "notes": "Undergraduates, GSAS students, and cross-registered students may take CS50 either Satisfactory/Unsatisfactory (SAT/UNS) or for a letter grade. To take CS50 SAT/UNS, register for catalog number 43861. To take CS50 for a letter grade, register for catalog number 4949. When taken for a letter grade, this course meets the General Education requirement for undergraduates for Empirical and Mathematical Reasoning. See course website for FAQs. This course will also meet on Fri 9/5 and Fri 10/17. Students with conflicts may watch those lectures online."
                    }
                ]
            }
        }
