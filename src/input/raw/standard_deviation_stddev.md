










 


Standard Deviation (StdDev)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?standard_deviation_stddev.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Standard Deviation (StdDev) | [Previous page](r_squared.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


In probability theory and statistics, standard deviation is a measure of the variability or dispersion of a population, a data set, or a probability distribution. A low standard deviation indicates that the data points tend to be very close to the same value (the mean), while high standard deviation indicates that the data are “spread out” over a large range of values.


 


... Courtesy of [Wikipedia](http://en.wikipedia.org/wiki/Standard_deviation)


 


 


Syntax
------


StdDev(int period)  

StdDev(ISeries<double> input, int period)


 


Returns default value  

StdDev(int period)[int barsAgo]  

StdDev(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period StdDev using default price type
double value = StdDev(20)[0];
Print("The current StdDev value is " + value.ToString());
 
// Prints the current value of a 20 period StdDev using high price type
double value = StdDev(High, 20)[0];
Print("The current StdDev value is " + value.ToString()); |



 


 


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