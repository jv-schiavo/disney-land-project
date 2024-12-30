"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')
# Set the backend to 'TkAgg' to force plots to open in a new window

def plot_reviews_pie_chart(data):
    """
    Displays a pie chart showing the number of reviews each park has received.
    """

    # Aggregate data by park
    park_counts = {}
    for row in data:
        park_name = row['Branch']
        if park_name in park_counts:
            park_counts[park_name] += 1
        else:
            park_counts[park_name] = 1

    # Prepare data for the pie chart
    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    # Create the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Reviews by Park")
    plt.show()


