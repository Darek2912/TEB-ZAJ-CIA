def load_img(file_name):
  #  plik = open(file_name)
    plik = open('zdam2.txt', 'w')
    return plik     #zeby zwrocic do zmiennej plik ktory zostal otwarty

def save_img(file_name, dane):
    plik = open(file_name, 'w')
    plik.write(dane)

img = load_img('zdam.txt')

save_img("zdam.txt", 'razdwatrzys')
print(img.readline())
print('dupa')
