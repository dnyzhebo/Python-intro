courses = ['Hist','Math','Physics','CompSci']

print(courses)
print(len(courses))
print(courses[0:2])
print(courses[2:])

#Methods to modify list

courses.append('Art')
print(courses)

courses.insert(0,'Art')

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)