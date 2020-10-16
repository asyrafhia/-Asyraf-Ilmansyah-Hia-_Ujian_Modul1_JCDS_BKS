def create_phone_number(number):
    if len(number) == 10:
        return '({}{}{}) {}{}{}-{}{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9])
    else:
        return 'Input 10 digits of number!'

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))  # (123) 456-7890
print(create_phone_number([1,2,3,4,6,7,8,9,0]))  # (123) 456-7890
