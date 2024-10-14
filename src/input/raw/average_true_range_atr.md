










 


Average True Range (ATR)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?average_true_range_atr.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Average True Range (ATR) | [Previous page](average_directional_movement_r.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


A measure of volatility introduced by Welles Wilder in his book: New Concepts in Technical Trading Systems.


 


The True Range indicator is the greatest of the following:


-current high less the current low.


-the absolute value of the current high less the previous close.


-the absolute value of the current low less the previous close.


 


The Average True Range is a moving average (generally 14-days) of the True Ranges. 


 


... Courtesy of [Investopedia](http://www.investopedia.com/terms/a/atr.asp)


 


The original Wilder formula for an exponential moving average with a smoothing constant (k = 1/ Period) is used to calculate the ATR.


 


Syntax
------


ATR(int period)  

ATR(ISeries<double> input, int period)


 


Returns default value  

ATR(int period)[int barsAgo]  

ATR(ISeries<double> input, int period)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 


 


Example
-------




| ns |
| --- |
| // Prints the current value of a 20 period ATR using default price type
double value = ATR(20)[0];
Print("The current ATR value is " + value.ToString()); |



 


 


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