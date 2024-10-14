










 


GetVolume()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getvolume.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
GetVolume() | [Previous page](gettime.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Returns the volume at the selected bar index value.


 


Method Return Value
-------------------


A long value represents the volume at the desired bar index.



Syntax
------


Bars.GetVolume(int index)


 


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
   // loop through all the rendered bars on the chart
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the volume value at the selected bar index value
     long volumeValue = Bars.GetVolume(barIndex);
     Print("Bar #" + barIndex + " volume value is " + volumeValue);
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
 
 
 



