










 


RoundToTickSize()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?roundtoticksize.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
RoundToTickSize() | [Previous page](rollovercollection.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Returns a value that is rounded up to the nearest valid value evenly divisible by the instrument's tick size.



Method Return Value
-------------------


A double value.


 


Syntax
------


Instrument.MasterInstrument.RoundToTickSize(double price)


 


Parameters
----------




|  |  |
| --- | --- |
| price | A double value representing a price |



 


Examples
--------




| ns |
| --- |
| //Takes the last 3 closes, divides them by 3, and rounds the value up to the nearest valid tick size
Value[0] = Instrument.MasterInstrument.RoundToTickSize((Close[0] + Close[1] + Close[2]) / 3); |






 
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
 
 
 



