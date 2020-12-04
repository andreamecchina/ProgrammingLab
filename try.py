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

        # Provo ad aprire il file        
        try:
            my_file = open(self.filename, 'r')

        # Lancio altrimenti una eccezione
        except Exception as e:
            
            # Stampo l'errore
            print('Error: ',e)
            
            # Esco dalla funzione ritornando niente
            return None
 
        # Apro e leggo il file, linea per linea
        for line in my_file:
   
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')

            # Se NON sto processando l’intestazione...
            if elements[0] != 'Date':

                # Setto la data e il valore
                date = elements[0] 
                value = elements[1]

                                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).

                # Provo se il valore è float
                try:
                    value = float(value)

                # Lancio l'eccezione
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Error: ',e)
                    
                    # Posso recuperare l'errore
                    continue
                
                # Aggiungo alla lista dei valori questo valore
                total_values.append(value)

        return total_values

# Test
file = CSVFile("shampoo_sales.csv")
data = file.get_data()
print("Data = ",data)