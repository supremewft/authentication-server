import secrets
import string
import json

def generate_key():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(16))

# Get user full name and subscription type
full_name = input("User full name: ")

# Ensure the full name is not empty
if len(full_name.strip()) == 0:
    raise ValueError("User name must not be empty.")

subscription_type = input("Subscription type: ")

validsubs = ['Speed','Silver','Gold','Platinum']
if (subscription_type not in validsubs):
    raise ValueError("Typo on key type")
identitiesquestion = input("Identities number: ")

access_token_chars = []

i = 0
if identitiesquestion == 1:
    access_token_chars.append(input("First 10 letters/numbers of access token: "))
else:
    access_token_chars = []
    while i<int(identitiesquestion):
        access_token_chars.append(input(f"10 character of identity number {i+1}: "))
        i += 1
    


# Generate a random key
key = generate_key()

# Create an entry for this key
key_entry = {
    "key": key,
    "username": full_name,
    "subscription_type": subscription_type,
    "access_token_chars": access_token_chars
}

# Append the new key entry to a JSON file
json_filename = 'keys.json'
try:
    with open(json_filename, 'r') as keyfile:
        key_data = json.load(keyfile)
except FileNotFoundError:
    key_data = []

key_data.append(key_entry)

with open(json_filename, 'w') as keyfile:
    json.dump(key_data, keyfile, indent=4)

print(f"Generated and saved key: {key}")