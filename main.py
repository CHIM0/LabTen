import matplotlib.pyplot as plt
import  re
import numpy as np

def read_and_draw(weights):
    the_file_path="testSet_Logistic.txt"
    the_file=open(the_file_path,encoding="utf-8")
    seq = re.compile("\s+")
    result=[]

    for line in the_file:
        one_line = seq.split(line.strip())
        result.append(one_line)

    the_file.close()

    x=[]
    y=[]
    kind=[]
    for everyone in result:
        x.append(float(everyone[0]))
        y.append(float(everyone[1]))
        kind.append([int(everyone[2]),0,0])

    plt.scatter(x[:],y[:],marker='o',c=kind)

    X = np.arange(min(x),max(x),0.001)
    Y = (-weights[0] - weights[1] * X) / weights[2]

    plt.plot(X,Y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Logistic Analyse")
    plt.show()

weights=[4.12,0.48,-0.6]
read_and_draw(weights)

