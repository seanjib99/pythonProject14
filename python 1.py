#s.n students take k apples and distribute each student evenly
#The remaining parts remain in the basket.
#How many apples will each single student get?
#How many apples will remain in the basket?The programs read the numbers N and k.


N=int(input("enter the number of students in class")]
K= int(input("enter the number of apple:")}

apples_get(K//N)

remaining_apples=(K%N)
print(f"each student got {apples_get}")
print (f"The remaining apples are {remaining_apples}")

# 4.N Given the integer N - the number of minutes that is passed since midnight.
# How many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers:
# The number of hours(between 0 and 23) and the number of minutes  (between 0 and 59)

N = int(input("Enter the number of minutes passed since midnight: "))
hours = N//60
minutes = N%60
print(f"The hours is {hours}")
print(f"The minutes is {minutes}")
print(f"It's {hours}:{minutes} now.")

