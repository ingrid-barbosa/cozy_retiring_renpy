label start:
    call prologue
    call house_selection
    if season == "spring":
        call spring_01
        call day_passed(1)
        call spring_02
        call day_passed(2)
        call spring_03
    elif season == "summer":
        call summer_01
        call day_passed(1)
        call summer_02
        call day_passed(2)
        call summer_03
    else:
        call autumn_01
        call day_passed(1)
        call autumn_02
        call day_passed(2)
        call autumn_03
    call day_passed(3)
    call endings
    return
