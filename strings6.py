text = """Hello" it's my favorite word."""

print(text.split('\''))


commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300"""

lines = commit.split("\n")

commit_id = lines[0].split(" ")[1]

print(commit_id)

a1 = lines[1].find(":")
a2 = lines[1].find("<")

print(lines[1][a1:a2].strip(": "), commit_id)
