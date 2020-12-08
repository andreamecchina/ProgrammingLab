def test_list(model):

    # Lista di test
    prev_months = [50.0,'fd',52,60,'ciao','']

    # Provo a predirre su questa lista
    try:
        pred = model.predict(prev_months)

    # Se non riesco lancio un'eccezione
    except:         
        print('la lista non controlla adeguatamente i dati')

    # Controllo ora il risultato
    if model.predict(prev_months) != 65.0:

        # Lancio l'eccezione
        raise Exception('la previsione non è corretta')

# Classe modello
class Model(object):

    # Non mi interessa ora
    def fit(self,data):
        pass

    # Per ora non faccio nulla
    def predict(self):
        pass

# Estendo la classe modello
class IncrementModel(Model):
    
    # Per ora non previsto
    def fit(self,data):
        raise NotImplementedError('questo modello non prevede un fit')

    # Predizione
    def predict(self,prev_months):

        # Dimensione della lista
        size = len(prev_months)

        # Indici da rimuovere
        to_remove = []

        # Controllo tipi dati della lista
        for i in range(size):
            
            # Se non è un numero
            if not isinstance(prev_months[i],int) and not isinstance(prev_months[i],float):
                
                # Segno l'indice da rimuovere
                to_remove.append(i)

        # Rimuovo gli elementi dalla lista
        for i in reversed(to_remove):
            prev_months.remove(prev_months[i])

        # Guardo quanti mesi ho
        if len(prev_months) < 2: 
            
            # Se ho meno di 2 mesi lancio una eccezione
            raise Exception('non ho abbastanza mesi per fare una predizione')

        # Incremento iniziale
        d = 0

        # Ciclo sui mesi 
        for i in range(len(prev_months)-1):
    
            # Aggiungo gli incrementi per coppie di mesi
            d += (prev_months[i+1]-prev_months[i])
            
        # Divido per il numero di mesi
        d /= (len(prev_months)-1)

        # Ritorno la previsione
        return prev_months[-1]+d

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
            if not isinstance(start,int) or not isinstance(end,int):

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

    # Leggi il file
    file = CSVFile("shampoo_sales.csv")
    data = file.get_data()

    # Scelgo i mesi che considero
    n_months = 3

    # Faccio la previsione
    model = IncrementModel()
    pred = model.predict(data[-n_months:])
    print("Vendite predette prossimo mese: ",pred)

    # Testo l'eccezione
    test_list(model)

# Raccolgo l'eccezione
except Exception as e:

    # Stampo l'eccezione
    print('Errore incontrato: ',e)