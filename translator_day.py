# Day Translator
# Senin > Monday

hari = {
    'senin': 'monday',
    'selasa': 'tuesday',
    'rabu': 'wednesday',
    'kamis': 'thursday',
    'jumat': 'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}

hari_list = list(hari.keys())
days_list = list(hari.values())

print(hari_list)
print(days_list)

var_inp = input('Masukkan hari (INA/ENG): ').lower()
if var_inp in hari_list:
    day = days_list[hari_list.index(var_inp)]
    print(f'Bahasa Inggris dari {var_inp} adalah {day}')
else:
    day = hari_list[days_list.index(var_inp)]
    print(f'Bahasa Indonesia dari {var_inp} adalah {day}')


