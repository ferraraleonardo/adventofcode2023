from multiprocessing import Process
"""
multiprocessing è una libreria per la creazione, la comunicazione e la sincronizzazione
tra processi nella programmazione parallela e concorrente
Process è una classe per creare processi eseguendo la funzione (o metodo) specificata come target.

"""

def process_function(data): # è definizione di una funzione 'process_function' che prende un argomento in questo caso è (data)
    result = data * 2 # La funzione raddoppia il valore (data) e lo assegna alla variabile (result)
    print(result) # Stampa il risultato

if __name__ == "__main__": # è la definizione di una lista 'data_list' contenente numeri
    data_list = [1, 2 , 3, 4]
    process = [] # è la definizione di una lista vuota

    for data in data_list:
        p = Process(target = process_function, args = (data,)) # Crea un oggetto di tipo Process con la funzione 'process_function' come target e 'data' come argomento
        process.append(p) # Aggiunge il Processo che abbiamo creato alla lista 'process'
        p.start() # Avvia l'esecuzione del processo separato

    for p in process:
        p.join() # Blocca il processo principale fino a quando il processo separato non termina