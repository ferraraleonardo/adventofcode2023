"""
-- Queue: classe che rappresenta una coda condivisa tra processi.
è utilizzata per consentire la comunicazione tra processi,
consentendo loro di scambiarsi dti in modo sicuro.
put(item): Aggiunge un elemento alla coda.
get(): Rimuove e restituisce un elemento dalla coda.
empty(): Restituisce True se la coda è vuota, altrimenti restituisci False.
full():. Restituisce True se la cosa è piena, altrimenti restituisce False.
qsize(): restituisce il numero di elementi presenti nella coda.
close(): Chiude la coda.
-- current_process: funzione che restituisce un oggetto Process
che rappresenta il processo in esecuzione.

"""
import os
from multiprocessing import *

def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process Pid: {current_process().pid}")

def process_function(data, result_queue):
    process_id()
    print("elabora: ", data)
    result = data * 2
    result_queue.put(result)

if __name__ == "main":
    data_list = [1, 2, 3, 4]
    result_queue = Queue()
    processes = []

    for data in data_list:
        p = processes(target = process_function, args=(data, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("il main stampa i risultati")
    while not result_queue.empty():
        result = result_queue.get()
        print(result)

