










 


LowestBar()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?lowestbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
LowestBar() | [Previous page](least_recent_occurence_lro.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns the number of bars ago the lowest price value occurred within the specified look-back period. 



Method Return Value
-------------------


An int value representing a value of bars ago.


 


Syntax
LowestBar(ISeries<double> series, int period)
----------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| period | The number of bars to check for the test condition |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   // store the lowest bar ago value
   int lowestBar = LowestBar(Low, Bars.BarsSinceNewTradingDay);
   
   //evaluate low price from lowest bar ago value
   double lowestPrice = Low[lowestBar];         
   
   //Printed result:  Lowest price of the session: 2087.25 - occurred 362 bars ago
   Print(string.Format("Lowest price of the session: {0} - occurred {1} bars ago", lowestPrice, lowestBar));            
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