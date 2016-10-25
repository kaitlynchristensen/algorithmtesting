import random
import math

tileCount = 3
boardParts = []

for i in range(tileCount):
  boardParts.append([])
  boardParts[i] = []
  for j in range(tileCount):
    boardParts[i].append({'x': (tileCount - 1) - i, 'y': (tileCount - 1) - j})

emptyLoc = {'x': boardParts[tileCount - 1][tileCount - 1]['x'], 'y': boardParts[tileCount - 1][tileCount - 1]['x']}

solved = False;

def initTiles():
    i = tileCount * tileCount - 1
    while (i > 0):
      j = math.floor(random.random() * i)
      xi = i % tileCount
      yi = math.floor(i / tileCount)
      xj = j % tileCount
      yj = math.floor(j / tileCount)
      swapTiles(xi, yi, xj, yj)
      i = i - 1

def swapTiles(i, j, k, l):
  temp = boardParts[i][j]
  boardParts[i][j] = boardParts[k][l]
  boardParts[k][l] = temp

def countInversions(i, j):
  inversions = 0;
  tileNum = j * tileCount + i;
  lastTile = tileCount * tileCount;
  tileValue = boardParts[i][j]['y'] * tileCount + boardParts[i][j]['x'];
  for q in range(tileNum + 1, lastTile):
    k = q % tileCount;
    l = math.floor(q / tileCount);

    compValue = boardParts[k][l]['y'] * tileCount + boardParts[k][l]['x']
    if tileValue > compValue and tileValue != (lastTile - 1):
      inversions = inversions + 1

  return inversions

def sumInversions():
  inversions = 0;
  for j in range(tileCount):
    for i in range(tileCount):
      inversions += countInversions(i, j)
  return inversions


def isSolvable(width, height, emptyRow):
  if (width % 2 == 1):
    return (sumInversions() % 2 == 0)
  else:
    return ((sumInversions() + height - emptyRow) % 2 == 0)

initTiles()
if (not isSolvable(tileCount, tileCount, emptyLoc['y'] + 1)):
  if (emptyLoc['y'] == 0 and emptyLoc['y'] <= 1):
    swapTiles(tileCount - 2, tileCount - 1, tileCount - 1, tileCount - 1);
  else:
    swapTiles(0, 0, 1, 0);

result = []
count = -1
found = False
for i in range(tileCount):
  result.append([])
  result[i] = []
  for j in range(tileCount): # search for item with value (i,j) to add to list
    found = False
    count = -1
    for x in range(tileCount):
      if found == True:
        break
      for y in range(tileCount):
        if boardParts[x][y]['x'] == i and boardParts[x][y]['y'] == j:
          result[i].append(count)
          found = True
          break
        count = count + 1

print (result)