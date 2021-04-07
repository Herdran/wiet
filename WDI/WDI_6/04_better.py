def func(x, y, cnt):
  T[x][y] = cnt
  if cnt == target_cnt:
    return True
  else:
    for v in vectors:
      _x = x + v[0]
      _y = y + v[1]
      if 0 <= _x and _x < N and 0 <= _y and _y < N:
        if T[_x][_y] == 0:
          if func(_x, _y, cnt+1):
            return True

    T[x][y] = 0
    return False

N = int(input())
T = [[0 for _ in range(N)] for _ in range(N)]
target_cnt = N*N
vectors = ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1))

print(func(0, 4, 1))

for r in T:
  print(r)