# 플로이드 워샬
def solution(n, signs):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if signs[i][k] == 1 and signs[k][j] == 1:
          signs[i][j] = 1
  return signs
