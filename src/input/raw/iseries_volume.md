










 


Volume







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseries_volume.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [VolumeSeries<double>](volumeseries.htm) &gt;
Volume | [Previous page](volumeseries.htm)
[Return to chapter overview](volumeseries.htm)










Definition
----------


A collection of historical bar volume values.


 




|  |
| --- |
| Note:    For working with [Cryptocurrency instruments](instrumenttype.htm) which report volume fractional, please use the [VOL()](volume.htm) indicator series, or store the volume for your script in a custom variable and convert alongside our [VOL()](volume.htm) indicator (Instrument.MasterInstrument.InstrumentType == InstrumentType.CryptoCurrency ? Core.Globals.ToCryptocurrencyVolume((long)Volume[0]) : Volume[0]).    |



 


 


Property Value
--------------


An ISeries<double> object. Accessing this property via an index [int barsAgo] returns a double value representing the volume of the referenced bar.


 


Syntax
------


Volume  

Volume[int barsAgo]


 



Examples
--------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
     // Is current volume greater than twice the prior bar's volume
     if (Volume[0] &gt; Volume[1] * 2)
         Print("We have increased volume");
 
     // Is the current volume greater than the 20 period moving average of volume
     if (Volume[0] &gt; SMA(Volume, 20)[0])
         Print("Increasing volume");
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
 
 
 



</double></double></t></double></t>