










 


GetSessionEndTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getsessionendtime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetSessionEndTime() | [Previous page](getopen.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the daily bar session ending time stamp relative to the current bar index value.


 




|  |
| --- |
| Note:  This method is ONLY intended for bars built from daily data.   If called on intraday data, GetSessionEndTime() will return the [Bars.GetTime()](gettime.htm) value. |



 


 


Method Return Value
-------------------


A DateTime structure that represents the daily bars ending time stamp at the desired bar index; intraday bars will return the time stamp at the current bar index value.



Syntax
------


Bars.GetSessionEndTime(int index)


 


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
   for (int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the time stamp at the selected bar index value
     DateTime timeValue = Bars.GetSessionEndTime(barIndex);
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
 
 
 



