import math

result = list()
file_name = 'text_3_var_11'
with open(file_name) as file:
    lines = file.readlines()

with open(f"result_{file_name}", "w") as file:
    for line in lines:
        nums = line.strip().split(',')
        for i in range(len(nums)):
            if nums[i] == "NA":
                nums[i] = (int(nums[i - 1]) + int(nums[i + 1])) / 2
        for num in nums:
            if math.sqrt(float(num)) >= 61:  # 50 + 11(номер варианта) = 61
                file.write(f"{int(num)},")

        file.write('\n')
