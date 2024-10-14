










 


Open







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?open.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
Open | [Previous page](medians.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


A collection of historical bar opening prices.


 


Property Value
--------------


An ISeries<double> type object. Accessing this property via an index value [int barsAgo] returns a double value representing the price of the referenced bar.



Syntax
------


Open  

Open[int barsAgo]


 



Examples
--------




| ns |
| --- |
| // Current bar opening price
double barOpenPrice = Open[0];
 
// Opening price of 10 bars ago
double barOpenPrice = Open[10];
 
// Current bar value of a 20 period simple moving average of opening prices
double value = SMA(Open, 20)[0]; |






 
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
 
 
 



</double></double></t></double></t>