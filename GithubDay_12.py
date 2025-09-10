{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37ffdf5f-e2fc-44cb-b875-4826f64d3f38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nohtyP\n"
     ]
    }
   ],
   "source": [
    "s = \"Python\"\n",
    "print(s[::-1])   # nohtyP\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3a2aece8-e83a-45ed-bcf9-a4bdc114476c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palindrome\n"
     ]
    }
   ],
   "source": [
    "s = \"madam\"\n",
    "print(\"Palindrome\" if s == s[::-1] else \"Not Palindrome\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4c753a02-783d-46ef-a69f-ea7c92c56f4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 5 is 120\n"
     ]
    }
   ],
   "source": [
    "n = 5\n",
    "fact = 1\n",
    "for i in range(1, n+1):\n",
    "    fact *= i\n",
    "print(f\"Factorial of {n} is\", fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9218431a-8751-49d0-a16f-0f52c643f1c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 "
     ]
    }
   ],
   "source": [
    "n = 7\n",
    "a, b = 0, 1\n",
    "for _ in range(n):\n",
    "    print(a, end=\" \")\n",
    "    a, b = b, a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "923ebd27-4585-4f2c-b0c3-271876206d36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vowel count: 4\n"
     ]
    }
   ],
   "source": [
    "s = \"Interview\"\n",
    "vowels = \"aeiouAEIOU\"\n",
    "count = sum(1 for ch in s if ch in vowels)\n",
    "print(\"Vowel count:\", count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bce66048-0983-4c03-80ff-53f1418fefdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime\n"
     ]
    }
   ],
   "source": [
    "n = 29\n",
    "prime = all(n % i != 0 for i in range(2, int(n**0.5)+1))\n",
    "print(\"Prime\" if prime and n > 1 else \"Not Prime\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "818be203-41c3-4fcb-9e24-fa1b9ff2a329",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Second Largest: 45\n"
     ]
    }
   ],
   "source": [
    "nums = [12, 45, 1, 78, 34, 78]\n",
    "unique_nums = list(set(nums))\n",
    "unique_nums.sort()\n",
    "print(\"Second Largest:\", unique_nums[-2])"
   ]
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
