#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ninstances_py.ninstances import ninstances
from mld_statistics_py.mld_statistics import MdlSta

def main():
    loop_condition=True

    while loop_condition == True:
        print("\nMenu:\n")
        print("0.- EXIT")
        print("1.- Number of instances, features and labels (Juan A. Romero)")
        print("2.- Multi-label Datasets and Statistics (Fernando León")

        main_input = int(input())

        if main_input == 0:
            loop_condition = False
            break
        elif main_input == 1:
            datafile=input("Introduce nombre de datafile: ")
            ninstances(datafile)
        elif main_input == 2:
            datafile = input("Introduce nombre de datafile: ")
            MdlSta(datafile)



if __name__ == "__main__":
    main()
