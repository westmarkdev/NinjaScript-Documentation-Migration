










 


Moving Average - Weighted (WMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_weighted_wma.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Weighted (WMA) | [Previous page](moving_average_-_volume_weight.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Weighted Moving Average gives the latest price more weight than prior prices. Each prior price in the period gets progressively less weight as they become older.


 


 


Syntax
------


WMA(int period)  

WMA(ISeries<double> input, int period)


 


Returns default value  

WMA(int period)[int barsAgo]  

WMA(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period WMA using default price type
double value = WMA(20)[0];
Print("The current WMA value is " + value.ToString());
 
// Prints the current value of a 20 period WMA using high price type
double value = WMA(High, 20)[0];
Print("The current WMA value is " + value.ToString()); |



 


 


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