import pandas as pd

def readTable():
  data = []
  df = pd.read_csv('./Iris.csv')
  for i in df.values:
    data.append(i)
  return data

def mountShapes(data):
  unknownShapeResponse = data[5:150:20]
  unknownShape = []
  for i in unknownShapeResponse:
    unknownShape.append(i[:5])
  knownShape = data[1:140:15]
  return knownShape, unknownShape, unknownShapeResponse

def knn(n_neighbors, knownShape, unknownShape ):
  for unknownItem in unknownShape:
    distances = []
    for knownItem in knownShape:
      # print('init------------')
      v1, v2, v3, v4 = knownItem[1] - unknownItem[1], knownItem[2] - unknownItem[2], knownItem[3] - unknownItem[3], knownItem[4] - unknownItem[4] 
      # print(v1, v2, v3, v4)
      q1, q2, q3, q4 = v1**2, v2**2, v3**2, v4**2
      # print(q1, q2, q3, q4)
      qSum = q1 + q2 + q3 + q4
      # print(qSum)
      euclideanDistance = qSum**(1/2)
      # print(f'desconhecido: {unknownItem}')
      # print(f'conhecido: {knownItem}')
      # print(f'distancia euclideana: {euclideanDistance}')
      distances.append([euclideanDistance, knownItem[5]])
    # print(f'---------{unknownItem}----------')
    # for i in distances:
    #   print(i)
    winners = sorted(distances, key=lambda x: x[0])[:n_neighbors]
     
    # print(winners)
    

def main():
  data = readTable()
  knownShape, unknownShape, unknownShapeResponse = mountShapes(data)
  knn(3, knownShape, unknownShape)

if __name__ == "__main__":
  main()