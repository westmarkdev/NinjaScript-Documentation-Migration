










 


Moving Average - Kaufman's Adaptive (KAMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_kaufmans_adap.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Kaufman's Adaptive (KAMA) | [Previous page](moving_average_-_hull_hma.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Developed by Perry Kaufman, this indicator is an EMA using an Efficiency Ratio to modify the smoothing constant, which ranges from a minimum of Fast Length to a maximum of Slow Length. 


 


 


Syntax
------


KAMA(int fast, int period, int slow)  

KAMA(ISeries<double> input, int fast, int period, int slow)


 


Returns default value  

KAMA(int fast, int period, int slow)[int barsAgo]  

KAMA(ISeries<double> input, int fast, int period, int slow)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| fast | Fast length |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |
| slow | Slow length |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period KAMA using default price type
double value = KAMA(2, 20, 30)[0];
Print("The current KAMA value is " + value.ToString());
 
// Prints the current value of a 20 period KAMA using high price type
double value = KAMA(High, 2, 20, 30)[0];
Print("The current KAMA value is " + value.ToString()); |



 


 


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