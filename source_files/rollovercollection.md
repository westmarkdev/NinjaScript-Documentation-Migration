










 


RolloverCollection







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rollovercollection.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
RolloverCollection | [Previous page](pointvalue.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the rollovers that have been configured for the [Master Instrument properties](editing_instruments.htm) used in for futures.



Property Value
--------------


A RolloversCollection configured for the current instrument.


 


Possible values are:




|  |  |
| --- | --- |
| ContractMonth | A DateTime structure representing the expiry month of a futures contract |
| Date | A DateTime structure representing the date of the rollover |
| Offset | A double value representing the number of points between contracts |



 


Syntax
------


Bars.Instrument.MasterInstrument.RolloverCollection


 


Examples
--------




| ns |
| --- |
| foreach(var rollover in Bars.Instrument.MasterInstrument.RolloverCollection)
{
     Print(rollover.ContractMonth);
     Print(rollover.Date);
     Print(rollover.Offset);
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
 
 
 



