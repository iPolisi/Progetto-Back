# Event Management System - Progetto PPM BACKEND 2026

**Studente:** Cristian Polisi 
**Matricola:** 7112822 

**Project Type:** Full-Stack Web Application  
**Framework:** Django  

##  Descrizione del Progetto
L'applicazione è un Event Management System che permette agli utenti di esplorare eventi, iscriversi per partecipare, e agli organizzatori di creare e gestire i propri eventi (ad eccezione dell'admin che, con i permessi superiori, ha la facoltà di osservare e modificare tutti gli eventi a sistema). L'interfaccia grafica è stata realizzata utilizzando Bootstrap 5 per garantire una navigazione pulita e responsive.

##  Funzionalità Implementate (per Ruolo)

* **Utente Non Autenticato (Visitatore):**
    * Visualizzazione della lista completa degli eventi disponibili (Titolo, data, descrizione, organizzatore).
    * Reindirizzamento alla pagina di Login se tenta di partecipare a un evento.
* **Utente Standard (Attendee):**
    * Iscrizione agli eventi tramite il pulsante "Partecipa".
    * Visualizzazione della dashboard "I Miei Eventi", contenente lo storico delle proprie iscrizioni.
    * Impossibilità di iscriversi due volte allo stesso evento (con relativo feedback visivo).
    * Possibilità di annullare la propria iscrizione.
* **Organizzatore (Organizer):**
    * Accesso a una Dashboard dedicata ("Modalità Organizzatore").
    * Operazioni CRUD complete: Creazione di nuovi eventi, Modifica ed Eliminazione dei *propri* eventi (o di tutti, se si è Admin).
    * Visualizzazione del conteggio degli iscritti per i propri eventi.
    * Protezione dei permessi: un organizzatore standard non può modificare o eliminare gli eventi creati da altri organizzatori.

##  Link al Deployment (Sito Live)
L'applicazione è pubblicata e testabile online al seguente indirizzo:  
 **https://sonopoli.pythonanywhere.com**

##  Database e Dati Demo
Il repository include il file `db.sqlite3`. Il database è **già pre-popolato** con eventi, iscrizioni e account fittizi generati appositamente per la valutazione del progetto.

###  Account di Demo per il Testing

1. utente: `sonoPoli` password: `admin1234.` Administrator (Superuser). Accesso completo a tutto il front-end e al pannello `/admin`.
2. utente: `org_demo` password: `org1234.`  Organizer. Può accedere alla dashboard, creare e gestire i propri eventi. 
3. utente: `user_demo` password: `user1234.`  Standard User.  Può visualizzare gli eventi, iscriversi e annullare l'iscrizione. 


##  Istruzioni per l'Installazione e l'Esecuzione Locale

Il progetto contiene tutto il necessario per essere eseguito in locale.

1. **Clona il repository:**
   ```bash
   git clone [https://github.com/iPolisi/Progetto-Back](https://github.com/iPolisi/Progetto-Back)
   cd Progetto-Back