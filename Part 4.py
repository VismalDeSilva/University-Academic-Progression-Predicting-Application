#I declare that my work contains no examples of misconduct such as plagiarism or collusion.
#Any code taken from other sources is referenced within my code solution.
#Vismal De Silva
#20220299
#w1953192
#Date - 13/12/2022

#initial values

list = [0, 20, 40, 60, 80, 100, 120]
progress = 0
trailer = 0
retriever = 0
exclude = 0
adding_dict = {}

#student version
def student_version():
 global input_pass, input_defer, input_fail, studentID

 studentID =input('Enter studentID:')

 while True:
    try:
        input_pass = int(input('Please enter your credits at pass '))
    except:
        print('Integer Required')
    else:
        if input_pass not in list:
            print('out of range')
        else:
            break

 while True:
    try:
        input_defer = int(input('Please enter your credits at defer'))
    except:
        print('Integer Required')
    else:
        if input_defer not in list:
                print('out of range')
        else:
            break

 while True:
    try:
        input_fail = int(input('Please enter your credit at fail'))
    except:
        print('Integer required')
    else:
        if input_fail not in list:
            print('out of range')
        else:
            break

    total_credits = input_pass + input_defer + input_fail

    if total_credits != 120:
        print('Total Incorrect')
        student_version()
    else:
        studentoutcome()

#student outcome
def studentoutcome():
    global validation ,progress, trailer, exclude, retriever, studentID, input_pass, input_defer, input_fail

    if input_pass == 120:
        print("progress")
        progress += 1

    elif input_pass == 100:
        print("Progress(Module Trailer)")
        trailer += 1

    elif input_fail >= 80:
        print("Exclude")
        exclude += 1

    else:
        print("Module Retriever")
        retriever += 1

#staff version
def staff_version():
    global input_pass, input_defer, input_fail, studentID
    studentID = input('Enter studentID:')

    while True:
        try:
            input_pass = int(input('Enter your total PASS credits'))
        except:
            print('Integer Required')
        else:
            if input_pass not in list:
                print('out of range')
            else:
                break

    while True:
        try:
            input_defer = int(input('Enter your total DEFER credits'))
        except:
            print('Integer Required')
        else:
            if input_defer not in list:
                print('out of range')
            else:
                break

    while True:
        try:
            input_fail = int(input('Enter your total Fail credits'))
        except:
            print('Integer Required')
        else:
            if input_fail not in list:
                print('out of range')
            else:
                break
    total_credits = input_pass + input_defer + input_fail
    if total_credits != 120:
        print('Total Incorrect')
        staff_version()
    else:
        staffoutcome()

#staffoutcome
def staffoutcome():
    global validation, progress, trailer, retriever, exclude, studentID

    if input_pass == 120:
        print("progress")
        adding_dict[studentID] = f'progress - {input_pass},{input_defer},{input_fail}'
        progress += 1

    elif input_pass == 100:
        print("progress(Module Trailer)")
        adding_dict[studentID] = f'Progress (Module Trailer)- {input_pass},{input_defer},{input_fail}'
        trailer += 1

    elif input_fail >= 80:
        print("Exclude")
        adding_dict[studentID] = f'Exclude - {input_pass},{input_defer},{input_fail}'
        exclude += 1

    else:
        print("Module Retriever")
        adding_dict[studentID] = f'Module Retriever- {input_pass},{input_defer},{input_fail}'
        retriever += 1

    user()

#asking whether user want to continue or quit
def user():
    global H

    H = input('Would you like to enter another set of data?\n'
              'Enter "y" for yes or "q" to quit and view results :').lower()

    if H == 'y':
        staff_version()

    elif H == 'q':
        horizontal_histogram()
    elif ValueError:
        print('Invalid Input')
        user()

#creating the horizontal histogram
def horizontal_histogram():
    print('---------------------------------')
    print('Horizontal Histogram')
    print('\nProgress', progress, ' : ', '*' * progress)
    print('\nTrailer', trailer, ' : ', '*' * trailer)
    print('\nRetriever', retriever, ' : ', '*' * retriever)
    print('\nExcluded', exclude, ' : ', '*' * exclude)

    total_outcome = progress + trailer + retriever + exclude
    print('\n', total_outcome, 'outcome in total.')
    print('---------------------------')

    for (element1,element2) in  adding_dict.items():
       print(element1, ':' , element2 , end='  ')


def main_part():
    print('------------', 'Menu', '----------')
    choice_1 = input('Enter 1 for student version ; Enter 2 for staff version : ')

    if choice_1 == '1':
        student_version()
        studentoutcome()

    elif choice_1 == '2':
        staff_version()

    else:
        print('Invalid Input')
        main_part()


main_part()


