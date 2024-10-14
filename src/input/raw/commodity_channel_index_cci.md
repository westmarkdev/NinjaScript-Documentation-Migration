










 


Commodity Channel Index (CCI)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?commodity_channel_index_cci.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Commodity Channel Index (CCI) | [Previous page](commitment-of-traders-(cot).htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Developed by Donald Lambert, the Commodity Channel Index (CCI) was designed to identify cyclical turns in commodities. The assumption behind the indicator is that commodities (or stocks or bonds) move in cycles, with highs and lows coming at periodic intervals.


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_CCI.html)


 


 


Syntax
------


CCI(int period)  

CCI(ISeries<double> input, int period)


 


Returns default value  

CCI(int period)[int barsAgo]  

CCI(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period CCI using default price type
double value = CCI(20)[0];
Print("The current CCI value is " + value.ToString());
 
// Prints the current value of a 20 period CCI using high price type
double value = CCI(High, 20)[0];
Print("The current CCI value is " + value.ToString()); |



 


 


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