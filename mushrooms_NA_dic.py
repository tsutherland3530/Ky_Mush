# Step 1: Create a Dictionary for Mushrooms from North America
import pandas as pd

# Step 1: Create a Dictionary for 40 Mushrooms from North America
north_america_mushrooms = [
    {
        'Name': 'Delicious Milk Cap, Lactarius Delicousness 1',
        'Description': 'Widespread and common. Broadly convex, dull orange to grey sometimes blotched or entirely green.',
        'Habitat': 'scattered under conifers. abundant in coastal pine forests.',
        'Growing_Seasons': ['winter', 'late Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bleeding Milk Cap 2',
        'Description': 'Broadly convex and broad. Reddish-brown to orange, orange, brown, or tan. Taste is mild to slightly bitter.',
        'Habitat': 'scattered under conifers. abundant in coastal pine forests.',
        'Growing_Seasons': ['Early winter', 'late Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Beechwood Sickener 3',
        'Description': 'A red-capped mushroom that causes sickness if consumed.',
        'Habitat': 'Deciduous woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': True
    },
    # Add the rest of the mushroom dictionaries here...

]

# Step 2: Combine the Two Dictionaries
all_mushrooms = north_america_mushrooms  # You can add mushrooms_kentucky here if needed

# Step 3: Create a DataFrame
all_mushrooms_df = pd.DataFrame(all_mushrooms)

# Step 4: Filter Data for Kentucky
kentucky_mushrooms_df = all_mushrooms_df[all_mushrooms_df['Habitat'] == 'Kentucky']

# Display the DataFrames
print("All Mushrooms DataFrame:")
print(all_mushrooms_df)
print("\nKentucky Mushrooms DataFrame:")
print(kentucky_mushrooms_df)
