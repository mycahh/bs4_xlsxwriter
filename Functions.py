from Constant import SPACES_BETWEEN_HEADER, A_COL, G_COL, J_COL

counter = 0

def incrementCounter():
    global counter

    counter += 1

def getPositionHeader():
    global counter

    incrementCounter()

    if counter == 1:
        return 1, 0
    else:
        pos = SPACES_BETWEEN_HEADER * (counter - 1)

        return pos, pos-1

def getTextHeader(pos, name):
    if pos == A_COL:
        return name
    elif pos == G_COL:
        return 'Tags'
    elif pos == J_COL:
        return 'Event'
    else:
        return ''

def createTag(name, typeURL):
    return f'{name} - {typeURL}'

def createEvent(name, typeURL):
    fname = name.lower().replace(' ', '')
    ftype =  typeURL.lower().replace(' ', '')
    return f'{fname}_{ftype}'

def hasClickURL(url):
    if url == 'No tiene':
        return False
    else:
        return True