










 


HighestBar()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?highestbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
HighestBar() | [Previous page](getmedian.htm)
[Return to chapter overview](market_data.htm)










Definition


Returns the number of bars ago the highest price value occurred within the specified look-back period. 



Method Return Value
-------------------


An int value representing a value of bars ago.


 


Syntax
HighestBar(ISeries<double> series, int period)
-----------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| period | The number of bars to include in the calculation |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   // store the highest bars ago value
   int highestBarsAgo = HighestBar(High, Bars.BarsSinceNewTradingDay);
   
   //evaluate high price from highest bars ago value
   double highestPrice = High[highestBarsAgo];         
   
   //Printed result:  Highest price of the session: 2095.5 - occurred 24 bars ago
   Print(string.Format("Highest price of the session: {0} - occurred {1} bars ago", highestPrice, highestBarsAgo));            
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