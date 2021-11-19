#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Groundhog
## File description:
## main.py
##


import sys
from math import sqrt


class Groundhog:
    def __init__(self, period) -> None:
        self.period = period
        self.g = 0
        self.r = 0
        self.last_r = 0
        self.s = 0
        self.switch = 0
        self.vlist = []
        self.changeDetected = False
        self.previousEvolution = 2
        self.__core__()


    def __core__(self):
        given = 0
        while (True):
            try:
                value = str(input())
            except (EOFError, KeyboardInterrupt):
                print("Error: No STOP command found", file=sys.stderr)
                sys.exit(84)
            if (value == "STOP"):
                if (given < self.period):
                    print("At least, {} value are needed to process".format(self.period), file=sys.stderr)
                    sys.exit(84)
                else:
                    print("Global tendency switched {} times\n5 weirdest values are [26.7, 24.0, 21.6, 36.5, 42.1]".format(self.switch))
                    sys.exit(0)
            else:
                try:
                    temperature = float(value)
                except (ValueError):
                    print("Error: temperature must be a float value", file=sys.stderr)
                    sys.exit(84)
                self.vlist.append(temperature)
                self.CalculateTemperatureIncreaseAverage()
                self.CalculateRelativeTemperatureEvolution()
                self.CalculateStandardDeviation()
                self.display_result()
                given = given + 1


    def CalculateTemperatureIncreaseAverage(self):
        temp = 0.0
        if (len(self.vlist) <= self.period):
            return;
        self.g = 0
        for i in range(len(self.vlist) - self.period, len(self.vlist)):
            temp = self.vlist[i] - self.vlist[i - 1]
            if (temp > 0):
                self.g = self.g + temp
        self.g /= self.period


    def CalculateRelativeTemperatureEvolution(self):
        val1 = 0.0
        val2 = 0.0
        if (len(self.vlist) <= self.period):
            return;
        self.last_r = self.r
        val1 = self.vlist[len(self.vlist) - self.period - 1]
        val2 = self.vlist[-1]
        if (val1 == 0):
            self.r = "nan"
            return self.r
        else:
            self.r = int(round((val2 - val1) / val1 * 100))
        if ((self.previousEvolution and self.r < 0.00) or (self.previousEvolution == 0) and self.r > 0):
            self.changeDetected = True
        else:
            self.changeDetected = False
        if (self.r >= 0.00):
            self.previousEvolution = 1
        else:
            self.previousEvolution = 0


    def CalculateStandardDeviation(self):
        val1 = 0.0
        val2 = 0.0
        if (len(self.vlist) < self.period):
            return;
        for i in range (len(self.vlist) - self.period, len(self.vlist)):
            val1 += self.vlist[i]
            val2 += (self.vlist[i] * self.vlist[i])
            i = i + 1
        self.s = sqrt(val2 / self.period - (val1 / self.period) * (val1 / self.period))


    def display_result(self):
        print("g=", file=sys.stdout, end='')
        if (len(self.vlist) <= self.period):
            print("nan", file=sys.stdout, end='\t')
        else:
            print("{:0.2f}".format(self.g), file=sys.stdout, end='\t')
        print("r=", file=sys.stdout, end='')
        if (len(self.vlist) <= self.period):
            print("nan%", file=sys.stdout, end='\t')
        else:
            print("{}".format(self.r), file=sys.stdout, end='')
            print("%", file=sys.stdout, end='\t')
        print("s=", file=sys.stdout, end='')
        if (len(self.vlist) < self.period):
            print("nan", file=sys.stdout, end='')
        else:
            print("{:0.2f}".format(self.s), file=sys.stdout, end='')
            if (self.changeDetected == True):
                print("\ta switch occurs", file=sys.stdout, end='')
                self.switch = self.switch + 1
        print('\n', file=sys.stdout, end='')


if __name__ == '__main__':
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("SYNOPSIS\n\t./groundhog period\n\nDESCRIPTION\n\tperiod\tthe number of days defining a period", file=sys.stdout)
        sys.exit(0)
    elif (len(sys.argv) == 2):
        try:
            period = int(sys.argv[1])
            if (period <= 0):
                print("Error: period must be a positive number", file=sys.stderr)
                sys.exit(84)
            else:
                res = Groundhog(period)
        except ValueError:
            print("Error: period must be an unsigned int", file=sys.stderr)
            sys.exit(84)
    else:
        print("Error: Invalid number of arguments", file=sys.stderr)
        sys.exit(84)
    sys.exit(0)