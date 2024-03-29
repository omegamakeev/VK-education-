#coding: utf-8
def process_measurements():
    lines = []
    while True: 
        line = input()
        if not line: 
            break
        lines.append(line)
    num_sequences = int(lines[0])
    max_values = []
    for i in range(1, num_sequences + 1):
        measurements = list(map(int, lines[i].split()))
        max_value = max(measurements)
        max_values.append(max_value)
    max_values.sort(reverse=True)
    result = ";".join(map(str, max_values))
    return result 
print(process_measurements())
