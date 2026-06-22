# Event Management System - Progetto PPM BACKEND 2026

**Studente:** Cristian Polisi 
**Matricola:** 7112822 

**Project Type:** Full-Stack Web Application  
**Framework:** Django  

## Descrizione del Progetto
L'applicazione è un "Event Management System" che permette agli utenti di esplorare eventi, iscriversi per partecipare, e agli organizzatori di creare e gestire i propri eventi (ad eccezione dell'admin che con i permessi superiori ho deciso di poter osservare e modificare tutto) L'interfaccia grafica è stata realizzata utilizzando Bootstrap 5.

## Funzionalità Implementate (per Ruolo)

* **Utente Non Autenticato (Visitatore):**
    * Visualizzazione della lista completa degli eventi disponibili (Titolo, data, descrizione, organizzatore).
    * Reindirizzamento alla pagina di Login se tenta di partecipare a un evento.
* **Utente Standard (Attendee):**
    * Iscrizione agli eventi tramite il pulsante "Partecipa".
    * Visualizzazione della dashboard "I Miei Eventi", contenente lo storico delle proprie iscrizioni.
    * Impossibilità di iscriversi due volte allo stesso evento (con relativo feedback visivo).
* **Organizzatore (Organizer):**
    * Accesso a una Dashboard dedicata ("Modalità Organizzatore").
    * Operazioni CRUD complete: Creazione di nuovi eventi, Modifica ed Eliminazione dei *propri* eventi.
    * Visualizzazione del conteggio degli iscritti per i propri eventi.
    * Protezione dei permessi: un organizzatore non può modificare o eliminare gli eventi creati da altri organizzatori.

## Istruzioni per l'Installazione e l'Esecuzione Locale

Il progetto contiene tutto il necessario per essere eseguito in locale, incluso il database pre-popolato.

1. **Clona il repository:**
   ```bash
   git clone https://github.com/iPolisi/Progetto-Back
   cd Progetto_Back