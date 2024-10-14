










 


IsRising()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rising.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
IsRising() | [Previous page](falling.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Evaluates a rising condition which is true when the current value is greater than the value of 1 bar ago.



Method Return Value
-------------------


This method returns true if a rising condition is present; otherwise, false.



Syntax
IsRising(ISeries<double> series)
---------------------------------------



Parameters
----------




|  |  |
| --- | --- |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // If the 20 period SMA is rising (in uptrend) go long
   if (IsRising(SMA(20)))
       EnterLong();
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
 
 
 



</double></double>