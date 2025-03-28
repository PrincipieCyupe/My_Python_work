# import the necessary libraries
import os
import string

# define a function to read the text files and if not found use default text taken from the text files manually

def read_and_process_the_files(filename, text):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        print(f"The file {filename} is found!")
    else:
        print(f"Warning: {filename} is not found! Using default text.")
        text = text
    return text.translate(str.maketrans("", "", string.punctuation)).lower().split()

# Store the contents of two essays essay1.txt and essay2.txt which will be used in case file are missing

text1 = "Programming is the backbone of software engineering, serving as the primary tool for transforming ideas into functional applications. It enables engineers to design, develop, and optimize software systems that solve real-world problems. Without programming, the theoretical aspects of software design would remain abstract and unusable. Mastery of programming languages allows engineers to implement algorithms, debug code, and ensure the efficiency of software. Furthermore, programming fosters creativity and innovation, as engineers can experiment with new solutions and technologies. In essence, programming is the bridge between concept and execution, making it indispensable in software engineering"
text2 = "Programming is a fundamental skill in software engineering, as it is the process through which software solutions are built and maintained. It allows engineers to create systems that automate tasks, improve productivity, and address complex challenges. By writing code, engineers can bring software designs to life, ensuring they meet user requirements and perform reliably. Additionally, programming encourages problem-solving and logical thinking, which are critical for optimizing software performance. As technology evolves, programming remains at the core of innovation, enabling engineers to adapt and develop cutting-edge applications. Thus, programming is not just a skill but a necessity in the field of software engineering"


words1 = read_and_process_the_files("essay1.txt", text1)
words2 = read_and_process_the_files("essay2.txt", text2)
# Counting the total numbers found from each text

counter1 = len(words1)
counter2 = len(words2)
print(f"The total number of words found in text1 is: {counter1} words")
print(f"The total number of words found in text2 is: {counter2} words")

# Looking for the common words, count, and list  them

common_words = set(words1) & set(words2)
print(f"The total number of common words found are: {len(common_words)} words.\nThose are:\n {common_words}")


# Finding the unique words from both essays
union = set(words1) | set(words2)

print(f"\nTHE UNIQUE WORDS ARE:\n {union}\n\n")

# Calculate the percentage of plagiarism
    # Count the common words in both essays (Intersection words)
    # Count the union words

Plag_results = round(((len(common_words)/len(union))*100), 2)
unique_sent = round((100 - Plag_results), 2)
if Plag_results > 49:
    print(f"There is a plagiarism of {Plag_results}%\n")

else:
    print("No plagiarism found")


print(f"{Plag_results}% of plagiarized sentences.\n{unique_sent}% of unique sentences.\n") 

# Create a function to allow user enter a word for checking if it is found in another essay

def search_for_a_word():
    user_input = input("Write any word here to check for similarties: ")
    if user_input in words1 or user_input in words2:
        print(f"{user_input} is found in one of the essays\n")
        return True
    else:
        print(f"{user_input} is not found\n")
        return False
search_for_a_word()
