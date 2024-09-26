










 


Rate of Change (ROC)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rate_of_change_roc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Rate of Change (ROC) | [Previous page](range_indicator_rind.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Rate of Change (ROC) indicator is a very simple yet effective momentum oscillator that measures the percent change in price from one period to the next. The ROC calculation compares the current price with the price n periods ago.


 


... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_ROC.htm)


 


 


Syntax
------


ROC(int period)  

ROC(ISeries<double> input, int period)


 


Returns default value  

ROC(int period)[int barsAgo]  

ROC(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period ROC using default price type
double value = ROC(20)[0];
Print("The current ROC value is " + value.ToString());
 
// Prints the current value of a 20 period ROC using high price type
double value = ROC(High, 20)[0];
Print("The current ROC value is " + value.ToString()); |



 


 


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