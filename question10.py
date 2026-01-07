#Write a programme to check a year is leap year or not
number = int(input("Enter a year"))
if((number%4==0 and number%100!=0) or (number%400==0)):
    print(f"The year {number} is leap year")
else:
    print(f"The year {number} is not leap year")