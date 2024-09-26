










 


ConvertFromVerticalPixels







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?convertfromverticalpixels.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartingExtensions](chartingextensions.htm) &gt;
ConvertFromVerticalPixels | [Previous page](convertfromhorizontalpixels.htm)
[Return to chapter overview](chartingextensions.htm)










Definition
----------


Converts a y-axis pixel coordinate from device pixels to application pixels.





|  |
| --- |
| Note:  For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](working_with_pixel_coordinates.htm) educational resource. |





Method Return Value
-------------------


A double representing a y-coordinate value in terms of application pixels



Syntax
------


ChartingExtensions.ConvertFromVerticalPixels(this int x, PresentationSource target)  

<int>.ConvertFromVerticalPixels(PresentationSource target)


 




|  |  |
| --- | --- |
| x | The vertical int coordinates in device pixels to convert |
| target | The [PresenationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion
 
Note:  For Charts, see [ChartControl.PresentationSource](presentationsource.htm) |





Example
-------




| ns |
| --- |
| int applicationPixelY;
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Obtain the application-pixel coordinate corresponding to a device-pixel Y value of 500
   applicationPixelY = ChartingExtensions.ConvertFromVerticalPixels(500, ChartControl.PresentationSource);
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
 
 
 



</int>