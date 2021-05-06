import grapheme as gr
import sys as sys
import json as json

f = open("testdata.json", "r")
t_emoji = json.loads(f.read())

print("Grapheme LEN |    LEN    |   LEN (UTF8)   | System Size in Bytes")

for key in t_emoji:

    x = t_emoji[key]
    print(  key, "\n", gr.length(x), "\t", len(x), "\t", len(x.encode("utf8")), "\t", sys.getsizeof(x), "\n" )
