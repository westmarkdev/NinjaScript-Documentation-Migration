










 


ConvertToHorizontalPixels







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?converttohorizontalpixels.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartingExtensions](chartingextensions.htm) &gt;
ConvertToHorizontalPixels | [Previous page](convertfromverticalpixels.htm)
[Return to chapter overview](chartingextensions.htm)










Definition
----------


Converts an x-axis pixel coordinate from application pixels to device pixels.





|  |
| --- |
| Note:  For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](working_with_pixel_coordinates.htm) educational resource. |





Method Return Value
-------------------


An int representing an x-coordinate value in terms of device pixels



Syntax
------


ChartingExtensions.ConvertToHorizontalPixels(this double x, PresentationSource target)  

<double>.ConvertToHorizontalPixels(PresentationSource target)


 




|  |  |
| --- | --- |
| x | The horizontal double coordinates in application pixels to convert |
| target | The [PresenationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion
 
Note:  For Charts, see [ChartControl.PresentationSource](presentationsource.htm) |




Example
-------




| ns |
| --- |
| int devicePixelX;
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Obtain the device-pixel coordinate corresponding to an application pixel X-value of 500
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
 
 
 



</double>