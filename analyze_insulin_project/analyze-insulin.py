import re

# Read the content from preproinsulin-seq.txt
with open("preproinsulin-seq.txt", "r") as file:
    content = file.read()

# Use regex to extract the amino acid sequence
match = re.search(r"ORIGIN\s*([\s\S]+?)\d*//", content)

if match:
    # Get the cleaned content (amino acid sequence)
    cleaned_content = re.sub(r"[\n\r\s\d\/]+", "", match.group(1))

    # Print the cleaned content to check
    print("Cleaned content:", cleaned_content)

    # Check the length of the cleaned content
    if len(cleaned_content) == 110:
        # Write the cleaned content to preproinsulin-seq-clean.txt
        with open("preproinsulin-seq-clean.txt", "w") as cleaned_file:
            cleaned_file.write(cleaned_content)
        print("Cleaning successful. Check preproinsulin-seq-clean.txt.")

        # Save specific ranges to different files
        ranges = [(1, 24, "lsinsulin-seq-clean.txt"),
                  (25, 54, "binsulin-seq-clean.txt"),
                  (55, 89, "cinsulin-seq-clean.txt"),
                  (90, 110, "ainsulin-seq-clean.txt")]

        for start, end, filename in ranges:
            subsequence = cleaned_content[start - 1:end]  # Adjust indices to 0-based
            with open(filename, "w") as subseq_file:
                subseq_file.write(subsequence)

            print(f"Saved amino acids {start}-{end} to {filename}.")
            print(f"Verify that {filename} has {end - start + 1} characters.")
    else:
        print("Cleaning unsuccessful. The cleaned content doesn't have 110 characters.")
        print("Actual length:", len(cleaned_content))
else:
    print("Error: Amino acid sequence not found.")
