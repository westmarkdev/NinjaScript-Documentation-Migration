










 


AxisYLeftWidth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?axisyleftwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
AxisYLeftWidth | [Previous page](axisxheight.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Measures the distance (in pixels) between the y-axis and the left edge of a chart.



Property Value
--------------


 A double representing the number of pixels separating the y-axis and the left edge of the chart.



Syntax
------


 <chartcontrol>.AxisYLeftWidth



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
     // Print the number of pixels between the y-axis and the left edge of the chart
     double leftWidth = chartControl.AxisYLeftWidth;
     Print(leftWidth);
} |



 


 


Based on the image below, AxisYLeftWidth reveals that the space between the y-axis and the left edge of the chart is 53 pixels on this chart.


 


![ChartControl_AxisYLeftWidth](chartcontrol_axisyleftwidth.png)


 




|  |
| --- |
| Note: When there are no left-justified data series on a chart, AxisYLeftWidth will return 0, as there will be no space between the y-axis and the left margin. |






 
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
 
 
 



</chartcontrol>