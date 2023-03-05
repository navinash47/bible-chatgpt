bible_path = "bible.txt"
bible_split_dir = "bible"

count = 0

with open(bible_path, "r") as f:
    while True:
        count += 1
        # Get next line from file
        line = f.readline()
        tag = line.split(":")[0]
        if len(tag) >= 2:
            with open("bible/{}.txt".format(tag), "a") as wf:
                wf.write(line)

        # if line is empty
        # end of file is reached
        if not line:
            break
