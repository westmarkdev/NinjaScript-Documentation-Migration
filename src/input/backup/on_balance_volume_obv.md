










 


On Balance Volume (OBV)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?on_balance_volume_obv.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
On Balance Volume (OBV) | [Previous page](n_bars_up.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


OBV is a simple indicator that adds a period's volume when the close is up and subtracts the period's volume when the close is down. A cumulative total of the volume additions and subtractions forms the OBV line. This line can then be compared with the price chart of the underlying security to look for divergences or confirmation.


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic-obv.htm)


 


 


Syntax
------


OBV()  

OBV(ISeries<double> input)


 


Returns default value  

OBV()[int barsAgo]  

OBV(ISeries<double> input)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |



 


Example
-------




| ns |
| --- |
| // Prints the current value of OBV
double value = OBV()[0];
Print("The current OBV value is " + value.ToString()); |



 


 


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