from lib.most_often import *

# def test_reminder():
#     # create an instance of the class
#     reminder = Reminder('Sam')
#     # call each method individually
#     reminder.remind_me_to('eat nourishing lunch')
#     # hold the method that you want to give the final result in a variable
#     result = reminder.remind()
#     # use assert to show what the test should return
#     assert result == 'eat nourishing lunch,Sam!'





# def test_most_often_starting_list():
#     starting_list = [1,2,3]
#     box = MostOften(starting_list)
#     assert starting_list == box.starting_list


def test_most_often_add_new():
    starting_list = [1,2,3,4]
    box = MostOften(starting_list)
    # create instance which has a list of 1,2,3,4
    box.add_new(5)
    assert box.starting_list == [1,2,3,4,5]



def test_most_often_highest_item():
    list = ['bread', 'jam', 'cakes', 'hummus']
    basket = MostOften(list)
    basket.add_new('bread')
    result = basket.get_most_often()
    assert result == 'bread'


def test_most_often_no_clear_winner():
    list = ['bread', 'jam', 'cakes', 'hummus']
    basket = MostOften(list)
    result = basket.get_most_often()
    assert result == 'no clear winner'


# bag = MostOften([1,2,3,4,5,5,5,5,5,5])

# bag.get_most_often()