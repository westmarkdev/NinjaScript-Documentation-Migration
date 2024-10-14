










 


Moving Average Convergence-Divergence (MACD)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_convergence-divergence_macd.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average Convergence-Divergence (MACD) | [Previous page](moving_average_-_zero_lag_expo.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


MACD uses moving averages, which are lagging indicators, to include some trend-following characteristics. These lagging indicators are turned into a momentum oscillator by subtracting the longer moving average from the shorter moving average. 


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_MACD1.html)


 


 


Syntax
------


MACD(int fast, int slow, int smooth)  

MACD(ISeries<double> input, int fast, int slow, int smooth)


 


Returns MACD value  

MACD(int fast, int slow, int smooth)[int barsAgo]  

MACD(ISeries<double> input, int fast, int slow, int smooth)[int barsAgo]


 


Returns average value  

MACD(int fast, int slow, int smooth).Avg[int barsAgo]  

MACD(ISeries<double> input, int fast, int slow, int smooth).Avg[int barsAgo]


 


Returns difference value  

MACD(int fast, int slow, int smooth).Diff[int barsAgo]  

MACD(ISeries<double> input, int fast, int slow, int smooth).Diff[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| fast | The number of bars to calculate the fast [EMA](moving_average_-_exponential_e.htm) |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| slow | The numbers of bars to calculate the slow EMA |
| smooth | The number of bars to calculate the EMA signal line |



 


 


Examples
--------




| ns |
| --- |
| // Prints the current MACD value
double value = MACD(12, 26, 9)[0];
Print("The current MACD value is " + value.ToString());
 
// Prints the current MACD average value
double value = MACD(12, 26, 9).Avg[0];
Print("The current MACD average value is " + value.ToString());
 
// Prints the current MACD difference value
double value = MACD(12, 26, 9).Diff[0];
Print("The current MACD difference value is " + value.ToString()); |



 


 


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
 
 
 



</double></double></double></double>