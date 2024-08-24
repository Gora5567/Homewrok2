import helper

helper.start_task(1)

car_model = "Toyota Corolla"
car_color = "Red"
car_year = 2020
car_doors = 4
car_color = "Blue"
print("Model:", car_model)
print("Color:", car_color)
print("Year:", car_year)
print("Doors:", car_doors)

helper.end_task(1)

helper.start_task(2)

age_person1 = 25
age_person2 = 30
age_person3 = 22
age_person4 = 27
age_person5 = 35
total_people = 5
average_age = (age_person1 + age_person2 + age_person3 + age_person4 + age_person5) / total_people
print("Average Age:", average_age)

helper.end_task(2)