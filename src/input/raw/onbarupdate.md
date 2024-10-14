










 


OnBarUpdate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onbarupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
OnBarUpdate() | [Previous page](maximumbarslookback.htm)
[Return to chapter overview](common.htm)










Definition
----------


An event driven method which is called whenever a bar is updated. The frequency in which OnBarUpdate is called will be determined by the "[Calculate](calculate.htm)" property. OnBarUpdate() is the method where all of your script's core bar based calculation logic should be contained.


 




|  |
| --- |
| Notes:  
•For [multi-timeframe and instrument scripts](multi-time_frame__instruments.htm), the OnBarUpdate method is called for each Bars object of a strategy.  You MUST filter for the exact bar update events using the "[BarsInProgress](barsinprogress.htm)" property you want your system logic to execute against. •Hosted indicators will need to be accessed by the hosting script to ensure OnBarUpdate functionality. This can be done by: 1) Calling [Update](update.htm) on the hosted indicator within the host script, 2) Including a plot in the hosted indicator and accessing the plot in the host script, 3) Including a plot in the hosted indicator and adding the indicator to the chart with [AddChartIndicator](addchartindicator.htm) (strategies only) |



 


 


Related Methods and Properties
------------------------------




|  |  |
| --- | --- |
| [BarsPeriod](barsperiod.htm) | The primary Bars object time frame (period type and interval). |
| [Calculate](calculate.htm) | Determines how often [OnBarUpdate()](onbarupdate.htm) is called for each bar. |
| [Count](count.htm) | The total number of bars or data points. |
| [CurrentBar](currentbar.htm) | A number representing the current bar in a Bars object that the OnBarUpdate() method in an indicator or strategy is currently processing. |
| [IsDataSeriesRequired](isdataseriesrequired.htm) | Determines if a Data Series is required for calculating this NinjaScript object. |
| [IsFirstTickOfBar](isfirsttickofbar.htm) | Indicates if the incoming tick is the first tick of a new bar. |
| [IsResetOnNewTradingDays](isresetonnewtradingdays.htm) | Determines if the specified bar series is using Break at EOD. |
| [IsTickReplays](istickreplays.htm) | Indicates the specified bar series is using Tick Replay. |
| [Update()](update.htm) | Forces the OnBarUpdate() method to be called so that indicator values are updated to the current bar. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


 


Syntax
You must override this method with the following syntax:
---------------------------------------------------------------



protected override void OnBarUpdate()  

{


   

}


 




|  |
| --- |
| Tip:  The NinjaScript code wizards automatically generates the method syntax for you. |





Parameters
----------


This method does not take any parameters
----------------------------------------





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (CurrentBar &lt; 1)
         return;
 
     // Compares the primary bar's low price to the 5-minute bar's low price
     if (Low[0] &gt; Lows[1])
         Print("The current bar's low price is greater");
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
 
 
 



