










 


n Bars Up







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?n_bars_up.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
n Bars Up | [Previous page](n_bars_down.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Evaluates for n number of consecutive higher closes. Returns a value of 1 when the condition is true or 0 when false. 


 


 


Syntax
------


NBarsUp(int barCount, bool barUp, bool higherHigh, bool higherLow)  

NBarsUp(ISeries<double> input, int barCount, bool barUp, bool higherHigh, bool higherLow)


 


Returns default value  

NBarsUp(int barCount, bool barUp, bool higherHigh, bool higherLow)[int barsAgo]  

NBarsUp(ISeries<double> input, int barCount, bool barUp, bool higherHigh, bool higherLow)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| barCount | The number of required consecutive higher closes |
| barUp | Each bar's close must be higher than the open; true or false |
| higherHigh | Consecutive higher highs required; true or false |
| higherLow | Consecutive higher lows required; true or false |



 


 


Example
-------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
   // Evaluates if we have 3 consecutive higher closes
   double value = NBarsUp(3, true, true, true)[0];
 
   if (value == 1)
       Print("We have three consecutive higher closes");
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