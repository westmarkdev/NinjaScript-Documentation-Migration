










 


KeyReversalDown







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?keyreversaldown.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [System Indicator Methods](indicators.htm) &gt;
KeyReversalDown | [Previous page](keltner_channel.htm)
[Return to chapter overview](indicators.htm)










Description
-----------


Returns a value of 1 when the current close is less than the prior close and the current high has penetrated the highest high of the last n bars.


 


 


Syntax
------


KeyReversalDown(int period)  

KeyReversalDown(ISeries<double> input, int period)


 


Returns default value  

KeyReversalDown(int period)[int barsAgo]  

KeyReversalDown(ISeries<double> input, int period)[int barsAgo]


 


 


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
| // If we get a reversal over the past 10 bars go short
if (KeyReversalDown(10)[0] == 1)
   EnterShort(); |



 


 


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