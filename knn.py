import csv

def readTable():
  data = []
  with open('Iris.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        data.append(line)
  return data

def mountShapes(data):
  print("Escolhe os 80% conhecidos")

def knn(n_neighbors, knownShape, unknownShape ):
  print("teste")

def main():
  data = readTable()
  for i in data:
    print(i)
  # knownShape, unknownShape = mountShapes(data)
  # knn(5, knownShape, unknownShape)

if __name__ == "__main__":
  main()