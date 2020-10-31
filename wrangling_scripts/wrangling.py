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
