/*!
 * Quasar Framework v2.13.0
 * (c) 2015-present Razvan Stoenescu
 * Released under the MIT License.
 */
(function(e,t){"object"===typeof exports&&"undefined"!==typeof module?module.exports=t():"function"===typeof define&&define.amd?define(t):(e="undefined"!==typeof globalThis?globalThis:e||self,e.Quasar=e.Quasar||{},e.Quasar.lang=e.Quasar.lang||{},e.Quasar.lang.ja=t())})(this,function(){"use strict";var e={isoName:"ja",nativeName:"日本語 (にほんご)",label:{clear:"クリア",ok:"OK",cancel:"キャンセル",close:"閉じる",set:"設定",select:"選択",reset:"リセット",remove:"削除",update:"更新",create:"作成",search:"検索",filter:"フィルタ",refresh:"再読込",expand:e=>e?`「${e}」を展開します。`:"拡大",collapse:e=>e?`「${e}」を折りたたむ`:"崩壊"},date:{days:"日曜日_月曜日_火曜日_水曜日_木曜日_金曜日_土曜日".split("_"),daysShort:"日_月_火_水_木_金_土".split("_"),months:"1月_2月_3月_4月_5月_6月_7月_8月_9月_10月_11月_12月".split("_"),monthsShort:"1月_2月_3月_4月_5月_6月_7月_8月_9月_10月_11月_12月".split("_"),headerTitle:e=>new Intl.DateTimeFormat("ja-JP",{weekday:"short",month:"short",day:"numeric"}).format(e),firstDayOfWeek:0,format24h:!0,pluralDay:"日間"},table:{noData:"データがありません",noResults:"検索結果がありません",loading:"読込中...",selectedRecords:e=>e>0?e+"行を選択中":"行を選択",recordsPerPage:"ページあたりの行数",allRows:"全て",pagination:(e,t,a)=>e+"-"+t+" ／ "+a,columns:"列"},editor:{url:"URL",bold:"太字",italic:"斜体",strikethrough:"取り消し線",underline:"下線",unorderedList:"箇条書き",orderedList:"段落番号",subscript:"下付き",superscript:"上付き",hyperlink:"リンク",toggleFullscreen:"全画面表示",quote:"引用文",left:"左揃え",center:"中央揃え",right:"右揃え",justify:"両端揃え",print:"印刷",outdent:"インデント解除",indent:"インデント",removeFormat:"書式解除",formatting:"書式",fontSize:"フォントサイズ",align:"揃え",hr:"横線を投入",undo:"元に戻す",redo:"やり直し",heading1:"ヘッダー 1",heading2:"ヘッダー 2",heading3:"ヘッダー 3",heading4:"ヘッダー 4",heading5:"ヘッダー 5",heading6:"ヘッダー 6",paragraph:"段落",code:"コード",size1:"小さい",size2:"やや小さい",size3:"普通",size4:"やや大きい",size5:"大きい",size6:"とても大きい",size7:"最大",defaultFont:"初期フォント",viewSource:"ソースを見る"},tree:{noNodes:"ノードがありません",noResults:"該当するノードがありません"}};return e});