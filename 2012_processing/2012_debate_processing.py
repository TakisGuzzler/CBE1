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
current_speaker = None  # Keep track of the current speaker

for line in lines:
    stripped_line = line.strip()  # Remove leading/trailing whitespace
    
    if stripped_line.startswith("ROMNEY:"):
        current_speaker = 'ROMNEY'
        romney_lines.append(stripped_line.replace("ROMNEY:", "").strip())
    elif stripped_line.startswith("OBAMA:"):
        current_speaker = 'OBAMA'
        obama_lines.append(stripped_line.replace("OBAMA:", "").strip())
    elif stripped_line.startswith("SCHIEFFER:"):
        current_speaker = 'SCHIEFFER'
        moderator_lines.append(stripped_line.replace("SCHIEFFER:", "").strip())
    elif current_speaker:  # If there's a current speaker, add the line to their dialogue
        if current_speaker == 'ROMNEY':
            romney_lines.append(stripped_line)
        elif current_speaker == 'OBAMA':
            obama_lines.append(stripped_line)
        elif current_speaker == 'SCHIEFFER':
            moderator_lines.append(stripped_line)

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
