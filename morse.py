
# Morse Translator
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMorse_code&psig=AOvVaw0HBhEbvQnFfy_XrJKyEdUR&ust=1593847693275000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMjt3b_HsOoCFQAAAAAdAAAAABAH


var = input('Masukkan kalimat: ').lower()
panjang = len(var)
morse = {'a':'.-',
        'b':'-...',
        'c':'-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g':'--.',
        'h':'....',
        'i':'..',
        'j':'.---',
        'k':'-.-',
        'l':'.-..',
        'm':'--',
        'n':'-.',
        'o':'---',
        'p':'.--.',
        'q':'--.-',
        'r':'.-.',
        's':'...',
        't':'-',
        'u':'..-',
        'v':'...-',
        'w':'.--',
        'x':'-..-',
        'y':'-.--',
        'z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',
        ' ':'|'
}
bantu = []
for i in range(0,panjang):
    bantu += morse[var[i]]  # list + string
    bantu.extend(' ')
    bantu_str = ''.join(bantu)
    if (i == panjang-1):
        print(bantu_str)
