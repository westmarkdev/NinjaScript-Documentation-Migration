










 


GetMedian()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getmedian.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
GetMedian() | [Previous page](getcurrentbidvolume.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns the statistical median value of the specified series over the specified look-back period. This method sorts the values of the specified look back period in ascending order and return the middle value.  

 




|  |
| --- |
| Notes: 
1. This method should NOT be confused with [Median](median.htm) prices defined as (High + Low) / 2. This method returns the statistical median of a series.
2. If an even number is passed as the look-back period, the average of the two middle values in the sorted values will be returned.  |



 


 


Method Return Value
-------------------


A double value representing the median value of the series.


 


Syntax
GetMedian(ISeries<double> series, int lookBackPeriod)
------------------------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| lookBackPeriod | Number of bars back to include in the calculation |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |



 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   // Print the median price of the last 10 open prices 
   //(current open price + look back period's 9 open prices before that)
   double openMedian = GetMedian(Open, 9);         
   Print("The median of the last 10 open prices is: " + openMedian);      
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