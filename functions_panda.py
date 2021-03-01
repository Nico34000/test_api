import pandas


def csv_file():
    """
    This function contains data from csv file. \n
    She return : 'id', 'Country', 'year',
    'emission', 'values', 'footnote', 'source'.
    """
    csv = pandas.read_csv('co2.csv', header=2, names=['id', 'Country', 'year',
                          'emission', 'values', 'footnote', 'source'])
    return csv


def country_list():
    """
    This function contains a list of countries we've in CSV.\n
    It serves us to have only a list of the countries present in csv.\n
    She return : 'China, Hong Kong SAR', 'Guatemala'...
    """
    df = csv_file()
    country_list = set(df['Country'].tolist())
    return country_list


def latest_by_country(country):
    """
    This function is used to send back country, year, and emission 
    for a country.\n
    We use .sort_value to return year in ascending order.\n
    She return with "France" (for exemple):
    'country': 'France', 'year': 2017, 'emissions': 306123.541
    """
    df = csv_file()
    df = df.loc[df['Country'].isin([country])].sort_values(['year'],
                                                           ascending=False)
    result = {}
    result["country"] = str(df.iloc[0][1])
    result["year"] = int(df.iloc[0][2])
    result["emissions"] = float(df.iloc[0][4])
    return result


def year_list():
    """
    This function contains a list of years we've in column year
    in csv.\n
    She return :["2016", "1985", "2017", "1995", "2005", 
    "1975", "2010", "2015"]
    """
    year_li = ["2016", "1985", "2017", "1995", "2005", "1975", "2010", "2015"]
    return year_li


def average_year(year):
    """
    This function does the average of values of emission (thousand metric...)
    for a given year.\n
    She return with "2017" (for exemple):
    'year': '2017', 'total': 219666.44571830984
    """
    df = csv_file()
    df = df.loc[df['year'].isin([year])]
    df = df[(df["emission"] == 'Emissions \
(thousand metric tons of carbon dioxide)')]
    mean_year = df.mean()['values']
    result = {}
    result["year"] = year
    result["total"] = float(mean_year)
    return result


def per_capi(country):
    """
    This function return values for emission (Per capital) 
    of all years for a given country.\n
    She return with "France" (for exemple):
    1975: 7.845, 1985: 6.209, 1995: 5.773, 2005: 5.887, 2010: 5.233, 
    2015: 4.5, 2016: 4.515, 2017: 4.565
    """
    df = csv_file()
    df = df.loc[df['Country'].isin([country])]
    df = df[(df["emission"] == 'Emissions \
per capita (metric tons of carbon dioxide)')]
    result = {}
    longeur = len(df)
    for i in range(longeur):
        result[int(df.iloc[i][2])] = float(df.iloc[i][4])
    return result
