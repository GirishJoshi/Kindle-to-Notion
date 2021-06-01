# splits kindle-clippings.md file into individual files for individual books.
# Used: https://elvisciotti.github.io/kindleparser/ to create .md form .txt

import re

filename = "kc.md"

sum = 0
with open(filename, "r") as f:
    data = f.read()
    # print("Here")
    # print(data)
    datalist = data.split("# ")
    datalist.pop(0)

    for e in datalist:

        title = e.split("\n", 1)[0]
        # print(title)

        content = e.replace(title, "")
        # print(content)

        if len(title) > 255:
            title = title[:250]

        title = re.sub("\W+", " ", title)
        title = title.rstrip()
        title = f"{title}.md"

        # print(title)

        # content = f"# {e}"
        # print(len(content))

        # print(content)
        # spath = os.path.join(path, title)
        # print(spath)
        if len(content) >= 1200:
            print(title)
            print(len(content))
            sum += 1
        """
        if len(content) > 1200:
            with open(title, "w") as fp:
                fp.write(content)
        """
# print(len(datalist))

# print(datalist[2])

print(f"Total Files: {sum}")
