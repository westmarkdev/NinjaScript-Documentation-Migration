










 


Moving Average - Mesa Adaptive (MAMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_mesa_adaptive.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Mesa Adaptive (MAMA) | [Previous page](moving_average_-_kaufmans_adap.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The MESA Adaptive Moving Average (MAMA) adapts to price movement in an entirely new and unique way. The adaptation is based on the rate change of phase as measured by the Hilbert Transform Discriminator. The advantage of this method of adaptation is that it features a fast attack average and a slow decay average so that composite average rapidly ratchets behind price changes and holds the average value until the next ratchet occurs. 


 


 


Syntax
------


MAMA(double fastLimit, double slowLimit)  

MAMA(ISeries<double> input, double fastLimit, double slowLimit)


 


Returns MAMA value  

MAMA(double fastLimit, double slowLimit)[int barsAgo]  

MAMA(ISeries<double> input, double fastLimit, double slowLimit)[int barsAgo]


 


Returns Fama (Following Adaptive Moving Average) value  

MAMA(double fastLimit, double slowLimit).Fama[int barsAgo]  

MAMA(ISeries<double> input, double fastLimit, double slowLimit).Fama[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| fastLimit | Upper limit of the alpha value |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| slowLimit | Lower limit of the alpha value |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period MAMA using default price type
double value = MAMA(0.5, 0.05).Default[0];
Print("The current MAMA value is " + value.ToString());
 
// Prints the current value of a 20 period Fama using high price type
double value = MAMA(High, 0.5, 0.05).Fama[0];
Print("The current Fama value is " + value.ToString()); |



 


 


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