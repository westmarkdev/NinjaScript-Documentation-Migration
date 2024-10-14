










 


Range Indicator (RIND)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?range_indicator_rind.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Range Indicator (RIND) | [Previous page](range.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Range indicator compares the intraday range (high - low) to the inter-day (close - previous close) range. When the inter-day range is less than the intraday range, the Range Indicator will be a high value. This signals an end to the current trend. When the Range Indicator is at a low level, a new trend is about to start.   

   

The Range Indicator was developed by Jack Weinberg and was introduced in his article in the June, 1995 issue of Technical Analysis of Stocks &amp; Commodities magazine.


 


 


Syntax
------


RIND(int periodQ, int smooth)  

RIND(ISeries<double> input, int periodQ, int smooth)


 


Returns default value  

RIND(int periodQ, int smooth)[int barsAgo]  

RIND(ISeries<double> input, int periodQ, int smooth)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| periodQ | The number of bars to include in the calculation for the short term stochastic range lookback |
| smooth | The number of bars to include for the EMA smoothing of the indicator |



 



Example
-------




| ns |
| --- |
| // Prints out a historical RIND value
double value = RIND(3, 10)[5];
Print("RIND value of 5 bars ago is " + value.ToString()); |



 


 


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