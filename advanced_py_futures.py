# future number 1 "unpacking"
# a, b, c = [1, 2, 3]
# print(a, b, c)

# extended Iterable Unpacking with *
# a, *b, c = [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"a:{a}, b:{b}, c:{c}")

# ignoring values with _#
# _, _, a = ["a", "b", 1]
# print(a)

# unpaking nested structures
# data = ("Alice", (25, "Engineer"))
# name, (age, proffession) = data
# print(age)

# combining lists with unpacking
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = [*list1, *list2]
# print(combined)

# combined dict unpacking
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5, "f": 6}
# combined_dict = {**dict1, **dict2}
# print((combined_dict))

# inline swap
# x = 10
# y = 20
# print(f"before swap x:{x}, y:{y}")
# x, y = y, x
# print(f"after swap x:{x}, y:{y}")
"""
მოკლე რას დეკორატორი მარტივად რომ ვთქვათ არის წინასწარ გაწერილი ფუნქცია რომელიც მოიაზრებს რაღაც ლოგიკას და შემდეგ იგი ამ ლოგიკას ახორციელებს სხვა ფუნქციაზე უხეშად რომ ვთქვათ სძენს მას ახალ თვისებებს მაგალითად.
რეალურად ვრაპერ ფუნქციის სახით ახცალ ფუნქციას ქმნი რომელიც სამოქმედო ფუნქციას იძახებს რომელიც პარამეტრია დეცორატორის და ამავდროულად ახორციელებს საკუთარ ლოგიკას

"""
from types import WrapperDescriptorType


def my_decorator(func):  # function that will be effected by decorator
    def wrapper(
        *args,
        **kwargs,  # wrapper function that will do some logic and than returns the function that beinged efected
    ):
        print("before function execution")
        result = func(*args, **kwargs)
        print("after function execution")
        return result  # here the aim function being executed

    return wrapper  # here wrapped being executed from decorator


@my_decorator
def hello_func(name):
    print(f"hello {name}")


hello_func("Merab")
