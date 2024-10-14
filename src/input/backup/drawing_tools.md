










 


Drawing Tools







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawing_tools.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Drawing Tools | [Previous page](upbrushdx.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Drawing Tools can be used to render custom shapes to a point on the chart to represent various information.  The methods and properties covered in this section are unique to custom Drawing Tools development. Following is an index of the documented properties and methods related to drawing tools.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AddPastedOffset()](addpastedoffset.htm) | A [virtual method](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) which is called every time a Drawing Tool is copied and pasted to a chart |
| [Anchors](anchors.htm) | Creates a collection of Chart Anchors which will represent various points of the drawing tool |
| [AttachedTo](attachedto.htm) | An object which holds information regarding where the drawing tool is attached |
| [ChartAnchor](chartanchor.htm) | Defines objects used by Drawing Tools which represent a point on the chart where the Drawing Tool is located |
| [ConvertToVerticalPixels](converttoverticalpixels.htm) | Used to convert the cursor position (pixels) to device pixels represented on the Y axis of the chart |
| [CreateAnchor()](createanchor.htm) | Used to create a new chart anchor at a specified mouse point |
| [DisplayOnChartsMenus](displayonchartsmenus.htm) | Determines if the drawing tool should be listed in the chart's drawing tool menus |
| [Dispose()](dispose.htm) | Releases any device resources used for the drawing tool |
| [DrawingState](drawingstate.htm) | Represents the current state of the drawing tool in order to perform various actions, such as building, editing, or moving |
| [DrawnBy](drawnby.htm) | Represents the NinjaScript object by which the drawing tool was created |
| [GetAttachedToChartBars()](getattachedtochartbars.htm) | Returns information which relate to the underlying bars series in which the drawing tool is attached |
| [GetClosestAnchor()](getclosestanchor.htm) | Returns the closest chart anchor within a specified maximum distance from the mouse cursor |
| [GetCursor()](getcursor.htm) | An event driven method which is called when a chart object is selected |
| [GetSelectionPoints()](getselectionpoints.htm) | Returns the chart object's data points where the user can interact |
| [Icon](icon_drawingtool.htm) | The shape which displays next to the drawing tool menu item |
| [IgnoresSnapping](ignoressnapping.htm) | Determines if the drawing tool chart anchor's will use the chart's Snap Mode mouse coordinates |
| [IgnoresUserInput](ignoresuserinput.htm) | Determines if the drawing tool can be clicked on by the user |
| [IsAttachedToNinjaScript](isattachedtoninjascript.htm) | Indicates if the drawing tool is currently [attached to](attachedto.htm) a NinjaScript object (such an indicator or a strategy) |
| [IsGlobalDrawingTool](isglobaldrawingtool.htm) | Indicates if the drawing tool is currently set as a Global Drawing object |
| [IsLocked](islocked.htm) | Determines if the drawing tool should be be locked in place |
| [IsUserDrawn](isuserdrawn.htm) | Indicates if the drawing tool was manually drawn by a user |
| [OnBarsChanged()](onbarschanged.htm) | An event driven method which is called any time the underlying bar series have changed for the chart where the drawing tool resides |
| [OnMouseDown()](onmousedown.htm) | An event driven method which is called any time the mouse pointer over the chart control has the mouse button pressed |
| [OnMouseMove()](onmousemove.htm) | An event driven method which is called any time the mouse pointer is over the chart control and a mouse is moving |
| [OnMouseUp()](onmouseup.htm) | An event driven method is called any time the mouse pointer is over the chart control and a mouse button is being released |
| [SupportsAlerts](supportsalerts.htm) | Indicates if the drawing tool can be used for manually configured alerts through the UI |
| [ZOrderType](zordertype.htm) | Determintes the order in which the drawing tool will be rendered |






 
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
 
 
 



