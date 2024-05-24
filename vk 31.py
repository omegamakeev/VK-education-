class ContextDictionary:
    def __init__(self):
        self.dictionary = None

    def __enter__(self):
        # YOUR CODE HERE
        self.dictionary = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        self.dictionary = None

    def put(self, key, value):
        if self.dictionary is not None:
            self.dictionary[key] = value
        else:
            raise RuntimeError("Dictionary is not available in the current context")

    def get(self, key):
        if self.dictionary is not None:
            return self.dictionary[key]
        else:
            raise RuntimeError("Dictionary is not available in the current context")

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)