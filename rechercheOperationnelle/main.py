import csv

def read_file(file_name):
    file = open(file_name, "r")
    array = []
    Wmax = file.readline().split()[1]
    for line in file:
            array.append(line.split()[1:])
    return array,Wmax

def triP1(array):
    print(sorted(array,key=lambda x: int(x[1])))
    return sorted(array,key=lambda x: int(x[1]))

def triP2(array):
    print(sorted(array,key=lambda x: int(x[1]),reverse=True))
    return sorted(array,key=lambda x: int(x[1]),reverse=True)

def triS1(array):
    print(sorted(array,key=lambda x: int(x[0])))
    return sorted(array,key=lambda x: int(x[0]))

def triS2(array):
    print(sorted(array,key=lambda x: int(x[0]),reverse=True))
    return sorted(array,key=lambda x: int(x[0]),reverse=True)

def glouton_tri(array,Wmax,tri):
    array = tri(array)
    P_total = 0
    score_total = 0
    x = []
    for i in range(len(array)):
        if int(array[i][0]) + P_total <= int(Wmax):
            x.append(1)
            P_total += int(array[i][0])
            score_total += int(array[i][1])
        else:
            x.append(0)
    return score_total,P_total

def test(array,Wmax,tri):
    score_total,P_total = glouton_tri(array,Wmax,tri)
    return score_total,P_total

def main(filename):
    array,Wmax = read_file(filename)

    score_totalP1,P_totalP1 = test(array,Wmax,triP1)
    score_totalP2,P_totalP2 = test(array,Wmax,triP2)
    score_totalS1,P_totalS1 = test(array,Wmax,triS1)
    score_totalS2,P_totalS2 = test(array,Wmax,triS2)
    return score_totalP1,P_totalP1,score_totalP2,P_totalP2,score_totalS1,P_totalS1,score_totalS2,P_totalS2,Wmax

instance = [
'inst4obj.txt',
'inst5obj.txt',
'inst10obj.txt',
'inst20obj.txt',
'inst35obj.txt',
'inst100obj.txt',
]

if __name__ == "__main__":
    array = []
    for instance_name in instance:
        score_totalP1,P_totalP1,score_totalP2,P_totalP2,score_totalS1,P_totalS1,score_totalS2,P_totalS2,Wmax = main(instance_name)
        array.append ([score_totalP1,P_totalP1,score_totalP2,P_totalP2,score_totalS1,P_totalS1,score_totalS2,P_totalS2,Wmax])

    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer. writerow(['instance','score_totalP1','P_totalP1','score_totalP2','P_totalP2','score_totalS1','P_totalS1','score_totalS2','P_totalS2','Wmax'])
        for i in range(len(array)):
            writer. writerow([instance[i],array[i][0],array[i][1],array[i][2],array[i][3],array[i][4],array[i][5],array[i][6],array[i][7],array[i][8]])
