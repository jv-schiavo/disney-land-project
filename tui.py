"""
This module provides the Text-User Interface (TUI) for the Disneyland Reviews project.
It handles all user interactions, including displaying menus and getting user input.

Author: Joao Victor Garcia Schiavo
Date: 27/12/2014
"""

def title():
    # Program title
    title = "Disneyland Park Review"
    print("-" * len(title))
    print(title)
    print("-" * len(title))

def menu_choice():
    """"
    Display the main menu and accepts user input
    """
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("\n[A] View Data")
    print("[B] Visualize Data")
    print("[C] Export Data")
    print("[X] Exit")
    return input().strip().upper()


    while True:

        choice = menu_choice()

        if choice == "A":
            print("\nYou have chosen option A - View Data")
        elif choice == "B":
            print("\nYou have chosen option B - Visualize Data")
        elif choice == "C":
            print("\nYou have chosen option C - Export Data")
        elif choice == "X":
            print("\nYou have chosen option X - Exit")
            print("Exiting program. Goodbye!")
            break  # Exit the program
        else:
            print("Please enter a valid option")


def view_data():
    """
    Display the sub-menu for 'View Data' and accepts user input
    """

    print("\nPlease enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    print("[X] Main Menu")
    return input().strip().upper() #str: the user's sub-menu choice

    while True:
        sub_choice_a = view_data()
        if sub_choice_a == "A":
            print("\nYou have chosen option A - View Reviews by Park")
        elif sub_choice_a == "B":
            print("\nYou have chosen option B - Number of Reviews by Park and Reviewer Location")
        elif sub_choice_a == "C":
            print("\nYou have chosen option C - Average Score per year by Park")
        elif sub_choice_a == "D":
            print("\nYou have chosen option D - Average Score per Park by Reviewer Location")
        elif sub_choice_a == "X":
            print("Returning to Main Menu...\n")
        else:
            print("\nPlease enter a valid option")


def visualize_data():
    """
    Display the sub-menu for 'Visualize Data' and accepts user input
    """

    print("\nPlease enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    print("[X] Main Menu")
    return input().strip().upper() #str: the user's sub-menu choice

    while True:
        sub_choice_b = visualize_data()
        if sub_choice_b == "A":
            print("\nYou have chosen option A - Most Reviewed Parks")
        elif sub_choice_b == "B":
            print("\nYou have chosen option B - Average Scores")
        elif sub_choice_b == "C":
            print("\nYou have chosen option C - Park Ranking by Nationality")
        elif sub_choice_b == "D":
            print("\nYou have chosen option D - Most Popular Month by Park")
        elif sub_choice_b == "X":
            print("Returning to Main Menu...\n")
        else:
            print("\nPlease enter a valid option")

def reviews_park(data):
    """
    Display all reviews for a specific park based on user input
    """
    print("\nYou have chosen option A - View Reviews by Park")
    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_"
                      "California, Disneyland_Paris)\n")

    # Filter reviews for the specified park
    filtered_reviews = [row for row in data if row['Branch'] == park_name]
    if not filtered_reviews:
        print(f"No reviews found for {park_name}")
        return

    print(f"\nReviews for {park_name}:")
    for review in filtered_reviews:
        print(f"Reviews ID: {review['Review_ID']}, Rating: {review['Rating']},"
              f"Date: {review['Year_Month']}, Location: {review['Reviewer_Location']}")

def rev_park_location(data):
    """
    Display the number of reviews a specific park has received from a given location
    """
    print("\nYou have chosen option B - Number of Reviews by Park and Reviewer Location")
    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_"
                      "California, Disneyland_Paris)\n")

    # Filter reviews for the specified park
    filtered_reviews = [row for row in data if row['Branch'] == park_name]
    if not filtered_reviews:
        print(f"No reviews found for {park_name}")
        return

    # Filter reviews for the specified reviewer location
    reviewer_location = input("\nPlease enter the reviewer location you wish to see reviews for: \n")

    filtered_location = [row for row in filtered_reviews if row['Reviewer_Location'] == reviewer_location]
    if not filtered_location:
        print(f"No reviews found for {park_name}")
        return

    # Display the number of reviews
    print(f"\nNumber of reviews for {park_name} from {reviewer_location}: {len(filtered_location)}")

def avg_rating(data):
    """
    Display the average rating for the given park in the given year
    """
    print("You have chosen option C - Average Score per year by Park")
    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_"
                      "California, Disneyland_Paris)\n")

    # Filter reviews for the specified park
    filtered_reviews = [row for row in data if row['Branch'] == park_name]
    if not filtered_reviews:
        print(f"No reviews found for {park_name}")
        return

    year = input("\nPlease enter the year you wish to see reviews for: \n")

    # Filter reviews for specified year
    filtered_date = [row for row in filtered_reviews if row['Year_Month'][:4] == year]
    if not filtered_date:
        print(f"No reviews found for {year}")
        return

    # Extract ratings
    ratings = [int(row['Rating']) for row in filtered_date if 'Rating' in row and row['Rating'].isdigit()]
    if not ratings:
        print("No valid ratings found in the dataset.")
        return None

    #Calculate the average
    average = sum(ratings) / len(ratings)

    #Display the average rating
    print(f"\n The average rating score for {park_name} in {year} is {average:.2f}")

def avg_score_park_location(data):
    """
    Display the average score per park by reviewer location
    """
    print("You have chosen option D - Average Score by Park and Reviewer Location")
    # Extract unique parks
    unique_parks = set(row['Branch'] for row in data)

    # Iterate over each park
    for park_name in unique_parks:
        print(f"\nAverage ratings for {park_name} by reviewer location:\n")

        # Filter data for the current park
        park_data = [row for row in data if row['Branch'] == park_name]

        # Extract unique locations for this park
        unique_locations = set(row['Reviewer_Location'] for row in park_data)

        # Calculate average ratings for each location
        for location in unique_locations:
            # Filter ratings for the current location
            ratings = [int(row['Rating']) for row in park_data if row['Reviewer_Location'] == location]

            # Calculate the average rating
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                print(f"{location}: {avg_rating:.2f}")
            else:
                print(f"No reviews found for {location}")
