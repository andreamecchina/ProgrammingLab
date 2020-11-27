# Definisco la classe
class CSVFile():

    # Inizializzo la classe
    def __init__(self,name):

        # L'attributo name contiene il nome del file
        self.filename = name

    # Metodo che torna dati come numeri di una lista
    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        total_values = []

        # Apro e leggo il file, linea per linea
        my_file = open(self.filename, "r") 
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

        return total_values

# Test
file = CSVFile("shampoo_sales.csv")
data = file.get_data()
print("Data = ",data)