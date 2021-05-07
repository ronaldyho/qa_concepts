import grapheme as gr
import sys as sys
import json as json

f = open("testdata.json", "r")
t_emoji = json.loads(f.read())

print("Grapheme LEN |    LEN    |   LEN (UTF8)   | System Size in Bytes")


l1 = gr.length(x)
l2 = len(x)
l3 = len(x.encode("utf8"))
l4 = sys.getsizeof(x)

for key in t_emoji:

    x = t_emoji[key]
    print( key )
    print(  x, "\n", l1, "\t", l2, "\t", l3, "\t", l4, "\n" )
