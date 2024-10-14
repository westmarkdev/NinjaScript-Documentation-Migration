










 


Slope()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?slope.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Analytical](market_data.htm) &gt;
Slope() | [Previous page](most_recent_occurence_mro.htm)
[Return to chapter overview](market_data.htm)










Definition
----------


Returns a measurement of the steepness of a price series (y value) measured by the change over time (x value).  The return value can also be thought of as the ratio between the startBarsAgo and endBarsAgo parameters passed to the method.  


 


The formula which is returned from the parameters passed is:  

 


(series[endBarsAgo] - series[startBarsAgo]) / (startBarsAgo - endBarsAgo)





|  |
| --- |
| Note:  The return value should NOT be confused with the angle (or radians) of a line that displays on the chart.   |



 


 


Method Return Value
-------------------


This method returns a double value indicating the slope of a line;  A value of 0 returns if the either the startBars or endBars parameters are less than 0 or both parameters are of equal value.


 


Syntax
Slope(ISeries<double> series, int startBarsAgo, int endBarsAgo)
----------------------------------------------------------------------





|  |
| --- |
| Warning:  The "startBarsAgo" parameter MUST be greater than the "endBarsAgo" parameter  |



 


 


Parameters
----------




|  |  |
| --- | --- |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |
| startBarsAgo | The starting point of a series to be evaluated |
| endBarsAgo | The ending point of a series to be evaluated |



 


 




|  |
| --- |
| Tip: Thinking in degrees, for example a 1 to -1 return range would translate to 45 to -45. To convert you could look into working with this formula - Math.Atan(Slope) * 180 / Math.PI |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   // Prints the slope of the 20 period simple moving average of the last 10 bars
   Print(Slope(SMA(20), 10, 0)); 
  
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