import os

# Define the parent folder path
parent_folder = r"C:\Users\r14ale\Desktop\Scrapping_ABB"

# Define the subfolder name
subfolder_name = "subfolder"

# Create the parent folder if it doesn't exist
if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)

# Create the subfolder inside the parent folder
subfolder_path = os.path.join(parent_folder, subfolder_name)
os.mkdir(subfolder_path)

# Print a success message
print(f"Created subfolder '{subfolder_name}' inside '{parent_folder}'.")
