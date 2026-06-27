{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ac24b5ad-ca28-4091-b585-52d1f372bf11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n",
      "21\n",
      "6.25 <class 'float'>\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "#create two variable and perform operation on it\n",
    "a = 25 \n",
    "b = 4\n",
    "print(a + b)\n",
    "print(a - b)\n",
    "print((a / b),type(a/b))\n",
    "print(a * b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9e3d32f4-f7fe-4d13-b2a4-9cb3231bee2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "a = 50\n",
    "b = 20\n",
    "print( a // b) #it is called as floor division it removes value which is after decimal point"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f23d7ac6-1163-466d-ab5b-70e0b7104b2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-3\n"
     ]
    }
   ],
   "source": [
    "# but when the floor devision is performed it will not similar for -50\n",
    "a = -50\n",
    "b = 20\n",
    "print(a // b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "92984d25-51e0-4059-9297-33dfe8c946ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "##The floor of a number is the greatest integer that is less than or equal to that number.\n",
    "\n",
    "\n",
    "##Positive numbers: You can think of // as \"remove the decimal.\"\n",
    "##Negative numbers: Think \"move left on the number line to the next whole number.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4ad74d71-982d-4ff5-a42a-65d2b71cfb36",
   "metadata": {},
   "outputs": [],
   "source": [
    "## % this operator is called as module operator which return the reminder\n",
    "# 99 % 10   # 9\n",
    "#123 % 10  # 3\n",
    "#4567 % 10 # 7\n",
    "#80 % 10   # 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3c6c30f6-3b8c-4b88-8cf1-77ec7c57fb3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# comparison operator are used to compare the two values they either return true or false\n",
    "print(10>4)\n",
    "#here if the condition is true it will return true"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7db86386-432a-4fa3-904f-f168c9ddcb11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(10 == 10)\n",
    "# this operation indicate both the number are equall"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b3c66dee-d5b9-45c1-832b-df5dfa1be63f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# != or <> indicates that they are not equall\n",
    "print(10 == 10)\n",
    "print(10 != 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bab8e1c6-6a76-49de-a775-257438bdc839",
   "metadata": {},
   "outputs": [],
   "source": [
    "# less than greater than less than equall t\n",
    "#> Greater than\n",
    "#< Less than\n",
    "#>= Greater than or equal to\n",
    "#<= Less than or equal to"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "627c5543-a2bf-4f59-8ff5-54b7f837c6d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character '→' (U+2192) (2404517639.py, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[19], line 6\u001b[1;36m\u001b[0m\n\u001b[1;33m    and → Both conditions must be true.\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid character '→' (U+2192)\n"
     ]
    }
   ],
   "source": [
    "#logical operator\n",
    "logical operators are used to combine two or more conditions.\n",
    "\n",
    "Think of them like decision-making words in English:\n",
    "\n",
    "and → Both conditions must be true.\n",
    "or → At least one condition must be true.\n",
    "not → Reverses the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "280471f9-4a55-4a5d-9707-7d21249a7518",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "age = 22\n",
    "salary = 50000\n",
    "\n",
    "print(age > 18 and salary > 40000)\n",
    "print(age < 18 or salary > 40000)\n",
    "print(not (salary < 30000))\n",
    "print(age == 22 and salary == 50000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "77b0f95e-a93e-4704-a906-cb63da4a96f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the person is eligible\n",
      "senior citizen\n",
      "indian citizen\n"
     ]
    }
   ],
   "source": [
    "age = 65\n",
    "citizen = True\n",
    "if age >= 18:\n",
    "    print(\"the person is eligible\")\n",
    "if age >= 60:\n",
    "    print(\"senior citizen\")\n",
    "if citizen := True:\n",
    "    print(\"indian citizen\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9a393a55-bb43-404b-a783-dd631ad03765",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is divisible by 2\n",
      "number is divisible by 3\n",
      "number is divisible by 5\n"
     ]
    }
   ],
   "source": [
    "num = 30\n",
    "if num / 2:\n",
    "    print(\"number is divisible by 2\")\n",
    "if num / 3:\n",
    "    print(\"number is divisible by 3\")\n",
    "if num / 5:\n",
    "    print(\"number is divisible by 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "4fc24525-e8ed-4974-ac62-fb39fd23f62b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is divisible by 2\n",
      "number is divisble by 3\n",
      "number is divisible by 5\n"
     ]
    }
   ],
   "source": [
    "# profesion code\n",
    "num = 30\n",
    "if num % 2 == 0:\n",
    "    print(\"number is divisible by 2\")\n",
    "if num % 3 == 0:\n",
    "    print(\"number is divisble by 3\")\n",
    "if num % 5 == 0:\n",
    "    print(\"number is divisible by 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0de7089b-6f78-4f55-a853-1c1eebab1ba5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number you want to enter 21\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the voter is eligible to vote\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"enter the number you want to enter\"))\n",
    "if age > 18:\n",
    "    print(\"the voter is eligible to vote\")\n",
    "else:\n",
    "    print(\"the voter is not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d0aa37f1-dcc0-43b6-a44d-119429bf996b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is positive\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number\"))\n",
    "if num > 0:\n",
    "    print(\"number is positive\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "987208ee-a82a-42aa-9601-171d6dc48572",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the number is even\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number\"))\n",
    "if num % 2 == 0:\n",
    "    print(\"the number is even\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5264c977-811e-4f0e-af3f-74c752ab3e6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the numbet 21\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the number is divisible by 7\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the numbet\"))\n",
    "if num % 7 == 0:\n",
    "    print(\"the number is divisible by 7\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "79991b7d-5eec-4654-aab7-9154a682139b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the age 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you can vote\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"enter the age\"))\n",
    "if age >= 18:\n",
    "    print(\"you can vote\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "b3d4211c-b003-43a1-a29c-3bd9f405bebe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the salary 600000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "high salary\n"
     ]
    }
   ],
   "source": [
    "salary = int(input(\"enter the salary\"))\n",
    "if salary > 50000:\n",
    "    print(\"high salary\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a83a2584-9a32-4c16-b550-f4484d8df1fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number 50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the number is divisible by 2\n",
      "the number is divisible by 5\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter the number\"))\n",
    "if num % 2 == 0:\n",
    "    print(\"the number is divisible by 2\")\n",
    "if num % 5 == 0:\n",
    "    print(\"the number is divisible by 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "4db9de0e-4e74-4024-8e6c-ae26329a9790",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the age 21\n",
      "enter the salary 90000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eligible for loan\n",
      "eligible for loan\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"enter the age\"))\n",
    "salary = int(input(\"enter the salary\"))\n",
    "if age >= 18 :\n",
    "    print(\"eligible for loan\")\n",
    "if salary >= 30000:\n",
    "    print(\"eligible for loan\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "13f1b42c-39a9-4117-8a55-134c31b286cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the marks of the user 98\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "excellent\n"
     ]
    }
   ],
   "source": [
    "marks = int(input(\"enter the marks of the user\"))\n",
    "if marks >= 90:\n",
    "    print(\"excellent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "2f74087a-50e3-4101-a8dc-78f9b81038e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the experince 6\n",
      "enter the rating 78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "promotion recommended\n"
     ]
    }
   ],
   "source": [
    "experience = int(input(\"enter the experince\"))\n",
    "rating = int(input(\"enter the rating\"))\n",
    "if experience >= 5 and rating >= 4.5:\n",
    "    print(\"promotion recommended\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "452ee12f-d0d3-42da-abd7-88222c0c96dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the age 23\n",
      "enter the salary 70000\n",
      "enter the experience 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eligible for premium credit card\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"enter the age\"))\n",
    "salary = int(input(\"enter the salary\"))\n",
    "experience = int(input(\"enter the experience\"))\n",
    "if age >= 21 and salary >= 50000 and experience >=2 :\n",
    "    print(\"eligible for premium credit card\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b4f85c9-0b8a-47f3-b437-0d010c5e0387",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
