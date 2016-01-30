"""Opgave omtrek"""
"""Author: Philippe Asselbergh  Lars Veelaert  Jonas Van Reeth"""
"""Date:30/01/2016"""

"""Aantal testgevallen"""
n = int(raw_input())

"""Getallen inlezen"""
for j in range(n):
    """Aantal vluchten in testgeval"""
    aantalVluchten, aantalVliegtuigen = raw_input().rstrip().split( )
    vluchten = [[0 for x in range(2)] for x in range(int(aantalVluchten))]
    vliegtuigen = [[0 for x in range(2)] for x in range(int(aantalVliegtuigen))]
    for i in range(int(aantalVluchten)):
        vluchten[i][0], vluchten[i][1] = raw_input().rstrip().split( )
    for i in range(int(aantalVliegtuigen)):
        vliegtuigen[i][0], vliegtuigen[i][1] = raw_input().rstrip().split( )
    if int(aantalVluchten) > int(aantalVliegtuigen):
        print j+1, "geen oplossing"
    oplossing = False
    for i in range(int(aantalVluchten)):
        for j in range(int(aantalVliegtuigen)):
            if int(vliegtuigen[j][0]) > int(vluchten[i][0]) and int(vliegtuigen[j][1]) > int(vluchten[i][1]):
                oplossing = True
    if oplossing == False:
        print j+1, "geen oplossing"
