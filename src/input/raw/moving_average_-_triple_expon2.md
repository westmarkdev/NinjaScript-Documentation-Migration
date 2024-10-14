










 


Moving Average - Triple Exponential (TRIX)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moving_average_-_triple_expon2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Moving Average - Triple Exponential (TRIX) | [Previous page](moving_average_-_triple_expone.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The triple exponential average (TRIX) indicator is an oscillator used to identify oversold and overbought markets, and it can also be used as a momentum indicator.


 


... Courtesy of [Investopedia](http://www.investopedia.com/articles/technical/02/092402.asp)


 


 


Syntax
------


TRIX(int period, int signalPeriod)  

TRIX(ISeries<double> input, int period, int signalPeriod)


 


Returns trix value  

TRIX(int period, int signalPeriod)[int barsAgo]  

TRIX(ISeries<double> input, int period, int signalPeriod)[int barsAgo]


 


Returns signal value  

TRIX(int period, int signalPeriod).Signal[int barsAgo]  

TRIX(ISeries<double> input, int period, int signalPeriod).Signal[int barsAgo]


 


 


Return Value
------------


double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.


 


 


Parameters
----------




|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |
| period | Number of bars used in the calculation |
| signalPeriod | Period for signal line |



 


 


Examples
--------




| ns |
| --- |
| // Prints the current value of a 20 period TRIX using default price type
double value = TRIX(20, 3).Default[0];
Print("The current TRIX value is " + value.ToString());
 
// Prints the current signal value of a 20 period TRIX using high price type
double value = TRIX(High, 20, 3).Signal[0];
Print("The current TRIX signal value is " + value.ToString()); |



 


 


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