










 


AxisYRightWidth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?axisyrightwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
AxisYRightWidth | [Previous page](axisyleftwidth.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Measures the distance (in pixels) between the y-axis and the right edge of a chart.



Property Value
--------------


 A double representing the number of pixels separating the y-axis and the right edge of the chart.



Syntax
------


 <chartcontrol>.AxisYRightWidth



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
     // Print the number of pixels between the y-axis and the right edge of the chart
     double rightWidth = chartControl.AxisYRightWidth;
     Print(rightWidth);
} |



 


 


Based on the image below, AxisYRightWidth reveals that the space between the y-axis and the right edge of the chart is 53 pixels on this chart.


 


![ChartControl_AxisYRightWidth](chartcontrol_axisyrightwidth.png)


 




|  |
| --- |
| Note: When there are no right-justified data series on a chart, AxisYRightWidth will return 0, as there will be no space between the y-axis and the right edge. |






 
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