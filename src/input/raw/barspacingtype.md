










 


BarSpacingType







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barspacingtype.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarSpacingType | [Previous page](chartcontrol_barsarray.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the type of bar spacing used for the primary [Bars](bars.htm) object on the chart.



Property Value
--------------


An enum representing one of the values below:


 




|  |  |
| --- | --- |
| EquidistantSingle | Indicates Equidistant Bar Spacing is used, and only one Bars object exists on the chart |
| EquidistantMulti | Indicates Equidistant Bar Spacing is used, and more than one Bars objects exist on the chart |
| TimeBased | Indicates Time-Based bar spacing is used |





Syntax
------


<chartcontrol>.BarSpacingType



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the type of bar spacing used on the chart
   Print(chartControl.BarSpacingType);
} |



 


 


Based on the image below, BarSpacingType confirms that there are multiple Bars objects configured on the chart, and that the chart is set to Equidistant Bar Spacing:


 


![ChartControl_BarSpacingType](chartcontrol_barspacingtype.png)





 
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