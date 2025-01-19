#to lower conversion
def lower_value(fname,lname,const):
    fname1 = fname.lower()
    lname1 = lname.lower()
    return f"{fname1} {lname1} {const}" #yesari mulitple value return garna milyo

fname = "sARAswoti"
lname = "KHAdka"
const = 8
res = lower_value(fname,lname,const)
print(f"lower formatted: {res}")

#multiple value return using list,tuples

# import statistics

# def mean_mode_median(list1):
#     return statistics.mean(list1),statistics.mode(list1),statistics.median(list1)

# a,b,c = mean_mode_median([2,3,20,5,6,8])
# print(f"mean is {a}, mode is {b}, median is {c} ")


#exercise

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def checking(year,month):
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]

year = int(input("Enter a year: "))
month = int(input("enter a month: "))
print(checking(year,month))


