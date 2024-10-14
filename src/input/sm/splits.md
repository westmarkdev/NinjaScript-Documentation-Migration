










 


Splits







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?splits.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Splits | [Previous page](rounddowntoticksize.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the Splits that have been configured for the [Master Instrument properties](editing_instruments.htm) used in for stocks.



Property Value
--------------


A collection of Splits configured for the current instrument.


 


Possible values are:




|  |  |
| --- | --- |
| Date | A DateTime structure representing the date of the split |
| Factor | A double value representing the number of points the stock split |



 


 


Syntax
------


Bars.Instrument.MasterInstrument.Splits


 


Examples
--------




| ns |
| --- |
| foreach (Split split in Bars.Instrument.MasterInstrument.Splits)
{
     Print(split.Date);
     Print(split.Factor);
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
 
 
 



