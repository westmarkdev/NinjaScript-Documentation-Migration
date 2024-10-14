










 


DisplayName







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?displayname.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
DisplayName | [Previous page](copydatavalues.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Sets the display name prefix used for all properties for a chart anchor. 


 


Property Value
--------------


A string value that is used to identify the name for a corresponding anchor.  Default value is null.


 


Syntax
------


<chartanchor>.DisplayName
=========================



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {          
       MyAnchor = new ChartAnchor();
       MyAnchor.DisplayName = "MyChartAnchor";
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