# Definisco la classe
class CSVFile():

    # Inizializzo la classe
    def __init__(self,name):

        # Provo se il nome del file è una stringa
        if not isinstance(name,str): 
            
            # Se non lo è lancio una eccezione
            raise Exception('il nome del file non è una stringa')

        # L'attributo name contiene il nome del file
        self.filename = name

    # Metodo che torna dati come numeri di una lista
    def get_data(self,start=None,end=None):

        # Inizializzo una lista vuota per salvare i valori
        total_values = []

        # Provo ad aprire il file        
        try:
            my_file = open(self.filename, 'r')

        # Lancio altrimenti una eccezione
        except Exception as e:
            
            # Stampo l'errore
            print('Errore incontrato: ',e)
            
            # Errore non recuperabile
            return None
 
        # Se do gli estremi
        if (start is not None) and (end is not None):
        
            # Indici righe devono essere interi
            if not isinstance(start,int) and not isinstance(end,int):

                # Errore non recuperabile
                raise Exception('estremi intervallo non interi')

            # Primo indice minore o uguale al secondo   
            if not start <= end:

                # Lancio l'eccezione
                raise Exception('il primo estremo deve essere <= rispetto al secondo')

        # Apro e leggo il file, linea per linea
        for line in my_file:
   
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')

            # Se NON sto processando l’intestazione...
            if elements[0] != 'Date':

                # Setto la data e il valore
                date = elements[0] 
                value = elements[1]

                try:
                    # Converto a il valore a float
                    value = float(value)

                # Se non ci riesco lancio l'eccezione
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore incontrato: ',e)
                    
                    # Posso recuperare l'errore
                    continue
                
                # Aggiungo alla lista dei valori questo valore
                total_values.append(value)

        # Se do gli estremi
        if (start is not None) and (end is not None):

            # Controllo gli estremi
            if start<=0 or end>len(total_values):

                raise Exception('input fuori dagli estremi di intervallo')

            # Sistemo primo indice
            start -= 1

        return total_values[start:end]

# Test
try:
    file = CSVFile("shampoo_sales.csv")

    # Provo passando le righe
    data1 = file.get_data(1,4)
    print("Data = ",data1)

    # Controllo funzioni ancora senza passare le righe
    data2 = file.get_data()
    print("Data = ",data2)

# Raccolgo l'eccezione
except Exception as e:
    print('Errore incontrato: ',e)