










 


Keltner Channel







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?keltner_channel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Keltner Channel | [Previous page](forecast_oscillator_fosc.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Keltner Channel indicator is based on volatility using a pair of values placed as an "envelope" around the data field.


 


 


Syntax
------


KeltnerChannel(double offsetMultiplier, int period)  

KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period)


 


Returns midline value  

KeltnerChannel(double offsetMultiplier, int period)[int barsAgo]  

KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period)[int barsAgo]


 


Returns upper band value  

KeltnerChannel(double offsetMultiplier, int period).Upper[int barsAgo]  

KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period).Upper[int barsAgo]


 


Returns lower band value  

KeltnerChannel(double offsetMultiplier, int period).Lower[int barsAgo]  

KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period).Lower[int barsAgo]


 


 


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
| // Prints the current upper value of a 20 period KeltnerChannel using default price type
double value = KeltnerChannel(1.5, 20).Upper[0];
Print("The current KeltnerChannel upper value is " + value.ToString());
 
// Prints the current lower value of a 20 period KeltnerChannel using high price type
double value = KeltnerChannel(High, 1.5, 20).Lower[0];
Print("The current KeltnerChannel lower value is " + value.ToString()); |



 


 


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