










 


Properties







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale_properties.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
Properties | [Previous page](panelindex.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Represents a number of properties available to the Chart Scale which can be configured to change the appearance of the scale.


 


![ChartPanel_Properites](chartpanel_properites.png)


 


 




|  |
| --- |
| Warning:  These are UI properties which are designed to be set by a user.  Attempting to modify these values through a custom script is NOT guaranteed to take effect.   |





Property Values
---------------




|  |  |
| --- | --- |
| YAxisRangeType | An YAxisRangeType enum, possible values are:
•Automatic•Fixed |
| AutoScaleDateRangeType | An AutoScaleDateRangeType enum, possible values are:
•ScreenDateRange•EntireDateRangeSeriesOnly |
| HorizontalGridlinesCalculation | An YAxisRangeType enum, possible values are:
•Automatic•Fixed |
| HorizontalGridlinesIntervalType | A HorizontalGridlinesIntervalType enum, possible values are:
•Ticks•Points•Pips |
| HorizontalGridlinesInterval | A double value representing the vertical interval of the horizontal axis |
| AutoScaleMarginType | An AutoScaleMarginType enum, possible values are:
•Percent•Price |
| AutoScaleMarginLower | A double value representing the lowest margin used for the chart scale |
| AutoScaleMarginUpper | A double value representing the highest margin used for the chart scale |
| YAxisScalingType | An YAxisScalingType enum, possible values are:
•Linear•Logarithmic  |
| FixedScaleMax | A double representing the highest series value used for the chart scale when the scale is fixed |
| FixedScaleMin | A double representing the lowest series value used for the chart scale when the scale is fixed |




Syntax
------


<chartscale>.Properties


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   if (chartScale.Properties.YAxisScalingType == YAxisScalingType.Linear)
   {
     // do something
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
 
 
 



</chartscale>