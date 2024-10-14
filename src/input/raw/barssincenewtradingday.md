










 


BarsSinceNewTradingDay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barssincenewtradingday.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
BarsSinceNewTradingDay | [Previous page](bars.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the number of bars elapsed since the start of the trading day relative to the current bar processing.


 


Property Value
--------------


An int value representing the number of bars elapsed.  This property cannot be set.


 


Syntax
Bars.BarsSinceNewTradingDay
----------------------------------



Examples
--------




| ns |
| --- |
| // Only process strategy logic after five bars have posted since the start of the trading day
protected override void OnBarUpdate()
{
   if (Bars.BarsSinceNewTradingDay &gt;= 5)
   {
     //Strategy logic here
   }
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
 
 
 



