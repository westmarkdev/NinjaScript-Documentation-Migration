










 


n Bars Down







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?n_bars_down.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
n Bars Down | [Previous page](net_change_display.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Evaluates for n number of consecutive lower closes. Returns a value of 1 when the condition is true or 0 when false.


 


 


Syntax
------


NBarsDown(int barCount, bool barDown, bool lowerHigh, bool lowerLow)  

NBarsDown(ISeries<double> input, int barCount, bool barDown, bool lowerHigh, bool lowerLow)


 


Returns default value  

NBarsDown(int barCount, bool barDown, bool lowerHigh, bool lowerLow)[int barsAgo]  

NBarsDown(ISeries<double> input, bool barCount, int barDown, bool lowerHigh, bool lowerLow)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| barCount | The number of required consecutive lower closes |
| barDown | Each bar's open must be less than the close; true or false |
| lowerHigh | Consecutive lower highs required; true or false |
| lowerLow | Consecutive lower lows required; true or false |



 


 


Example
-------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
   // Evaluates if we have 3 consecutive lower closes
   double value = NBarsDown(3, true, true, true)[0];
 
   if (value == 1)
       Print("We have three consecutive lower closes");
} |



 


 


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