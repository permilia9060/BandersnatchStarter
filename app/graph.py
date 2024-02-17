from altair import Chart, Tooltip, X, Y, TitleParams, Color, Scale  # imports from Altair library
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """Create a scatter plot chart using Altair.

    Parameters:
        df (DataFrame): The DataFrame holds the data.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        target (str): The column name for the target.
    """
    vis = Chart(  # Initializes a new chart object
        df,
        title=f"{y} by {x} for {target}"
    ).mark_circle(size=80).encode(  # Marks will be circle and size 80.Encode maps data columns to visual properties.
        x=x,  # Maps x column name to the x-axis.
        y=y,  # # Maps x column name to the y-axis.
        color=target,  # color encoding is being applied to the target column
        tooltip=Tooltip(df.columns.to_list())  # Sets up tooltips for the graph. Tooltips are additional
        # information that appears when you hover over a data point.
    ).properties(  # Sets various properties of the graph.
        width=400,  # Sets width of the graph.
        height=400,  # Sets width of the graph.
        padding=50,
        background="#202020"
    ).configure(
        legend={
            "titleColor": "#D0D0D0",
            "labelColor": "#D0D0D0",
            "padding": 10  # Extra space used to achieve formatting requirements.
        },
        title={
            "color": "#D0D0D0",
            "fontSize": 25,
            "offset": 30  # Provides the offset for the title element.
        },
        axis={
            "titlePadding": 20,
            "titleColor": "#D0D0D0",
            "labelPadding": 5,
            "labelColor": "#D0D0D0",
            "gridColor": "#C8C8C8",
            "tickColor": "#D0D0D0",  # Refers to the color of the tick marks or grid lines.
            "tickSize": 10
        },
        view={
            "stroke": "black"  # Refers to color of the outline.
        }
    )

    return vis