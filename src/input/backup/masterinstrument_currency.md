










 


Currency







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?masterinstrument_currency.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
Currency | [Previous page](compare.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Indicates the currency configured for the [Master Instrument properties](editing_instruments.htm).



Property Value
--------------


A type of Currency which is configured for the current master instrument.


 


Syntax
------


Bars.Instrument.MasterInstrument.Currency


 



Examples
--------




| ns |
| --- |
| if (Bars.Instrument.MasterInstrument.Currency != Currency.UsDollar)
{
 //Prints if the currency is not UsDollar and indicates what currency it is
 Print ("Warning: Instruments base currency is not UsDollar, it is " + Bars.Instrument.MasterInstrument.Currency);
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
 
 
 



