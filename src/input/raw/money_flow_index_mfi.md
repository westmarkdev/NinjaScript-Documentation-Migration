










 


Money Flow Index (MFI)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?money_flow_index_mfi.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Money Flow Index (MFI) | [Previous page](momentum.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Money Flow Index (MFI) is a momentum indicator that is similar to the Relative Strength Index (RSI) in both interpretation and calculation. However, MFI is a more rigid indicator in that it is volume-weighted, and is therefore a good measure of the strength of money flowing in and out of a security.


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_MFI.htm)


 


 


Syntax
------


MFI(int period)  

MFI(ISeries<double> input, int period)


 


Returns default value  

MFI(int period)[int barsAgo]  

MFI(ISeries<double> input, int period)[int barsAgo] 


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |



 



Example
-------




| ns |
| --- |
| // Prints the current value of a 20 period MFI using default price type
double value = MFI(20)[0];
Print("The current MFI value is " + value.ToString()); |



 


 


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