










 


TickSize







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ticksize.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
TickSize | [Previous page](slope.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


The minimum fluctuation value which is always a value of 1-tick for the corresponding master instrument.


 


 


Property Value
--------------


A double value that represents the minimum fluctuation of an instrument.


 


Syntax
------


TickSize


 


 




|  |
| --- |
| Warning:  This property should NOT be accessed during State.SetDefaults from within the [OnStateChange()](onstatechange.htm) method, all bars series would be guaranteed to have loaded in State.DataLoaded |



 


 


Examples
--------




| ns |
| --- |
| // Prints the ticksize to the output window
Print("The ticksize of this instrument is " + TickSize);
 
// Prints the value of the current bar low less one tick size
double value = Low[0] - TickSize;
Print(value); |






 
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
 
 
 



