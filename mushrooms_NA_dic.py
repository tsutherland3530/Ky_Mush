# Step 1: Create a Dictionary for 40 Mushrooms from North America

north_america_mushrooms = [
    {
        'Name': 'Delicious Milk Cap, Lactarius Delicousness 1',
        'Description': 'Widespread and common.  broadly convex, dull orange to grey sometimes blotched or entirely green. 1.',
        'Habitat': 'scattered under conifers.  abundant in coastal pine forests.',
        'Growing_Seasons': [ 'winter', 'late Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bleeding Milk Cap 2',
        'Description': 'Broadly convex and broad.  Reddish-brown to orange, orange, brown, or tan.  Taste is mild to slightly bitter. 2.',
        'Habitat': 'scattered under conifers.  abundant in coastal pine forests.',
        'Growing_Seasons': ['Early winter', 'late Fall'],
        'Is_Poisonous': False
    },
    'Name': 'Beechwood Sickener 3',
        'Description': 'A red-capped mushroom that causes sickness if consumed.',
        'Habitat': 'Deciduous woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': True
    },
    {
        'Name': 'Beefsteak Fungus 4',
        'Description': 'Resembles a slab of raw meat, with a reddish-brown upper surface.',
        'Habitat': 'On the wood of deciduous trees',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Birch Polypore 5',
        'Description': 'Conk fungus with a woody appearance, often found on birch trees.',
        'Habitat': 'Birch trees',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Birch Woodwart 6',
        'Description': 'Small, wood-rotting mushroom found on birch wood.',
        'Habitat': 'Birch wood',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bitter Beech Bolete 7',
        'Description': 'A bolete mushroom with a bitter taste.',
        'Habitat': 'Beech woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': True
    },
    {
        'Name': 'Bitter Bolete 8',
        'Description': 'A bolete mushroom known for its bitter taste.',
        'Habitat': 'Woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': True
    },
    {
        'Name': 'Black Bulgar 9',
        'Description': 'Dark-colored mushroom with a distinctive appearance.',
        'Habitat': 'Mixed woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Black Morel 10',
        'Description': 'Highly prized edible mushroom with a distinctive honeycomb appearance.',
        'Habitat': 'Woodlands and open areas',
        'Growing_Seasons': ['Spring'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blackening Brittlegill 11',
        'Description': 'Brittlegill mushroom that blackens with age or when bruised.',
        'Habitat': 'Mixed woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blackening Polypore 12',
        'Description': 'Polypore mushroom that darkens with age.',
        'Habitat': 'Dead wood',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blackening Waxcap 13',
        'Description': 'Waxcap mushroom that blackens with age.',
        'Habitat': 'Grassy areas',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blue Roundhead 14',
        'Description': 'Mushroom with a blue-tinged cap and stem.',
        'Habitat': 'Woodlands and grassy areas',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blushing Bracket 15',
        'Description': 'Bracket fungus with a blushing appearance when touched.',
        'Habitat': 'Woodlands',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blushing Rosette 16',
        'Description': 'Mushroom with a rosette-like arrangement of caps.',
        'Habitat': 'Grassy areas',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Blushing Wood Mushroom 16',
        'Description': 'Wood-loving mushroom with a tendency to blush.',
        'Habitat': 'Woodlands',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bovine Bolete 18',
        'Description': 'Bolete mushroom with a preference for cow pastures.',
        'Habitat': 'Grassy areas and woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bronze Bolete 19',
        'Description': 'Bolete mushroom with a bronze-colored cap.',
        'Habitat': 'Mixed woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Brown Birch Bolete 20',
        'Description': 'Bolete mushroom commonly found near birch trees.',
        'Habitat': 'Birch woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Brown Rollrim 21',
        'Description': 'Mushroom with a rolled rim and brown cap.',
        'Habitat': 'Woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Bruising Webcap 22',
        'Description': 'Webcap mushroom that bruises when handled.',
        'Habitat': 'Mixed woodlands',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    }
    {
        'Name': 'Honey Fungus 23',
        'Description': 'Cluster-forming fungus with honey-colored caps',
        'Habitat': 'Woodlands and forests',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': True  # Note: Some species are edible, but some can be toxic.
    },
    {
        'Name': 'Dryad’s Saddle 24',
        'Description': 'Large, fan-shaped mushroom with brown scales',
        'Habitat': 'Deciduous trees',
        'Growing_Seasons': ['April', 'May', 'June', 'July', 'August'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Morel Mushrooms 25',
        'Description': 'Distinctive honeycomb appearance with a hollow stem',
        'Habitat': 'Woodlands and grassy areas',
        'Growing_Seasons': ['Spring'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Chanterelles 26',
        'Description': 'Golden-yellow mushrooms with a funnel shape',
        'Habitat': 'Woodlands and mossy areas',
        'Growing_Seasons': ['Summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': "Lion’s Mane 27",
        'Description': 'White, shaggy appearance resembling a lion’s mane',
        'Habitat': 'Deciduous trees',
        'Growing_Seasons': ['Late summer', 'Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Yellowfoot Mushrooms 28',
        'Description': 'Small mushrooms with yellow caps and stems',
        'Habitat': 'Woodlands and grassy areas',
        'Growing_Seasons': ['Late summer'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Common Bonnet Mushroom 28',
        'Description': 'Small to medium-sized mushroom with a conical cap',
        'Habitat': 'Woodlands and grassy areas',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Hedgehog Mushrooms 29',
        'Description': 'Fungi with spines instead of gills on the underside',
        'Habitat': 'Woodlands',
        'Growing_Seasons': ['Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Oyster Mushrooms 30',
        'Description': 'Oyster-shaped mushrooms with a broad cap',
        'Habitat': 'Woodlands and on trees',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Pear-shaped Puffball 31',
        'Description': 'Small, pear-shaped mushroom that releases spores when mature',
        'Habitat': 'Grassy areas',
        'Growing_Seasons': ['Fall'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Chicken of the Woods 32',
        'Description': 'Bright orange shelf-like fungus',
        'Habitat': 'Deciduous trees',
        'Growing_Seasons': ['Late August', 'September', 'October'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Turkey-tail Mushrooms 33',
        'Description': 'Colorful turkey tail mushroom',
        'Habitat': 'Dead trees and logs',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    },
    {
        'Name': 'Velvet Foot 34',
        'Description': 'Dark-colored mushroom with a velvety stem',
        'Habitat': 'Woodlands and on decaying wood',
        'Growing_Seasons': ['All year'],
        'Is_Poisonous': False
    }
    
    
    
    
    
    
    
    
    
  f
]

# Step 2: Combine the Two Dictionaries
all_mushrooms = mushrooms_kentucky + north_america_mushrooms

# Step 3: Create a DataFrame
all_mushrooms_df = pd.DataFrame(all_mushrooms)

# Step 4: Filter Data for Kentucky
kentucky_mushrooms_df = all_mushrooms_df[all_mushrooms_df['Habitat'] == 'Kentucky']

# Display the DataFrames
print("All Mushrooms DataFrame:")
print(all_mushrooms_df)

print("\nKentucky Mushrooms DataFrame:")
print(kentucky_mushrooms_df)