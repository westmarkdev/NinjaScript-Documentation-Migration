










 


IsSelected







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isselected.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
IsSelected | [Previous page](isinhittest.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Indicates a chart object is currently selected. When this property is set to true in a [DrawingTool](drawingtool.htm), the [GetSelectionPoints()](getselectionpoints.htm) will be called.  


 


Property Value
--------------


This property returns true to indicate that the chart object is selected; otherwise, false. Default set to false.  


 




|  |
| --- |
| Warning:  This property value is ONLY guaranteed to be settable by the object to which it belongs (e.g., from within a [DrawingTool](drawing_tools.htm)).  Modifying its value from an external object (such as attempting to set a DrawingTool.IsSelected from an indicator) can result in the property automatically returning the value handled by its source.  In other words, unless you are working with a chart object type directly (e.g., building a custom drawing tool), the IsSelected property should be considered read-only. |



 


 


Syntax
------


IsSelected



Examples
--------




|  |
| --- |
| ns Reading the IsSelected property from an indicator |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   foreach(DrawingTool drawTool in DrawObjects)
   {
     // only apply logic below to types of "Rectangle")
     if(drawTool.GetType().ToString().Contains("Rectangle"))
     {
         // safely cast as dynamic type at run-time
         dynamic myRect = drawTool;
 
         // Changes the brush to pink to indicating selected
         if(drawTool.IsSelected)
         {            
           myRect.AreaBrush = Brushes.Pink;      
         }               
         // otherwise, set back to default value on next render pass
         else myRect.AreaBrush = Brushes.CornflowerBlue;   
      
     }
   }
} |







|  |
| --- |
| ns Explicitly setting the IsSelected property from a DrawingTool type |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{            
   if(DrawingState == DrawingState.Building)
   {
     if(dataPoint.IsEditing)
     {               
         // do something            
     }  
 
     // when done editing anchor, set the state to normal and unselect the drawing object
     else if(dataPoint.IsEditing)
     {
         DrawingState = DrawingState.Normal;
         IsSelected = false;
     }
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
 
 
 



