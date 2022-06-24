from random import*
from time import*
from os import*
def c():
    print("------------------------------------------------")
print("pY-DOS Boot Loader Version 2.21:")
c()
print("1.Start DOS Normally")
c()
print('2.DOS Boot Manager')
c()
boot1 = int(input("Lc:>"))
def dos():
    while 1:
        c()
        data1 = """
          |-------------------------|
          |          pY-DOS         |
          |        Version 4.0.2    |
          |           22H1          |
          |-------------------------|
          """
        print(data1)
        cmd01 = input("APPs(app) Turn off(off)")
        c()
        if cmd01 == "app" or "APP" or "App":
            cmd2 = input("Calculator(cal) Guessing Numbers(guess) Back(back)")
            if cmd2 =="cal" or "Cal":
                Caldata = """
          |-------------------------|
          |         Calculator      |
          |         for    the      |
          |           pY-DOS        |
          |       Version22H1       |
          |-------------------------|
                """
                c()
                print(Caldata)
                c()
                print("1=+ 2=- 3=* 4=/")
                u = int(input())
    
                c()
                num1 = int(input("The first number:"))
                num2 = int(input("The second number:"))
                ans = 0
                if u == 1:
                    ans = ans + num1 + num2
                elif u == 2:
                    ans = ans + num1 - num2
                elif u == 3:
                    ans = ans + num1 * num2
                else:
                    ans = ans + num1 / num2
                print(ans)
            elif cmd2 == "guess":
                c()
                print("The number is between 1 and 100.")
                number = int(input())
                NUM = randint(1,100)
                if number < NUM:
                    
                    print("It is small.")
                elif number > NUM:
                    print("It is big.")
                else:
                    print("You are right!")
            elif cmd2 == "back":
                pass
        elif cmd01 == "off":
            break
if boot1 == 2:
    c()
    print("DOS Boot Manager:(Version 2.21)")
    print("1.Start DOS Normally")
    print("2.Safe Mode")
    boot3 = int(input(""))
    if boot3 == 1:
        dos()
    elif boot3 == 2:
        c()
        print("DOS Loading files...")
        print("1.DOS.py")
        print("2.GuessingNum.py")
        print("3.Set.py")
        print("4.Cal.py")
        sleep(0.75)
        dos()
elif boot1 == 1:
    dos()
