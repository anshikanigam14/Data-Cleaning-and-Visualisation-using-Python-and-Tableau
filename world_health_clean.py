import pandas as pd
import os

def life_expectancy_and_fertility():
        # Read life expectancy and total fertility csv files
        life_expectancy = pd.read_csv("life_expectancy_raw.csv")
        total_fertility = pd.read_csv("total_fertility_raw.csv")

        # Convert the years columns into row using melt function. Pandas.melt() unpivots a DataFrame from wide format to a long format for a more computer-friendly form
        life_expectancy = life_expectancy.melt(id_vars=['region','country_code','type','parent_code'],
                                               var_name='years',
                                               value_name="Life_expectancy")

        total_fertility = total_fertility.melt(id_vars=['region','country_code','type','parent_code'],
                                               var_name='years',
                                               value_name="total_fertility")
        life_expectancy = life_expectancy[life_expectancy['type'].str.replace(" ", "") == 'Country/Area']
        total_fertility = total_fertility[total_fertility['type'].str.replace(" ", "") == 'Country/Area']
        return life_expectancy, total_fertility

def imr():
    # Read infant mortality rates files for both sexes
    imr = pd.read_csv("imr_raw.csv")
    # Convert the years columns into row using melt function. Pandas.melt() unpivots a DataFrame from wide format to a long format for a more computer-friendly form
    imr = imr.melt(id_vars=['region', 'country_code', 'type', 'parent_code'],
                                           var_name='years',
                                           value_name="imr")
    imr = imr[imr['type'].str.replace(" ", "") == 'Country/Area']
    return imr

def total_population():
        # Read the total population csv file
        total_population = pd.read_csv("total_population_raw.csv")

        col_names = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961',
                     '1962', '1963', '1964', '1965', '1966', '1967',
                     '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
                     '1980', '1981', '1982', '1983', '1984', '1985',
                     '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                     '1998', '1999', '2000', '2001', '2002', '2003',
                     '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
                     '2016', '2017', '2018', '2019', '2020']

        # Replace any null values in the columns to be aggregated with 0
        for i in col_names:
                total_population[i] = total_population[i].fillna(0)

        # Strip leading and trailing spaces and convert the resulting col into int
        for i in col_names:
                total_population[i] = total_population[i].str.replace(" ", "").astype(int)

        # Using step size of 6 eg. 1950-1955, 1955-1960... bundle and add the columns(which contain year wise population)
        # This is done to maintain the uniformity in years in all three datasets( fertility, population and life expectancy)
        years = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966,1967,
                 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984,1985,
                 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,2003,
                 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
        for i in years[::6]:
                if (i > 2015):
                        break
                total_population[str(i) + '-' + str(i + 5)] = total_population.loc[:, str(i):str(i + 5)].sum(axis=1)
        # Drop the individual columns present originally
        total_population.drop(columns=col_names, inplace=True)

        # Convert the years columns into row using melt function. Pandas.melt() unpivots a DataFrame from wide format to a long format for a more computer-friendly form
        total_population = total_population.melt(id_vars=['region','country_code','type','parent_code'],
                                               var_name='years',
                                               value_name="total_population")
        total_population = total_population[total_population['type'].str.replace(" ", "") == 'Country/Area']
        return  total_population

def merged_data(p_in,l_in,f_in, imr_in):
    dfs = [p_in,l_in,f_in, imr_in]
    df_inner = pd.merge((pd.merge((pd.merge(p_in, l_in, how='inner', on='country_code', suffixes=('', '_y'))), f_in, how='inner', on='country_code', suffixes=('', '_y'))), imr_in, how = 'inner', on= 'country_code', suffixes=('', '_y'))
    print(df_inner.columns)
    suffixes = ('', '_y')
    to_drop = [x for x in df_inner if x.endswith('_y') or x.startswith('type')]
    df_inner.drop(to_drop, axis=1, inplace = True)
    return df_inner

def dump_data_to_csv(population_in,life_in,fertility_in, merged_in, mortality_in):
    # Delete the csv files if already present and regenerates them
    files = ['population_clean.csv','life_expectancy_clean.csv','total_fertility_clean.csv', 'imr_clean.csv', 'merged_data_clean.csv']
    for f in files:
        if os.path.isfile(f):
            os.remove(f)

    population_in.to_csv('population_clean.csv', index = False)
    life_in.to_csv('life_expectancy_clean.csv', index = False)
    fertility_in.to_csv('total_fertility_clean.csv', index = False)
    mortality_in.to_csv('imr_clean.csv', index=False)
    merged_in.to_csv('merged_data_clean.csv', index = False)

if __name__ == "__main__":
    print("Cleaning Life Expectancy and Fertility")
    l, f = life_expectancy_and_fertility()
    print("Cleaning Population data")
    p = total_population()
    print("Cleaning Infant Mortality Rate")
    i = imr()
    print("Joining all three data set into one")
    m = merged_data(p,l,f,i)
    print("Dumping life_expectancy_clean, total_fertility_clean,population_clean, imr_clean data into CSV files")
    dump_data_to_csv(p,l,f,m,i)
