import turtle
import math
print("你喜欢我吗？  喜欢输入y 不喜欢输入n")
a = input("input:")
if a == "y":
    print("我也喜欢你")
    print("那你愿意做我女朋友吗？  愿意输入y 拒绝输入n")
    b = input("input:")
    if b == "y":
        
                print("那我们要一直走下去\n"*1024)
                wn = turtle.Screen()
                wn.setworldcoordinates(-2, -2, 2, 2)
                alex = turtle.Turtle()
                alex.color("red")
                alex.pensize(2)
                alex.penup()
                alex.speed(0)
                walkStart = -1
                walkEnd = 1
                i = walkStart
                j = walkEnd
                while i <= 0 and j >= 0:
                    y1 = math.sqrt(1 - i * i) + (i * i) ** (1/3.0)
                    y2 = -math.sqrt(1 - i * i) + (i * i) ** (1/3.0)
                    y3 = math.sqrt(1 - j * j) + (j * j) ** (1/3.0)
                    y4 = -math.sqrt(1 - j * j) + (j * j) ** (1/3.0)
                    alex.setx(i)
                    alex.sety(y1)
                    alex.dot()
                    alex.sety(y2)
                    alex.dot()
                    alex.setx(j)
                    alex.sety(y3)
                    alex.dot()
                    alex.sety(y4)
                    alex.dot()
                    i += 0.01
                    j -= 0.01
                print("I love  you\n"*1024)
                import time 
                print ("  " );
                time.sleep(10);
    else:
             print("我想让你做我女朋友"*2048)
             import time 
             print ("  " );
             time.sleep(10);
else:
            print("猜到了 ，你怎么会喜欢我")
            print("但是我喜欢你")
            print("我想让你做我女朋友\n"*2048)
            import time 
            print ("  " );
            time.sleep(10);
