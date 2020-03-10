from math import sin, cos, sqrt, atan2, radians

def is_in_circle(lat1, lon1, lat2, lon2, radius):
    # R is approximate radius of earth in km
    R = 6373.0 
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    #Difference between the two lon's and lat's
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) #Great Circle fomula COPIED 
    distance = R * c
    if distance <= radius:
        #print('Co-ord is in the area')
        return True
    else:
        #print('Co-ord is outside the area')
        return False
