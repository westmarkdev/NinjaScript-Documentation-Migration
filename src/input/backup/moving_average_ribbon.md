










 


Moving Average Ribbon







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_ribbon.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average Ribbon | [Previous page](moving_average_convergence-divergence_macd.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Moving Average Ribbon is a series of incrementing moving averages.


 


Syntax
------


MovingAverageribbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)


MovingAverageribbon(ISeries<double> input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)


 


Returns the MovingAverage1 value (Replace the 1 with the desired moving average you want the value to return)


MovingAverageribbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]


MovingAverageribbon(ISeries<double> input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| RibbonMAType | Moving average to use for calculations |
| basePeriod | Number of bars used in the calculation for the fastest moving average |
| incrementalPeriod | Number of bars to increase for the calculation in each additional moving average |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of the 3rd moving average
double value = MovingAverageRibbon(RibbonMAType.Exponential, 10, 10).MovingAverage3[0];
Print("The current 3rd moving average's value is " + value.ToString()); |






 
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
 
 
 



</double></double>