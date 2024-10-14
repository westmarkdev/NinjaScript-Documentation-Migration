










 


Instrument







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?instrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt;
Instrument | [Previous page](instruments_ninjascript.htm)
[Return to chapter overview](instruments_ninjascript.htm)










Definition
----------


A tradable symbol.  Represents an instance of a [Master Instrument](masterinstrument.htm)


 




|  |
| --- |
| Warning: The properties in this class should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Exchange](exchange.htm) | Exchange of the current instrument |
| [Expiry](expiry.htm) | Expiration date of the futures contract |
| [FullName](instrument_fullname.htm) | Full name of the instrument |
| [GetInstrument()](getinstrument.htm) | Returns an Instrument object by the master instrument name configured in the database.   |
| [MasterInstrument](masterinstrument.htm) | An instrument's configuration settings.  These are settings and properties which are defined in the [Instrument](instruments.htm) window. |
| FundmentalData | Instrument thread specific [FundamentalData](fundamentaldata.htm) events |
| MarketData | Instrument thread specific [MarketData](marketdata.htm) events |
| MarketDepth | Instrument thread specific [MarketDepth](marketdepth.htm) events |
| Dispatcher | A Dispatcher used for subscribing to Instrument related events See [Multi-Threading Considerations](multi-threading.htm) |






 
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
 
 
 



