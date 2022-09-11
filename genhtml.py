from hireg import gen_hireg
import networkx as nx
import matplotlib.pyplot as plt

def pprops(G, g6, f):
    print("<b>Graph6:</b> {} <br/>".format(g6.decode()), file=f)
    degree_sequence = sorted([d for n, d in G.degree()])
    print("<b>Degree sequence:</b> {} <br/>".format(degree_sequence), file=f)

def cimage(G, i):
    n = G.order()
    plt.clf()
    nx.draw(G)
    plt.savefig("html/graph_{}_{}.png".format(n,i))

def create_html_n(n, g6s):
    f = open("html/graphs_{}.html".format(n), "w")
    print("<html>", file=f)
    print("  <body>", file=f)
    for i in range(len(g6s)):
        G = nx.from_graph6_bytes(g6s[i])
        if n < 9:
            print("    <img src=\"graph_{}_{}.png\"/> <br/>".format(n, i), file=f)
            cimage(G, i)
        pprops(G, g6s[i], f)
        if i != len(g6s)-1:
            print("    <hr/>", file=f)
    print("  </body>", file=f)
    print("</html>", file=f)

def genall(s):
    f = open("html/index.html", "w")
    print("<html>", file=f)
    print("  <body>", file=f)
    print("  Index of Kakan graphs: <br/><br/>", file=f)
    for n in s:
        g6s = gen_hireg(n)
        create_html_n(n, g6s)
        number_of = len(g6s)
        print("    <a href=\"graphs_{}.html\">n = {}</a>".format(n,n), file=f, end=None)
        if number_of == 1:
            print(" ({} graph)<br/>".format(number_of), file=f)
        else:
            print(" ({} graphs)<br/>".format(number_of), file=f)
    print("    <br/><br/>", file=f)
    print("<b>Definition:</b> A graph G is a <i>Kakan graph</i> if it (i) contains no vertices of degree 0, and (ii) no pair of non-adjacent vertices in G have the same degree.", file=f)
    print("  </body>", file=f)
    print("</html>", file=f)

genall(range(2,10))
