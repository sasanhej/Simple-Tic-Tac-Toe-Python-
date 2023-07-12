import string

wc=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
x='X'
o='O'
xwin=False
owin=False
inp="_________"
c=[x for x in inp]
print("---------")
print("| {} {} {} |".format(c[0],c[1],c[2]))
print("| {} {} {} |".format(c[3],c[4],c[5]))
print("| {} {} {} |".format(c[6],c[7],c[8]))
print("---------")

while True:
     while True:
          np = input().split()
          if np[0] not in string.digits or np[1] not in string.digits:
               print("You should enter numbers!")
          elif np[0] not in '123' or np[1] not in '123':
               print("Coordinates should be from 1 to 3!")
          elif c[(int(np[0]) - 1) * 3 + int(np[1]) - 1] != '_':
               print("This cell is occupied! Choose another one!")
          else:
               break
     c[(int(np[0]) - 1) * 3 + int(np[1]) - 1] = 'X'
     print("---------")
     print("| {} {} {} |".format(c[0],c[1],c[2]))
     print("| {} {} {} |".format(c[3],c[4],c[5]))
     print("| {} {} {} |".format(c[6],c[7],c[8]))
     print("---------")
     for i in range(8):
          if c[wc[i][0]]==x and c[wc[i][1]]==x and c[wc[i][2]]==x:
               xwin=True
          if c[wc[i][0]]==o and c[wc[i][1]]==o and c[wc[i][2]]==o:
               owin=True
     _c=c.count('_')
     if xwin==False and owin==False and _c==0:
          print("Draw")
          break
     if xwin==True and owin==False:
          print("X wins")
          break
     if xwin==False and owin==True:
          print("O wins")
          break
