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

def plot_avg_scores_bar_chart(data):
    """
    Displays a single bar chart showing the average number of reviews each park has received.
    """

    # Aggregate data by park
    park_counts = {}
    park_scores= {}

    for row in data:
        park_name = row['Branch']
        rating = int(row['Rating'])

        if park_name in park_scores:
            park_scores[park_name] += rating # Sum the scores for the park
            park_counts[park_name] += 1 # Count the reviews for the park
        else:
            park_scores[park_name] = rating
            park_counts[park_name] = 1

    # Calculate the average scores
    average_scores = {park: park_scores[park] / park_counts[park]
                      for park in park_scores}

    # Prepare data for bar chart
    labels = list(average_scores.keys())
    heights = list(average_scores.values())

    # Create the bar chart
    plt.figure(figsize=(10,6))
    plt.bar(labels, heights, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.xlabel("Park Name")
    plt.ylabel("Average Rating")
    plt.title("Average Review Scores by Park")
    plt.show()

