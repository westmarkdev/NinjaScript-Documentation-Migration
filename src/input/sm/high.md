










 


High







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?high.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
High | [Previous page](closes.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


A collection of historical bar high prices.


 


Property Value
--------------


An ISeries<double> type object. Accessing this property via an index value [int barsAgo] returns a double value representing the price of the referenced bar.


 


Syntax
------


High  

High[int barsAgo]



 



Examples
--------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
     // Make sure we have at least 20 bars
     if (CurrentBar &lt; 20)
         return;
 
     // Evaluates for higher highs
     if (High[0] &gt; High[1] &amp;&amp; High[1] &gt; High[2])
         Print("Two successive higher highs");
 
     // Gets the current value of a 20 period SMA of high prices
     double value = SMA(High, 20)[0];
     Print("The value is " + value.ToString());
} |






 
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