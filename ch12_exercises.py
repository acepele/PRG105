"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 12.1 simple recursion
print("=" * 10, "Section 12.1 simple recursion", "=" * 10)


# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested
def main():
    times_requested(10)


def times_requested(times):
    if times > 0:
        print("Hooray!")
        times_requested(times - 1)


main()


# 2) Call the function with a parameter value of 5.
def main():
    times_requested(5)  # the main function calls the message function passing the argument 5.


main()

# TODO 12.2-12.3 problem solving with recursion
print("=" * 10, "Section 12.2-12.3 problem solving with recursion", "=" * 10)


# 1) Create a function that uses recursion to sum the numbers in a list.
#    The function should have one parameter, the list of numbers
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    my_sum = range_sum(numbers, 0, 14)
    print('The sum of items in the list is ', my_sum)


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


main()

# 2) Call the function using the numbers list as a parameter
