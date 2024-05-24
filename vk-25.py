class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        # YOUR CODE HERE
        return Circle.pi * radius ** 2

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)