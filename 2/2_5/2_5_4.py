R=hex(int(input()))
G=hex(int(input()))
B=hex(int(input()))
R=R[2:].rjust(2,'0').upper()
G=G[2:].rjust(2,'0').upper()
B=B[2:].rjust(2,'0').upper()
print("#"+R+G+B)