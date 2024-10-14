










 


SuperDOM Column







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?superdom_column.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
SuperDOM Column | [Previous page](waitforococlosingbracket.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom SuperDOM Columns can be used to add additional functionality to the [SuperDOM](superdom.htm) window. The methods and properties covered in this section are unique to custom SuperDOM column development.


 




|  |
| --- |
| Tip:  The system SuperDOM Columns which ship with NinjaTrader are open source and you can review their implementation from the [NinjaScript Editor](ns_explorer.htm) SuperDOMColumn folder, or by using the text editor of your choice by reviewing the source code located in Documents\NinjaTrader 8\bin\Custom\SuperDomColumns |



 



In this section
---------------




|  |  |
| --- | --- |
| [MarketDepth](superdom_marketdepth.htm) | Provides Level 2 information for a SuperDOMColumn. |
| [OnMarketData()](superdomcolumn_onmarketdata.htm) | Called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. The OnMarketData() method updates can include but is not limited to the bid, ask, last price and volume. |
| [OnOrderUpdate()](superdomcolumn_onorderupdate.htm) | Called every time an [order](order.htm) changes state. An order will change state when a change in order quantity, price or state (e.g. working to filled) occurs. |
| [OnPositionUpdate()](superdomcolumn_onpositionupdate.htm) | Called every time a [position](position.htm) changes state. |
| [OnPropertyChanged()](onpropertychanged.htm) | This method should be used any time you wish to repaint the column instead of calling [OnRender()](superdomcolumn_onrender.htm) directly. |
| [OnRender()](superdomcolumn_onrender.htm) | Used to draw custom content to the SuperDOM Column, such as a Grid. |
| [OnRestoreValues()](onrestorevalues.htm) | Called when the column is restored (e.g. from a workspace). |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



