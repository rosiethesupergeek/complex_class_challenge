# import the file you want to test

from lib.reminder import *

# to test a class you need to test each part of the class

# define a test function to do so
def test_reminder():
    # create an instance of the class
    reminder = Reminder('Sam')
    # call each method individually
    reminder.remind_me_to('eat nourishing lunch')
    # hold the method that you want to give the final result in a variable
    result = reminder.remind()
    # use assert to show what the test should return
    assert result == 'eat nourishing lunch,Sam!'

    