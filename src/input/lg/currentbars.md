










 


CurrentBars







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?currentbars.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [AddDataSeries()](adddataseries.htm) &gt;
CurrentBars | [Previous page](barsperiods.htm)
[Return to chapter overview](adddataseries.htm)










Definition
----------


Holds an array of int values representing the number of the current bar in a Bars object. An int value is added to this array when calling the [AddDataSeries()](adddataseries.htm) method. Its purpose is to provide access to the [CurrentBar](currentbar.htm) of all Bars objects in a multi-instrument or multi-time frame script. 


 




|  |
| --- |
| Note:    In [multi series](multi-time_frame__instruments.htm) processing, the CurrentBars starting value will be -1 until all series have processed the first bar. |



 



Property Value
--------------


An array of int values.


 




|  |
| --- |
| Warning: This property should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |



 


 


Syntax
------


CurrentBars[int barSeriesIndex]


 


Examples
--------




| ns Indicator ([BarsRequiredToPlot](barsrequiredtoplot.htm)) |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the script. It will automatically be assigned
         // a Bars object index of 1 since the primary data the indicator is run against
         // set by the UI takes the index of 0.
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
     }
}
 
protected override void OnBarUpdate()
{
     // Evaluates to make sure we have at least 20 (default value of BarsRequiredToPlot)
     // or more bars in both Bars objects before continuing.
     if (CurrentBars[0] &lt; BarsRequiredToPlot || CurrentBars[1] &lt; BarsRequiredToPlot)
         return;
 
     // Indicator script logic calculation code...
} |



 





| ns Strategy ([BarsRequiredToTrade](barsrequiredtotrade.htm)) |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the script. It will automatically be assigned
         // a Bars object index of 1 since the primary data the indicator is run against
         // set by the UI takes the index of 0.
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
     }
}
 
protected override void OnBarUpdate()
{
     // Evaluates to make sure we have at least 20 (default value of BarsRequiredToTrade)
     // or more bars in both Bars objects before continuing.
     if (CurrentBars[0] &lt; BarsRequiredToTrade || CurrentBars[1] &lt; BarsRequiredToTrade)
         return;
 
     // Strategy script logic calculation code...
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
 
 
 



