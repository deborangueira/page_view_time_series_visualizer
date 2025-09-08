import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv') # importing dataframe
df['date'] = pd.to_datetime(df['date']) #transforming "date" data type from object (I confirmed it with "df.dtype") into datetime
df = df.set_index('date') #defined date as the index 

# Clean data
df = df[# creating a new dataframe with cleaned data
    # I'll take only the data that represents 95% of the original dataframe based on the interval defined bellow:     
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot(): # Matplotlib to draw a line chart
    # Draw line plot

    fig = df.plot.line(figsize=(15,5), # chart's size and proportion
                        color='blue'); # color of the line
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019'); # title of the chart
    plt.xlabel('Date'); # x-axis legend
    plt.xticks(rotation = 0) # set the legend of x-axis to fully horizontal
    plt.ylabel('Page Views'); # y-axis legend

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    #Since the index is a datetimeIndex (I confirmed it with 'df_bar.index.dtype'), it has atributes like .year, .month, .day, etc that returns a array with this specific information.
    df_bar['year'] = df.index.year # Creates the 'year' column in df_bar by adding the year values ​​extracted from the df index.
    df_bar['month'] = df.index.month_name() # Creates the 'month' column in df_bar by adding the month values ​​extracted from the df index.

    # grouping and organizing the df
    df_bar_group = df_bar.groupby(['year', 'month'])['value'].mean() # group by year, than subgroup by month and show the mean of the values for each
    df_bar_group = df_bar_group.unstack(level='month') # reshape the df making it wide insted of long, where each column is a month and each line a year
    df_bar_group = df_bar_group[['January', 'February', 'March', 'April', 'May',
                                'June', 'July', 'August', 'September', 'October', 'November', 'December']] # organize the order of the months

    # Draw bar plot
    fig = df_bar_group.plot.bar(figsize=(7,7)).figure # creating a bar chart based on the "df_bar_group" and setting the proportion of the image
    plt.xlabel('Years');
    #plt.xticks(rotation = 0)
    plt.ylabel('Average Page Views');
    plt.legend(title='Months');

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
