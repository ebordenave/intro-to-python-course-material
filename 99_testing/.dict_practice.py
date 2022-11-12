# pets = {'name': 'Ernie', 'animal': 'dog', 'breed': 'Pug', 'age': 2}
#
# for k, v in pets.items():
#     print(k, v)


def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(Name='Marlena', Job='Leadership Coach', Topic='Education')
#
# Unpacking dictionaries is the opposite of packing them. It can be used if you have an existing dictionary that you
# would like to send to a function.
#
# Consider this code:
#
# teacher = {
#   'name':'Ashley',
#   'job':'Instructor',
#   'topic':'Python'
# }
#
# def print_teacher(name, job, topic): print(name) print(job) print(topic) First, we have a dictionary called teacher
# that holds three key:value pairs: name, job, and topic, each with corresponding values.
#
# Then, we have a function called print_teacher that receives three arguments, name, job, and topic.
#
# To pass the data from the teacher dictionary to this function, we can use unpacking to easily and quickly
# extrapolate the data into a format the function will accept.
#
# To do that, we use a function call where the passed argument is **teacher.
#
# print_teacher(**teacher) This ** unpacks all the key:value pairs in the teacher dictionary into three keyword
# arguments, which are then accepted by the function into the three corresponding parameters.


