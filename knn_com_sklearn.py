import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def readTable():
    data = []
    df = pd.read_csv('./Iris.csv')
    for i in df.values:
        data.append(i)
    return data

def mountShapes(data):
    knownShape, unknownShapeResponse = train_test_split(data[1:], test_size=0.2)
    return knownShape, unknownShapeResponse

def knn(n_neighbors, knownShape, unknownShape):
    predicao = []
    for unknownItem in unknownShape:
        distances = []
        for knownItem in knownShape:
            v1, v2, v3, v4 = knownItem[1] - unknownItem[1], knownItem[2] - unknownItem[2], knownItem[3] - unknownItem[3], knownItem[4] - unknownItem[4]
            q1, q2, q3, q4 = v1 ** 2, v2 ** 2, v3 ** 2, v4 ** 2
            qSum = q1 + q2 + q3 + q4
            euclideanDistance = qSum ** (1 / 2)

            # print(f'desconhecido: {unknownItem}')
            # print(f'conhecido: {knownItem}')
            # print(f'distancia euclideana: {euclideanDistance}')
            distances.append([euclideanDistance, knownItem[5]])

        winners = sorted(distances, key=lambda x: x[0])[:n_neighbors]
        #print(winners)
    
        types = [winner[1] for winner in winners]
        resultado = 0
        tipo_vencedor = ""
        for i in types:
            if resultado > types.count(i):
                continue
            resultado = types.count(i)
            tipo_vencedor = i
            
        predicao.append(tipo_vencedor)
        
        #print(f'A espécie da planta No. {unknownItem[0]}  é: {tipo_vencedor}')
        
    return predicao


def main():
    
    vizinhos = int(input("Insira o numero de vizinhos"))
    for i in range(10):
        teste=[]
        
        data = readTable()
        knownShape, unknownShapeResponse = mountShapes(data)
        predicao = knn(vizinhos, knownShape, unknownShapeResponse)
        
        for i in unknownShapeResponse:
            teste.append(i[5])
        print(classification_report(teste, predicao))

if __name__ == "__main__":
    main()
