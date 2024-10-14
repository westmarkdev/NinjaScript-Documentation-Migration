










 


Stochastics RSI (StochRSI)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?stochastics_rsi_stochrsi.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Stochastics RSI (StochRSI) | [Previous page](stochastics_fast.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


This is an indicator on indicator implementation. It is simply a [Stochastics](stochastics.htm) indicator applied on [RSI](relative_strength_index_rsi.htm).


 


 


Syntax
------


StochRSI(int period)  

StochRSI(ISeries<double> input, int period)


 


Returns default value  

StochRSI(int period)[int barsAgo]  

StochRSI(ISeries<double> input, int period)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 


 


Example
-------




| ns |
| --- |
| // Evaluates if the current bar StochRSI value is greater than the value one bar ago
if (StochRSI(14)[0] &gt; StochRSI(14)[1])
   Print("Stochastics RSI is rising"); |



 


 


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