cough_med_amt = 3
head_med_amt = 3
tummy_med_amt = 3

inventory = { 'cough_med':cough_med_amt, 'head_med':head_med_amt, 'tummy_med':tummy_med_amt }

def Pharmacy(inventory):

    #assert cough_med or head_med >= 0
    #print('medicine too low. Please recheck math.')

    if cough_med_amt and head_med_amt >= 1:
        # Requires an as statement
        print(f'Cough medicine: {cough_med_amt} \n Head medicine: {head_med_amt} \n Tummy medicine: {tummy_med_amt}')

def InvReq(inventory):
    req =[]
    for i in inventory:
        if inventory[i] <= 5:
            req.append(10 - inventory[i])

    for i in req:
        print(f'Request {i}')

InvReq(inventory)
