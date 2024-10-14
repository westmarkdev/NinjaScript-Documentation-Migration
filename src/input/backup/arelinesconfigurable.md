










 


AreLinesConfigurable







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?arelinesconfigurable.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddLine()](addline.htm) &gt;
AreLinesConfigurable | [Previous page](addline.htm)
[Return to chapter overview](addline.htm)










Definition
----------


Determines if the [line](addline.htm)(s) used in an indicator are configurable from within the indicator dialog window.


 



Property Value
--------------


A bool which true if any indicator line(s) are configurable; otherwise, false. Default set to true.


 


Syntax
------


AreLinesConfigurable


 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         AddLine(Brushes.Gray, 30, "Lower");
         AreLinesConfigurable = false; // Indicator lines are not configurable
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
 
 
 



