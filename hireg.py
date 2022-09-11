import networkx as nx
import matplotlib.pyplot as plt
import sys
import subprocess

def geng(n, arguments=b""):
    cmd = subprocess.run(["geng",str(n)]+arguments.split(),capture_output = True)
    g6s = cmd.stdout.split(b"\n")
    if g6s[-1] == b"":
        g6s = g6s[:-1]
    return g6s

def is_hireg(G):
    H = nx.complement(G)
    if 0 in dict(G.degree()).values():
        return False
    for e in H.edges():
        if G.degree(e[0]) == G.degree(e[1]):
            return False
    return True

def gen_hireg(n, arguments=b""):
    lst = []
    for g6 in geng(n, arguments):
        G = nx.from_graph6_bytes(g6)
        if is_hireg(G):
            lst += [g6]
    return lst
