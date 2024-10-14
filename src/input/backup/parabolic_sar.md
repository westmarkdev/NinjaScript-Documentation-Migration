










 


Parabolic SAR







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?parabolic_sar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Parabolic SAR | [Previous page](order_flow_vwap2.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The parabolic SAR is a technical indicator that is used by many traders to determine the direction of an asset's momentum and the point in time when this momentum has a higher-than-normal probability of switching directions.


 


... Courtesy of [Investopedia](http://www.investopedia.com/articles/technical/02/042202.asp)


 


 


Syntax
------


ParabolicSAR(double acceleration, double accelerationMax, double accelerationStep)


ParabolicSAR(ISeries<double> input, double acceleration, double accelerationMax, double accelerationStep)


 


 


Returns default value  

ParabolicSAR(double acceleration, double accelerationMax, double accelerationStep)[int barsAgo]  

ParabolicSAR(ISeries<double> input, double acceleration, double accelerationStep, double accelerationMax)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| acceleration | Acceleration value |
| accelerationStep | Step value used to increment acceleration value |
| accelerationMax | Max acceleration value |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |



 



Example
-------




| ns |
| --- |
| // Prints the current value of ParabolicSAR using default price type
double value = ParabolicSAR(0.02, 0.2, 0.02)[0];
Print("The current ParabolicSAR value is " + value.ToString()); |



 


 


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