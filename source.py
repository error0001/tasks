# tasks https://pythonworld.ru/osnovy/tasks.html
import os
import unittest

def Arithmetic(inA, inOper, inB):
    if isinstance(inA,str):
        inA = float(inA)
    if isinstance(inB,str):
        inB = float(inB)
    print("Work ar.")
    if inA != None and inOper != None and inB != None:
        if inOper == '+':
            return inA + inB
        if inOper == '-':
            return inA - inB
        if inOper == '*':
            return inA * inB
        if inOper == '/' and inA != 0 and inB != 0:
            return float(inA / inB)
        else:
            return "Error with '/'"

if __name__ == '__main__':
    print("Start app.")
    answer = Arithmetic(
        input("Write A: "),
        input("Write oper: "),
        input("Write B: "))
    print(answer)