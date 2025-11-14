count = int(input())
stu_info = dict()
for times in range(count):
    stu_input = input().split(',')
    stu_info[stu_input[0].strip()] = int(max(stu_input[1:]))

sorted_stu_info = sorted(stu_info.items(), key=lambda item:item[1], reverse=True)

for key, value in sorted_stu_info:
    print(f'{key}, {value}')