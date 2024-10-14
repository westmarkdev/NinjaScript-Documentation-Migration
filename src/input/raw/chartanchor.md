










 


ChartAnchor







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartanchor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
ChartAnchor | [Previous page](attachedto.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Defines objects used by Drawing Tools which represent a point on the chart where the Drawing Tool is located.


 


Syntax
------


class ChartAnchor


 


Constructors
------------




|  |  |
| --- | --- |
| new ChartAnchor() | Initializes a new instance of the ChartAnchor object |
| new ChartAnchor(DateTime time, double price, [ChartControl](chartcontrol.htm) chartControl) | Initializes a new instance of the ChartAnchor object using time, price, and relative chart control |
| new ChartAnchor(DateTime time, double yValue, int currentBar, [ChartControl](chartcontrol.htm) chartControl) | Initializes a new instance of the ChartAnchor object using time, y-axis coordinates, current bar, and relative chart control |



 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [CopyDataValues()](copydatavalues.htm) | Copies the ChartAnchor time and price values from on anchor to another |
| [DisplayName](displayname.htm) | A string value which sets the name prefix used for all properties for a chart anchor |
| [DrawingTool](drawingtool.htm) | The drawing tool which owns a chart anchor |
| [DrawnOnBar](drawnonbar.htm) | Gets the current bar value that the chart anchor is drawn by a NinjaScript object.   |
| [GetPoint()](getpoint.htm) | Returns a chart anchor's data points. |
| [IsBrowsable](isbrowsable.htm) | A bool value determining the anchor is visible on the UI. |
| [IsEditing](isediting.htm) | A bool value determining the anchor is currently being edited |
| [IsNinjaScriptDrawn](isninjascriptdrawn.htm) | Indicates if the chart anchor was drawn by a NinjaScript object |
| [IsXPropertiesVisible](isypropertyvisibile.htm) | A bool value determining the X properties are visible on the UI |
| [IsYPropertyVisible](isypropertyvisibile.htm) | A bool value determining the Y data value is visible on the UI |
| [MoveAnchor()](moveanchor.htm) | Moves a Chart Anchor's x and y values from start point by a delta point amount. |
| [MoveAnchorX()](moveanchorx.htm) | Moves an anchor x values from start point by a delta point amount |
| [MoveAnchorY()](moveanchory.htm) | Moves an anchor y values from start point by a delta point amount |
| [Price](price.htm) | Determines price value the chart anchor is drawn. |
| [SlotIndex](barindex.htm) | Indicates the nearest bar slot where anchor is drawn.   |
| [Time](time.htm) | Determines date/time value the chart anchor is drawn. |
| [UpdateFromPoint()](updatefrompoint.htm) | Updates an anchor's x and y values from a given point (in device pixels) |
| [UpdateXFromPoint()](updatexfrompoint.htm) | Updates an anchor's X values from a given point (in device pixels) |
| [UpdateYFromPoint()](updateyfrompoint.htm) | Updates an anchor's Y value from a given point (in device pixels) |





Examples
--------




| ns |
| --- |
| public ChartAnchor MyAnchor { get; set; }   // declares the "MyAnchor" ChartAnchor object
 
public override IEnumerable<chartanchor> Anchors { get { return new[] { MyAnchor }; } } //adds the "MyAnchor" ChartAnchor object to a collection of anchors used to interact with your anchors
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Description = @"Drawing tool example";
     Name = "SampleDrawingTool";
 
     MyAnchor = new ChartAnchor(); //creates a new instances of the ChartAnchor object
     MyAnchor.IsEditing   = true;
     MyAnchor.DrawingTool = this;
     MyAnchor.IsBrowsable = false;
   }
}
 
public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   if (DrawingState == DrawingState.Editing)
   {
     if (MyAnchor.IsEditing)
     {
         //if anchor is editing, update anchor point
         dataPoint.CopyDataValues(MyAnchor);
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
 
 
 



</chartanchor>