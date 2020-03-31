# geogdist.py
# Version 0.3

import math

def distance( latlngA, latlngB):
    '''
    distance( (latA,lngA), (latB,lngB) ) -> float (distance in km)

    Returns the approximate straight line distance between two nearby points
    on the surface
    of the Earth assuming a sphere. With the default value of R of 6371.009
    the distance will be in kilometers.
    See also: https://en.wikipedia.org/wiki/Geographical_distance
    Returns -1 if lat or lng co-ords are empty.

    '''
    if len(latlngA) != 2 or len(latlngB) != 2:
        d = -1
        return d
    
    
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)
    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R
    return d

#testing in geodist_test.py
