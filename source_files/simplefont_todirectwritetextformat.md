










 


ToDirectWriteTextFormat()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?simplefont_todirectwritetextformat.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [SimpleFont](simplefont_class.htm) &gt;
ToDirectWriteTextFormat() | [Previous page](simplefont_applyto.htm)
[Return to chapter overview](simplefont_class.htm)










Definition
----------


Converts a [SimpleFont](simplefont_class.htm) object to a [SharpDX](sharpdx.htm) compatible font which can be used for chart rendering.


 




|  |
| --- |
| Note:  For more information please see the educational resource on [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering.htm) |





Method Return Value
-------------------


A [DirectWrite.TextFormat](sharpdx_directwrite_textformat.htm) object
---------------------------------------------------------------------


 




|  |
| --- |
| Warning:  The returned DirectWrite.TextFormat object should be disposed of immediately when finished drawing text. |



 


 


Syntax
------


<simplefont>.ToDirectWriteTextFormat()


 


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Set text to chart label simple font object
   SharpDX.DirectWrite.TextFormat textFormat = chartControl.Properties.LabelFont.ToDirectWriteTextFormat();
 
   // use the textFormat in a RenderTarget.DrawText() or DrawTextLayout() method
 
   // do not forget to dispose text format when finished
   textFormat.Dispose();
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
 
 
 



</simplefont>