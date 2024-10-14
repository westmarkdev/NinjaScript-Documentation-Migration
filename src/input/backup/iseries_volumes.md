










 


Volumes







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseries_volumes.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [VolumeSeries<double>](volumeseries.htm) &gt;
Volumes | [Previous page](iseries_volume.htm)
[Return to chapter overview](volumeseries.htm)










Definition
----------


Holds an array of ISeries<double> objects holding historical bar volumes. An ISeries<double> object is added to this array when calling the [AddDataSeries()](adddataseries.htm) method. Its purpose is to provide access to the volumes of all Bars objects in a multi-instrument or multi-time frame script. 


 




|  |
| --- |
| Note:    For working with [Cryptocurrency instruments](instrumenttype.htm) which report volume fractional, please use the [VOL()](volume.htm) indicator series, or store the volume for your script in a custom variable and convert alongside our [VOL()](volume.htm) indicator (Instrument.MasterInstrument.InstrumentType == InstrumentType.CryptoCurrency ? Core.Globals.ToCryptocurrencyVolume((long)Volume[0]) : Volume[0]).    |



 


 


Property Value
--------------


An array of ISeries<double> objects.


 


Syntax
Volumes[int barSeriesIndex][int barsAgo]
-----------------------------------------------




Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the strategy and is automatically assigned
         // a Bars object index of 1 since the primary data the strategy is run against
         // set by the UI takes the index of 0.
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
     }
} 
 
protected override void OnBarUpdate()
{ 
     // Compares the primary bar's volume to the 5-minute bar's volume
     if (Volumes[0][0] &gt; Volumes[1][0])
         Print("The primary bar's volume is greater");
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
 
 
 



</double></double></double></double></t></double></t>