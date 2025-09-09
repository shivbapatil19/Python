{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f721376d-45f1-417c-b7d7-86508af84a78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3, 4, 5, 6)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create the tuple of 6 number\n",
    "num=(1,2,3,4,5,6)\n",
    "num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "53206377-6f8e-4e4a-b879-d9cfe025461f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 2, 3)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the starting 3 numbers of the tuple\n",
    "num[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "53c8ec0e-52a2-4e9b-9f03-a43cb97f51b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 6)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the last 2 digit of the tuple\n",
    "num[-2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "87c10c99-7c21-4480-8f16-fe496f7d66dc",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Try to change the 2nd element of the tuple. \u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m#Observe and explain the error.\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m num[\u001b[38;5;241m2\u001b[39m]\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m99\u001b[39m\n\u001b[0;32m      4\u001b[0m num\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "#Try to change the 2nd element of the tuple. \n",
    "#Observe and explain the error.\n",
    "num[2]=99\n",
    "num\n",
    "#here it means that the value cannot be insereted once the tuple is created\n",
    "#list= mutable\n",
    "#tuple=immutable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4dc4f735-63d6-4a44-851b-01c56387a581",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('red', 'blue', 'green', 'yellow', 'black')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#concatenation of the two tuples\n",
    "t1 = (\"red\", \"blue\", \"green\")\n",
    "t2 = (\"yellow\", \"black\")\n",
    "t3=t1+t2\n",
    "t3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "38d6573e-b505-456c-adfc-42c985cce6f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = (22, 43, 43, 12, 55, 43, 77, 75, 157, 55)\n",
    "#count how many times 43 occur\n",
    "count=t.count(43)\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9308f147-26df-4c9c-96b1-3a53749379eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the lenght of the tuple\n",
    "length=len(t)\n",
    "length"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "969cd663-6027-4ba2-8868-f52319324393",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11, 22, 33, 44, 55, 66)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#convert list into tuple\n",
    "list=[11,22,33,44,55,66]\n",
    "\n",
    "tup=tuple(list)\n",
    "tup\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b03a506f-287b-45c5-afea-0974e9fd07ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the 33 is in the list\n"
     ]
    }
   ],
   "source": [
    "#check wheaterr 33 is in list or not\n",
    "if 33 in tup:\n",
    "    print(\"the 33 is in the list\")\n",
    "else:\n",
    "    print(\"the 33 is not in the list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "63bacc1b-0fa6-4e70-971a-4d9848590f19",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[29], line 4\u001b[0m\n\u001b[0;32m      1\u001b[0m t \u001b[38;5;241m=\u001b[39m (\u001b[38;5;241m34\u001b[39m, \u001b[38;5;241m12\u001b[39m, \u001b[38;5;241m89\u001b[39m, \u001b[38;5;241m45\u001b[39m, \u001b[38;5;241m12\u001b[39m, \u001b[38;5;241m67\u001b[39m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;66;03m# Sort in ascending order\u001b[39;00m\n\u001b[1;32m----> 4\u001b[0m asc \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mtuple\u001b[39m(\u001b[38;5;28msorted\u001b[39m(t))   \u001b[38;5;66;03m# here 'tuple' is the built-in function\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAscending:\u001b[39m\u001b[38;5;124m\"\u001b[39m, asc)\n\u001b[0;32m      7\u001b[0m \u001b[38;5;66;03m# Sort in descending order\u001b[39;00m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object is not callable"
     ]
    }
   ],
   "source": [
    "t = (34, 12, 89, 45, 12, 67)\n",
    "\n",
    "# Sort in ascending order\n",
    "asc = tuple(sorted(t))   # here 'tuple' is the built-in function\n",
    "print(\"Ascending:\", asc)\n",
    "\n",
    "# Sort in descending order\n",
    "desc = tuple(sorted(t, reverse=True))\n",
    "print(\"Descending:\", desc)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb2d3b4e-723d-4b81-8a16-4066937f87aa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:ana]",
   "language": "python",
   "name": "conda-env-ana-py"
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
