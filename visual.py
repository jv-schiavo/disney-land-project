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
    Display a single bar chart showing the average number of reviews each park has received.
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

def plot_top_10_location(data):
    """
    Display a bar chart that shows the top 10 locations that gave the highest average rating for that park
    """

    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_"
                      "California, Disneyland_Paris)\n")

    park_data = [row for row in data if row['Branch'] == park_name]
    if not park_data:
        print(f"\n{park_name} is not in the data")
        return

    # Aggregate data by location
    location_scores = {}
    location_counts = {}

    for row in park_data:
        location = row['Reviewer_Location']
        rating = int(row['Rating'])

        if location in location_scores:
            location_scores[location] += rating
            location_counts[location] += 1
        else:
            location_scores[location] = rating
            location_counts[location] = 1

    # Calculate average scores by location
    average_scores = {location: location_scores[location] / location_counts[location]}

    # Sort locations by average rating and select top 10
    sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Prepare data for the bar chart
    labels = [location for location, _ in sorted_locations]
    heights = [score for _, score in sorted_locations]

    # Create the bar chart
    plt.bar(labels, heights, color='green')
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.title(f"Top 10 Locations by Average Rating for {park_name}")
    plt.show()

