"""Opgave omtrek"""
"""Author: Philippe Asselbergh  Lars Veelaert  Jonas Van Reeth"""
"""Date:30/01/2016"""

"""Aantal testgevallen"""
n = int(raw_input())

"""Getallen inlezen"""
for j in range(n+1):
    """Aantal vluchten in testgeval"""
    aantalVluchten = int(raw_input())
    ts = [[0 for x in range(4)] for x in range(aantalRechthoek)]
    for i in range(aantalRechthoek):
        rechthoek=raw_input()
        ts[i] = rechthoek.split( )
    x = xComponentRechthoek(ts)
    y = yComponentRechthoek(ts)
    num_list = [[0 for z in range(y)] for z in range(x)]
    for i in range(aantalRechthoek):
        for j in range(int(ts[i][0]),int(ts[i][0])+int(ts[i][2])):
            for k in range(int(ts[i][1]),int(ts[i][1])+int(ts[i][3])):
                num_list[j][k] = 1

    """bereken omtrek"""
    om = berekenOmtrek(num_list)
    """bereken oppervlakte"""
    op = oppervlakte(num_list)

    """omtrek"""
    out1.append(om)
    """oppervlakte"""
    out2.append(op)

for x in range(n+1):
    """nummer _ oppervlakte _ omtrek"""
    print x+1, out2[x] , out1[x]
