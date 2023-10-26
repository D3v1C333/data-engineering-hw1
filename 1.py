import re

result = dict()
file_name = 'text_1_var_11'
with open(file_name) as file:
    lines = file.readlines()

for line in lines:
    line = re.sub(r'[!?,.\n]', ' ', line)
    words = line.split()

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

with open(f"result_{file_name}", "w") as f:
    for key, value in sorted_result.items():
        f.write(f"{key}: {value}\n")
