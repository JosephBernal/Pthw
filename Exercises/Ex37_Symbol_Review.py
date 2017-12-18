def Pharmacy():
    cough_med = 3
    head_med = 2

    assert cough_med or head_med !<=0:
    print('medicine too low. Please recheck math.')

    if cough_med and head_med >= 1:
        # Requires an as statement
        print(f'The amount of cough medicine left in your building: {cough_med} \n The amount of head medicine left in your building: {head_med}')
