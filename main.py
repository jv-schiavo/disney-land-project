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

    data = load_csv()

    while True:

        # Display the main menu and get user input
        choice = menu_choice() # Call function from tui.py to display the menu

        if choice == 'X':
            break # Exit the program

        elif choice == 'A':

            while True:
                # Display the sub-menu after option A
                sub_choice_a = view_data()
                if sub_choice_a == 'X':
                    break

                elif sub_choice_a == 'A':
                    # Pass the loaded dataset
                    reviews_park(data)

                elif sub_choice_a == 'B':
                    # Pass the loaded dataset
                    rev_park_location(data)

                elif sub_choice_a == 'C':
                    # Pass the loaded dataset
                    avg_rating(data)

                elif sub_choice_a == 'D':
                    # Pass the loaded dataset
                    avg_score_park_location(data)

                else:
                    view_data()

        elif choice == 'B':
            while True:
                # Display the sub-menu after option B
                sub_choice_b = visualize_data()
                if sub_choice_b == 'X':
                    break

                elif sub_choice_b == 'A':
                    # Pass the plot
                    plot_reviews_pie_chart(data)

                elif sub_choice_b == 'B':
                    # Pass the plot
                    plot_avg_scores_bar_chart(data)

                elif sub_choice_b == 'C':
                    # Pass the plot
                    plot_top_10_location(data,min_reviews=100)

                elif sub_choice_b == 'D':
                    # Pass the plot
                    plot_bar_chart_month(data)

                else:
                    visualize_data()

        elif choice == 'C':
            export_menu(data)
        else:
            menu_choice()


if __name__ == "__main__":
    main()