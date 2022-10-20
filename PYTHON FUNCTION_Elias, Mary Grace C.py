"""
Problem 1_1:
Write a function problem1_1() that prints "Problem Set 1". 

Tip: Be careful that your program outputs this exact phrase with no additional 
characters.  It will be graded automatically and must be precise.  Here is the
run of my solved problem 1_1:

problem1_1()
Problem Set 1

Note the problem1_1() is what I typed to run the problem and "Problem Set 1" is
what it printed out.  There will typically be a sample run such as this either 
before or after the statement of each problem. This helps clarify what you
are expected to do and shows how the auto-grader expects it to look.
"""
def problem1_1():
    print("Problem Set 1")
def problem1_1():
    print("Problem Set 1")
    return
problem1_1()





"""
Problem 1_2:
Write a function problem1_2(x,y) that prints the sum and product of the
numbers x and y on separate lines, the sum printing first.
"""

"""
Test run. Note that the grader program will use different numbers:

problem1_2(3,5)
8
15
"""
def problem1_2(x,y):
    print(x+y)
    print(x*y)
x = int(input("Choose a value for x: "))
y = int(input("Choose a value for y: "))

print(problem1_2(x,y))
print("")



"""
Problem 1_3:
Write a function 'problem1_3(miles)' to convert miles to feet. There are
5280 feet in each mile. Make the print out a statement as follows:
"There are 10560 feet in 2 miles."  Except for the numbers this statement 
should be exactly as written.

Tip: Watch the spacing before and after your numbers.  Make sure that it is 
just one space or the auto-grader may not give you credit.
"""


"""
Test run. Note that the grader program will use different numbers:

problem1_3(5)
There are 26400 feet in 5 miles.
"""
def problem1_3(miles):
    feet = 5280*miles
    return feet

miles = int(input("Give a measurement in miles: "))
feet = problem1_3 (miles)
print("There are " + str(feet) + " feet in " + str(miles) + " miles.")
print("")



"""
Problem 1_4:
Write a function problem1_4() that computes the area of a trapezoid. Here is the
formula: A = (1/2)(b1+b2)h. In the formula b1 is the length of one of the 
bases, b2 the other. The height is h and the area is A. Basically, this 
takes the average of the two bases times the height. For a rectangle b1 = b2, 
so this reduces to b1*h. This means that you can do a pretty good test of the 
correctness of your function using a rectangle (that way you can compute the 
answer in your head). Use input statements to ask for the bases and the height.
Convert these input strings to real numbers using float(). Print the output
nicely EXACTLY like mine below.

Tip: Be careful that your output on the test case below is exactly as shown
so that the auto-grader judges your output correctly.  The auto-grader does
not look at your input statements, so you don't have to use my input prompts
if you don't want to. However, the auto-grader will enter the three inputs in
the order shown. See the other test run below.

problem1_4()

Enter the length of one of the bases: 3

Enter the length of the other base: 4

Enter the height: 8
The area of a trapezoid with bases 3.0 and 4.0 and height 8.0 is 28.0

"""  
def problem1_4():
    pass
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    A = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases",b1,"and",b2,"and height",h, "is", A)
problem1_4()


"""
Another test run. In grading, expect different input numbers to be used.

problem1_4()

Enter the length of one of the bases: 10

Enter the length of the other base: 11

Enter the height: 12
The area of a trapezoid with bases 10.0 and 11.0 and height 12.0 is 126.0

"""


