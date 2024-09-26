










 


InstrumentType







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?instrumenttype.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt; [MasterInstrument](masterinstrument.htm) &gt;
InstrumentType | [Previous page](formatprice.htm)
[Return to chapter overview](masterinstrument.htm)










Definition
----------


Returns the type of instrument.



Property Value
--------------


An InstrumentType representing the type of an instrument.


 


Possible values are:


 


InstrumentType.Future


InstrumentType.Stock


InstrumentType.Index


InstrumentType.Forex 


InstrumentType.Cfd


InstrumentType.Cryptocurrency



Syntax
------


Instrument.MasterInstrument.InstrumentType


 



Examples
--------




| ns |
| --- |
| if (Instrument.MasterInstrument.InstrumentType == InstrumentType.Future)
{
 // Do something
}
else
{
 // Do something else
} |




 


Additional Access Information
This property can be accessed without a null reference check in the OnBarUpdate() event handler. When the OnBarUpdate() event is triggered, there will always be an Instrument object. Should you wish to access this property elsewhere, check for null reference first. e.g. if (Instrument != null)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





 
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
 
 
 



