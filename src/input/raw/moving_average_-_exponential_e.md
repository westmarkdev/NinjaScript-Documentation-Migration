










 


Moving Average - Exponential (EMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_exponential_e.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Exponential (EMA) | [Previous page](moving_average_-_double_expone.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The exponential moving average is but one type of a moving average. In a simple moving average, all price data has an equal weight in the computation of the average with the oldest value removed as each new value is added. In the exponential moving average equation the most recent market action is assigned greater importance as the average is calculated. The oldest pricing data in the exponential moving average is however never removed.


 


 


Syntax
------


EMA(int period)  

EMA(ISeries<double> input, int period)


 


Returns default value  

EMA(int period)[int barsAgo]  

EMA(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period EMA using default price type
double value = EMA(20)[0];
Print("The current EMA value is " + value.ToString());
 
// Prints the current value of a 20 period EMA using high price type
double value = EMA(High, 20)[0];
Print("The current EMA value is " + value.ToString()); |



 


 


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