# JoshuaEvans Assignment 6

This Python program cleans and formats messy contact information into a neat directory. It standardizes names, phone numbers, emails, and addresses using basic string methods — no functions used.
 What It Does

Reads contact info in this format:

name|phone|email|address


Cleans and formats each field:

Names: Proper capitalization

Phones: (XXX) XXX-XXXX format

Emails: Lowercase

Addresses: Title case and proper state abbreviation

Displays a clean directory and a summary.

 Example Output:
=== CONTACT DIRECTORY ===
Name:    John Doe
Phone:   (555) 123-4567
Email:   john@email.com
Address: 123 Main Street, Raleigh, NC 27601

=== DIRECTORY SUMMARY ===
Total contacts processed: 2

=== FORMATTED FOR PRINTING ===
Doe, John           (555) 123-4567      john@email.com

🧠 Key String Methods

.split() · .join() · .strip() · .title() · .upper() · .lower() · .replace() · .isdigit() · .isalpha()
