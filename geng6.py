from hireg import gen_hireg
import sys

def gento(n):
    g6s = gen_hireg(n)
    f = open("graphs/kakan_n{}.g6".format(n), "w")
    for g6 in g6s:
        print(g6.decode(), file=f)

if len(sys.argv) != 2:
    print("Usage: python3 {} <n>".format(sys.argv[0]))
    print("  n : number of vertices")
else:
    gento(int(sys.argv[1]))
