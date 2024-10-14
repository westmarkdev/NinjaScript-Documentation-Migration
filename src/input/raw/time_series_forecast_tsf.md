










 


Time Series Forecast (TSF)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?time_series_forecast_tsf.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Time Series Forecast (TSF) | [Previous page](swing.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Time Series Forecast function displays the statistical trend of a security's price over a specified time period based on linear regression analysis. Instead of a straight linear regression trendline, the Time Series Forecast plots the last point of multiple linear regression trendlines. This is why this indicator may sometimes referred to as the "moving linear regression" indicator or the "regression oscillator."


 


 


Syntax
------


TSF(int forecast, int period)  

TSF(ISeries<double> input, int forecast, int period)


 


Returns default value  

TSF(int forecast, int period)[int barsAgo]  

TSF(ISeries<double> input, int forecast, int period)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| forecast | Forecast period |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 


 


Example
-------




| ns |
| --- |
| // Prints the current value of a 20 period TSF using default price type
double value = TSF(3, 20)[0];
Print("The current TSF value is " + value.ToString()); |



 


 


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