










 


Adaptive Price Zone (APZ)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?adaptive_price_zone_apz.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Adaptive Price Zone (APZ) | [Previous page](accumulation_distribution_adl.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Adaptive Price Zone indicator from the S&amp;C, September 2006 article "Trading With An Adpative Price Zone" by Lee Leibfarth is a set of bands based on a short term double smooth exponential moving average. The bands form a channel that surrounds the average price and tracks price fluctuations quickly, especially in volatile markets. As price crosses above the zone it can signal an opportunity to sell in anticipation of a reversal. As price crosses below the zone it can signal an opportunity to buy in anticipation of a reversal. 


 


 


Syntax
------


APZ(double bandPct, int period)   

APZ(ISeries<double> input, double bandPct, int period)


 


Returns upper band value   

APZ(double bandPct, int period).Upper[int barsAgo]   

APZ(ISeries<double> input, double bandPct, int period).Upper[int barsAgo]


 


Returns lower band value   

APZ(double bandPct, int period).Lower[int barsAgo]   

APZ(ISeries<double> input, double bandPct, int period).Lower[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| bandPct | The number of standard deviations |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 



Example
-------




| ns |
| --- |
| // Prints the current upper band value of a 20 period APZ
double upperValue = APZ(2, 20).Upper[0];
Print("The current APZ upper value is " + upperValue.ToString()); |



 


 


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