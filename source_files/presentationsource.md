










 


PresentationSource







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?presentationsource.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
PresentationSource | [Previous page](mousedownpoint.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Provides a reference to the base window in which the chart is rendered. PresentationSource can be used when converting application pixels to/from device pixels via the helper methods in the [ChartingExtensions](chartingextensions.htm) class.



Property Value
--------------


A [PresentationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) object representing the base window in which the chart is rendered.



Syntax
------


ChartControl.PresentationSource



Example
-------




| ns |
| --- |
| int devicePixelX;
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Obtain the device-pixel coordinate corresponding to an application-pixel X value of 500
   devicePixelX = ChartingExtensions.ConvertToHorizontalPixels(500, ChartControl.PresentationSource);
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
 
 
 



