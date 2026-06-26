{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "33fca308-30e8-4617-a62b-b89e198f678e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shiva 22 pune\n"
     ]
    }
   ],
   "source": [
    "#starting from very basic what is variable\n",
    "## variable work like the container in which we can store something\n",
    "#here variable is created as \"name\" and \"shiva\" is the element in it\n",
    "name=\"shiva\"\n",
    "age=22\n",
    "city=\"pune\"\n",
    "print(name,age,city)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "42d37d99-a02b-4376-896b-1b74b4101477",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shiva 22 5.6 True\n",
      "<class 'str'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "#datatypes = python automatically detedt the data type\n",
    "## integer = 485,0,-1\n",
    "##float= 53.8,-0.1\n",
    "##string= shiva,ayush,arnav\n",
    "##boolen= True,False in this two form only\n",
    "#always remember boolen data type is starting with capital letter\n",
    "name=\"shiva\"\n",
    "age=22\n",
    "height=5.6\n",
    "student=True\n",
    "\n",
    "print(name,age,height,student)\n",
    "\n",
    "print(type(name))\n",
    "print(type(age))\n",
    "print(type(height))\n",
    "print(type(student))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "99f0cac6-d981-47cc-a4c9-4c7f92bda3ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "#updating the variable\n",
    "age=11\n",
    "age=12\n",
    "print(age)\n",
    "##here age is updated from 11 to 12\n",
    "## it can be also update using dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "72230692-cf2e-47ab-8a71-7b137333f3f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ages': 14}\n"
     ]
    }
   ],
   "source": [
    "student={\n",
    "    \"ages\":13\n",
    "}\n",
    "student.update({\"ages\":14})\n",
    "print(student)\n",
    "#here age is updated"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ef228009-984c-487b-827f-f4ccc05aa54e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shiva 33 rightangeltraingle\n"
     ]
    }
   ],
   "source": [
    "# create variable print them using print\n",
    "name = \"shiva\"\n",
    "age = 33\n",
    "angle = \"rightangeltraingle\"\n",
    "print(name,age,angle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6b4a624d-a295-47bb-95be-14048cfffdb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "499.99\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "#ceeate the following variable and print them\n",
    "price = 499.99\n",
    "quantity = 3\n",
    "print(price)\n",
    "print(quantity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fa88d4e3-19fc-4a2f-a856-a3862b050b57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "name = \"shiva\"\n",
    "age = 22\n",
    "cgpa = 7.09\n",
    "placed = False\n",
    "print(type(name))\n",
    "print(type(age))\n",
    "print(type(cgpa))\n",
    "print(type(placed))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ef047f02-2ae2-4d08-8491-c5131133053c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 20 30\n"
     ]
    }
   ],
   "source": [
    "a,b,c = 10,20,30\n",
    "print(a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cd2250fb-959a-4a65-8eb3-5339b2a15257",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = x\n",
    "\n",
    "x = 20\n",
    "\n",
    "print(x)\n",
    "print(y) #predict output without running\n",
    "#x=20\n",
    "#y=10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e4ce72e8-12a0-45d9-9e93-bb1170a11096",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name shiva <class 'str'>\n",
      "age 22 <class 'int'>\n",
      "college gh raisonu <class 'str'>\n",
      "branch cse ai <class 'str'>\n",
      "cgpa 8.0 <class 'float'>\n",
      "is_looking_job True <class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "name=\"shiva\"\n",
    "age=22\n",
    "college=\"gh raisonu\"\n",
    "branch=\"cse ai\"\n",
    "cgpa=8.0\n",
    "is_looking_job = True\n",
    "print(\"name\",name,type(name))\n",
    "print(\"age\",age,type(age))\n",
    "print(\"college\",college,type(college))\n",
    "print(\"branch\",branch,type(branch))\n",
    "print(\"cgpa\",cgpa,type(cgpa))\n",
    "print(\"is_looking_job\",is_looking_job,type(is_looking_job))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "cd128666-1e46-4928-a249-17339ad7b29d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35000\n"
     ]
    }
   ],
   "source": [
    "##salary = 30000\n",
    "##Update the salary to 35000.\n",
    "##Then increase it by 5000.\n",
    "\n",
    "Print the final salary.\n",
    "salary = 30000\n",
    "salary = salary + 5000\n",
    "print( salary )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d4d03470-82ab-4ebc-9bfc-541e2eae7747",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a 20\n",
      "b 10\n"
     ]
    }
   ],
   "source": [
    "#swap the value without using 3rd varialble\n",
    "a=10\n",
    "b=20\n",
    "a,b=b,a\n",
    "print(\"a\",a)\n",
    "print(\"b\",b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "42326ec0-d513-44ff-be88-fe8031ccef18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "x = 5\n",
    "y = x\n",
    "\n",
    "x = x + 5#value are been update\n",
    "y = y + 10\n",
    "\n",
    "print(x)\n",
    "print(y)\n",
    "#here output will be x=10 and y=20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "dacabd80-ad5f-493c-b46f-c7310b67c7d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "## = is used as assign operator is used to assign\n",
    "## == comparison operator is used to compared"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "26607cf0-862b-4b68-b6dd-4e275dff158d",
   "metadata": {},
   "outputs": [],
   "source": [
    "## 2. Why is Python called a dynamically typed language?\n",
    "\n",
    "# In Python, you don't need to specify the data type when creating a variable.\n",
    "#age = 22\n",
    "#int age = 22 \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98cd12f4-0662-45af-a287-9d437ee5c1c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "age = 22\n",
    "age = \"Twenty Two\"\n",
    "\n",
    "print(type(age))\n",
    "# here age is updated from 22 to twenty two\n",
    "#and data type is converted fromm int to string\n"
   ]
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
