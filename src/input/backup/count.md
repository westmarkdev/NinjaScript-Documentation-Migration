










 


Count







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?count.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnBarUpdate()](onbarupdate.htm) &gt;
Count | [Previous page](calculate.htm)
[Return to chapter overview](onbarupdate.htm)










Definition
----------


The total number of bars or data points.



Property Value
--------------


An int value representing the the total number of bars.


 


Syntax
------


Count


 



Examples
--------




| ns |
| --- |
| //If there are less than 365 bars on the chart, text indicates how many bars are on the chart
if (Count &lt; 365)
{
 Draw.TextFixed(this, "tag1", "There are " + Count + " bars on the chart", TextPosition.BottomRight);
} |




 




|  |
| --- |
| Tip: [CurrentBar](currentbar.htm) value is guaranteed to be &lt;= Count - 1. This is because of the NinjaTrader multi-threaded architecture, the Count value can have additional bars as inflight ticks come in to the system. |






 
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
 
 
 



