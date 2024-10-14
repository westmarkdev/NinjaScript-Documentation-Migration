










 


Double Stochastics







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?double_stochastics.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Double Stochastics | [Previous page](donchian_channel.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Double Stochastics is a variation of the [Stochastics](stochastics.htm) indicator developed by William Blau.


 


 


Syntax
------


DoubleStochastics(int period)  

DoubleStochastics(ISeries<double> input, int period)


 


Returns default value  

DoubleStochastics(int period)[int barsAgo]  

DoubleStochastics(ISeries<double> input, int period)[int barsAgo]


 


Returns %K value  

DoubleStochastics(int period).K[int barsAgo]  

DoubleStochastics(ISeries<double> input, int period).K[int barsAgo]


 


 


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
| // Prints the current value
double value = DoubleStochastics(10)[0];
Print("The current Double Stochastics value is " + value.ToString());
 
// Prints the current %K value
double value = DoubleStochastics(10).K[0];
Print("The current Double Stochastics %K value is " + value.ToString()); |



 


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