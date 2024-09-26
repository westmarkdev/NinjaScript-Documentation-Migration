










 


Linear Regression Intercept







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?linear_regression_intercept.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Linear Regression Intercept | [Previous page](linear_regression.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


The Linear Regression Intercept provides the intercept value of the [Linear Regression](linear_regression.htm) trendline.


 


 


Syntax
------


LinRegIntercept(int period)  

LinRegIntercept(ISeries<double> input, int period)


 


Returns default value  

LinRegIntercept(int period)[int barsAgo]  

LinRegIntercept(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current intercept value of a 20 period LinReg using default price type
double value = LinRegIntercept(20)[0];
Print("The current intercept value is " + value.ToString());
 
// Prints the current intercept value of a 20 period LinReg using high price type
double value = LinRegIntercept(High, 20)[0];
Print("The current intercept value is " + value.ToString()); |



 


 


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