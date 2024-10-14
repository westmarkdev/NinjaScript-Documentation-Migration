










 


Directional Movement (DM)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?directional_movement_dm.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Directional Movement (DM) | [Previous page](darvas.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Same as the [ADX](average_directional_index_adx.htm) indicator with the addition of the +DI and -DI values. 


 


... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dmi.asp)


 


Syntax
------


DM(int period)  

DM(ISeries<double> input, int period)


 


Returns default ADX value  

DM(int period)[int barsAgo]  

DM(ISeries<double> input, int period)[int barsAgo]


 


Returns +DI value  

DM(int period).DiPlus[int barsAgo]  

DM(ISeries<double> input, int period).DiPlus[int barsAgo]


 


Returns -DI value  

DM(int period).DiMinus[int barsAgo]  

DM(ISeries<double> input, int period).DiMinus[int barsAgo]


 


 


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
| // Prints the current value of a 20 period +DI using default price type
double value = DM(20).DiPlus[0];
Print("The current +DI value is " + value.ToString()); |



 


 


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
 
 
 



</double></double></double></double>