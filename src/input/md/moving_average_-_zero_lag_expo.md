










 


Moving Average - Zero Lag Exponential (ZLEMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_zero_lag_expo.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Zero Lag Exponential (ZLEMA) | [Previous page](moving_average_-_weighted_wma.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Zero-Lag Exponential Moving Average is a variation on the Exponential Moving Average. The Zero-Lag keeps the benefit of the heavier weighting of recent values, but attempts to remove lag by subtracting older data to minimize the cumulative effect.


 


... Courtesy of [FMLabs](http://www.fmlabs.com/reference/default.htm?url=ZeroLagExpMA.htm)


 


 


Syntax
------


ZLEMA(int period)  

ZLEMA(ISeries<double> input, int period)


 


Returns default value  

ZLEMA(int period)[int barsAgo]  

ZLEMA(ISeries<double> input, int period)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 


 


Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period ZLEMA using default price type
double value = ZLEMA(20)[0];
Print("The current SMA value is " + value.ToString());
 
// Prints the current value of a 20 period ZLEMA using high price type
double value = ZLEMA(High, 20)[0];
Print("The current ZLEMA value is " + value.ToString()); |



 


 


Source Code
-----------


You can view this indicator method source code by selecting the menu New &gt; NinjaScript Editor &gt; Indicators within the NinjaTrader Control Center window.





 
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