CTCC = [133,149,153,173,177,180,181,189,199]
CUCC = [130,131,132,145,155,156,166,171,175,176,185,186,166]
CMCC = [134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198]
def fun():
    tel = input('please input your Telephone number：')

    if len(tel) == 11:  # lenth in 11
        a = int(tel[0:3])  # get  top three of Telephone number to int
        if tel.isdigit() is True:  # must be numeral（use isdigit function）
            if a in CTCC:  # Determine whether the top three numbers are in the CTCC list
                print('your Telephone belong to CTCC')
                fun()
            elif a in CUCC:  # Determine whether the top three numbers are in the CUCC list
                print('your Telephone belong to CUCC')
                fun()
            elif a in CMCC:  # Determine whether the top three numbers are in the CMCC list
                print('your Telephone belong to CMCC')
                fun()
            else: print('Telephone number is wrong')
        else: print('Telephone number must be numeral')
    else: print('Telephone number must be 11')
fun()