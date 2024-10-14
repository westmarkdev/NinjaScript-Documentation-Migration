










 


Compare()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?compare.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Compare() | [Previous page](masterinstrument.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Compares two price values with respect to the Instrument [TickSize](ticksize.htm) to ensure accuracy when dealing with floating point math.



Method Return Value
-------------------


An int value.


 


A value of "1" is returned if price1 is greater than price2


A value of "-1" is returned if price1 is less than price2   

A value of "0" if price1 is equal to price2


 


Syntax
Instrument.MasterInstrument.Compare(double price1, double price2)
------------------------------------------------------------------------


Parameters
----------




|  |  |
| --- | --- |
| price1 | A double value representing a price |
| price2 | A double value representing a price |



 


Examples
--------




| ns |
| --- |
| double newPrice = Close[0] + High[0] + Open[0];
if (Instrument.MasterInstrument.Compare(newPrice, Close[1]) == 1)
     // Do something since price1 is greater than price2 |






 
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
 
 
 



