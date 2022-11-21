def study_schedule(permanence_period, target_time):
    quantity = 0
    if type(target_time) != int:
        return None
    else:
        while target_time > permanence_period:
            target_time -= permanence_period
            quantity += 1
        return quantity
