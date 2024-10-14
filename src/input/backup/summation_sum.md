










 


Summation (SUM)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?summation_sum.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Summation (SUM) | [Previous page](stochastics_rsi_stochrsi.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Returns the sum of the values taken over a specified period.


 


 


Syntax
------


SUM(int period)  

SUM(ISeries<double> input, int period)


 


Returns default value  

SUM(int period)[int barsAgo]  

SUM(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period SUM using default price type
double value = SUM(20)[0];
Print("The current SUM value is " + value.ToString());
 
// Prints the current value of a 20 period SUM using high price type
double value = SUM(High, 20)[0];
Print("The current SUM value is " + value.ToString()); |



 


 


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