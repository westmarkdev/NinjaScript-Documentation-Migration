










 


AddBar()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?addbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
AddBar() | [Previous page](bars_type.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Adds new data points for the Bars Type.


 


Syntax
------


AddBar(Bars bars, double open, double high, double low, double close, DateTime time, long volume)


AddBar(Bars bars, double open, double high, double low, double close, DateTime time, long volume, double bid, double ask)


 


Parameters
----------




|  |  |
| --- | --- |
| bars | The Bars object of your bars type |
| open | A double value representing the open price |
| high | A double value representing the high price |
| low | A double value representing the low price |
| close | A double value representing the close price |
| time | A DateTime value representing the time |
| volume | A long value representing the volume |
| bid | A double value representing the bid price |
| ask | A double value representing the ask price |



 


 



Examples
--------




| ns |
| --- |
| AddBar(bars, open, high, low, close, time, (long)Math.Min(volumeTmp, bars.BarsPeriod.Value)); |






 
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
 
 
 



