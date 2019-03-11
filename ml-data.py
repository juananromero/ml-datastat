#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ninstances_py.ninstances import ninstances
from ninstances_py.ninstances import cardinality
def main():
    loop_condition=True

    while loop_condition == True:
        print("\nMenu:\n")
        print("0.- EXIT")
        print("1.- Number of instances, features and labels (Juan A. Romero)")
        print("2. Cardinality (Manuel Mendoza Hurtado)")

        main_input = int(input())

        if main_input == 0:
            loop_condition = False
            break
        elif main_input == 1:
            datafile=input("Introduce nombre de datafile: ")
            ninstances(datafile)
            break
        elif main_input == 2:
            print("Funcionalidad añadida por Manuel Mendoza Hurtado ")
            datafile=input("Introduce nombre de datafile: ")
            cardinality(datafile)
            break

if __name__ == "__main__":
    main()
