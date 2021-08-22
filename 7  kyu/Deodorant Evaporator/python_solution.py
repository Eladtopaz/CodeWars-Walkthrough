def evaporator(content, evap_per_day, threshold):
    i = 0
    restrict = (threshold / 100) * content
    while(content > restrict):
        content = content - (content * (evap_per_day / 100))
        i += 1
    return i
