# Funzione di test risultato noto
def test_list(model):

    # Lista di test
    prev_months = [8,'sda',19,'','4',31,41,50,52,60]

    # Provo a predirre su questa lista
    try:
        pred = model.predict(prev_months)

    # Se non riesco lancio un'eccezione
    except:         
        print('la lista non controlla adeguatamente i dati')

    # Controllo ora il risultato
    if model.predict(prev_months) != 68.0:

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
    
    # Implementazione
    def fit(self,data):

        # Incremento iniziale
        self.global_avg_increment = 0

        # Non serve controllare di nuovo input
        # siccome questa funzoine viene chiamata
        # solo da predict che già controlla

        # Ciclo sui mesi tranne 3
        for i in range(len(data)-4):
    
            # Aggiungo gli incrementi per coppie di mesi
            self.global_avg_increment += (data[i+1]-data[i])
            
        # Divido per il numero di mesi
        self.global_avg_increment /= (len(data)-4)

        #raise NotImplementedError('questo modello non prevede un fit')

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

        # Calcolo incremento su ultimi 3 mesi
        for i in range(3-1):
            d += (prev_months[-1-i]-prev_months[-2-i])
            
        # Divido per il numero di mesi usati
        d /= 2

        # Fit sugli altri mesi
        self.fit(prev_months)

        # Medio i due incrementi
        return prev_months[-1]+(d+self.global_avg_increment)/2

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

    # Faccio la previsione
    model = IncrementModel()
    pred = model.predict(data[0:24])
    print("Vendite predette prossimo mese: ",pred)

    # Plot per confronto slides
    from matplotlib import pyplot
    pyplot.plot(data[0:24]+ [pred], color='tab:red')
    pyplot.plot(data[0:24], color='tab:blue')
    pyplot.show()

    # Testo l'eccezione
    test_list(model)

# Raccolgo l'eccezione
except Exception as e:

    # Stampo l'eccezione
    print('Errore incontrato: ',e)