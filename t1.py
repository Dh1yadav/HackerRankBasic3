# Enter your code here. Read input from STDIN. Print output to STDOUT

import math as mth

AB = int(input())
BC = int(input())


m = mth.sqrt(AB**2+BC**2)
theta = mth.acos(BC/m )

print(round(mth.degrees(theta)),'\u00b0',sep="")
