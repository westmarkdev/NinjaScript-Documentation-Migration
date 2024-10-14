










 


BackBrush







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?backbrush.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
BackBrush | [Previous page](allowremovalofdrawobjects.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Sets the brush used for painting the chart panel's background color for the current bar.


 




|  |
| --- |
| Note: This property will only set the back color for the panel the indicator is running.  To set background color for all panels, please see the [BackBrushAll](backbrushall.htm) property. |



 


Property Value
--------------


A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object that represents the color of the current chart bar.


 


Syntax
------


BackBrush


 




|  |
| --- |
| Warning:  You may have up to 65,535 unique BackBrush instances, therefore, using [static predefined brushes](working_with_brushes.htm) should be favored.  Alternatively,  in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created. |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Sets the chart panel back color to pale green
     BackBrush = Brushes.PaleGreen;
 
     // Sets the back color to to null which will use the default color set in the chart properties dialog window
     BackBrush = null;
 
     // Sets the back color to maroon when the closing price is less than the 20 period SMA // and to lime green when above (see image below)
     BackBrush = SMA(20)[0] &gt;= Close[0] ? Brushes.Maroon : Brushes.LimeGreen;
} |



 


 


![MAPriceBars](mapricebars.png)





 
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
 
 
 



