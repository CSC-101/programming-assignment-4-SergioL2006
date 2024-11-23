from data import CountyDemographics
#Part 1
#Returns total population of all counties in 2014
def population_total(demos:list[CountyDemographics]) -> int:
    popTot = 0
    #iterates through counties 2014 year and adds on then returns value
    for x in demos:
        popTot += x.population['2014 Population']

    return popTot

#Part 2
#Filters counties by state
def filter_by_state(demos:list[CountyDemographics], abr:str) -> list[CountyDemographics]:
    chosenOnes = []
    #Iterates through each county to as a check
    for x in demos:
        #If the state abbreviation is equal to the one inputed then append the state wanted
        if x.state == abr:
            chosenOnes.append(x)

    return chosenOnes

#Part 3
#Finds the population in specifically wanted education in 2014
def population_by_education(demos:list[CountyDemographics], koi:str) -> float:
    interests = 0
    #iterates through each county
    for x in demos:
        #if it matches the key of interest in education then it repeatedly adds
        if koi in x.education:
            interests += (x.education[koi] * 0.01) * x.population['2014 Population']
        else:
        #if they key of interest does not match then adds 0 since there is nothing there
            interests += 0

    return round(interests, 2)

#finds total population by specified ethnicities in 2014
def population_by_ethnicity(demos: list[CountyDemographics], koi:str) -> float:
    interests = 0
    for x in demos:
        # if it matches the key of interest in ethnicities then it repeatedly adds
        if koi in x.ethnicities:
            interests += (x.ethnicities[koi] * 0.01) * x.population['2014 Population']
        else:
            # if they key of interest does not match then adds 0 since there is nothing there
            interests += 0

    return round(interests, 2)

#finds amount of people below poverty level in 2014
def population_below_poverty_level(demos:list[CountyDemographics]) -> float:
    poverty = 0
    #iterates through the counties
    for x in demos:
        #adds people below poverty in each county
        poverty += (x.income['Persons Below Poverty Level'] * 0.01) * x.population['2014 Population']

    return round(poverty, 2)

#Part 4
#obtains percent of people in specified education in 2014
def percent_by_education(demos:list[CountyDemographics], koi:str) -> float:
    #holders for total population and total key of interest
    totpop = 0
    totkoi = 0
    #iterates through counties
    for x in demos:
        #adds total population of each county
        totpop += x.population['2014 Population']
        #adds total education of specified key of interest
        if koi in x.education:
            totkoi += (x.education[koi] * 0.01) * x.population['2014 Population']
        else:
        #if it does not exist then adds 0
            totkoi += 0
    #multiplied by 100 to make into a percentage rounded by 2 decimal places
    return round(totkoi/totpop, 2) * 100

def percent_by_ethnicity(demos:list[CountyDemographics], koi:str) -> float:
    #holders for total population and total key of interest
    totpop = 0
    totkoi = 0
    #iterates through each county
    for x in demos:
        #adds population fo each county
        totpop += x.population['2014 Population']
        #adds each specified ethnicity from each county
        if koi in x.ethnicities:
            totkoi += (x.ethnicities[koi] * 0.01) * x.population['2014 Population']
        else:
        #if key of interest does not exist add 0
            totkoi += 0
    #rounds value then multiples by 100 for its percentage
    return round(totkoi/totpop, 2) * 100

def percent_below_poverty_level(demos:list[CountyDemographics]) -> float:
    #place holders for total population and total below poverty line
    totpop = 0
    totpov = 0
    #iterates through each county
    for x in demos:
        #adds total population adds total people in poverty from each county
        totpop += x.population['2014 Population']
        totpov += (x.income['Persons Below Poverty Level'] * 0.01 ) * x.population['2014 Population']
    #divides poverty by population the multiplies by 100 for the percentage
    return round(totpov/totpop, 2) * 100

#Part 5
#grabs counties with education percentage greater than key of interest
def education_greater_than(demos:list[CountyDemographics], koi:str, percent:float) -> list[CountyDemographics]:
    final = []
    #iteratest through counties
    for x in demos:
        #checks if percentage key of interest of said county greater than percent then appends if so
        if x.education[koi] > percent:
            final.append(x)

    return final
#grabs counties with education percentage less than key of interest
def education_less_than(demos:list[CountyDemographics], koi:str, percent:float) -> list[CountyDemographics]:
    final = []
    #iterates through counties
    for x in demos:
        #checks if percentage key of interest of said county less than percent then appends if so
        if x.education[koi] < percent:
            final.append(x)

    return final

#grabs counties with ethnicities percentage greater than key of interest
def ethnicity_greater_than(demos:list[CountyDemographics], koi:str, percent:float) -> list[CountyDemographics]:
    final = []
    #iterates through counties
    for x in demos:
        #checks if percentage key of interest of said county greater than percent then appends if so
        if x.ethnicities[koi] > percent:
            final.append(x)

    return final

#grabs counties with ethnicities percentage less than key of interest
def ethnicity_less_than(demos:list[CountyDemographics], koi:str, percent:float) -> list[CountyDemographics]:
    final = []
    #iterates through counties
    for x in demos:
        #checks if percentage key of interest of said county less than percent then appends if so
        if x.ethnicities[koi] < percent:
            final.append(x)

    return final

#grabs counties with poverty percentage greater than key of interest
def below_poverty_level_greater_than(demos:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    final = []
    #iterates through counties
    for x in demos:
        #checks if percentage key of interest of said county greater than percent then appends if so
        if x.income['Persons Below Poverty Level'] > percent:
            final.append(x)

    return final

#grabs counties with poverty percentage less than key of interest
def below_poverty_level_less_than(demos:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    final = []
    #iterates through counties
    for x in demos:
        #checks if percentage key of interest of said county less than percent then appends if so
        if x.income['Persons Below Poverty Level'] < percent:
            final.append(x)

    return final
