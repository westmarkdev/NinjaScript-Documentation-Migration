﻿










 


Opens







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?opens.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
Opens | [Previous page](open.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


Holds an array of ISeries<double> objects holding historical bar open prices. An ISeries<double> object is added to this array when calling the [AddDataSeries()](adddataseries.htm) method. Its purpose is to provide access to the open prices of all Bars objects in a multi-instrument or multi-time frame script. 


 


Property Value
--------------


An array of ISeries<double> objects.


 


Syntax
Opens[int barSeriesIndex][int barsAgo]
---------------------------------------------


 


 



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
     // Compares the primary bar's open price to the 5-minute bar's open price
     if (Opens[0][0] &gt; Opens[1][0])
         Print("The primary bar's open price is greater");
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