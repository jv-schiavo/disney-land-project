"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.

Author: Joao Victor Garcia Schiavo
Date: 31/12/2024
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
    bars = plt.bar(labels, heights, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.xlabel("Park Name")
    plt.ylabel("Average Rating")
    plt.title("Average Review Scores by Park")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2),
                 ha='center', va='bottom', fontsize=10)
    plt.show()

def plot_top_10_location(data, min_reviews=100):
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
        location = row.get('Reviewer_Location')
        rating = int(row['Rating'])

        if location in location_scores:
            location_scores[location] += rating
            location_counts[location] += 1
        else:
            location_scores[location] = rating
            location_counts[location] = 1

    # Calculate average scores by location
    average_scores = {}

    for location, total_score in location_scores.items():
        count = location_counts[location]
        average = total_score / count
        average_scores[location] = average


    # Filter out locations with fewer reviews than the threshold
    filtered_locations = {location: location_scores[location] / location_counts[location]
                          for location in location_scores if location_counts[location] >= min_reviews}

    if not filtered_locations:
        print(f"No locations meet the minimum review threshold of {min_reviews}.")
        return

    # Sort locations by average rating and select top 10
    sorted_locations = sorted(filtered_locations.items(), key=lambda x: x[1], reverse=True)[:10]
    top_10_locations = sorted_locations[:10]

    # Prepare data for the bar chart
    location_mapping = {"United Kingdom": "UK",
                        "United States": "USA",
                        "United Arab Emirates": "UAE"}

    labels = [location_mapping.get(location, location) for location, _ in top_10_locations]
    heights = [score for _, score in top_10_locations]

    # Create the bar chart
    bars = plt.bar(labels, heights, color='green')
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.title(f"Top 10 Locations by Average Rating for {park_name}")
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, round(yval, 2),
                 ha='center', va='bottom', fontsize=10)
    plt.show()

def plot_bar_chart_month(data):
    """
        Display a bar chart that shows the average rating that park received for each month of the year.
        """

    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_"
                      "California, Disneyland_Paris)\n")

    # Filter data for the specified park
    park_data = [row for row in data if row['Branch'] == park_name]
    if not park_data:
        print(f"\n{park_name} is not in the data.")
        return

    # Aggregate data by month
    month_scores = {str(i): 0 for i in range (1, 13)}
    month_counts = {str(i): 0 for i in range (1, 13)}

    for row in park_data:
        try:
            # Extract the month from Year_Month and normalize to single digit
            year_month = row.get('Year_Month')
            if not year_month or '-' not in year_month:
                continue

            month = year_month.split('-')[1].lstrip('0')

            rating = int(row['Rating'])
            month_scores[month] += rating
            month_counts[month] += 1

        except (ValueError, IndexError) as e:
            print(f"Error processing row {row}: {e}")
            continue

    # Calculate average scores for each month
    average_scores = {
        month: (month_scores[month] / month_counts[month]) if month_counts[month] > 0 else 0
        for month in month_scores
    }

    # Define month order and sort
    month_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    sorted_average_scores = [
        (month, average_scores[month])
        for month in month_order if month in average_scores
    ]

    # Check for empty data after filtering
    if not sorted_average_scores:
        print(f"No ratings data available for {park_name}.")
        return

    # Unpack sorted scores into labels and heights
    labels, heights = zip(*sorted_average_scores)
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    labels = [month_names[int(month) - 1] for month in labels]

    bars = plt.bar(labels, heights, color='lightpink')
    plt.title(f"Average Ratings for {park_name} by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, round(yval, 2),
                 ha='center', va='bottom', fontsize=10)
    plt.show()


