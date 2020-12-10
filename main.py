def load_file(file_name):   #tworzenie funkcji ktora uploaduje plik i zwraca module write 
    plik = open(file_name, "w")
    return plik 

def save_to_file(file,dane): 
    file.write(str(dane))   #tworzy funkcje ktora zapisuje dane do pliku ktory jest w module write 


file = load_file('zdam.txt')
save_to_file(file,"dane")
