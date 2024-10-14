










 


Exchanges







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?exchanges.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Exchanges | [Previous page](dividends.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


A collection of exchange(s) configured for the [Master Instrument properties](editing_instruments.htm).



Property Value
--------------


A collection of Exchanges which represent the exchanges configured for the current instrument.


 


Syntax
------


Bars.Instrument.MasterInstrument.Exchanges



Examples
--------




| ns |
| --- |
| foreach(Exchange exchange in Bars.Instrument.MasterInstrument.Exchanges)
{
 Print(exchange); // Default, Nasdaq, NYSE
}     |






 
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
 
 
 



