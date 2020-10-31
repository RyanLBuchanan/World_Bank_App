import pandas as pd
import plotly.graph_objs as go

def cleandata(dataset, keepcolumns = ['Country Name', '1990', '2015'], value_variables = ['1990', '2015']):
    """Clean World Bank data for a visualization Dashboard

    Keep data range of dates in keep_columns variable and data for the top 10 economies
    Reorient the columns into a year, country and value
    Save the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """
    df = pd.read_csv('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv', skiprows=4)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    top10country = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
    df = df[df['Country Name'].isin(top10country)]

    # Melt year columns and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = value_variables)
    df_melt.columns = ['country', 'year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # Output clean csv file
    return df_melt

def return_figures():
    """Create four plotly Visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

# first chart plots arable land from 1990 to 2015 in top 10 economies
# as a line chart
    graph_one = []
    """ Datasets DO NOT match tutorial!!! """
    df = cleandata('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv')
    df.columns = ['country', 'year', 'hectaresarablelandperperson']
    df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
    countrylist = df.country.unique().tolist()

    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].hectaresarablelandperperson.tolist()
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_one = dict(title = 'Change in Hectares Arable Land <br> per Person 1990 to 2015',
                xaxis = dict(title = 'Year',
                    autotick=False, tick0=1990, dtick=25),
                yaxis = dict(title = 'Hectares')
                    )

    # Second chart plots arable land for 2015 as a bar chart
    graph_two = []
    """ Datasets DO NOT match tutorial!!! """
    df = cleandata('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv')
    df.columns = ['country', 'year', 'hectaresarablelandperperson']
    df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
    df = df[df['year'] == 2015]

    graph_two.append(
        go.Bar(
        x = df.country.tolist(),
        y = df.hectaresarablelandperperson.tolist()
        )
    )

    layout_two = dict(title = 'Hectares Arable Land per Person in 2015',
                xaxis = dict(title = 'Country'),
                yaxis = dict(title = 'Hectares per Person')
                    )

    # Third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    """ Datasets DO NOT match tutorial!!! """
    df = cleandata('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv')
    df.columns = ['country', 'year', 'percentrural']
    df.sort_values('percentrural', ascending=False, inplace=True)
    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].percentrural.tolist()
        graph_three.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_three = dict(title = 'Change in Rural Population <br> (Percent of Total Population)',
                xaxis = dict(title = 'Year',
                    autotick=False, tick0=1990, dtick=25),
                yaxis = dict(title = 'Percent')
                    )

    # Fourth chart shows rural population vs arable land
    graph_four = []

    value_variables = [str(x) for x in range(1995, 2016)]
    keepcolumns = [str(x) for x in range(1995, 2016)]
    keepcolumns.insert(0, 'Country Name')

    """ Datasets DO NOT match tutorial!!! """
    df_one = cleandata('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv', keepcolumns, valuevariables)
    df_two = cleandata('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv', keepcolumns, valuevariables)

    df_one.columns = ['country', 'year', 'variable']
    df_two.columns = ['country', 'year', 'variable']

    df = df_one.merge(df_two, on=['country', 'year'])
    for country in countrylist:
        x_val = df[df['country'] == country].variable_x.tolist()
        y_val = df[df['country'] == country].variable_y.tolist()
        year = df[df['country'] == country].year.tolist()
        country_label = df[df['country'] == country].country.tolist()

        text = []
        for country, year in zip(country_label, year):
            text.append(str(country) + ' ' + str(year))

        graph_four.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'markers',
            text = text,
            name = country,
            textposition = 'top'
            )
        )

    

# Filter for 1990 and 2015, top 10 economies
# df = df[['Country Name', '1990', '2015']]
# countrylist = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
# df = df[df['Country Name'].isin(countrylist)]
#
# # Melt year columns and convert year to date time
# df_melt = df.melt(id_vars='Country Name', value_vars = ['1990', '2015'])
# df_melt.columns = ['country', 'year', 'variable']
# df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year
#
# # Add column names
# df_melt.columns = ['country', 'year', 'percentrural']
#
# # Prepare data into x, y lists for plotting
# df_melt.sort_values('percentrural', ascending=False, inplace=True)
#
# data = []
# for country in countrylist:
#     x_val = df_melt[df_melt['country'] == country].year.tolist()
#     y_val = df_melt[df_melt['country'] == country].percentrural.tolist()
#     data.append((country, x_val, y_val))
#     print(country, x_val, y_val)
