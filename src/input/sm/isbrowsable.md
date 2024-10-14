










 


IsBrowsable







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isbrowsable.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
IsBrowsable | [Previous page](getpoint.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Determines if the anchor are visible on the UI.  When set to true, the anchors Y and X values can be viewed from the Drawing Objects properties.


 


Property Value
--------------


A bool value which when true will display the anchor data values from the drawing object properties; otherwise false.  Default value is true.


 


Syntax
------


<chartanchor>.IsBrowsable
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
MyAnchor.IsBrowsable = true;
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