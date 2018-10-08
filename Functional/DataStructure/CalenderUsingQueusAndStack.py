from DataStructure import StackUsingLinkList as sl
from ObjectOriented import QuesUsingLinkList as ql
import datetime
def dayOfWeek(dd, mm, yy):
    # sum is the variable which is initialized with0 value
    sum = 0
    # month is a dictionary which is having the month code every month has a code
    month = {"1": "0", "2": "3", "3": "3", "4": "6", "5": "1", "6": "4", "7": "6", "8": "2", "9": "5", "10": "0",
             "11": "3", "12": "5", }
    # century is a dictionary which is having the century code
    century = {"1700": "4", "1800": "2", "1900": "0", "2000": "6", "2100": "4", "2200": "2", "2300": "0"}
    # day is a dictionary which is having day code
    day = {0: "sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    yr = int(yy[-2:])
    y0 = (yr + int(yr / 4)) % 7
    m0 = int(month[mm])
    i = str(int(yy) - yr)
    c0 = int(century[i])
    sum = c0 + m0 + y0 + int(dd)
    if (int(yy) % 4 == 0 and int(yy) % 100 != 0 or int(yy) % 400 == 0 and int(mm) < 3):
        sum = sum - 1
    day1 = {"sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3,  "Thursday": 4, "Friday" :5 ,"Saturday":6}
    return (day1[day[sum % 7]])

def totalNoOfDays(mm,yy):
    if (int(yy) % 4 == 0 and int(yy) % 100 != 0 or int(yy) % 400 == 0 and int(mm) == 3):
        return 29
    else:
       totaldays={"1":"31","2":"28","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31","9":"30","10":"31","11":"30","12":"31"}
       return totaldays[str(mm)]

week=ql.Queue()

week.enqueue("sa")
week.enqueue("fr")
week.enqueue("th")
week.enqueue("we")
week.enqueue("tu")
week.enqueue("mo")
week.enqueue("su")
try:
 mm,yy=input("Enter the month and the year in formate mm/yyyy\n\t\t\t eg 3/2014").split("/")
 datetime.datetime(int(yy), int(mm), int(1))

except:
    print("Invalid month or year imput")
    exit()
if len(yy)<4:
      print("Invalid month or year imput")
      exit()
cal=[[],[],[],[],[],[],[]]
temp=1
count=temp
k=1
d=int((dayOfWeek(1,mm,yy)))
for i in range(0,d):
    cal[i].insert(0,"  ")
for i in range(1,8):
     while temp<=int(totalNoOfDays(mm,yy)):
             v=str(temp)
             if len(v)<2:
                 v=v+" "
             k=len(cal[int(dayOfWeek(i,mm,yy))])
             cal[int(dayOfWeek(i,mm,yy))].insert(k+1,str(v)+"")#append(temp)
             temp=temp+7
             k=k+1
     temp=count+i

for i in range(7):
   l=7-len(cal[i])
   for j in range(l):
       k = len(cal[i])
       cal[i].insert(k+1," ")


day=ql.Queue()

for i in reversed(range(len(cal))):
    for j in reversed(range(len(cal[i]))):
        day.enqueue(cal[i][j])

weekday=ql.Queue()
for i in range(7):
    for j in range(len(cal[i])):
        weekday.enqueue(day.dequeue())
    weekday.enqueue(week.dequeue())

stcal=sl.Stack()
for i in range(56):
  stcal.push(weekday.dequeue())

for i in range(56):
   if stcal.peep()=="mo" or stcal.peep()=="tu" or stcal.peep()== "we" or stcal.peep()=="th" or stcal.peep()=="fr" or stcal.peep()== "sa":
       print()
   print(stcal.poop(),end=" ")


