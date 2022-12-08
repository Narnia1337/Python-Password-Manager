import random
import string

# create a function to generate a random password
def generate_password():
    # generate a random string of lowercase and uppercase letters and digits
    password = "".join(random.choices(string.ascii_letters + string.digits, k=19))
    return password

# create a dictionary to store the website names and generated passwords
passwords = {}

# define the websites for which to generate passwords
# to add more websites, just add in a comma after the closed quotes and put the website in quotes

website_names = ["Facebook", "Twitter", "LinkedIn", "GitHub", "Roblox", "Discord", "Gmail/Google", "TikTok"]

# generate a password for each website
for website in website_names:
    password = generate_password()
    # store the website and generated password in the dictionary
    passwords[website] = password

# print the generated passwords
print(passwords)

# write the passwords to a file
with open("generated_passwords.txt", "w") as f:
    for website, password in passwords.items():
        f.write(f"{website}: {password}\n")
    
