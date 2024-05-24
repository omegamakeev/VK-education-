class Person:
    def __init__(self, age):
        # YOUR CODE HERE
        self._age = age if age >= 0 else 0

    @property
    def age(self):
        # YOUR CODE HERE
        return self._age

    @age.setter
    def age(self, value):
        # YOUR CODE HERE
        self._age = value if value >= 0 else 0

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)