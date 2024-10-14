










 


ChartScale







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
ChartScale | [Previous page](y_coordinate_chartpanel.htm)
[Return to chapter overview](chart.htm)










The ChartScale class includes a range of properties related to the Y-Axis values of the [ChartPanel](chartpanel.htm) on which the calling script resides.  The ChartScale can be configured to Right, Left, or Overlay.


 


![ChartScale_1](chartscale_1.png)


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [GetPixelsForDistance()](getpixelsfordistance.htm) | Returns the number of device pixels between the value passed to the method representing a series point value on the chart scale |
| [GetValueByY()](getvaluebyy.htm) | Returns the series value on the chart scale determined by a y pixel coordinate on the chart |
| [GetValueByYWpf()](getvaluebyywpf.htm) | Returns the series value on the chart scale determined by a WPF coordinate on the chart |
| [GetYByValue()](getybyvalue.htm) | Returns the chart's y-pixel coordinate on the chart determined by a series value represented on the chart scale |
| [GetYByValueWpf()](getybyvaluewpf.htm) | Returns a WPF coordinate on the chart determined by a series value represented on the chart scale |
| [Height](height.htm) | Indicates the overall distance (from top to bottom) of the chart scale in device pixels |
| [IsVisible](chartscale_isvisible.htm) | Indicates if the chart scale is viewable on the UI |
| [MaxMinusMin](maxminusmin.htm) | The difference between the chart scale's [MaxValue](chartscale_maxvalue.htm) and [MinValue](chartscale_minvalue.htm) represented as a y value |
| [MaxValue](chartscale_maxvalue.htm) | The highest displayed value on the chart scale |
| [MinValue](chartscale_minvalue.htm) | The lowest rendered value on the chart scale |
| [PanelIndex](panelindex.htm) | The panel on which the chart scale resides |
| [Properties](chartscale_properties.htm) | Represents a number of properties available to the Chart Scale which can be configured to change the appearance of the scale |
| [ScaleJustification](chartscale_scalejustification.htm) | Indicates the location of the chart scale relative to the chart control |
| [Width](width.htm) | Indicates the overall distance (from left to right) of the chart scale in device pixels |






 
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
 
 
 



