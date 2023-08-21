from os import listdir, mkdir
from os.path import isfile, join, splitext
import re
import urllib3

path = "content/podcasts"

files = [f for f in listdir(path) if isfile(join(path, f))]


for file in files:
    filename = f"{splitext(file)[0]}.mp3"
    f = open(f"content/podcasts/{file}", "r")
    file_content = f.read()
    f.close()
    print("Original:\n")
    print(file_content)
    print("\n")
    fw = open(f"content/podcasts/{file}", "w")
    writeback = re.sub("//media", "http://media", file_content)
    print(writeback + "\n")
    fw.write(writeback)
    fw.close()