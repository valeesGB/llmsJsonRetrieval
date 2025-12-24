#just a simple script to download images from URLs listed in a text file
import requests
import os

# Name of the file containing the links
file_path = 'resume_image_filenames_skipped_files.txt'
# Folder to save images
save_folder = 'skipped_resume_image1'

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

try:
    with open(file_path, 'r') as file:
        links = file.readlines()

    for link in links:
        url = link.strip()  # Remove whitespace/newlines
        
        if not url:
            continue

        # Extract filename from URL (e.g., "o2bu86se8x8d1.jpeg")
        filename = os.path.join(save_folder, url.split("/")[-1])

        print(f"Downloading: {filename}...")

        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
            else:
                print(f"Failed to download {url} (Status code: {response.status_code})")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    print("All done!")

except FileNotFoundError:
    print(f"Could not find the file: {file_path}")