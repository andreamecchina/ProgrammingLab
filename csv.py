def list_sum(the_list): 
    sum = 0
    for item in the_list: 
        sum += item
    return sum

# Inizializzo una lista vuota per salvare i valori
total_values = []

# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r") 
for line in my_file:
   
    # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')

    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':

        # Setto la data e il valore
        date = elements[0] 
        value = elements[1]
        
        # Aggiungo alla lista dei valori questo valore
        total_values.append(float(value))

# Somma
print("Somma vendite = ",round(list_sum(total_values),3))
