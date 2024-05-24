class Dictionary:
    def __init__(self, dictionary):
        # YOUR CODE HERE
        self._dictionary = dictionary

    def __call__(self, key):
        # YOUR CODE HERE
        if key in self._dictionary:
            return self._dictionary[key]
        else:
            return None

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)