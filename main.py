# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#156 + 178 + 165 + 171 + 187
#Write your code below this row 👇
count = 0

for list_item in student_heights:
  count += list_item
print(count)

length_of_height = len(student_heights)

dividing = round(count / length_of_height)
print(dividing)