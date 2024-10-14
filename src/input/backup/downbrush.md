










 


DownBrush







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?downbrush.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
DownBrush | [Previous page](chartstyletype.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the down bars for the ChartStyle.


 




|  |
| --- |
| Note: This Windows Presentation Forms (WPF) implementation of the Brush class is not directly used to paint bars on the chart. Instead it is converted to a SharpDX Brush in the [DownBrushDX](downbrushdx.htm) property. This property is used to capture user input for changing brush colors. |



 


 


Property  Value
---------------


A [WPF](https://msdn.microsoft.com/en-us/library/ms754130(v=vs.110).aspx) Brush object used to paint the down bars


 


Syntax
------


DownBrush


 


Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.Configure)
   {
       // Set a new name for the DownBrush property
       SetPropertyName("DownBrush", "DecliningBrush");
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
 
 
 



