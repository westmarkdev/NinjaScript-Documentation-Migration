










 


MasterInstrument







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?masterinstrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Instruments](instruments_ninjascript.htm) &gt; [Instrument](instrument.htm) &gt;
MasterInstrument | [Previous page](getinstrument.htm)
[Return to chapter overview](instrument.htm)










Definition
----------


An instrument's configuration settings.  These are settings and properties which are defined in the [Instrument](instruments.htm) window.


 




|  |
| --- |
| Warning:  The properties in this class should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded. |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Compare()](compare.htm) | Returns an int value compares two price values with respect to the Instrument tick size |
| [Currency](currency.htm) | The currency that the instrument traded in |
| [Description](masterinstrument_description.htm) | A  written representation of a given instrument |
| [Dividends](dividends.htm) | A collection of dividends for stock instruments |
| [Exchanges](exchanges.htm) | A collection of exchanges configured for an instrument |
| [FormatPrice()](formatprice.htm) | Returns a string representing the price formatted to the nearest tick size |
| [InstrumentType](instrumenttype.htm) | The type of instrument |
| [MergePolicy](mergepolicy.htm) | The Merge Policy that is configured for the current master instrument. |
| [Name](masterinstrument_name.htm) | The name of the instrument. |
| [GetNextExpiry()](getnextexpiry.htm) | Returns a DateTime structure representing the next futures expiry for a given date |
| [PointValue](pointvalue.htm) | Currency value of 1 full point of movement |
| [RolloverCollection](rollovercollection.htm) | A collection of expiration dates and offsets for futures instruments |
| [RoundToTickSize()](roundtoticksize.htm) | Rounds the value up to the nearest valid value |
| [RoundDownToTickSize()](rounddowntoticksize.htm) | Rounds the value down to the nearest valid value |
| [Splits](splits.htm) | A collection of splits for stock instruments |
| [TickSize](ticksize.htm) | The smallest movement in price configured |
| [Url](url.htm) | A web url where contract details have been collected |






 
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
 
 
 



