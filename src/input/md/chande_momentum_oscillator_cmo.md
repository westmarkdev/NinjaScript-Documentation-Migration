










 


Chande Momentum Oscillator (CMO)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chande_momentum_oscillator_cmo.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Chande Momentum Oscillator (CMO) | [Previous page](chaikin_volatility.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Chande Momentum Oscillator was developed by Tushar S. Chande and is described in the 1994 book The New Technical Trader by Tushar S. Chande and Stanley Kroll. This indicator is a modified [RSI](relative_strength_index_rsi.htm). Where the RSI divides the upward movement by the net movement (up / (up + down)), the CMO divides the total movement by the net movement ((up - down) / (up + down)). Values under -50 indicate oversold conditions while values over 50 indicate overbought conditions.


 


 


Syntax
------


CMO(int period)  

CMO(ISeries<double> input, int period)


 


Returns default value  

CMO(int period)[int barsAgo]  

CMO(ISeries<double> input, int period)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | The number of bars to include in the calculation |



 



Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period CMO using default price type
double value = CMO(20)[0];
Print("The current CMO value is " + value.ToString());
 
// Prints the current value of a 20 period CMO using high price type
double value = CMO(High, 20)[0];
Print("The current CMO value is " + value.ToString()); |



 


 


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