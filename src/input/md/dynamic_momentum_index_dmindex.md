










 


Dynamic Momentum Index (DMIndex)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?dynamic_momentum_index_dmindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Dynamic Momentum Index (DMIndex) | [Previous page](double_stochastics.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


An indicator used in technical analysis that determines overbought and oversold conditions of a particular asset. This indicator is very similar to the relative strength index (RSI). The main difference between the two is that the RSI uses a fixed number of time periods (usually 14), while the dynamic momentum index uses different time periods as volatility changes.


 


... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dynamicmomentumindex.asp)


 


 


Syntax
------


DMIndex(int smooth)  

DMIndex(ISeries<double> input, int smooth)


 


Returns default value  

DMIndex(int period)[int barsAgo]  

DMIndex(ISeries<double> input, int smooth)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| smooth | The number of bars to include in the calculation |



 



Example
-------




| ns |
| --- |
| // Prints the current value of DMIndex using default price type
double value = DMIndex(3)[0];
Print("The current DMIndex value is " + value.ToString()); |



 


 


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