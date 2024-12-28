"""
This module provides the Text-User Interface (TUI) for the Disneyland Reviews project.
It handles all user interactions, including displaying menus and getting user input.

Author: Joao Victor Garcia Schiavo
Date: 27/12/2014
"""


def menu_choice():
    # Display the main menu and accepts user input
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("\n[A] View Data")
    print("[B] Visualize Data")
    print("[X] Exit")
    return input().strip().upper() #str: the user's menu choice


def view_data():
    # Display the sub-menu for 'View Data' and accepts user inpt
    print("\nPlease enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    return input().strip().upper() #str: the user's sub-menu choice

def visualize_data():
    # Display the sub-menu for 'Visualize Data' and accepts user input
    print("\nPlease enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    return input().strip().upper() #str: the user's sub-menu choice

def reviews_park(data):
    # Display all reviews for a specific park based on user input
    park_name = input("\nPlease enter the name park you wish to see reviews for: (Eg: Disneyland_HongKong, Disneyland_California)")
    # Filter reviews for the specified park
    filtered_reviews = [row for row in data if row['Branch'] == park_name]

    if not filtered_reviews:
        print(f"No reviews found for {park_name}")
        return

    print(f"\nReviews for {park_name}:")
    for review in filtered_reviews:
        print(f"Reviews ID: {review['Review ID']}, Rating: {review['Rating']},"
              f"Date: {review['Year_Month']}, Location: {review['Reviewer_Location']}")
