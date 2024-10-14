










 


Stochastics







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?stochastics.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Stochastics | [Previous page](standard_error_stderror.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Developed by George C. Lane in the late 1950s, the Stochastic Oscillator is a momentum indicator that shows the location of the current close relative to the high/low range over a set number of periods. Closing levels that are consistently near the top of the range indicate accumulation (buying pressure) and those near the bottom of the range indicate distribution (selling pressure). 


 


... Courtesy of [StockCharts](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:stochastic_oscillator_fast_slow_and_full)


 


 


Syntax
------


Stochastics(int periodD, int periodK, int smooth)  

Stochastics(ISeries<double> input, int periodD, int periodK, int smooth)


 


Returns %D value  

Stochastics(int periodD, int periodK, int smooth).D[int barsAgo]  

Stochastics(ISeries<double> input, int periodD, int periodK, int smooth).D[int barsAgo]


 


Returns %K value  

Stochastics(int periodD, int periodK, int smooth).K[int barsAgo]  

Stochastics(ISeries<double> input, int periodD, int periodK, int smooth).K[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| periodD | The period for the moving average of periodD |
| periodK |  The period for the moving average of periodK |
| smooth | The smoothing value to be used |



 



Examples
--------




| ns |
| --- |
| // Prints the current %D value
double value = Stochastics(7, 14, 3).D[0];
Print("The current Stochastics %D value is " + value.ToString());
 
// Prints the current %K value
double value = Stochastics(7, 14, 3).K[0];
Print("The current Stochastics %K value is " + value.ToString()); |



 


 


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
 
 
 



</double></double></double>