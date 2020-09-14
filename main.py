import math

def into_reversed_chunks(l, n):
    for i in range(0, len(l), n):
        chunk = l[i:i+n]
        chunk.reverse()
        yield chunk

input = 1848

print("Question:")
print(f"{input}/10 = ?/2 = ?/16")
print()

loop_num = input
binary_nums = []
loop_nums = []
while loop_num != 0:
    loop_nums.append(loop_num)
    binary_nums.append(loop_num%2)
    loop_num = math.trunc(loop_num / 2)

print("Convert to binary:")
count = 0
biggest_num = len(str(max(loop_nums)))
for num in binary_nums:
    if count == 0:
        symbol = "^"
    else:
        symbol = "|"
    print(f"{loop_nums[count]:{biggest_num}} | {num} {symbol}")
    count += 1
print(f"{0:{biggest_num}} |   -")
print()

binary_nums.reverse()
binary_str = "".join(str(v) for v in binary_nums)
binary_nums.reverse()

count = 0
binary_check = []
binary_check_str_0 = ""
binary_check_str_1 = ""
start = True
for i in binary_nums:
    if i == 1:
        binary_check.append(pow(2, count))
        if not start:
            symbol = "+"
        else:
            symbol = ""
            start = False
        binary_check_str_0 += f"{symbol} 2^{count} "
        binary_check_str_1 += f"{symbol} {pow(2, count)} "
    count += 1
binary_checked = sum(binary_check)

print("Check if converting to binary was correct:")
print(f"{input}/10 = {binary_str}/2 ={binary_check_str_0}={binary_check_str_1}= {binary_checked}/10")
print()

print("Convert to hex:")
chunks = list(into_reversed_chunks(binary_nums, 4))
hexa_parts = []
hexa_parts_str = []
for chunk in chunks:
    res = 0
    for i in chunk:
        res = (res << 1) | i
    if res > 9:
        dec_to_hex = ["A", "B", "C", "D", "E", "F"]
        res_str = dec_to_hex[res - 10]
        letter = f"= {res_str}"
    else:
        res_str = str(res)
        letter = ""
    hexa_parts.append(res)
    hexa_parts_str.append(res_str)
    print(f"{chunk} = {res} {letter}")
print()

hexa_parts_str.reverse()
hexa_str = "".join(str(v) for v in hexa_parts_str)

count = 0
hexa_check = []
hexa_check_str_0 = ""
hexa_check_str_1 = ""
hexa_check_str_2 = ""
start = True
for i in hexa_parts:
    hexa_check.append(i * pow(16, count))
    if not start:
        symbol = "+"
    else:
        symbol = ""
        start = False
    hexa_check_str_0 += f"{symbol} {i}*(16^{count}) "
    hexa_check_str_1 += f"{symbol} {i}*{pow(16, count)} "
    hexa_check_str_2 += f"{symbol} {i * pow(16, count)} "
    count += 1
hexa_checked = sum(hexa_check)

print("Check if converting to hex was correct:")
print(f"{input}/10 = {hexa_str}/16 ={hexa_check_str_0}={hexa_check_str_1}={hexa_check_str_2}= {hexa_checked}/10")
print()


print("Answer:")
print(f"{input}/10 = {binary_str}/2 = {hexa_str}/16")
