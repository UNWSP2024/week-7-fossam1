#Samuel Foss
#Program 3 US_Population
#10/15
from ftplib import all_errors


# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # Now have the user enter a year.
    while True:
        enteryear = int(input("Enter a year: "))
        enterstate = input("Enter a state: ")
        enterpop = int(input("Enter the population: "))
        all_entered_values.append([enteryear, enterstate, enterpop])

        decision = input("Would you like to enter another state? : ").lower()
        if decision == "no": break
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    yeartofind = int(input("What year would you like to find the total population? : "))
    sum_population_for_year(all_entered_values,yeartofind)

def sum_population_for_year(all_entered_values, year_to_sum):
    totalpopulation = 0

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.
    for i in all_entered_values:
        if i[0] == year_to_sum:
            totalpopulation += i[2]
# print the totalled population
    print(f"The total population in {year_to_sum} is {totalpopulation}")

# Call the main function.
if __name__ == '__main__':
    main()

#Output
#Enter a year: 2020
#Enter a state: minnesota
#Enter the population: 5542756
#Would you like to enter another state? : yes
#Enter a year: 2020
#Enter a state: iowa
#Enter the population: 5201945
#Would you like to enter another state? : yes
#Enter a year: 2021
#Enter a state: texas
#Enter the population: 3059888
#Would you like to enter another state? : no
#What year would you like to find the total population? : 2020
#The total population in 2020 is 10744701

#Process finished with exit code 0
