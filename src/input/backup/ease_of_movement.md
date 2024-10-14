










 


Ease of Movement







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ease_of_movement.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Ease of Movement | [Previous page](dynamic_momentum_index_dmindex.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Ease of Movement indicator was designed to illustrate the relationship between volume and price change. It shows how much volume is required to move prices.


 


High Ease of Movement values occur when prices are moving upward with light volume. Low values occur when prices are moving downward on light volume. If prices are not moving or if heavy volume is required to move prices then the indicator will read near zero. A buy signal is produced when it crosses above zero. A sell signal is produced when the indicator crosses below zero (prices are moving downward more easily).


 


 


Syntax
------


EaseOfMovement(int smoothing, int volumeDivisor)  

EaseOfMovement(ISeries<double> input, int smoothing, int volumeDivisor)


 


Returns default value  

EaseOfMovement(int smoothing, int volumeDivisor)[int barsAgo]  

EaseOfMovement(ISeries<double> input, int smoothing, int volumeDivisor)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| smoothing | The number of bars used to smooth the signal |
| volumeDivisor | The value used to calculate the box ratio |



 



Example
-------




| ns |
| --- |
| // Prints the current value of Ease of Movement using default price type
double value = EaseOfMovement(14, 10000)[0];
Print("The current Ease of Movement value is " + value.ToString()); |



 


 


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