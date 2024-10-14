










 


Donchian Channel







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?donchian_channel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Donchian Channel | [Previous page](disparity_index.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


A moving average indicator developed by Richard Donchian. It plots the highest high and lowest low over a specific period.


 


 


Syntax
------


DonchianChannel(int period)  

DonchianChannel(ISeries<double> input, int period)


 


Returns mean value (middle band) at a specified bar index  

DonchianChannel(int period)[int barsAgo]  

DonchianChannel(ISeries<double> input, int period)[int barsAgo]


 


Returns upper band value at a specified bar index  

DonchianChannel(int period).Upper[int barsAgo]  

DonchianChannel(ISeries<double> input, int period).Upper[int barsAgo]


 


Returns lower band value at a specified bar index  

DonchianChannel(int period).Lower[int barsAgo]  

DonchianChannel(ISeries<double> input, int period).Lower[int barsAgo]


 


 


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
| // Prints the current upper value of a 20 period DonchianChannel using default price type
double value = DonchianChannel(20).Upper[0];
Print("The current DonchianChannel upper value is " + value.ToString());
 
// Note the above call with a barsAgo of 0 includes the current Upper channel in the value. If we want to check for example for a break of this value, storing the last bar's channel value would be needed.
double value = DonchianChannel(20).Upper[1];
         
if (High[0] &gt; value)
   Draw.ArrowUp(this, CurrentBar.ToString(), true, 0, Low[0] - TickSize, Brushes.Blue); |



 


 


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