










 


DrawingTool







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawingtool.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
DrawingTool | [Previous page](displayname.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


The DrawingTool object which owns a chart anchor.


 


Property Value
--------------


A IDrawingTool object representing the owner of the chart anchor


 


Syntax
------


<chartanchor>.DrawingTool
=========================



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {   
Name = "SampleDrawingTool";       
MyAnchor = new ChartAnchor();
MyAnchor.DrawingTool = this; //NinjaTrader.NinjaScript.DrawingTools.SampleDrawingTool
     }
     else if (State == State.Configure)
     {
 
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
 
 
 



</chartanchor>