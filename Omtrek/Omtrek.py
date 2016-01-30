"""Opgave omtrek"""
"""Author: Philippe Asselbergh, Lars Veelaert, Jonas van Reeth"""
"""Date:30/01/2016"""

def berekenOmtrek (grid_array):
    max_x =len(grid_array) -1
    max_y =len(grid_array[0]) -1
        
    omtrek = 0
    
    x = 0
    
    while x <= max_x +1:
        y = 0
        while y <= max_y +1:
            ###
            
            if x == 0:
                xp = 0
            else:
                if y != max_y+1:
                    xp = grid_array[x-1][y]
                else:
                    xp = 0
            if y == 0:
                yp = 0
            else:
                if x != max_x +1:
                    yp = grid_array[x][y-1]
                else:
                    yp = 0
            if x == max_x+1:
                a = 0
                
            elif y == max_y +1:
                a = 0
            else:
                a = grid_array[x][y]
                            
            ## a en xp en yp
            if a != xp:
                omtrek = omtrek +1
            if a != yp:
                omtrek = omtrek +1
            
            ###
            y = y + 1
        x = x +1
    return omtrek

def oppervlakte(n):
    opp=0
    maxX= len(n)
    maxY= len(n[0])
    for x in range(maxX):
        for y in range(maxY):
            opp = opp + n[x][y]
    return opp

def xComponentRechthoek(ts):
    maxX=0
    for i in range(len(ts)):
        maxX=max(int(ts[i][0])+int(ts[i][2]),maxX)
    return maxX

def yComponentRechthoek(ts):
    maxY=0
    for i in range(len(ts)):
        maxY=max(int(ts[i][1])+int(ts[i][3]),maxY)
    return maxY

"""omtrek"""
out1=[]
"""oppervlakte"""
out2=[]
"""Aantal testgevallen"""
n = int(raw_input(""))

"""Getallen inlezen"""
for j in range(n+1):
    """Aantal rechthoeken in testgeval"""
    aantalRechthoek = int(raw_input(""))
    ts = [[0 for x in range(4)] for x in range(aantalRechthoek)]
    for i in range(aantalRechthoek):
        rechthoek=raw_input("")
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
    print x+1, out2[x], out1[x]
