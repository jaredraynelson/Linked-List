from course import Course
from courselist import CourseList
dict_lyst_courses = {}
def read_file(file):
    '''
    TAKES A COMMA DELIMITED TXT FILE AND CREATE A DICTIONARY
    '''
    global dict_lyst_courses
    with open(file, 'r') as f:

        lines = f.readlines()
        for line in lines:
            elements = line.strip().split(',')
            if elements[0] not in dict_lyst_courses:
                dict_lyst_courses[elements[0]] = elements




def main():
    '''
    CREATES AN OBJECT linked_lyst & PRINTS IT
    & USES COURSE METHOD TO CALCULATE GPA
    '''
    global dict_lyst_courses
    read_file('data.txt')
    linked_lyst = CourseList()
    for i in dict_lyst_courses.keys():
        linked_lyst.insert(Course(int(i),dict_lyst_courses[i][1],
        float(dict_lyst_courses[i][2]),float(dict_lyst_courses[i][-1])))
    print(linked_lyst)
    print('CUMULATIVE GPA:',f'{linked_lyst.calculate_gpa():.3f}')



if __name__ == '__main__':
    main()