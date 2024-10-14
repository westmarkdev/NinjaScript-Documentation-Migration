










 


Median







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?median.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
Median | [Previous page](lows.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


A collection of historical bar median prices. Median price = (High + Low) / 2.


 


Property Value
--------------


An ISeries<double> type object. Accessing this property via an index value [int barsAgo] returns a double value representing the price of the referenced bar.



Syntax
------


Median  

Median[int barsAgo]




Examples
--------




| ns |
| --- |
| // Current bar median price
double barMedianPrice = Median[0];
 
// Median price of 10 bars ago
double barMedianPrice = Median[10];
 
// Current bar value of a 20 period exponential moving average of median prices
double value = EMA(Median, 20)[0]; |






 
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