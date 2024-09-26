










 


Moving Average - Simple (SMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_simple_sma.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Simple (SMA) | [Previous page](moving_average_-_mesa_adaptive.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Simple Moving Average is calculated by summing the closing prices of the security for a period of time and then dividing this total by the number of time periods. Sometimes called an arithmetic moving average, the SMA is basically the average stock price over time.


 


 


Syntax
------


SMA(int period)  

SMA(ISeries<double> input, int period)


 


Returns default value  

SMA(int period)[int barsAgo]  

SMA(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period SMA using default price type
double value = SMA(20)[0];
Print("The current SMA value is " + value.ToString());
 
// Prints the current value of a 20 period SMA using high price type
double value = SMA(High, 20)[0];
Print("The current SMA value is " + value.ToString()); |



 


 


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