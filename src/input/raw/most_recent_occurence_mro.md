﻿










 


Most Recent Occurrence (MRO)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?most_recent_occurence_mro.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
Most Recent Occurrence (MRO) | [Previous page](lowestbar.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns the number of bars ago that the test condition evaluated to true within the specified look back period expressed in bars.  The MRO() method starts from the current bar works away (backward) from it. 





|  |
| --- |
| Note: This method does NOT work on [multi-series](multi-time_frame__instruments.htm) strategies and indicators.  |





Method Return Value
-------------------


An int value representing the number of bars ago. Returns a value of -1 if the specified test condition did not evaluate to true within the look-back period.


 


Syntax
------


MRO(Func<bool> condition, int instance, int lookBackPeriod)
-----------------------------------------------------------





|  |
| --- |
| Warnings:  
1.  The "instance" parameter MUST be greater than 0.  
2.  The "lookBackPeriod" parameter MUST be greater than 0.  
3.  Please check the Log tab for any other exceptions that may be thrown by the condition function parameter. |





Parameters
----------




|  |  |
| --- | --- |
| condition | A true/false expression |
| instance | The occurrence to check for (1 is the most recent, 2 is the 2nd most recent, etc...) |
| lookBackPeriod | The number of bars to look back to check for the test condition. The test evaluates on the current bar and the bars within the look-back period. |



 


 




|  |
| --- |
| Tip:  The syntax for the "condition" parameter uses [lambda expression](http://msdn.microsoft.com/en-us/library/bb397687.aspx) syntax |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Prints the high price of the most recent up bar over the last 10 bars (current bar + look back period's 9 bars before that)
   int barsAgo = MRO(() =&gt; Close[0] &gt; Open[0], 1, 9);
   if (barsAgo &gt; -1)
       Print("The bar high was " + High[barsAgo]);   
} |



 


   

See Also  

[Least Recent Occurrence(LRO)](least_recent_occurence_lro.htm)





 
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
 
 
 



</bool>