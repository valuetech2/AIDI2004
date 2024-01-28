{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d210320b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A random number between 1 and 20:  8\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "x = randint(1,20)\n",
    "print('A random number between 1 and 20: ',x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e797bbe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of pi is 3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "from math import pi\n",
    "print ('The value of pi is',pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2c2637f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.435\n",
      "123.54\n",
      "120.0\n"
     ]
    }
   ],
   "source": [
    "print(abs(-1.435))\n",
    "print(round(123.53563,2))\n",
    "print(round(123.53563,-1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f6fcd0f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__doc__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " 'acos',\n",
       " 'acosh',\n",
       " 'asin',\n",
       " 'asinh',\n",
       " 'atan',\n",
       " 'atan2',\n",
       " 'atanh',\n",
       " 'ceil',\n",
       " 'comb',\n",
       " 'copysign',\n",
       " 'cos',\n",
       " 'cosh',\n",
       " 'degrees',\n",
       " 'dist',\n",
       " 'e',\n",
       " 'erf',\n",
       " 'erfc',\n",
       " 'exp',\n",
       " 'expm1',\n",
       " 'fabs',\n",
       " 'factorial',\n",
       " 'floor',\n",
       " 'fmod',\n",
       " 'frexp',\n",
       " 'fsum',\n",
       " 'gamma',\n",
       " 'gcd',\n",
       " 'hypot',\n",
       " 'inf',\n",
       " 'isclose',\n",
       " 'isfinite',\n",
       " 'isinf',\n",
       " 'isnan',\n",
       " 'isqrt',\n",
       " 'lcm',\n",
       " 'ldexp',\n",
       " 'lgamma',\n",
       " 'log',\n",
       " 'log10',\n",
       " 'log1p',\n",
       " 'log2',\n",
       " 'modf',\n",
       " 'nan',\n",
       " 'nextafter',\n",
       " 'perm',\n",
       " 'pi',\n",
       " 'pow',\n",
       " 'prod',\n",
       " 'radians',\n",
       " 'remainder',\n",
       " 'sin',\n",
       " 'sinh',\n",
       " 'sqrt',\n",
       " 'tan',\n",
       " 'tanh',\n",
       " 'tau',\n",
       " 'trunc',\n",
       " 'ulp']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math \n",
    "dir(math)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1258e1fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import *\n",
    "math.sqrt(25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "482a75bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any value: 8\n",
      "Enter any value: 9\n",
      "9.125\n",
      "9.12\n"
     ]
    }
   ],
   "source": [
    "#Write a program that can solve this (|x-y|)/x+y\n",
    "\n",
    "x=float(input('Enter any value: '))\n",
    "y=float(input('Enter any value: '))\n",
    "solution=abs((x-y))/x+y\n",
    "print (solution)\n",
    "print (round(solution,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0a8c75f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "53"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Len operator\n",
    "name = \"THIS IS CEPHAS ICT HUB, HOME OF DATA SCIENCE LEARNING\"\n",
    "len(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c05a6e4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#in operator\n",
    "'valuetech' in name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "355ed26a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#python strings are immutable that means we can modify any part of them"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5ade3215",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Abiodun adeniyi'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#strings method\n",
    "\n",
    "name = 'abiodun adeniyi'\n",
    "name.capitalize()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "70a7ed32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'                               abiodun adeniyi                                '"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.center(78)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "cff87df0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.count('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "baad2fbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Vbiodun Vdeniyi'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name.replace('a', 'V')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "365240fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " name.index ('b')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "53c92ffb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a letter7dt788rdfg\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res = input(\"Enter a letter\")\n",
    "res.isalpha()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02c46a4e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
