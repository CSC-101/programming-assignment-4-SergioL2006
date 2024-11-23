import sys
import build_data
import hw3

from data import CountyDemographics

full_data = build_data.get_data()
#brekas command line to be readable
def break_command(operation) -> list:
    #check to see if first part is an actual command
    ini_check = ['display', 'filter-state', 'filter-gt', 'filter-lt', 'population_total', 'population', 'percent']
    parts = operation.strip().split(':') #Breaks the semicolons
    for x in ini_check:#Checks if it is correct, if so returns the value if not gives an error
        if parts[0] == x:
            return parts
    return SyntaxError #Checks for erros

#used to run the command
def execution(cmd, county_data):
    entries = 0 #If it is for instance the states amount
    if cmd[0] == "display": #Displays all
        print("County Data:") #Adds print county data then shows all the data within county
        filter = county_data
        for x in filter:
            print(x)
    elif cmd[0] == "filter-state": #looks for the state filter
        filter = hw3.filter_by_state(county_data, cmd[1])
        for x in filter: #For each in filter adds new entry as that is what is wanted
            entries += 1
        print("Filter: State == ", cmd[1], "Entries: ", entries) #Prints the entries of specified state

    elif cmd[0] == "filter-gt": #Filters percentage if greater or lower
        splitSearch = cmd[1].split('.') #This section needs another break as there is further specification
        if splitSearch[0] == "Education": #Each of these account for the specified data ands uses functions from hw3 to complete it then returns new set of county data
            filter = hw3.education_greater_than(county_data, str(splitSearch[1]), int(cmd[2]))
        elif splitSearch[0] == "Ethnicities":
            filter = hw3.ethnicity_greater_than(county_data, str(splitSearch[1]), int(cmd[2]))
        elif splitSearch[0] == "Income":
            filter = hw3.below_poverty_level_greater_than(county_data, int(cmd[2]))
        else:
            return SyntaxError #if there is an error with the specification returns syntax error
        print("2014 ", cmd[1])
        for x in filter: #Shows all the data
            print(x)

    elif cmd[0] == "filter-lt": #filters for percentages less than what was wanted
        splitSearch = cmd[1].split('.') #since more specific with area needs one more breakdown with operation syntax
        if splitSearch[0] == "Education": #each of these are the specifications
            filter = hw3.education_less_than(county_data, str(splitSearch[1]), int(cmd[2]))
        elif splitSearch[0] == "Ethnicities":
            filter = hw3.ethnicity_less_than(county_data, str(splitSearch[1]), int(cmd[2]))
        elif splitSearch[0] == "Income":
            filter = hw3.below_poverty_level_less_than(county_data, int(cmd[2]))
        else:
            return SyntaxError #If there is an error prints a syntax error

        print("2014 ", cmd[1])
        for x in filter: #Prints all the new data that was chosen
            print(x)

    elif cmd[0] == "population-total": #grabs total population and prints it
        filter = hw3.population_total(county_data)
        print("2014 Population: ", filter)

    elif cmd[0] == "population": #takes percentage of the total population
        splitSearch = cmd[1].split('.') #since there is smaller specification needs the break from operations syntax
        if splitSearch[0] == "Education":
            filter = hw3.population_by_education(county_data, str(splitSearch[1]))
        elif splitSearch[0] == "Ethnicities":
            filter = hw3.population_by_ethnicity(county_data, str(splitSearch[1]))
        elif splitSearch[0] == "Income":
            filter = hw3.population_below_poverty_level(county_data)
        else:
            return SyntaxError #prints syntax error if there was an issue with specification
        print("2014 ", cmd[1], "Total ", filter)

    elif cmd[0] == "percent": #Percent is used to find percent of said specific data
        splitSearch = cmd[1].split('.') #as well has more specifics with how operation syntax is needed so another breaking
        if splitSearch[0] == "Education": #goes through each specification category
            filter = hw3.percent_by_education(county_data, str(splitSearch[1]))
        elif splitSearch[0] == "Ethnicities":
            filter = hw3.percent_by_ethnicity(county_data, str(splitSearch[1]))
        elif splitSearch[0] == "Income":
            filter = hw3.percent_below_poverty_level(county_data)
        else:
            return SyntaxError #prints error if it wrong
        print("2014 ", cmd[1], "Total ", filter, "%") #prints out the code
    return filter #Returns the filtered data depending on what is given

def main():
    file = open(sys.argv[1])#Grabs system
    content = file.readlines() #Reads through each line of code
    x = 1 #Beginning of future iteration

    try:
        specific_group = execution(break_command(content[0]), full_data) #Grabs initial commandline of code which should be specification
        while x <= len(content)-1:
            new = execution(break_command(content[x]), specific_group) #Obtains new data with the new sample group
            specific_group = [new] #only used/works if looking to specify further, if not it will end there or give error code with how specifications were made
            x += 1 #Iterates through lines of code

        if (len(content) - 1) > 0:
            return new #If theres multiple will return new as that is the value holding the newer ones
        else:
            return specific_group #Returns the value if only one line of code

    except:
        print("Error Code, Line: ", x) #Used if there is an error, specifically how operation is written in the code

main()