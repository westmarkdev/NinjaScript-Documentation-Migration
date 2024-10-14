










 


Dividends







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?dividends.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Dividends | [Previous page](masterinstrument_description.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


An collection of Dividends configured for the [Master Instrument properties](editing_instruments.htm) used in for stocks.



Property Value
--------------


A collection of Dividends configured for the current instrument.


 


Possible values are:




|  |  |
| --- | --- |
| Amount | A double value representing the amount in dollars which was paid on the date of the dividend |
| Date | A DateTime structure representing the date of the dividend |



 


Syntax
------


Bars.Instrument.MasterInstrument.Dividends


 


Examples
--------




| ns |
| --- |
| foreach(Dividend dividends in Bars.Instrument.MasterInstrument.Dividends)
{
   Print(dividends.Amount);
   Print(dividends.Date);
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
 
 
 



