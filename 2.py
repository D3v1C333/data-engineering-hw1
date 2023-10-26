result = list()
file_name = 'text_2_var_11'
with open(file_name) as file:
    lines = file.readlines()

for line in lines:
    nums = line.strip().split('/')
    line_sum = 0

    for index, num in enumerate(nums):
        line_sum += int(num)
    result.append(line_sum / (index + 1))

with open(f"result_{file_name}", "w") as f:
    for result_average in result:
        f.write(f"{result_average}\n")
