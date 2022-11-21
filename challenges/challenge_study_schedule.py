def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    quantity = 0
    for i in permanence_period:
        if type(i[0]) != int or type(i[1]) != int:
            return None
        else:
            quantity += 1 if (i[0] <= target_time <= i[1]) else 0
    return quantity
