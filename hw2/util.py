import numpy as np

# key should be a numpy array
def inv_key(key):
    det = int(round(np.linalg.det(key)))
    inv = np.linalg.inv(key)
    tem = (inv * det)
    modinv = np.mod(det ** 29, 31)
    return np.around(np.mod(tem * modinv, 31)).astype(int)


def to_number(k):
    if ord(k) >= 65 and ord(k) <= 90:
        return ord(k)-65
    if k == ',':
        return 28
    if k == '_':
        return 26
    if k == '.':
        return 27
    if k == '?':
        return 29
    if k == '!':
        return 30
    else:
        return 0


def to_char(k):
    if k >= 0 and k <= 25:
        return chr(k+65)
    if k == 28:
        return ','
    if k == 26:
        return '_'
    if k == 27:
        return '.'
    if k == 29:
        return '?'
    if k == 30:
        return '!'
    else:
        return ' '
