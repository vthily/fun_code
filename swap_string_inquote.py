import sys

def req1(inputstr):
    outputstr = list(inputstr)
    first_open_quote = inputstr.index('(')
    last_close_quote = inputstr.rindex(')')

    first_ind = first_open_quote + 1
    mirror_ind = last_close_quote - 1

    for i in range(last_close_quote - first_open_quote):
        if ((first_ind < mirror_ind) and (inputstr[first_ind] != '(') and (inputstr[mirror_ind] != ')')):
            temp = outputstr[first_ind]
            outputstr[first_ind] = outputstr[mirror_ind]
            outputstr[mirror_ind] = temp
            
            first_ind = first_ind + (i + 1)
            mirror_ind = mirror_ind - (i + 1)

        elif ((inputstr[first_ind] == '(') or (inputstr[mirror_ind] == ')')):
            first_ind = inputstr.index('(', first_ind, mirror_ind) + 1
            mirror_ind = inputstr.rindex(')', first_ind, mirror_ind + 1) - 1
            continue

        else:
            continue
    print(''.join(outputstr).replace('(', '').replace(')', ''))


def req2(inputstr):
    outputstr = list(inputstr)
    first_ind = 0
    mirror_ind = len(inputstr) - 1

    for i in range(len(inputstr)):
        if (first_ind < mirror_ind):
            temp = outputstr[first_ind]
            outputstr[first_ind] = outputstr[mirror_ind]
            outputstr[mirror_ind] = temp

            first_ind = first_ind + 1
            mirror_ind = mirror_ind - 1

    return (''.join(outputstr))

if __name__ == "__main__":
    inputstr = ""
    outputstr = list("")
    if (len(sys.argv) > 1):
        inputstr = sys.argv[1]
        outputstr = list(inputstr)

    no_open_quotes = inputstr.count('(')
    no_close_quotes = inputstr.count(')')

    if (no_open_quotes != no_close_quotes):
        print (inputstr)
        exit(0)
    
    if (no_open_quotes == 0):
        print (inputstr)
        exit(0)

    last_open_quote = inputstr.rindex('(')
    first_close_quote = inputstr.index(')')
    updated_str = inputstr
    while (last_open_quote != -1):
        new_str = req2(updated_str[(last_open_quote + 1):(first_close_quote)])
        temp_str = updated_str[0:last_open_quote] + new_str + updated_str[(first_close_quote + 1):]
        updated_str = temp_str

        if (updated_str.count('(') == 0):
            last_open_quote = -1
            continue

        last_open_quote = updated_str.rindex('(')
        first_close_quote = updated_str.index(')')

    exit(0)
