










 


IsTransparent







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?istransparent.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
IsTransparent | [Previous page](icon_chartstyle.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


Indicates the bars in the ChartStyle are transparent.


 


Property Value
--------------


A bool which, when true, indicates that the UpBrush, DownBrush, and Stroke.Brush are all set to transparent. Returns false if any of the three are not transparent.


 


Syntax
------


IsTransparent


 


 


Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.Configure)
   {
       //Print a message if the UpBrush, DownBrush, and Stroke.Brush are all transparent
       if (IsTransparent)
           Print("All bars are currently set to transparent");
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
 
 
 



