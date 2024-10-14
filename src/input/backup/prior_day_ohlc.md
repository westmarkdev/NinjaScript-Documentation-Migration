










 


Prior Day OHLC







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?prior_day_ohlc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Prior Day OHLC | [Previous page](price_oscillator.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The prior day (session) open, high, low and close values.


 




|  |
| --- |
| Note: Only use this indicator on intraday series. |




Syntax
------


PriorDayOHLC()  

PriorDayOHLC(ISeries<double> input)


 


Returns prior session open value  

PriorDayOHLC().PriorOpen[int barsAgo]  

PriorDayOHLC(ISeries<double> input).PriorOpen[int barsAgo]


 


Returns prior session high value  

PriorDayOHLC().PriorHigh[int barsAgo]  

PriorDayOHLC(ISeries<double> input).PriorHigh[int barsAgo]


 


Returns prior session low value  

PriorDayOHLC().PriorLow[int barsAgo]  

PriorDayOHLC(ISeries<double> input).PriorLow[int barsAgo]


 


Returns prior session close value  

PriorDayOHLC().PriorClose[int barsAgo]  

PriorDayOHLC(ISeries<double> input).PriorClose[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |



 


 


Example
-------




| ns |
| --- |
| // Prints the value of the prior session low
double value = PriorDayOHLC().PriorLow[0];
Print("The prior session low value is " + value.ToString()); |



 



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
 
 
 



</double></double></double></double></double>