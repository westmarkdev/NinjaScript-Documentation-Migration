










 


BarBrush







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barbrush.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
BarBrush | [Previous page](backbrushesall.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Sets the brush used for painting the color of a price bar's body.



Property Value
--------------


A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object that represents the color of this price bar.


 




|  |
| --- |
| Tip: To set the price bar color to an empty color which uses the default bar color property, set the BarBrush to null for that bar. |



 


Syntax
------


BarBrush


 




|  |
| --- |
| Warning:  You may have up to 65,535 unique BarBrush instances, therefore, using [static predefined brushes](working_with_brushes.htm) should be favored.  Alternatively,  in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created. |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Sets the bar color to yellow
     BarBrush = Brushes.Yellow;
 
     // Sets the brush used for the bar color to its default color as defined in the chart properties dialog
     BarBrush = null;
 
     // Sets the bar color to yellow if the 20 SMA is above the 50 SMA and the closing
     // price is above the 20 SMA (see image below)
     if (SMA(20)[0] &gt; SMA(50)[0] &amp;&amp; Close[0] &gt; SMA(20)[0])
         BarBrush = Brushes.Yellow;
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
 
 
 



