# Python program to merge two files
data = data2 = ""

# Reading data from first file
with open("ko.md") as fp:
    data = fp.read()
with open("kp.md") as fp:
    data2 = fp.read()

# Merging two files into one another file
data += "\n"
data += data2

with open("kindleclippings.md", "w") as fp:
    fp.write(data)
