import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Mushroom": ["Morels", "Chanterelles", "Boletes", "Honey mushrooms", "Shiitake"],
    "Grow_Season": ["Spring", "Summer-Fall", "Summer-Fall", "Summer-Fall", "Year-round"],
    "Poisonings": [5, 2, 3, 1, 0],
    "Popularity": [90, 70, 60, 50, 30]
}

df = pd.DataFrame(data)

import csv

# Comparing grow seasons to poisonings
seasons_poisonings = df.groupby("Grow_Season")["Poisonings"].sum()
seasons_poisonings.plot(kind="bar", color="skyblue")
plt.title("Grow Seasons vs. Poisonings")
plt.xlabel("Grow Season")
plt.ylabel("Number of Poisonings")
plt.show()

# Pie chart of the most popular wild mushrooms
most_popular = df.nlargest(3, "Popularity")
plt.pie(most_popular["Popularity"], labels=most_popular["Mushroom"], autopct='%1.1f%%', startangle=140)
plt.axis("equal")
plt.title("Most Popular Wild Mushrooms in Kentucky")
plt.show()

# Sort by popularity
sorted_df = df.sort_values(by="Popularity", ascending=False)

# Display the sorted DataFrame
print("Database of Most Found Mushrooms to Least Found Mushrooms:")
print(sorted_df)

# Data for the mushrooms
mushrooms = [
    {
        "Genus": "Morchella",
        "Species": "esculenta",
        "Harvest Season": "Spring",
        "Location": "Kentucky",
        "Description": "Morels are highly sought after edible mushrooms with a distinctive honeycomb appearance.",
        "Nutritional Information": "Rich in protein, vitamins, and minerals."
    },
    {
        "Genus": "Cantharellus",
        "Species": "cibarius",
        "Harvest Season": "Summer-Fall",
        "Location": "Kentucky",
        "Description": "Chanterelles have a vibrant yellow color and a fruity aroma. They are known for their mild, peppery flavor.",
        "Nutritional Information": "Low in calories, a good source of vitamin C and vitamin D."
    },
    # Add information for the other mushrooms here
]

# Specify the CSV file path
csv_file = "mushrooms_of_kentucky.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="") as file:
    fieldnames = ["Genus", "Species", "Harvest Season", "Location", "Description", "Nutritional Information"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(mushrooms)

# Function to search for a mushroom by name
def search_mushroom_by_name(name):
    for mushroom in mushrooms:
        if name.lower() in f"{mushroom['Genus']} {mushroom['Species']}".lower():
            return mushroom
    return None

while True:
    user_input = input("Enter the name of a mushroom (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    mushroom = search_mushroom_by_name(user_input)
    if mushroom:
        print("Mushroom Information:")
        for key, value in mushroom.items():
            print(f"{key}: {value}")
    else:
        print("Mushroom not found.")
# more barplot visualization using Seaborn 
pip install seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    "Mushroom": ["Morels", "Chanterelles", "Boletes", "Honey mushrooms", "Shiitake"],
    "Popularity": [90, 70, 60, 50, 30]
}

df = pd.DataFrame(data)

# Create a bar plot using Seaborn
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
sns.set(style="whitegrid")
sns.barplot(x="Popularity", y="Mushroom", data=df, palette="viridis")

plt.title("Mushroom Popularity in Kentucky")
plt.xlabel("Popularity")
plt.ylabel("Mushroom")
plt.show()

