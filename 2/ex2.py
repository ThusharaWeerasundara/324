from dataclasses import dataclass   #to make student class
from typing import List, Dict       #to use in Student class

@dataclass

class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]

def load_course_registrations(filename: str) -> List[Student]:

    students = []  #list to store student objects

    with open(filename) as file:    #open input file

        for line in file:   #using a loop to create student objects and store them in a list
            row = line.strip()
            fname,lname,*courses = row.split(',')
            student = Student(fname,lname,courses)
            students.append(student)
           
    return students #return list



students = load_course_registrations("details.txt") #calling to read the file and get list of students

sorted_by_names = sorted(students, key = lambda s: s.surname + s.given_name) #return a new list after sorting by name ex2
sorted_by_courses = sorted(students, key = lambda s: len(s.registered_courses)) #return a new list after sorting by no. of courses ex2(b)

print("Sort by name")
print(sorted_by_names[0]) #checking values
print(sorted_by_names[1])
print(sorted_by_names[2])
print(sorted_by_names[3])
print(sorted_by_names[4])

print("\nSort by no. of courses ex2(b)")
print(sorted_by_courses[0]) #checking values
print(sorted_by_courses[1])
print(sorted_by_courses[2])
print(sorted_by_courses[3])
print(sorted_by_courses[4])



