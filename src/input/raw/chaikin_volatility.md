










 


Chaikin Volatility







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chaikin_volatility.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Chaikin Volatility | [Previous page](chaikin_oscillator.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Chaikin Volatility Indicator is the difference between two moving averages of a volume weighted accumulation-distribution line. By comparing the spread between a security's high and low prices, it quantifies volatility as a widening of the range between the high and the low price.


 


 


Syntax
------


ChaikinVolatility(int mAPeriod, int rOCPeriod)  

ChaikinVolatility(ISeries<double> input, int mAPeriod, int rOCPeriod)  

   

Returns default value  

ChaikinVolatility(int mAPeriod, int rOCPeriod)[int barsAgo]  

ChaikinVolatility(ISeries<double> input, int mAPeriod, int rOCPeriod)[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| mAPeriod | Number of bars used in the moving average calculation |
| rOCPeriod | Number of bars used in the rate of change calculation  |



 



Example
-------




| ns |
| --- |
| // Prints the current value of the 20 period Chaikin Volatility
double value = ChaikinVolatility(20, 20)[0];
Print("The current Chaikin Volatility value is " + value.ToString()); |



 


 


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