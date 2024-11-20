import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
lower_limit = df["value"].quantile(0.025)
upper_limit = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_limit) & (df["value"] <= upper_limit)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], '-r')

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=12)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Page Views", fontsize=12)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
   # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(15,13))
    df_bar.plot(kind='bar', stacked= False,ax=ax)

    # Set labels and title
    plt.xlabel("Years", fontsize=16)
    plt.ylabel("Average Page Views", fontsize=16)

    # Customize the legend
    plt.legend(title="Months", labels=[
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
        # Prepare data for box plots
    df_box = df.copy()
    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.month
    df_box['Month Name'] = df_box.index.strftime('%b')  # For month names
    df_box = df_box.sort_values('Month')  # Ensure months are in order


    # Set up the figure
    fig, axes = plt.subplots(1, 2, figsize=(18, 5))

    # Year-wise Box Plot
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize=14)
    axes[0].set_xlabel("Year", fontsize=12)
    axes[0].set_ylabel("Page Views", fontsize=12)

    # Month-wise Box Plot
    sns.boxplot(x='Month Name', y='value', data=df_box, order=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ], ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize=14)
    axes[1].set_xlabel("Month", fontsize=12)
    axes[1].set_ylabel("Page Views", fontsize=12)

    # Adjust layout for clarity
    fig.savefig('box_plt.png')
    return fig