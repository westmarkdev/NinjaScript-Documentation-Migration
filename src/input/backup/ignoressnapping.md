










 


IgnoresSnapping







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ignoressnapping.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IgnoresSnapping | [Previous page](icon_drawingtool.htm)
[Return to chapter overview](drawing_tools.htm)










Definition  

Determines if the drawing tool chart anchor's will use the chart's Snap Mode mouse coordinates.


 


Property Value
--------------


A bool value which when true the drawing tool ignores snapping; otherwise false.  Default is set to false.


 


Syntax
------


IgnoresSnapping



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          IgnoresSnapping = true; // Set this to true to receive non-snapped mouse coordinates
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
 
 
 



