










 


GetTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?gettime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetTime() | [Previous page](getsessionendtime.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the time stamp at the current bar index value.


 




|  |
| --- |
| Note: This method will return what is displayed in the chart's data box.  For formatting purposes, the value returned is NOT guaranteed be equal to the [TimeSeries](timeseries.htm) value.  If you are using daily bars and need the session end time, you should use [Bars.GetSessionEndTime()](getsessionendtime.htm) instead. |



 


 


Method Return Value
-------------------


A DateTime structure that represents the time stamp at the desired bar index.



Syntax
------


Bars.GetTime(int index)


 


Parameters
----------




|  |  |
| --- | --- |
| index | An int representing an absolute bar index value |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
   // loop through only the rendered bars on the chart
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the time stamp at the selected bar index value
     DateTime timeValue = Bars.GetTime(barIndex);
     Print("Bar #" + barIndex + " time stamp is " + timeValue);
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
 
 
 



