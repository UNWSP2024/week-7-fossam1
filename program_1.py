#Samuel Foss
#Program 1 Rainfall
#10/15
from multiprocessing.forkserver import set_forkserver_preload
from pickletools import markobject
from pydoc import apropos
from tokenize import maybe

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.



def main():

    rain = []

    for month in range(1, 13):
                rainamount = float(input(f"Enter in inches the amount of rainfall for month {month}: "))
                rain.append(rainamount)

    totalrain = sum(rain)
    averagerain = sum(rain) / len(rain)
    highrain = rain.index(max(rain)) + 1
    lowrain = rain.index(min(rain)) + 1

    print(f"\nThe total rainfall for the year was {totalrain:.2f} inches")
    print(f"The average monthly rainfall was {averagerain:.2f} inches")
    print(f"The month with the highest rainfall was Month {highrain} with {max(rain):.2f} inches")
    print(f"The month with the lowest rainfall was Month {lowrain} with {min(rain):.2f} inches")

if __name__ == '__main__':
    main()

#Output
#Enter in inches the amount of rainfall for month 1: 1
#Enter in inches the amount of rainfall for month 2: 4
#Enter in inches the amount of rainfall for month 3: 6
#Enter in inches the amount of rainfall for month 4: 1
#Enter in inches the amount of rainfall for month 5: 7
#Enter in inches the amount of rainfall for month 6: 4
#Enter in inches the amount of rainfall for month 7: 5
#Enter in inches the amount of rainfall for month 8: 6
#Enter in inches the amount of rainfall for month 9: 5
#Enter in inches the amount of rainfall for month 10: 4
#Enter in inches the amount of rainfall for month 11: 5
#Enter in inches the amount of rainfall for month 12: 9

#The total rainfall for the year was 57.00 inches
#The average monthly rainfall was 4.75 inches
#The month with the highest rainfall was Month 12 with 9.00 inches
#The month with the lowest rainfall was Month 1 with 1.00 inches

#Process finished with exit code 0
