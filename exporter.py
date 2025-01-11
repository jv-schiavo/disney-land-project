"""
This module is responsible to export aggregate data into different file formats: (txt, csv, json)
using Object-Oriented Programing

Author: Joao Victor Garcia Schiavo
Date: 11/01/2025
"""

class Exporter:
    def __init__(self, format):
        self.format = format

    def export(self, data, filename):
        if self.format == "TXT":
            self.export_txt(data, filename)
        elif self.format == "CSV":
            self.export_csv(data, filename)
        elif self.format == "JSON":
            self.export_json(data, filename)

    def export_txt(self, data, filename):
        with open(filename, "w") as f:
            for park, info in data.items():
                f.write(f"Park: {park}\n")
                f.write(f"Number of Reviews: {info['total_reviews']}\n")
                f.write(f"Number of Positive Reviews: {info['positive_reviews']}\n")
                f.write(f"Average Score: {info['avg_score']:.2f}\n")
                f.write(f"Number of Countries Reviewed: {info['countries_reviewed']}\n\n")

    def export_csv(self, data, filename):
        with open(filename, "w") as f:
            f.write("Park,Total Reviews,Positive Reviews,Average Score,Countries Reviewed\n")
            for park, info in data.items():
                f.write(
                    f"{park},{info['total_reviews']},{info['positive_reviews']},{info['avg_score']:.2f},{info['countries_reviewed']}\n")

    def export_json(self, data, filename):
        import json
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


# Aggregator class that gathers all the necessary info for each park.
class ParkDataAggregator:
    def aggregate(self, data):
        aggregated_data = {}
        unique_parks = set(row['Branch'] for row in data)

        for park_name in unique_parks:
            park_data = [row for row in data if row['Branch'] == park_name]
            total_reviews = len(park_data)
            positive_reviews = sum(1 for row in park_data if int(row['Rating']) > 3)
            avg_score = sum(int(row['Rating']) for row in park_data) / total_reviews
            unique_countries = set(row['Reviewer_Location'] for row in park_data)

            aggregated_data[park_name] = {
                'total_reviews': total_reviews,
                'positive_reviews': positive_reviews,
                'avg_score': avg_score,
                'countries_reviewed': len(unique_countries)
            }

        return aggregated_data


# Submenu to choose the export format
def export_menu(data):
    print("\nExport Menu:")
    print("[A] Export as TXT")
    print("[B] Export as CSV")
    print("[C] Export as JSON")
    print("[X] Main Menu")

    sub_choice_c = input("Enter your choice: ").strip().upper()

    if sub_choice_c == "A":
        print("\nYou have chosen option A - Export as TXT")
        format = "TXT"
    elif sub_choice_c == "B":
        print("\nYou have chosen option B - Export as CSV")
        format = "CSV"
    elif sub_choice_c == "C":
        print("\nYou have chosen option C - Export as JSON")
        format = "JSON"
    elif sub_choice_c == "X":
        return  # Go back to the main menu
    else:
        print("Invalid choice! Returning to main menu.")
        return

    aggregator = ParkDataAggregator()
    aggregated_data = aggregator.aggregate(data)

    exporter = Exporter(format)
    filename = f"parks_data.{format.lower()}"
    exporter.export(aggregated_data, filename)

    print(f"Data exported successfully to {filename}!")








