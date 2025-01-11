"""
This module controls the overall program flow for the Disneyland Reviews project.
It serves as the entry point for the application, displaying the main menu
and calling relevant functions from other modules based on user input.

Author: Joao Victor Garcia Schiavo
Date: 27/12/2024
"""
from process import load_csv
from exporter import export_menu
from tui import (title,menu_choice, view_data, visualize_data, reviews_park, rev_park_location, avg_rating,
                 avg_score_park_location)
from visual import plot_reviews_pie_chart, plot_avg_scores_bar_chart, plot_top_10_location, plot_bar_chart_month


def main():
    """
        Main function that runs the Disneyland Reviews program.

        Displays the main menu, handles user input, and directs the program
        flow to sub-menus or exits the program.
        """
    title()

    file_path = r'C:\Users\Joao Victor\Downloads\project_template\disneyland_reviews.csv'
    data = load_csv(file_path)

    while True:

        # Display the main menu and get user input
        choice = menu_choice() # Call function from tui.py to display the menu

        if choice == 'X':
            print("\nYou have chosen option X - Exit")
            print("Exiting program. Goodbye!")
            break # Exit the program

        elif choice == 'A':
            print("\nYou have chosen option A - View Data")

            while True:
                # Display the sub-menu after option A
                sub_choice_a = view_data()
                if sub_choice_a == 'X':
                    break

                elif sub_choice_a == 'A':
                    print("\nYou have chosen option A - View Reviews by Park")
                    # Pass the loaded dataset
                    reviews_park(data)

                elif sub_choice_a == 'B':
                    print("\nYou have chosen option B - Number of Reviews by Park and Reviewer Location")
                    # Pass the loaded dataset
                    rev_park_location(data)

                elif sub_choice_a == 'C':
                    print("You have chosen option C - Average Score per year by Park")
                    # Pass the loaded dataset
                    avg_rating(data)

                elif sub_choice_a == 'D':
                    print("You have chosen option D - Average Score by Park and Reviewer Location")
                    # Pass the loaded dataset
                    avg_score_park_location(data)

                else:
                    print("Invalid choice. Please try again.\n")
                    view_data()

        elif choice == 'B':
            print("\nYou have chosen option B - Visualize Data")

            while True:
                # Display the sub-menu after option B
                sub_choice_b = visualize_data()
                if sub_choice_b == 'X':
                    print("Returning to Main Menu...\n")
                    break

                elif sub_choice_b == 'A':
                    print("\nYou have chosen option A - Most Reviewed by Parks")
                    # Pass the plot
                    plot_reviews_pie_chart(data)

                elif sub_choice_b == 'B':
                    print("\nYou have chosen option B - Average Scores")
                    # Pass the plot
                    plot_avg_scores_bar_chart(data)

                elif sub_choice_b == 'C':
                    print("You have chosen option C - Park Ranking by Nationality")
                    # Pass the plot
                    plot_top_10_location(data,min_reviews=100)

                elif sub_choice_b == 'D':
                    print("You have chosen option D - Most Popular Month by Park")
                    # Pass the plot
                    plot_bar_chart_month(data)

                else:
                    print("Invalid choice. Please try again.\n")
                    visualize_data()

        elif choice == 'C':
            print("\nYou have chosen option C - Export Data")
            export_menu(data)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()