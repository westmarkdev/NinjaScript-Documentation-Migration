










 


Close







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?close.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [PriceSeries<double>](priceseries.htm) &gt;
Close | [Previous page](priceseries.htm)
[Return to chapter overview](priceseries.htm)










Definition
----------


A collection of historical bar close prices.


 


Property Value
--------------


A ISeries<double> type object. Accessing this property via an index value [int barsAgo] returns a double value representing the price of the referenced bar.


 




|  |
| --- |
| Note: When an indicator uses another indicator as input series, Close will represent the closing price of the input series' input series. For example, if MyCustomIndicator uses an ADX as input series, then referencing Close[0] in MyCustomIndicator will provide the Close price for the ADX's input series. |



 


Syntax
------


Close  

Close[int barsAgo]




Examples
--------




| ns |
| --- |
| // OnBarUpdate method
protected override void OnBarUpdate()
{
     // Evaluates if the current close is greater than the prior bar close
     if (Close[0] &gt; Close[1])
         Print("We had an up day");
} |






 
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
 
 
 



</double></double></t></double></t>