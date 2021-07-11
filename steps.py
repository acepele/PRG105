days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
Min = 20000000
Max = 0
days_and_steps = {}
print("You will be entering the date and the number of steps taken for each day in a week.")


def steps(day):
    total = 0
    for step in day:
        total += day[step]
    average = total / len(days)
    print("Your average of steps was: " + str(average))

def max(day):
    for step in day:
        if day[step] > max:
            max[step] = (day[step])
    print("Your max number of steps is: " + str(max))
