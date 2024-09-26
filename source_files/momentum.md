










 


Momentum







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?momentum.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Momentum | [Previous page](minimum_min.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


By measuring the amount that a security's price has changed over a given time span, the Momentum indicator provides an indication of a market's velocity and to some degree, a measure of the extent to which a trend still holds true. It can also be helpful in spotting likely reversal points.


 


 


Syntax
------


Momentum(int period)  

Momentum(ISeries<double> input, int period)


 


Returns default value


Momentum(int period)[int barsAgo]  

Momentum(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period Momentum using default price type
double value = Momentum(20)[0];
Print("The current Momentum value is " + value.ToString());
 
// Prints the current value of a 20 period Momentum using high price type
double value = Momentum(High, 20)[0];
Print("The current Momentum value is " + value.ToString()); |



 


 


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