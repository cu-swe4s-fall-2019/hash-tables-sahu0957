import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(
        description="reads from hash_tables.py stdin to graphically show\
        hashing strategy efficiencies")
parser.add_argument("outfile",
            help="output png file", type=str)
parser.add_argument("x_label",
            help="label of the x axis", type=str)
parser.add_argument("y_label",
            help="label of the y axis", type=str)


args = parser.parse_args()

out_file = args.outfile
x_label = args.x_label
y_label = args.y_label

X = []
Y = []
i = 0


B = sys.stdin

try:
    for l in B:
        A = l.rstrip().split()
        if len(A) == 3:
            X.append(float(A[1]))
            Y.append(float(A[2]))
        elif len(A) == 2:
            X.append(float(i))
            Y.append(float(A[1]))
            i+=1
        else:
            sys.stderr.write("Stdin is the wrong dimension! Exiting...")
            sys.exit(1)

    width=3
    height=3
    fig = plt.figure(figsize=(width,height),dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.savefig(out_file, bbox_inches='tight')

except ValueError:
    # If the plot can't be created, we will print this message
    # and exit
    sys.stderr.write('Nonnumber entries in stdin! Exiting...')
    sys.exit(1)
