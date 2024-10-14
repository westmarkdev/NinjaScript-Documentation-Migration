










 


ConvertToVerticalPixels







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?converttoverticalpixels2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartingExtensions](chartingextensions.htm) &gt;
ConvertToVerticalPixels | [Previous page](converttohorizontalpixels.htm)
[Return to chapter overview](chartingextensions.htm)










Definition
----------


Converts a y-axis pixel coordinate from application pixels to device pixels.





|  |
| --- |
| Note:  For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](working_with_pixel_coordinates.htm) educational resource. |





Method Return Value
-------------------


An int representing a y-coordinate value in terms of device pixels



Syntax
------


ChartingExtensions.ConvertToVerticalPixels(this double x, PresentationSource target)  

<double>.ConvertToVerticalPixels(PresentationSource target)


 




|  |  |
| --- | --- |
| x | The vertical double coordinates in application pixels to convert |
| target | The [PresenationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion
 
Note:  For Charts, see [ChartControl.PresentationSource](presentationsource.htm) |





Example
-------




| ns |
| --- |
| int devicePixelY;
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Obtain the device-pixel coordinate corresponding to an application-pixel Y value of 500
   devicePixelY = ChartingExtensions.ConvertToVerticalPixels(500, ChartControl.PresentationSource);
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
 
 
 



</double>