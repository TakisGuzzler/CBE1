# Define the input filename
input_filename = 'obama_debate.txt'

# Initialize empty lists for each speaker
romney_lines = []
obama_lines = []
moderator_lines = []

# Read the debate text from the file with UTF-8 encoding
with open(input_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Loop through each line and classify based on the speaker
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespace
    if line.startswith("ROMNEY:"):
        romney_lines.append(line.replace("ROMNEY:", "").strip())
    elif line.startswith("OBAMA:"):
        obama_lines.append(line.replace("OBAMA:", "").strip())
    elif line.startswith("SCHIEFFER:"):
        moderator_lines.append(line.replace("SCHIEFFER:", "").strip())

# Write Romney's lines to a file
with open('romney.txt', 'w', encoding='utf-8') as romney_file:
    romney_file.write("\n".join(romney_lines))

# Write Obama's lines to a file
with open('obama.txt', 'w', encoding='utf-8') as obama_file:
    obama_file.write("\n".join(obama_lines))

# Write Moderator's lines to a file
with open('moderator.txt', 'w', encoding='utf-8') as moderator_file:
    moderator_file.write("\n".join(moderator_lines))

print("Debate lines have been written to separate text files.")
