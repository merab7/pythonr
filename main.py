# OOP in python


# self is an instance
class Employee:
    # this is init function we can say that this is initialation function or contractor
    # functio witch is being run authomathicaly after every instantation of the
    # object from this class
    raise_amount = 1.04  # this raize amount is a class variable and
    employee_num = 0  # ეს აᲠᲡ თანამშრომელთა რაოდენობა და როცა კლასი იქნება გამოძახებული მე მოინდა რომ თნამშრომლის რაოდენობა ზოგადად კლასში გაიზარდოს და
    # არა ინსტენსის მიხედვით რაც აზრს მოკლებული იქნება შესაბამისად +=1 იმპლემენტაცია მოხდება initფუნქციაში რომელიც აქტიურდება ავტომატურად ყოველ ინიცირებაზე კლასისა
    # ოღOნდ აქ მთაქფვარი ისაა რომ ის გაწერილი იქნება slef-ის გარეშე პირდაპირ კლასით Employee.employee_num

    # it can be accessed from every instance of clas or from every method of class
    # but to be accessed form method we have to nuse instance or class name itself (self.rize_amount OR Employee.rize_amount)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.employee_num += 1

    def fullName(self):
        """
        returns the fullname of the employee as a string
        """
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # creating alternativ constructor using class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
        """
        here cls is the representation of Employee as self is the representation of each object made from this class
        """


emp1 = Employee(first="merab", last="todua", pay="70000$")
emp2 = Employee(first="test", last="user", pay="90000$")

emp_str_1 = "John-Doe-70000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
