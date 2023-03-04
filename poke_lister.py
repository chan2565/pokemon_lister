import requests
from time import sleep

### CONFIG ###
# Set the range to generate the CSV, inclusive
start_num = 1
end_num = 1008

# Set the API root URI for Pokémon info
root_uri = "https://pokeapi.co/api/v2/pokemon/"

# Output filename
filename = "pokemon_list.csv"
### END CONFIG ###


### FUNCTIONS ###
def cap_words(words):
    out_str = ""
    split = words.split("-")
    for word in split:
        out_str = out_str + word.capitalize() + " "
    out_str = out_str.strip()
    return out_str

def gen_line(json):
    num = json["id"]
    name = cap_words(json["name"])
    line = str(num) + ',' + name + "\n"
    return line
### END FUNCTIONS ###


### MAIN ###
with open(filename, 'w') as file:
    # Write CSV header
    file.write("Number,Name\n")

    # Step through Pokémon
    for num in range(start_num, end_num + 1):
        # Pause for API limits
        sleep(.1)

        # Get info
        json = requests.get(root_uri + str(num)).json()
        
        # Format line
        line = gen_line(json)

        # Print/Write CSV line
        print(line)
        file.write(line)
### END MAIN ###
