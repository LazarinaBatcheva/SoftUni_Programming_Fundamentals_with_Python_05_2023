number_of_people = int(input())
elevator_capacity = int(input())
courses = 0
if number_of_people % elevator_capacity == 0:
    courses = number_of_people / elevator_capacity
else:
    courses = number_of_people // elevator_capacity + 1
print(courses)