# import os
# import random
# import textwrap
# from os import path


# current_dir = os.path.abspath(os.path.dirname(__file__))
# ascii_path = os.path.join(current_dir, "ascii-images")
# module_data = path.join(current_dir, "content")
# quotes_path = path.join(module_data, "quotes")


# if not os.path.exists(ascii_path):
#     print(f"Directory {ascii_path} does not exist. Please create it and add some text files.")
#     exit(1)


# try:
#     text_files = [f for f in os.listdir(ascii_path) if f.endswith(".txt")]
#     if not text_files:
#         print(f"Directory {ascii_path} does not contain any text files.")
#         exit(1)
# except PermissionError:
#     print(f"Permission denied to access directory {ascii_path}.")
#     exit(1)

# random_text_file = random.choice(text_files)
# random_text_path = os.path.join(ascii_path, random_text_file)

# def build_bubble(quote=""):
#     wrap_limit = 50
#     wrap_list = textwrap.wrap(quote, wrap_limit)

#     if len(wrap_list) == 1:
#         wrap_limit = len(wrap_list[0])

    
#     wrap_list = [" " + line + " " * (wrap_limit - len(line) + 1) + "|" for line in wrap_list]

#     bubble_top = "  " + "_" * (wrap_limit + 2)
#     bubble_middle = "\n".join([" |" + line + "|" for line in wrap_list])
#     bubble_bottom = "  " + "-" * (wrap_limit + 2)

#     return f"{bubble_top}\n{bubble_middle}\n{bubble_bottom}"

# def hello():
#     try:
#         with open(quotes_path, encoding='utf8') as quotes_file:
#             print(build_bubble(random.choice(quotes_file.readlines())))
#     except FileNotFoundError:
#         print(f"Quotes file not found at {quotes_path}.")
#         exit(1)
#     except Exception as e:
#         print(f"Error reading quotes file {quotes_path}: {e}")
#         exit(1)

#     try:
#         with open(random_text_path, 'r', encoding='utf8') as file:
#             text_content = file.read()
#             print(text_content)
#     except Exception as e:
#         print(f"Error reading text file {random_text_path}: {e}")
#         exit(1)

# if __name__ == "__main__":
#     hello()
import os
import random
import textwrap
from os import path

# Define paths
current_dir = os.path.abspath(os.path.dirname(__file__))
ascii_path = os.path.join(current_dir, "ascii-images")
module_data = path.join(current_dir, "content")
quotes_path = path.join(module_data, "quotes")

# Check if the ascii-images directory exists
if not os.path.exists(ascii_path):
    print(f"Directory {ascii_path} does not exist. Please create it and add some text files.")
    exit(1)

# Get list of text files in the ascii-images directory
try:
    text_files = [f for f in os.listdir(ascii_path) if f.endswith(".txt")]
    if not text_files:
        print(f"Directory {ascii_path} does not contain any text files.")
        exit(1)
except PermissionError:
    print(f"Permission denied to access directory {ascii_path}.")
    exit(1)

random_text_file = random.choice(text_files)
random_text_path = os.path.join(ascii_path, random_text_file)

def build_bubble(quote=""):
    wrap_limit = 50
    wrap_list = textwrap.wrap(quote, wrap_limit)

    if len(wrap_list) == 1:
        wrap_limit = len(wrap_list[0])

    wrap_list = [" " + line + " " * (wrap_limit - len(line) + 1) + "|" for line in wrap_list]

    bubble_top = "  " + "_" * (wrap_limit + 2)
    bubble_middle = "\n".join([" |" + line + "|" for line in wrap_list])
    bubble_bottom = "  " + "-" * (wrap_limit + 2)

    return f"{bubble_top}\n{bubble_middle}\n{bubble_bottom}"

def hello():
    # Read and print a random quote
    try:
        with open(quotes_path, encoding='utf8') as quotes_file:
            quote = random.choice(quotes_file.readlines()).strip()
            print(build_bubble(quote))
    except FileNotFoundError:
        print(f"Quotes file not found at {quotes_path}.")
        exit(1)
    except Exception as e:
        print(f"Error reading quotes file {quotes_path}: {e}")
        exit(1)

    # Read and print a random ASCII art text file
    try:
        with open(random_text_path, 'r', encoding='utf8') as file:
            text_content = file.read()
            print(text_content)
    except FileNotFoundError:
        print(f"Text file not found at {random_text_path}.")
        exit(1)
    except Exception as e:
        print(f"Error reading text file {random_text_path}: {e}")
        exit(1)

if __name__ == "__main__":
    hello()
