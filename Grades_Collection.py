from statistics import median


def current_grade():
    print("To stop the program enter stop!")
    grade_list = []
    bigger_than_past = []
    bigger_than_average = []
    bigger_than_median = []
    position = 0
    #Loop to get the grades
    i = 1
    while i != 0:
        grade = input("Enter a grade: ")
        if grade == "stop" or grade == "Stop" or grade == "STOP":
            i = 0
        else:
            grade = int(grade)
            if 0 >= grade >= 100:
                print("Please enter a valid grade 'Between 0 and 100' ")
                print("To stop the program enter stop!")
            else:
                grade_list.append(grade)
                position = position + 1
    print("Grades: " + str (grade_list))
    # Calling the function to get the past grade
    past_grade = func_get_past_grade_()

    # List of umbers bigger than the entered past grade
    bigger_than_past = func_list_bigger_than_number(grade_list,past_grade)
    bigger_than_past.sort(reverse=True)
    print("Grades bigger than the past grade: " + str(bigger_than_past))

    #The average of the grades
    grade_average = sum(grade_list)/len(grade_list)
    print("Average grade: " + str(grade_average))

    # List of numbers bigger than the average grade
    bigger_than_average = func_list_bigger_than_number(grade_list,grade_average)
    bigger_than_average.sort(reverse=True)
    print("Grades bigger than the average grade: " + str(bigger_than_average))

    # The median
    calculated_median = median(grade_list)
    print("Median: " + str(calculated_median))

    # List of numbers bigger than the median
    bigger_than_median = func_list_bigger_than_number(grade_list,calculated_median)
    bigger_than_median.sort(reverse=True)
    print("Grades bigger than the median: " + str(bigger_than_median))

#Function to get a list bigget than a number 
def func_list_bigger_than_number(grade_list,the_number):
    bigger_than_number = []
    for x in grade_list:
        if the_number <= x:
            bigger_than_number.append(x)
    return bigger_than_number
    
#Function to get the past grade
def func_get_past_grade_():
    j = 1
    while j != 0:
        past_grade = input("Enter a past grade: ")
        past_grade = int(past_grade)
        if 0 >= past_grade >= 100:
            print("Please enter a valid grade 'Between 0 and 100' ")
        else:
            j = 0
    return past_grade


current_grade()






