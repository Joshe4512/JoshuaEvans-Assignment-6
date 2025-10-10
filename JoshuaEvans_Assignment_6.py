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

    # --- Phone cleaning ---
    phone_field = fields[1].strip()
    digits_only = ""
    for char in phone_field:
        if char.isdigit():
            digits_only += char
# Loop goes through the number and only keeps digits and only recognizes numbers
    if len(digits_only) == 11 and digits_only[0] == '1':
        digits_only = digits_only[1:] # if there is an area code in the number this loop removes it

    if len(digits_only) == 10:
        area = digits_only[:3]
        prefix = digits_only[3:6]
        line_num = digits_only[6:]
        phone = f"({area}) {prefix}-{line_num}"
    else:
        phone = "INVALID"
        #Loop ensures that the number has ten digits and formats it properly and if not its marked as invalid

    # --- Email cleaning ---
    email_field = fields[2].strip() #Removes outer spaces
    email = email_field.lower().replace(' ', '').replace(',', '') #removes spaces and commas
    if '@' not in email or '.' not in email.split('@')[-1]:
        email = "INVALID"

    # --- Address cleaning ---
    address_field = fields[3].strip()
    parts = [p.strip() for p in address_field.split(',')]
    cleaned_parts = []

    for part in parts:
        words = part.split()
        clean_words = []
        for w in words:
            if w.isalpha() and len(w) == 2:
                clean_words.append(w.upper())  # state abbreviation
            else:
                clean_words.append(w.title())  # normal word
        cleaned_parts.append(' '.join(clean_words))

    address = ', '.join(cleaned_parts)

    contacts.append((name, phone, email, address))
    count += 1

# === Output Section ===
print("\n=== CONTACT DIRECTORY ===\n")

for i, (name, phone, email, address) in enumerate(contacts, start=1):
    print(f"CONTACT {i}:")
    print(f"Name:    {name}")
    print(f"Phone:   {phone}")
    print(f"Email:   {email}")
    print(f"Address: {address}\n")

print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {count}\n")

print("=== FORMATTED FOR PRINTING ===")
for name, phone, email, address in contacts:
    # Split name into first and last for formatted listing
    parts = name.split()
    if len(parts) >= 2:
        last = parts[-1]
        first = ' '.join(parts[:-1])
        formatted_name = f"{last}, {first}"
    else:
        formatted_name = name
    print(f"{formatted_name:<30}{phone:<20}{email}")
