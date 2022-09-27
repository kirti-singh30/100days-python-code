import random
# names = ["Avinash","Kirti","Anshul","Golu","Kaju","Molu"]
# student_score = {student:random.randint(1, 100) for student in names}
# print(student_score)
#passed_student = {student:score for (student,score)in student_score.items() if score > 60}


#print(passed_student)
#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#result = {word:len(word) for word in sentence.split()}
# alternate method
#new_sentence = sentence.split()
#print(new_sentence)
#result = {new_key:new_value for item in list} # its a structure of writing a dict comp with list
#result = {word:len(word) for word in new_sentence}
#print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:temp_c * 9/5 +32 for (day,temp_c)in weather_c.items()}
# print(weather_f)
import pandas

weather_x = {
    "student": [12,14,27],
    "Tuesday": [14,34,56],
    "Wednesday":[15,45,67],
}
weather_x_dataframe = pandas.DataFrame(weather_x)
# for (key,value) in weather_x_dataframe.items():
#     print(key)
#loop through the dataframe
for(index,row) in weather_x_dataframe.iterrows():
    if row.student == 14:
        print(row.Wednesday)
weather_y = {row.student:row.Wednesday for (index,row)in weather_x_dataframe.iterrows()}
print(weather_y)