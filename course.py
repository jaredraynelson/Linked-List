from courselist import CourseList

class Course():
    def __init__(self, number=0, name='', credit_hr=0.0, grade=0.0):
        '''
        course number, course name, credit hours, grade
        '''
        self.course_number = number
        self.course_name = name
        self.credit_hour = credit_hr
        self.grade_value = grade
        self.next = None
        self.is_instance_check()

    def __str__(self):
        '''returns a string representing a single
        # Course as shown in the Program Output section'''
        return ('CS'+str(self.course_number)+' '+self.course_name+' Grade:' +
                str(self.grade_value)+' Credit Hours: '+str(self.credit_hour))

    def number(self):
        '''retrieve Course Number as an integer'''
        return self.course_number

    def name(self):
        '''retrieve Course Name as a string'''
        return self.course_name

    def credit_hr(self):
        '''retrieve Credits as a flotaing-points number'''
        return float(self.credit_hour)

    def grade(self):
        '''retreive grade as a numberic value in range 4.0-0.0
        print(self.grade)'''
        return float(self.grade_value)

    def is_instance_check(self):
        '''
        AUTOMATICALLY CHECKS TO SEE IF THE CORRECT
        VALUES ARE PUT INTO THE CLASS

        COURSE = INT, NAME = STR, GRADE & CREDIT_HR = FLOAT

        '''
        if not isinstance(self.course_number, int) or  self.course_number<0:
            raise ValueError
        if not isinstance(self.course_name, str):
            raise ValueError
        if not isinstance(self.credit_hour, float) or self.credit_hour < 0:
            raise ValueError
        if not isinstance(self.grade_value, float) or self.grade_value < 0:
            raise ValueError

