










 


IsInHitTest







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isinhittest.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
IsInHitTest | [Previous page](forcerefresh.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Indicates a user is currently clicking in the chart panel in which the calling script resides. 





|  |
| --- |
| Note: In addition to the example below, IsInHitTest can also be tested directly on chart objects (for example, myHorizontalLine.IsInHitTest). In this case, the IsInHitTest property of a specific object will refer to the panel in which the calling script resides, even if the calling script resides in a different panel than the object itself. |




Property Value
--------------


This property returns true to indicate that the chart panel in which the script resides is being clicked on; otherwise, false. Default set to false.


 


Syntax
------


IsInHitTest



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{            
   if(IsInHitTest)
   {
       Print("user clicked on object");   
      
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
 
 
 



