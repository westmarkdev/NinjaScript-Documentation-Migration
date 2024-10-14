










 


IsFalling()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?falling.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
IsFalling() | [Previous page](highestbar.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Evaluates a falling condition which is true when the current value is less than the value of 1 bar ago. 



Method Return Value
-------------------


This method returns true if a falling condition is present; otherwise, false.


 


Syntax  

IsFalling(ISeries<double> series)



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
   // If the 20 period SMA is falling (in downtrend) go short
   if (IsFalling(SMA(20)))
       EnterShort();               
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