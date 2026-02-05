contacts = {
    "Hamsa": "123-456-7890",
    "Bindhu": "987-654-3210",
    "Deepthi": "555-666-7777"
}
contacts["Gowthami"] = "222-333-4444"        
contacts["Hamsa"] = "111-222-3333"       
existing_contact = contacts.get("Bindhu", "Contact not found")
non_existing_contact = contacts.get("Varsha", "Contact not found")
print("Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
print("\nSafe Lookups:")
print(f"Bindhu: {existing_contact}")
print(f"Varsha: {non_existing_contact}")

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("Is ID05 in unique_users?", "ID05" in unique_users)
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))
print("Unique User IDs:", unique_users)

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique to Friend A:", unique_to_a)