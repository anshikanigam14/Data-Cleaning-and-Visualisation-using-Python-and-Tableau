### Data Cleaning and Visualisation using Python and Tableau

[Data source (United Nations)](https://population.un.org/wpp/Download/Standard/Population/)

##### Datasets used:
1. ###### Life expectancy at birth (both sexes combined) by region, subregion and country, 1950-2100

   Life expectancy at birth reflects the overall mortality level of a population. It summarizes the mortality pattern that prevails across all age groups - children and adolescents, adults and the elderly. Definition. Average number of years that a newborn is expected to live if current mortality rates continue to apply.

2. ###### Total population (both sexes combined) by region, subregion and country, annually for 1950-2100
    
    The total population of humans currently living.
3. ###### Total fertility by region, subregion and country, 1950-2100 (live births per woman)	
    
    Total period fertility measures the number of children a woman would have in the course of her life if the fertility rates observed at each age in the year in question remained unchanged.
4. ###### Infant mortality rate (both sexes combined) by region, subregion and country, 1950-2100 
    
    Infant Mortality Rate is the number of resident newborns in a specified geographic area (country, state, county, etc.) dying under one year of age divided by the number of resident live births for the same geographic area (for a specified time period, usually a calendar year) and multiplied by 1,000.


###### Data Cleaning and aggregation using Python:

Using Pandas cleaned the respective raw data files and merged into a single data file containing pivoted life expectancy, IMR, total fertility, total population values across years 1950-2015, region, years and country code.
The merged file thus obtained can be used for statistical analysis and data visualisation.


###### Data Visualisation using Tableau:

1. Created an animated viz using Avg Total fertility, Avg Life expectancy and Total population for all countries.


![Viz_1](https://raw.githubusercontent.com/anshikanigam14/Data-Cleaning-and-Visualisation-using-Python-and-Tableau/master/1.PNG)


2. Created a world map showing variation of Avg Infant Mortality Rates for all countries.


![Viz_2](https://raw.githubusercontent.com/anshikanigam14/Data-Cleaning-and-Visualisation-using-Python-and-Tableau/master/2.PNG)