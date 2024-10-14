










 


Moving Average - Variable (VMA)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_variable_vma.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Variable (VMA) | [Previous page](moving_average_-_triple_expon2.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


A Variable Moving Average is an exponential moving average that automatically adjusts its smoothing percentage based on market volatility. Giving more weight to the current data increases sensitivity thus making it a better signal indicator for short and long term markets.


 


 


Syntax
------


VMA(int period, int volatilityPeriod)  

VMA(ISeries<double> input, int period, int volatilityPeriod)


 


Returns default value  

VMA(int period, int volatilityPeriod)[int barsAgo]  

VMA(ISeries<double> input, int period, int volatilityPeriod)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |
| volatilityPeriod | The number of bars used to calculate the [CMO](chande_momentum_oscillator_cmo.htm) based volatility index |



 



Examples
--------




| ns |
| --- |
| // OnBarUpdate method of a strategy
protected override void OnBarUpdate()
{
   // Print out the VMA value of lows 3 bars ago for fun
   double value = VMA(Low, 9, 9)[3];
   Print("The value is " + value.ToString());
 
   // Go long if price closes above the current VMA value
   if (Close[0] &gt; VMA(9, 9)[0])
       EnterLong();
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