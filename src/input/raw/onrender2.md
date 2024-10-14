










 


OnRender()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onrender2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
OnRender() | [Previous page](iseditable.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


Used to draw custom content to a Market Analyzer Column, such as a graph.  


 
This method is called during the following conditions:
--------------------------------------------------------


 


•The Market Analyzer is scrolled

•The user changes the Market Analyzer's properties through the Properties menu

•The Market Analyzer first loads (e.g. restoring from a workspace)

•The height / width of the Market Analyzer window changes

•A user re-sizes the content area by dragging the splitter between the columns

 




|  |
| --- |
| Note:  While similar to a Chart Indicator's [OnRender()](onrender.htm) method, the Market Analyzer Column uses [WPF Drawing Context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) class, rather than the SharpDX library used for [chart rendering](rendering.htm).  Concepts between these two methods are guaranteed to be different. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
You must override the method in your Market Analyzer column with the following syntax:
---------------------------------------------------------------------------------------------


 


protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)   

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| dc | The [drawing context](https://msdn.microsoft.com/en-us/library/system.windows.media.drawingcontext(v=vs.110).aspx) for the column |
| renderSize | The rendering size for the column |



 


 




|  |
| --- |
| Tip:  In order to force OnRender() to be called under a specific condition, call the [OnPropertyChanged()](onpropertychanged.htm) method which will force the entire column to repaint.  This approach should be used instead of calling OnRender() directly. |





Examples
--------




| ns |
| --- |
| protected override void OnRender(DrawingContext dc, System.Windows.Size renderSize)
{
   // Rendering logic for our Market Analyzer column
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
 
 
 



