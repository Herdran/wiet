def even_digits_in_base_5(tab, n):
  for x in range(n):
    for y in range(n):
      cnt = 0
      if tab[x][y] == 0:
        cnt = 1
      else:
        while tab[x][y] > 0:
          if (tab[x][y]%5)%2 == 0:
            cnt += 1 
          tab[x][y] //= 5
      tab[x][y] = cnt


tab1 = [[2, 2], [2, 2]]
tab2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
n1 = len(tab1)
n2 = len(tab2)
even_digits_in_base_5(tab1, n1)
even_digits_in_base_5(tab2, n2)

res = False
for x2 in range(-n1+1, n2):
  for y2 in range(-n1+1, n2):
    cnt = 0
    field_cnt = 0
    for x1 in range(n1):
      for y1 in range(n1):
        _x2 = x2 + x1
        _y2 = y2 + y1
        if 0 <= _x2 and _x2 < n2 and 0 <= _y2 and _y2 < n2:
          field_cnt += 1
          if tab1[x1][y1] == tab2[_x2][_y2]:
            cnt += 1

    if cnt/field_cnt >= 0.33:
      res = True

print(res)