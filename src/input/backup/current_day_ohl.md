










 


Current Day OHL







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?current_day_ohl.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Current Day OHL | [Previous page](correlation.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The current day (session) open, high and low values.


 




|  |
| --- |
| Note: Only use this indicator on intraday series. |




Syntax
------


CurrentDayOHL()  

CurrentDayOHL(ISeries<double> input)


 


Returns current session open value  

CurrentDayOHL().CurrentOpen[int barsAgo]  

CurrentDayOHL(ISeries<double> input).CurrentOpen[int barsAgo]


 


Returns current session high value  

CurrentDayOHL().CurrentHigh[int barsAgo]  

CurrentDayOHL(ISeries<double> input).CurrentHigh[int barsAgo]


 


Returns current session low value  

CurrentDayOHL().CurrentLow[int barsAgo]  

CurrentDayOHL(ISeries<double> input).CurrentLow[int barsAgo]


 


 


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
| // Prints the current value of the session low
double value = CurrentDayOHL().CurrentLow[0];
Print("The current session low value is " + value.ToString()); |



 


 


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