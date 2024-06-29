/*!
 * Quasar Framework v2.13.0
 * (c) 2015-present Razvan Stoenescu
 * Released under the MIT License.
 */
(function(e,t){"object"===typeof exports&&"undefined"!==typeof module?module.exports=t():"function"===typeof define&&define.amd?define(t):(e="undefined"!==typeof globalThis?globalThis:e||self,e.Quasar=e.Quasar||{},e.Quasar.lang=e.Quasar.lang||{},e.Quasar.lang.uk=t())})(this,function(){"use strict";function e(e,t){return t[e%10===1&&e%100!==11?0:e%10>=2&&e%10<=4&&(e%100<10||e%100>=20)?1:2]}var t={isoName:"uk",nativeName:"Українська",label:{clear:"Очистити",ok:"OK",cancel:"Скасувати",close:"Закрити",set:"Встановити",select:"Обрати",reset:"Скинути",remove:"Видалити",update:"Оновити",create:"Створити",search:"Пошук",filter:"Фільтр",refresh:"Оновити",expand:e=>e?`Розгорнути "${e}"`:"Розгорнути",collapse:e=>e?`Згорнути "${e}"`:"Згорнути"},date:{days:"Неділя_Понеділок_Вівторок_Середа_Четвер_П`ятниця_Субота".split("_"),daysShort:"Нд_Пн_Вт_Ср_Чт_Пт_Сб".split("_"),months:"Січень_Лютий_Березень_Квітень_Травень_Червень_Липень_Серпень_Вересень_Жовтень_Листопад_Грудень".split("_"),monthsShort:"Січ_Лют_Бер_Кві_Тра_Чер_Лип_Сер_Вер_Жов_Лис_Гру".split("_"),firstDayOfWeek:1,format24h:!0,pluralDay:"днів"},table:{noData:"Немає даних",noResults:"Співпадінь не знайдено",loading:"Завантаження...",selectedRecords:t=>t>0?t+" "+e(t,["рядок обраний","рядки обрані","рядків обрано"])+".":"Жодного рядку не обрано.",recordsPerPage:"Рядків на сторінці:",allRows:"Усі",pagination:(e,t,a)=>e+"-"+t+" з "+a,columns:"Колонки"},editor:{url:"URL",bold:"Напівжирний",italic:"Курсив",strikethrough:"Закреслений",underline:"Підкреслений",unorderedList:"Маркований список",orderedList:"Нумерований список",subscript:"Підрядковий",superscript:"Надрядковий",hyperlink:"Гіперпосилання",toggleFullscreen:"Повноекранний режим",quote:"Цитата",left:"Вирівнювання по лівому краю",center:"Вирівнювання по центру",right:"Вирівнювання по правому краю",justify:"Вирівнювання по ширині",print:"Друк",outdent:"Зменшити відтуп",indent:"Збільшити відступ",removeFormat:"Видалити форматування",formatting:"Форматування",fontSize:"Розмір шрифту",align:"Вирівнювання",hr:"Вставити горизонтальну лінію",undo:"Відмінити",redo:"Повторити",heading1:"Заголовок 1",heading2:"Заголовок 2",heading3:"Заголовок 3",heading4:"Заголовок 4",heading5:"Заголовок 5",heading6:"Заголовок 6",paragraph:"Параграф",code:"Код",size1:"Дуже маленький",size2:"Маленький",size3:"Нормальний",size4:"Середній",size5:"Великий",size6:"Дуже великий",size7:"Величезний",defaultFont:"Шрифт за замовчуванням",viewSource:"Переглянути джерело"},tree:{noNodes:"Немає доступних вузлів",noResults:"Співпадінь не знайдено"}};return t});