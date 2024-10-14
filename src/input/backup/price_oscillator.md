










 


Price Oscillator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?price_oscillator.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Price Oscillator | [Previous page](polarized_fractal_efficiency_p.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Price Oscillator is an indicator based on the difference between two [moving averages](moving_average_-_exponential_e.htm), and is expressed as either a percentage or in absolute terms.


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_priceOscillator.html)


 


 


Syntax
------


PriceOscillator(int fast, int slow, int smooth)  

PriceOscillator(ISeries<double> input, int fast, int slow, int smooth)


 


Returns default value  

PriceOscillator(int fast, int slow, int smooth)[int barsAgo]  

PriceOscillator(ISeries<double> input, int fast, int slow, int smooth)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| fast | The number of bars to calculate the fast [EMA](moving_average_-_exponential_e.htm) |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| slow | The number of bars to calculate the slow [EMA](moving_average_-_exponential_e.htm) |
| smooth | The number of bars to calculate the [EMA](moving_average_-_exponential_e.htm) signal line |



 


 


Example
-------




| ns |
| --- |
| // Prints the current value of a 20 period PriceOscillator using default price type
double value = PriceOscillator(12, 26, 9)[0];
Print("The current PriceOscillator value is " + value.ToString()); |



 


 


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