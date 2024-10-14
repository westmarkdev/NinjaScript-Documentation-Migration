










 


PanelUI







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?panelui.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
PanelUI | [Previous page](onrendertargetchanged.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


The zero-based index of the chart panel in which the calling script is configured. 


 




|  |
| --- |
| Note: The "Panel" property configured in the Indicators or Strategies window on a chart is non-zero-based, while PanelUI is zero-based. For example, if an indicator is configured in Panel # 1 in the Indicators window, PanelUI will return an index of 0. If the indicator were configured in Panel # 4 in the Indicators window, PanelUI would return an index of 3. |




Property Value
--------------


An int value representing the panel the object is configured.  This property is read-only.


 


Syntax
------


PanelUI



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Print the zero-based panel index on which the script is configured
   Print("My object is on is on panel # " + PanelUI);
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
 
 
 



