










 


OnRenderTargetChanged()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onrendertargetchanged.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
OnRenderTargetChanged() | [Previous page](onrender.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Called whenever a Chart's [RenderTarget](rendertarget.htm) is created or destroyed. [OnRenderTargetChanged()](onrendertargetchanged.htm) is used for creating / cleaning up resources such as a SharpDX.Direct2D1.Brush used throughout your NinjaScript class.


 




|  |
| --- |
| Notes:   
1. A [RenderTarget](rendertarget.htm) will be created and destroyed several times during the lifetime of a chart.  For example, a user resizing the chart would cause the RenderTarget to be re-created as the chart is rendered to reflect the new dimensions.  Another example is when a user clicks on the chart as a RenderTarget is used during [hit testing](isinhittest.htm).  Since there are multiple RenderTargets, you MUST ensure the resource being used belongs to the destination target.  In practice, all you need to understand is if you are using a device resource (e.g., custom [SharpDX Brush)](brushes.htm) throughout different event methods, you should recreate these resource during OnRenderTargetChanged() which ensures the device resource is updated correctly as the devices context changes.
2. During initialization your NinjaScript indicators and strategies are guaranteed to see [State.Configure](onstatechange.htm) before OnRenderTargetChanged() would be called. |





Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


You may override the method in your indicator with the following syntax:


 


public override void OnRenderTargetChanged()  

{  

}


 




|  |
| --- |
| Warning:  Each DirectX [render target](rendertarget.htm) requires its own brushes. You must create a brushes directly in [OnRender()](onrender.htm) or using OnRenderTargetChanged().  If you do not you will receive an error at run time similar to: 
 
"A direct X error has occured while rendering the chart: HRESULT: [0x88990015], Module: [SharpDX.Direct2D1], ApiCode: [D2DERR\_WRONG\_RESOURCE\_DOMAIN/WrongResourceDomain], Message: The resource was realized on the wrong render target. : Each DirectX render target requires its own brushes. You must create brushes directly in OnRender() or using OnRenderTargetChanged().
 
Please see the example below on using OnRenderTargetChanged() with brush that needs to be recalculated, or [OnRender()](onrender.htm) for an example of recreating a static brush. |



 


 


Parameters
----------


This method does not accept any parameters


 




|  |
| --- |
| Tips: 
1.If you are exclusively using resources in OnRender() (e.g., not passing values from OnStateChange() or other events) you only need to create and dispose of the resource in OnRender().  The OnRenderTargetChanged() concepts illustrated below would not need to be applied.2.For a walk through for using the SharpDX RenderTarget, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering.htm) |



 


 


Examples
--------




| ns Recalculating a SharpDX Brush conditionally in OnBarUpdate() |
| --- |
| private SharpDX.Direct2D1.Brush dxBrush = null; // the SharpDX brush used for rendering      
private System.Windows.Media.SolidColorBrush brushColor; // used to determine the color of the brush conditionally
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "OnRenderTargetChanged Example";
     IsOverlay = false;
   }
}
 
protected override void OnBarUpdate()
{
   if (Close[0] &gt; Open[0])
   {
     brushColor = Brushes.Green;
   }
 
   else if (Close[0] &lt; Open[0])
   {
     brushColor = Brushes.Red;
   }
 
   else brushColor = Brushes.Blue;
}
 
public override void OnRenderTargetChanged()
{
   // if dxBrush exists on first render target change, dispose of it
   if (dxBrush != null)
   {
     dxBrush.Dispose();
   }
 
   // recalculate dxBrush from value calculated in OnBarUpdated when RenderTarget is recreated
   if (RenderTarget != null)
     dxBrush = brushColor.ToDxBrush(RenderTarget);
}
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // fill a custom SharpDX rectangle using the dx brush
   RenderTarget.FillRectangle(new SharpDX.RectangleF(ChartPanel.X, ChartPanel.Y, ChartPanel.W, ChartPanel.H), dxBrush);
} |



 


 




| ns Recalculating a SharpDX Brush based on user input |
| --- |
| private SharpDX.Direct2D1.Brush dxBrush = null; // the SharpDX brush used for rendering      
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "OnRenderTargetChanged Example";
     IsOverlay = false;
     UserBrush = Brushes.Red; // user selection pushed to the UI
   }
}
public override void OnRenderTargetChanged()
{
   // if dxBrush exists on first render target change, dispose of it
   if (dxBrush != null)
   {
     dxBrush.Dispose();
   }
 
   // recalculate dxBrush from user defined brush when RenderTarget is recreated
   if (RenderTarget != null)
     dxBrush = UserBrush.ToDxBrush(RenderTarget);
}
 
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // fill a custom SharpDX rectangle using the dx brush
   RenderTarget.FillRectangle(new SharpDX.RectangleF(ChartPanel.X, ChartPanel.Y, ChartPanel.W, ChartPanel.H), dxBrush);
}
 
[XmlIgnore]
public Brush UserBrush { get; set; } // brush selection set by user in UI
 
[Browsable(false)]
public string MyBrushSerialize // string used to serialize selection set by user in UI
{
   get { return Serialize.BrushToString(UserBrush); }
   set { UserBrush = Serialize.StringToBrush(value); }
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
 
 
 



