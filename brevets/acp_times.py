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

max_speed = {"0-200": 34, "200-400": 32, "400-600": 30, "600-1000": 28, "1000-1300": 26}
min_speed = {"0-600": 15, "600-1000": 11.428, "1000-1300": 13.333}

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

    o_time = 0
    if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km

    for i in max_speed:
        speed = max_speed[i]
        low, high = list(map(int, i.split("-")))
        if low <= control_dist_km <= high:
            o_time += (control_dist_km - low) / speed
            break
        if control_dist_km > high:
            o_time += (high - low) / speed

    hours, minutes = divmod(o_time, 1)
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

    c_time = 0
    set_time = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75, 1200: 90}
    if control_dist_km >= brevet_dist_km:
        c_time = set_time[brevet_dist_km]
    elif control_dist_km <= 60:
        c_time += (control_dist_km / 20) + 1
    else:
        for i in min_speed:
            speed = min_speed[i]
            low, high = list(map(int, i.split("-")))
            if low <= control_dist_km <= high:
                c_time += (control_dist_km - low) / speed
                break
            if control_dist_km > high:
                c_time += (high - low) / speed

    hours, minutes = divmod(c_time, 1)
    minutes = round(minutes * 60)
    return brevet_start_time.shift(hours=hours, minutes=minutes)
