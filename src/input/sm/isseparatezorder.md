










 


IsSeparateZOrder







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isseparatezorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
IsSeparateZOrder | [Previous page](isoverlay.htm)
[Return to chapter overview](chart.htm)










Definition
----------


Determines the [ZOrder](chart_zorder.htm) of the drawing object will be different than the NinjaScript object that drew it.  When false the drawing object will share the same ZOrder.


 


Property Value
--------------


This property returns true if the object is drawn on a separate ZOrder; otherwise, false. Default set to false.


 


Syntax
------


IsSeparateZOrder


 


 


Example
-------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Instantiate a Dot object
   Dot myDot = Draw.Dot(this, "NewDot", true, 5, High[5], Brushes.Black);
 
   // Set the Dot object to use a separate Z-Order than the indicator that created it
   myDot.IsSeparateZOrder = true;
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
 
 
 



