"""Opgave omtrek"""
"""Author: Philippe Asselbergh  Lars Veelaert  Jonas Van Reeth"""
"""Date:30/01/2016"""

"""Aantal testgevallen"""
n = int(raw_input())

"""Getallen inlezen"""
for j in range(n+1):
    """Aantal vluchten in testgeval"""
    aantalVluchten, aantalVliegtuigen = raw_input().rstrip().split( )
    vluchten = [[0 for x in range(2)] for x in range(int(aantalVluchten))]
    vliegtuigen = [[0 for x in range(2)] for x in range(int(aantalVliegtuigen))]
    for i in range(int(aantalVluchten)):
        vluchten[i][0], vluchten[i][1] = raw_input().rstrip().split( )
    for i in range(int(aantalVliegtuigen)):
        print 1
