def calculate_mean(string_numbers):
    numbers = [int(x) for x in string_numbers.split()]
    return sum(numbers) / len(numbers)

while True:
    user_input = input()
    if not user_input:
        break
    print(calculate_mean(user_input))