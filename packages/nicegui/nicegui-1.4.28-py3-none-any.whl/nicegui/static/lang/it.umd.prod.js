/*!
 * Quasar Framework v2.13.0
 * (c) 2015-present Razvan Stoenescu
 * Released under the MIT License.
 */
(function(e,i){"object"===typeof exports&&"undefined"!==typeof module?module.exports=i():"function"===typeof define&&define.amd?define(i):(e="undefined"!==typeof globalThis?globalThis:e||self,e.Quasar=e.Quasar||{},e.Quasar.lang=e.Quasar.lang||{},e.Quasar.lang.it=i())})(this,function(){"use strict";var e={isoName:"it",nativeName:"Italiano",label:{clear:"Pulisci",ok:"OK",cancel:"Annulla",close:"Chiudi",set:"Imposta",select:"Seleziona",reset:"Ripristina",remove:"Rimuovi",update:"Aggiorna",create:"Crea",search:"Cerca",filter:"Filtra",refresh:"Aggiorna",expand:e=>e?`Espandi "${e}"`:"Espandere",collapse:e=>e?`Comprimi "${e}"`:"Crollo"},date:{days:"Domenica_Lunedì_Martedì_Mercoledì_Giovedì_Venerdì_Sabato".split("_"),daysShort:"Dom_Lun_Mar_Mer_Gio_Ven_Sab".split("_"),months:"Gennaio_Febbraio_Marzo_Aprile_Maggio_Giugno_Luglio_Agosto_Settembre_Ottobre_Novembre_Dicembre".split("_"),monthsShort:"Gen_Feb_Mar_Apr_Mag_Giu_Lug_Ago_Set_Ott_Nov_Dic".split("_"),firstDayOfWeek:1,format24h:!0,pluralDay:"giorni"},table:{noData:"Nessun dato disponibile",noResults:"Nessuna corrispondenza trovata",loading:"Caricamento...",selectedRecords:e=>e>0?e+" "+(1===e?"riga selezionata":"righe selezionate")+".":"Nessuna riga selezionata.",recordsPerPage:"Righe per pagina:",allRows:"Tutte",pagination:(e,i,a)=>e+"-"+i+" di "+a,columns:"Colonne"},editor:{url:"URL",bold:"Grassetto",italic:"Corsivo",strikethrough:"Barrato",underline:"Sottolineato",unorderedList:"Lista non ordinata",orderedList:"Lista ordinata",subscript:"Pedice",superscript:"Apice",hyperlink:"Hyperlink",toggleFullscreen:"Fullscreen on/off",quote:"Citazione",left:"A sinistra",center:"Centra",right:"A destra",justify:"Giustificato",print:"Stampa",outdent:"Diminuisci identazione",indent:"Aumenta identazione",removeFormat:"Rimuovi formattazione",formatting:"Formattazione",fontSize:"Dimensione del font",align:"Allinea",hr:"Inserisci righello orizzontale",undo:"Indietro",redo:"Avanti",heading1:"Intestazione 1",heading2:"Intestazione 2",heading3:"Intestazione 3",heading4:"Intestazione 4",heading5:"Intestazione 5",heading6:"Intestazione 6",paragraph:"Paragrafo",code:"Codice",size1:"Molto piccolo",size2:"Piccolo",size3:"Normale",size4:"Medio-largo",size5:"Grande",size6:"Molto grande",size7:"Massimo",defaultFont:"Font predefinito",viewSource:"Vedi la fonte"},tree:{noData:"Nessun nodo disponibile",noResults:"Nessuna corrispondenza trovata"}};return e});