










 


Relative Spread Strength (RSS)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?relative_spread_strength_rss.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Relative Spread Strength (RSS) | [Previous page](regression_channel.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Developed by Ian Copsey, Relative Spread Strength is a variation to the [Relative Strength Index](relative_strength_index_rsi.htm). 


 


 


Syntax
------


RSS(int eMA1, int eMA2, int length)


RSS(ISeries<double> input, int eMA1, int eMA2, int length)


 


Returns default value


RSS(int eMA1, int eMA2, int length)[int barsAgo]


RSS(ISeries<double> input, int eMA1, int eMA2, int length)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| eMA1 | First EMA's period |
| eMA2 | Second EMA's period |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| length | Number of bars used in the calculation |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of the RSS using default price type
double value = RSS(10, 40, 5)[0];
Print("The current RSS value is " + value.ToString());
 
// Prints the current value of the RSS using high price type
double value = RSS(High, 10, 40, 5)[0];
Print("The current RSS value is " + value.ToString()); |



 


 


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