










 


Moving Average - T3 (T3)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_t3_t3.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - T3 (T3) | [Previous page](moving_average_-_simple_sma.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The T3 is a type of moving average, or smoothing function. It is based on the DEMA. The T3 takes the DEMA calculation and adds a vfactor which is between zero and 1. The resultant function is called the GD, or Generalized DEMA. A GD with vfactor of 1 is the same as the DEMA. A GD with a vfactor of zero is the same as an Exponential Moving Average. The T3 typically uses a vfactor of 0.7.


 


... Courtesy of [FMLabs](http://www.fmlabs.com/reference/default.htm?url=T3.htm)


 


 


Syntax
------


T3(int period, int tCount, double vFactor)


T3(ISeries<double> input, int period, int tCount, double vFactor)


 


Returns default value


T3(int period, int tCount, double vFactor)[int barsAgo]


T3(ISeries<double> input, int period, int tCount, double vFactor)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |
| tCount | Number of smooth iterations |
| vFactor | A multiplier fudge factor |



 


 


Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period T3 using default price type
double value = T3(20, 3, 0.7)[0];
Print("The current T3 value is " + value.ToString());
 
// Prints the current value of a 20 period T3 using high price type
double value = T3(High, 20, 3, 0.7)[0];
Print("The current T3 value is " + value.ToString()); |



 


 


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