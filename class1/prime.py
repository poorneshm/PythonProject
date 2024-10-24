from os import cpu_count
from sys import exc_info
import sys
import printstream

def calculator(first_num,second_num):
    total = first_num + second_num
    print("Total : {}". format(total))


calculator(1,2)












cpu_count = cpu_count()
exc_info  = exc_info()
e_print = print()

if True:
    print("Hello World!")
    print(type(cpu_count))
    print(type(exc_info))
    print(type(cpu_count))
    print(dir(sys))
    print("My CPU Count: ", cpu_count,  "and My system Exc Info: ", exc_info)
    print("My CPU Count : {} and My system Exc Info : {}".format(cpu_count,exc_info,cpu_count))
    #print("My CPU Count : {} and My system Exc Info : {}". format(cpu_count))
    print(dir(printstream))
    print(f"My CPU Count : {cpu_count} and My system Exc Info : {exc_info}")

else:
    print("Good Morning!")
