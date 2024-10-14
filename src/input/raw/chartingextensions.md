










 


ChartingExtensions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartingextensions.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
ChartingExtensions | [Previous page](timepainted.htm)
[Return to chapter overview](chart.htm)










The ChartingExtensions class provides helper methods useful for converting a pixel coordinate from application-specific pixels (i.e., WPF coordinates) to Device Independent Pixels. 


 




|  |
| --- |
| Note:  More information about the differences between application pixels and device pixels can be found on the [Working with Pixel Coordinates](working_with_pixel_coordinates.htm) page. |





ChartingExtensions Helper Methods
---------------------------------




|  |  |
| --- | --- |
| [ConvertFromHorizontalPixels](convertfromhorizontalpixels.htm) | Converts a horizontal coordinate (x) from device pixels to application pixels |
| [ConvertFromVerticalPixels](convertfromverticalpixels.htm) | Converts a vertical coordinate (y) from device pixels to application pixels |
| [ConvertToHorizontalPixels](converttohorizontalpixels.htm) | Converts a horizontal coordinate (x) in application pixels to device pixels |
| [ConvertToVerticalPixels](converttoverticalpixels2.htm) | Converts a vertical coordinate (y) in application pixels to device pixels |






 
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
 
 
 



