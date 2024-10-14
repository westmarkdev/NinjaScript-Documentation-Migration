










 


IsYAxisDisplayedOverlay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyaxisdisplayedoverlay.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
IsYAxisDisplayedOverlay | [Previous page](isyaxisdisplayedleft.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates an object on the chart is using the Overlay scale justification.



Property Value
--------------


A boolean value. When True, indicates that one or more objects on the chart are using the Overlay scale justification; otherwise False.



Syntax
------


<chartcontrol>.IsYAxisDisplayedOverlay



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the value of IsYAxisDisplayedOverlay
   Print("Is Overlay used? " + chartControl.IsYAxisDisplayedOverlay);
} |



 


 


Based on the image below, IsYAxisDisplayedOverlay confirms that the an object on the chart, in this case an SMA indicator, is using the Overlay scale justification.


 


![ChartControl_IsXAxisDisplayedOverlay](chartcontrol_isxaxisdisplayedoverlay.png)





 
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
 
 
 



</chartcontrol>