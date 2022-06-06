class Node(object):
    '''
    A WAY WHICH YOU CAN REFERENCE
    ANY OBJECT THROUGH A NODE WITH
    A NEXT VALUE AND A REFERENCE TO
    THE OBJECT ITSELF = course_info
    '''
    def __init__(self, course_info=None):
        self.course_info = course_info
        self.next = None


class CourseList(object):
    '''
    MAKES A LIST OF NODES FROM
    WHATEVER NODES ARE PLACED IN IT
    '''
    def __init__(self):
        self.head = None
        self.counter = 0


    def __str__(self):
        '''
        PRINTS OUT STRING METHOD
        '''

        tmp_str = ''
        node = self.head
        while node:
            tmp_str += str(node.course_info)+ '\n'
            node = node.next
        return tmp_str


    def __iter__(self):
        '''
        THE ITERATION METHOD
        '''
        node = self.head #CS1400
        while node:
            yield node
            node = node.next


    def insert(self, inserted_value):
        '''
        INSERTS AN OBJECT IN THE LIST IN ASCENDING ORDER
        (LEAST TO GREATEST) BASED ON CLASS NUMBER
        '''
        self.counter += 1
        new_node = Node(inserted_value)
        current_node = self.head
        # THE FIRST TYPE = NOTHING IN LIST
        if self.head is None:
            self.head = new_node
            # THE SECOND TYPE = 1 ITEM IN LIST
        elif self.counter == 2:
            if new_node.course_info.course_number < current_node.course_info.course_number:
                temp_node = current_node
                self.head = new_node
                new_node.next = temp_node
            else:
                current_node.next = new_node
            # THE THIRD TYPE = MULTIPLE ITEMS IN LIST
        else:
            # THREE CASES.

            current_node = self.head
            next_node = current_node.next
            #  FIRST CASE:
            if new_node.course_info.course_number < current_node.course_info.course_number:
                new_node.next = current_node
                self.head = new_node

            else:
                next_node = current_node.next
                while next_node:
                    # SECOND CASE IF SOMEWHERE IN MIDDLE OF LIST
                    if (new_node.course_info.course_number > current_node.course_info.course_number 
                    and new_node.course_info.course_number < next_node.course_info.course_number):
                        new_node.next = current_node.next
                        current_node.next = new_node
                        return

                    current_node = next_node
                    next_node = next_node.next
                #  GET TO END OF WHILE LOOP AND MAKE INSERTION AT END OF LIST
                current_node.next = new_node



    def remove(self, item):
        '''
        # RECEIVES THE COURSE NUMBER AND ELIMINATES THAT FROM CURRENT LIST
        '''
        self.counter -= 1
        current_node = self.head
        next_node = current_node.next
        previous_node = None
        while current_node:
            if current_node.course_info.course_number == item:
                # IN THIS CASE, THIS IS THE FIRST ELEMENT IN THE LIST
                if previous_node is None:
                    self.head = next_node
                    current_node.next = None
                    return
                else:
                    previous_node.next = next_node
                    current_node.next = None
                    return

            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

    def remove_all(self,item):
        '''
        # RECEIVES THE COURSE NUMBER AND ELIMINATES ALL INSTANCES OF COURSE NUMBER  FROM CURRENT LIST
        '''
        current_node = self.head
        next_node = current_node.next
        previous_node = None
        while next_node:
            if current_node.course_info.course_number == item:
                # IN THIS CASE, THIS IS THE FIRST ELEMENT IN THE LIST
                if previous_node is None:
                    self.counter -= 1
                    self.head = next_node
                    current_node.next = None

                else:
                    self.counter -= 1
                    previous_node.next = next_node
                    current_node.next = None


            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

    def calculate_gpa(self):
        '''
        CALCULATES THE GPA OF THE ENTIRE LINKED LIST
        '''
        if self.head==None:
            return 0.0
        else:
            credits = 0
            gpa = 0
            node = self.head
            while node:
                credits += node.course_info.credit_hour
                gpa += (node.course_info.grade_value*node.course_info.credit_hour)
                node = node.next

        return gpa/credits


    def size(self):
        return self.counter


    def is_sorted(self):
        lyst = []
        node = self.head
        while node:
            lyst.append(node.course_info.course_number)
            node = node.next
        if lyst == sorted(lyst):
            return True
        else:
            return False

    def find(self, item):
        '''
        FIND ELEMENT IN THE LINKED LIST, RETURNS TRUE, FALSE IF NOT FOUND.
        '''
        current_node = self.head
        next_node = current_node.next
        while current_node:
            if current_node.course_info.course_number == item:
                return current_node.course_info
            current_node = next_node
            next_node = current_node.next
        return False