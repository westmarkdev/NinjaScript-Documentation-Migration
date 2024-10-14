










 


IsNinjaScriptDrawn







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isninjascriptdrawn.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
IsNinjaScriptDrawn | [Previous page](isediting.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Indicates if the chart anchor was drawn by a NinjaScript object (such as an indicator or strategy).


 


Property Value
--------------


A bool value which returns true of the object was drawn by other NinjaScript object; otherwise false.  This property is read-only.


 


Syntax
------


<chartanchor>.IsNinjaScriptDrawn
================================


 


Examples
--------




| ns |
| --- |
| //unlocks the NinjaScript drawn object and allows the user to modify the anchor, while the NinjaScript object still 'owns' the object
protected override void OnBarUpdate()
{
     foreach(IDrawingTool dt in DrawObjects)
         {
           DrawingTools.Line sampleLine = dt as DrawingTools.Line;
            
           if (sampleLine != null &amp;&amp; sampleLine.StartAnchor.IsNinjaScriptDrawn)
           {
               sampleLine.IsLocked = false;
               Print(sampleLine.StartAnchor.ToString());
           }
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