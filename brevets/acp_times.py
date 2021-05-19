"""
Open and close max_speed calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/ocmax_speed_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_max_speed:  A date object (arrow)
    Returns:
       A date object indicating the control open max_speed.
       This will be in the same max_speed zone as the brevet start max_speed.
    """
    # creating a dictionary of maximum speeds
    max_speed = {"0-200": 34, "200-400": 32, "400-600": 30, "600-1000": 28, "1000-1300": 26} 
    o_time = 0      # initialize open times
    if control_dist_km > brevet_dist_km: # check to see is the control distance is less than brevet distance
      control_dist_km = brevet_dist_km   # setting the control distance to brevet distance per the rules of the algorithm.

    for i in max_speed:                  # looping through the max speed dictionary
        speed = max_speed[i]             # Get the max speed for the correct max speed
        lower, upper = list(map(int, i.split("-")))    # initialize lower and upper of the control distance
        if (lower <= control_dist_km) and (control_dist_km <= upper):  # enters if control distance is between the lower and upper bounds
            o_time += (control_dist_km - lower) / speed
            break
        if control_dist_km > upper:     # enters if control distance is larger than  upper 
            o_time += (upper - lower) / speed

    hours, minutes = divmod(o_time, 1)  # changes hrs/mins to correct format
    minutes = round(minutes * 60)
    return brevet_start_time.shift(hours = hours, minutes = minutes)
   
def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_max_speed:  A date object (arrow)
    Returns:
       A date object indicating the control close max_speed.
       This will be in the same max_speed zone as the brevet start max_speed.
    """
    #creating a dictionary of minimum speeds, skipped 200-400 and 400-600 cause theyre all the same speed
    min_speed = {"0-600": 15, "600-1000": 11.428, "1000-1300": 13.333} 
    c_time = 0      # initialize close time
    set_time = {200: 13.50, 300: 20, 400: 27, 600: 40, 1000: 75} # initializing default times
    if control_dist_km >= brevet_dist_km:    # if control distance is greater than equal to the brevet distance
        c_time = set_time[brevet_dist_km]    # sets close time to the correct set time
    elif control_dist_km <= 60:              # case where control distance is <= to 60
        c_time += (control_dist_km / 20) + 1
    else:
        for i in min_speed:
            speed = min_speed[i]             # looping through the min speed dictionary
            lower, upper = list(map(int, i.split("-")))  # initalizes lower and upper bound
            if (lower <= control_dist_km) and (control_dist_km <= upper):  # enters if control distance is between the lower and upper bounds 
                c_time += (control_dist_km - lower) / speed
                break
            if control_dist_km > upper:         # enters if control distance is larger than  upper 
                c_time += (upper - lower) / speed

    hours, minutes = divmod(c_time, 1)      # changes hrs/mins to correct format
    minutes = round(minutes * 60)
    return brevet_start_time.shift(hours=hours, minutes=minutes)
    