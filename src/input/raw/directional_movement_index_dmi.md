










 


Directional Movement Index (DMI)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?directional_movement_index_dmi.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
Directional Movement Index (DMI) | [Previous page](directional_movement_dm.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


An indicator developed by J. Welles Wilder for identifying when a definable trend is present in an instrument. That is, the DMI tells whether an instrument is trending or not.


 


...Courtesy of [FMLabs](http://www.fmlabs.com/reference/default.htm?url=DX.htm)


 


Syntax
------


DMI(int period)  

DMI(ISeries<double> input, int period)


 


Returns default value  

DMI(int period)[int barsAgo]  

DMI(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // Prints the current value of a 20 period DMI using default price type
double value = DMI(20)[0];
Print("The current DMI value is " + value.ToString()); |



 


 


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