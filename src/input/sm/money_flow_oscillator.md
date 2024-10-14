










 


Money Flow Oscillator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?money_flow_oscillator.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Money Flow Oscillator | [Previous page](money_flow_index_mfi.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Money Flow Oscillator measures the amount of money flow volume over a specific period. A move into positive territory indicates buying pressure while a move into negative territory indicates selling pressure.


 


Syntax
------


MoneyFlowOscillator(int period)


MoneyFlowOscillator(ISeries<double> input, int period)


 


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
| // Prints the current value of a 10 period Money Flow Oscillator
double value = MoneyFlowOscillator(10)[0];
Print("The current Money Flow Oscillator value is " + value.ToString()); |






 
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
 
 
 



</double>