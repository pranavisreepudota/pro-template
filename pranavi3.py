{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "45b0df24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "2000\n",
      "2\n",
      "rent is: 4800.0\n"
     ]
    }
   ],
   "source": [
    "m=int(input())\n",
    "r=int(input())\n",
    "d=int(input())\n",
    "if(m==4 or m==6 or m==11 or m==12):\n",
    "    t=((20/100)*r*d)+(r*d)\n",
    "    print(\"rent is:\",t)\n",
    "else:\n",
    "    print(\"rent is:\",(r*d))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7cdb8efc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60.01\n",
      "160\n",
      "60.01\n",
      "no\n"
     ]
    }
   ],
   "source": [
    "s=float(input())\n",
    "d=float(input())\n",
    "t=float(input())\n",
    "if(s>=t and d<=1):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fa91ab53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60.01\n",
      "1\n",
      "60\n",
      "yes\n"
     ]
    }
   ],
   "source": [
    "s=float(input())\n",
    "d=float(input())\n",
    "t=float(input())\n",
    "if(s>=t and d<=1):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "76f66ccf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "59.99\n",
      "1\n",
      "60\n",
      "no\n"
     ]
    }
   ],
   "source": [
    "s=float(input())\n",
    "d=float(input())\n",
    "t=float(input())\n",
    "if(s>=t and d<=1):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b50138f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "10\n",
      "14\n",
      "3\n",
      "9\n",
      "yes\n"
     ]
    }
   ],
   "source": [
    "a=float(input())\n",
    "b=float(input())\n",
    "c=float(input())\n",
    "d=float(input())\n",
    "e=float(input())\n",
    "cost=a*350.34+b*230.90+c*190.55+d*125.30+e*180.90\n",
    "if(cost<=15000):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7ec8417d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "20\n",
      "24\n",
      "13\n",
      "9\n",
      "no\n"
     ]
    }
   ],
   "source": [
    "a=float(input())\n",
    "b=float(input())\n",
    "c=float(input())\n",
    "d=float(input())\n",
    "e=float(input())\n",
    "cost=a*350.34+b*230.90+c*190.55+d*125.30+e*180.90\n",
    "if(cost<=15000):\n",
    "    print(\"yes\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf3b8fb1",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
