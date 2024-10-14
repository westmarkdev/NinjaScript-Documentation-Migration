










 


Percentage Price Oscillator (PPO)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?percentage_price_oscillator_pp.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Percentage Price Oscillator (PPO) | [Previous page](parabolic_sar.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Percentage Price Oscillator shows the percentage difference between two [exponential moving averages](moving_average_-_exponential_e.htm). 


 


 


Syntax
------


PPO(int fast, int slow, int smooth)  

PPO(ISeries<double> input, int fast, int slow, int smooth)


 


Returns default value  

PPO(int fast, int slow, int smooth)[int barsAgo]  

PPO(ISeries<double> input, int fast, int slow, int smooth)[int barsAgo]


 


Returns smoothed value  

PPO(int fast, int slow, int smooth).Smoothed[int barsAgo]  

PPO(ISeries<double> input, int fast, int slow, int smooth).Smoothed[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| fast | The number of bars to calculate the fast EMA |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| slow | The number of bars to calculate the slow EMA |
| smooth | The number of bars to calculate the EMA signal line |



 



Example
-------




| ns |
| --- |
| // Prints the current value of a 20 period Percentage Price Oscillator
double value = PPO(12, 26, 9)[0];
Print("The current Percentage Price Oscillator value is " + value.ToString()); |



 


 


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
 
 
 



</double></double></double>