










 


DisplayOnChartsMenus







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?displayonchartsmenus.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
DisplayOnChartsMenus | [Previous page](createanchor.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Determines if the drawing tool displays in the chart's drawing tool menus.


 


Property Value
--------------


A bool value, when true the drawing tool will be created on the chart's drawing tool menu; otherwise false.  Default value is true.


 


Syntax
------


DisplayOnChartsMenus


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name                 = @"My Drawing Tool";
     DisplayOnChartsMenus = true;
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
 
 
 



