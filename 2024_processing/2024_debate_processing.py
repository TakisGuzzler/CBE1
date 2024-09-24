# Define the input filename
input_filename = '2024_presidential_debate.txt'

# Initialize empty lists for each participant
vp_lines = []
president_lines = []
moderator_lines = []

# Read the debate text from the file with UTF-8 encoding
with open(input_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Loop through each line and classify based on the speaker
current_speaker = None  # Keep track of the current speaker

for line in lines:
    stripped_line = line.strip()  # Remove leading/trailing whitespace
    
    # Identify speakers
    if stripped_line.startswith("HARRIS:"):
        current_speaker = 'VP'
        vp_lines.append(stripped_line.replace("HARRIS:", "").strip())
    elif stripped_line.startswith("TRUMP:"):
        current_speaker = 'PRESIDENT'
        president_lines.append(stripped_line.replace("TRUMP:", "").strip())
    elif stripped_line.startswith("MUIR:") or stripped_line.startswith("DAVIS:"):
        current_speaker = 'MODERATOR'
        moderator_lines.append(stripped_line.replace("MUIR:", "").replace("DAVIS:", "").strip())
    elif current_speaker:  # If there's a current speaker, add the line to their dialogue
        if current_speaker == 'VP':
            vp_lines.append(stripped_line)
        elif current_speaker == 'PRESIDENT':
            president_lines.append(stripped_line)
        elif current_speaker == 'MODERATOR':
            moderator_lines.append(stripped_line)

# Write Vice President's lines to a file
with open('vp_harris.txt', 'w', encoding='utf-8') as vp_file:
    vp_file.write("\n".join(vp_lines))

# Write President's lines to a file
with open('president_trump.txt', 'w', encoding='utf-8') as president_file:
    president_file.write("\n".join(president_lines))

# Write Moderators' lines to a file
with open('moderators.txt', 'w', encoding='utf-8') as moderator_file:
    moderator_file.write("\n".join(moderator_lines))

print("Debate lines have been written to separate text files for the Vice President, President, and Moderators.")
