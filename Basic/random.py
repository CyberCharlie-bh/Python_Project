import random

# Fake first names
first_names = ["Zyra", "Korben", "Liora", "Jaxen", "Velda",
               "Fynlee", "Quorin", "Saphira", "Tavian", "Nyx"]

# Fake last names
last_names = ["Thalor", "Vexley", "Draven", "Korrin", "Zelwin",
              "Fynrick", "Quellor", "Sundrax", "Tavros", "Nyther"]

# Fake street names
street_names = ["Shadowlane", "Crystal Avenue", "Ironwood Street", "Mooncrest Drive", "Falcon Road",
                "Obsidian Court", "Silverpine Lane", "Ember Way", "Stormridge Boulevard", "Goldenleaf Street"]

# Fake cities
fake_cities = ["Grimvale", "Mistwood", "Ravenmoor", "Stormhollow", "Ashenport",
               "Dragonspire", "Cindermere", "Frostholt", "Nightshade", "Sunveil"]

# Fake states
states = ["Eldoria", "Vexaria", "Cindralis", "Frostgard", "Drakonia",
          "Lumoria", "Ashvalen", "Sylveria", "Thaloria", "Oblivara"]

for i in range(10):
    
    # The names of people
    
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(f'{first} {last}\n')

    # Phone Number
    n1 = random.randint(100,999)
    n2 = random.randint(100,999)
    n3 = random.randint(1000,9999)
    print(f'{n1}{n2}{n3}\n')

    # Location
    
    street_number = random.randint(1,99)
    random_street = random.choice(street_names)
    random_city = random.choice(fake_cities)
    random_states = random.choice(states)
    print(f'{street_number} St. {random_street}\n{random_city}\n{random_states}\n\n')

