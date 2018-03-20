{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello word\n"
     ]
    }
   ],
   "source": [
    "print(\"hello word\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "你好！ 我想找实习工作，但是我是JAVA专业，学的PHP 然而呢 找什么工作\n"
     ]
    }
   ],
   "source": [
    "print(\"你好！ 我想找实习工作，但是我是JAVA专业，学的PHP 然而呢 找什么工作\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "你好烂\n"
     ]
    }
   ],import turtle
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

   "source": [
    "print(\"你好烂\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "世界那么大！很悲\n"
     ]
    }
   ],
   "source": [
    "print(\"世界那么大！很悲\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love who\n"
     ]
    }
   ],
   "source": [
    "s = \"I love who\"\n",
    "\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "我们真是弱爆了\n"
     ]
    }
   ],
   "source": [
    "print(\"我们真是弱爆了\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love %s\n"
     ]
    }
   ],
   "source": [
    "s = \"I love %s\"\n",
    "\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love vivian\n"
     ]
    }
   ],
   "source": [
    "print(\"I love %s\"%\"vivian\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "全都是扯淡！\n"
     ]
    }
   ],
   "source": [
    "print(\"全都是扯淡！\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "全都是扯淡！\n"
     ]
    }
   ],
   "source": [
    "print(\"全都是扯淡！\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "全都是扯淡！\n"
     ]
    }
   ],
   "source": [
    "print(\"全都是扯淡！\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "全都是扯淡！\n"
     ]
    }
   ],
   "source": [
    "print(\"全都是扯淡！\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "你好吗\n"
     ]
    }
   ],
   "source": [
    "print(\"你好吗\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "我不好\n"
     ]
    }
   ],
   "source": [
    "print(\"我不好\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"123\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "score = input(\"请输入学生成绩：\")\n",
    "\n",
    "score = input(score)\n",
    "\n",
    "if score >= 90:\n",
    "\n",
    " print(\"学习很棒\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
