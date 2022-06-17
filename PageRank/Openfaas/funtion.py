import sys
import igraph


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return int(buf)


if(__name__ == "__main__"):
    size = get_stdin()

    graph = igraph.Graph.Barabasi(size, 10)

    result = graph.pagerank()

    print(result)
