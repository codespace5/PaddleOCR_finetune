import os

# Define the folder containing the images and text files
folder_path = './train'

# Initialize a list to hold the pairs
data_pairs = []

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg'):
        # Construct the corresponding text file name
        text_filename = filename.replace('.jpg', '.txt')
        image_path = os.path.join(folder_path, filename)
        text_path = os.path.join(folder_path, text_filename)
        
        # Check if the text file exists
        if os.path.isfile(text_path):
            # Read the content of the text file
            with open(text_path, 'r', encoding='utf-8') as file:
                text_content = file.read().strip()
            
            # Append the pair to the list
            data_pairs.append((os.path.abspath(image_path), text_content))

# Define the output text file path
# output_text_path = os.path.join(folder_path, 'train.txt')
output_text_path = './train.txt'
# Write the pairs to the text file
with open(output_text_path, 'w', encoding='utf-8') as file:
    for image_path, text_content in data_pairs:
        file.write(f'{image_path}, {text_content}\n')

print(f"Text file has been created at {output_text_path}")
