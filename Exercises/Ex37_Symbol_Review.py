def shipment():

inventory = { cough_med:cough_med_amt, head_med:head_med_amt, tummy_med:tummy_med_amt }

def Pharmacy():

    #assert cough_med or head_med >= 0
    #print('medicine too low. Please recheck math.')

    if cough_med and head_med >= 1:
        # Requires an as statement
        print(f'Cough medicine: {cough_med_amt} \n Head medicine: {head_med_amt} \n Tummy medicine: {tummy_med_amt} ')

Pharmacy()