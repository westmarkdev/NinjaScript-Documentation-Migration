










 


KeyReversalUp







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?keyreversalup.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
KeyReversalUp | [Previous page](keyreversaldown.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Returns a value of 1 when the current close is greater than the prior close and the current low has penetrated the lowest low of the last n bars.


 


 


Syntax
------


KeyReversalUp(int period)  

KeyReversalUp(ISeries<double> input, int period)


 


Returns default value  

KeyReversalUp(int period)[int barsAgo]  

KeyReversalUp(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // If we get a reversal over the past 10 bars go long
if (KeyReversalUp(10)[0] == 1)
   EnterLong(); |



 


 


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