from fuzzywuzzy import fuzz

# Initialize an empty list to store country names
country_table = []
city_table=[]
state_table=[]
    

# Read country names from the file
with open("Country.txt", "r", encoding="utf-8") as file:
    for line in file:
        country_table.append(line.strip())  # Remove leading/trailing whitespace

# Read city names from the file
with open("City.txt", "r", encoding="utf-8") as file:
    for line in file:
        city_table.append(line.strip())  # Remove leading/trailing whitespace
# Read state names from the file
with open("State.txt", "r", encoding="utf-8") as file:
    for line in file:
        state_table.append(line.strip())  # Remove leading/trailing whitespace
def find_geospatial_entities(sentence):
    # Split the sentence into tokens using basic whitespace tokenization
    tokens = sentence.split()

    geospatial_entities = []

    for token in tokens:
        # Check if the token is a geospatial entity by fuzzy matching against tables
        canonical_name, table = None, None

        for name in country_table:
            if fuzz.ratio(token.lower(), name.lower()) >= 85:  # Adjust the threshold as needed
                canonical_name, table = name, "Country"
                break

        if not canonical_name:
            for name in city_table:
                if fuzz.ratio(token.lower(), name.lower()) >= 85:
                    canonical_name, table = name, "City"
                    break

        if not canonical_name:
            for name in state_table:
                if fuzz.ratio(token.lower(), name.lower()) >= 85:
                    canonical_name, table = name, "State"
                    break

        if canonical_name:
            geospatial_entities.append({"Token": token, "Canonical name": canonical_name, "Table": table})

    return geospatial_entities

# Example usage:
input_sentence = input("Enter any Sentence or Question to find out the GeoEntity in it :")
entities = find_geospatial_entities(input_sentence)

for entity in entities:
    print(f"Token: {entity['Token']}, Canonical name: {entity['Canonical name']}, Table: {entity['Table']}")
