print("Enter contact information (format: name|phone|email|address):\n")#AI explained the useage of :\n

contacts = [] #list that stores contacts
count = 0 #Keeps track of how many contatcts are stored

while True:
    line = input()
    if line.lower() == "done":# turns input into lowercase
        break
    if not line.strip(): # skips empty lines
        continue

    fields = line.split('|') #Splits the text when a vertical bar is present
    if len(fields) != 4:
        print("Invalid format. Please use name|phone|email|address.")
        continue
# Checks if there are exactly 4 part and if not then gives user the proper format
    # --- Name cleaning ---
    name_field = fields[0].strip() #Removes spaces before or after the name
    name_parts = name_field.split() # Breaks name into individual words
    name = ' '.join(name_parts).title() # Puts them back together and then capatalizes the name properly
