# -*- coding: utf-8 -*-

main_text = '''Benvenuto nel Catalogo di InventoryBot!
Qui puoi trovare una raccolta di tutti gli oggetti (si spera) disponibili su @InventoryBot.

Gli oggetti generalmente vengono aggiunti al catalogo dagli utenti stessi, per fare in modo di essere sempre al passo con i nuovi aggiornamenti.
Contribuire e' molto semplice, per sapere come fare fai il comando /helpcontribuisci .

Per consultare il catalogo puoi usare i comandi /inventario e /conta.
Per ulteriori informazioni su come funzionano usa /helpcomandi .

Per qualsiasi tipo di segnalazione, suggerimento o dubbio non esitare a contattare direttamente @Carlovan.'''

commands_text = '''Per consultare il catalogo puoi utilizzare i comandi /inventario e /conta.
<b>Comando inventario</b>
Il comando /inventario ti permette di filtrare il catalogo e di ottenere la lista degli oggetti corrispondenti alla tua ricerca.
Puoi filtrare il catalogo specificando una o più rarità.
<i>Ad esempio</i>
<i>Se volessi vedere tutti gli oggetti R utilizzerei il comando:</i>
<code>/inventario r</code>
<i>Se volessi vedere gli oggetti R e gli oggetti R+ utilizzerei:</i>
<code>/inventario r r+</code>
È inoltre possibile cercare gli oggetti tramite il nome. In questo caso il bot si comporta nello stesso identico modo di @InventoryBot.
<i>Ad esempio</i>
<i>Se volessi vedere tutti i bauli utilizzerei il comando</i>
<code>/inventario baule</code>
<i>Se volessi vedere se esiste il baule di platino potrei fare:</i>
<code>/inventario baul plati</code>
Per affinare la ricerca è possibile utilizzare sia la rarità che il nome; è sufficiente inserire prima tutte le rarità e poi il nome dell'oggetto.
<i>Ad esempio</i>
<i>Se volessi cercare i bauli che siano R oppure S potrei usare</i>
<code>/inventario r s baul</code>
Se si esegue il comando <code>/inventario</code> senza specificare nessun filtro si otterrà la lista di tutti gli oggetti.

<b>Comando conta</b>
Il comando /conta si comporta nello stesso identico modo del comando /inventario, tranne per il fatto che non fornisce la lista degli oggetti ma solo il numero.
<i>Ad esempio il risultato del comando</i>
<code>/conta uman</code>
<i>è 3 perchè esistono 3 oggetti che corrispondono a questa ricerca (tibia umana, teschio umano, femore umano).</i>
Quindi con il comando <code>/conta</code> senza specificare altro otterremo il numero totale di oggetti contenuti nel catalogo.

<b>Comando ultimi</b>
Utilizzando il comando /ultimi è possibile vedere gli ultimi 10 oggetti aggiunti <b>al catalogo</b> (non necessariamente al gioco).

<b>Comando confronta</b>
Il comando /confronta invece ti permette di controllare il tuo inventario personale e sapere quali oggetti ti mancano.
Questo comando si utilizza in modo simile a /inventario per filtrare il catalogo.
Dopo aver fatto il comando vai su @InventoryBot, fai <code>/inventario</code> e inoltrami il risultato.
<i>Ad esempio</i>
<i>Per controllare quali S mi mancano devo fare</i>
<code>/confronta s</code>
<i>poi devo andare su @InventoryBot, fare </i><code>/inventario s</code><i> e inoltrare il messaggio al catalogo.</i>
Ovviamente è possibile applicare più filtri, quindi se volessi sapere quali bauli mi mancano farei
<code>/confronta baul</code>
e poi su @InventoryBot <code>/inventario baul</code>.
Per annullare il comando /confronta è sufficiente scrivere /annulla.
'''

contribute_text = '''Contribuire alla costruzione del catalogo è molto semplice!
L'unica cosa che devi fare è andare su @InventoryBot, digitare <code>/inventario</code> e inoltrare la risposta a me.
Siccome però l'inventario di @InventoryBot ha una lunghezza limitata, è meglio se mi inoltri i risultati di comandi come <code>/inventario c</code> oppure <code>/inventario r</code>.
Se ti accorgi della mancanza di un particolare oggetto dal catalogo puoi anche inoltrarmi il risultato del comando <code>/mostra</code>.

Una volta fatto io ti dirò quali oggetti hai aggiunto, per farti sapere come hai contribuito 😊
GRAZIE!!
'''
