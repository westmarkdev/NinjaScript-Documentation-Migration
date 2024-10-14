










 


OnRender()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onrender.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
OnRender() | [Previous page](oncalculateminmax.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Used to render custom drawing to a chart from various chart objects, such as an [Indicator](indicator.htm), [DrawingTool](drawingtool.htm) or [Strategy](strategy.htm). 


 




|  |
| --- |
| Notes: 
1.This method uses the 3rd party SharpDX library to render custom Direct2D Text and Shapes.  For a walk through for using the SharpDX, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering.htm)2.The OnRender() method frequently runs once the [State](state.htm) has reached State.Realtime in response to market data updates or a user interacting with the chart (e.g., clicking, resizing, rescaling, etc.)3.For performance optimizations, the timing of the calls to OnRender() are buffered to at least 250ms, and re-renders once internal logic determines that values may be out-of-date.  See also [ForceRefresh()](forcerefresh.htm) for more details4.When using the [Strategy Analyzer](strategy_analyzer.htm), OnRender() does NOT call until you switch to the "Chart" display and renders from State.Terminated.  As a result, this method should NOT be relied on for historical Strategy backtesting logic and should ONLY be used for rendering purposes5.Unlike market data events and strategy order related events, there is NO guarantee that the barsAgo indexer used for [Series<t>](seriest.htm) objects are in sync with the current bars in progress.  As a result, you should favor using an absolute index method to look up values (e.g., [<series>.GetValueAt()](getvalueat.htm), [Bars.GetOpen()](getopen.htm), etc)6.While OnRender() is an excellent means for customizing and enhancing indicators and strategies, its application can easily be abused, resulting in unforeseen performance issues which you may not catch until the right conditions (e.g., in the hands of your users during an FOMC event)7.Please limit any calculations or algorithms you may be tempted run in OnRender() simply to rendering. You should always favor precomputed values and store them for rendering later as the preferred approach to working with the OnRender() method (e.g., reusing brushes, passing values from [OnBarUpdate()](onbarupdate.htm), etc.).  See also [OnRenderTargetChanged()](onrendertargetchanged.htm) method for more information on reusing Brushes8.If you are using this method as an opportunity to "hook" onto a user related event, such as when a user selects a 3rd party control, you should alternatively consider using the events of that control independent of official NinjaScript events. See also [TriggerCustomEvent()](triggercustomevent.htm) |



 


 


Method Return Value
-------------------


This method does not return a value



Syntax
------


protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  

{  

     

}


 




|  |
| --- |
| Warning:  Each DirectX [render target](rendertarget.htm) requires its own brushes. You must create a brushes directly in OnRender() or using [OnRenderTargetChanged()](onrendertargetchanged.htm).  If you do not you will receive an error at run time similar to: 
 
"A direct X error has occured while rendering the chart: HRESULT: [0x88990015], Module: [SharpDX.Direct2D1], ApiCode: [D2DERR\_WRONG\_RESOURCE\_DOMAIN/WrongResourceDomain], Message: The resource was realized on the wrong render target. : Each DirectX render target requires its own brushes. You must create brushes directly in OnRender() or using OnRenderTargetChanged().
 
Please see [OnRenderTargetChanged()](onrendertargetchanged.htm) for examples of a brush that needs to be recalculated, or the example below of recreating a static brush. |



 



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) object (the chart's bar-related properties and x-axis) |
| chartScale | A [ChartScale](chartscale.htm) object (the chart's y-axis) |



 


 




|  |
| --- |
| Tips:  
•Please see the help guide topic on [Working with Brushes](working_with_brushes.htm) for general information on using brushes and advanced brush concepts•If you are using standard [Plots](plots.htm) along with custom rendering from an indicator or strategy, you will need to ensure to call the base.OnRender() method for those plots to display. |



 


 


Examples
--------




| ns Using a static SharpDX Brush to render a rectangle on the chart panel |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // implicitly recreate and dispose of brush on each render pass
   using (SharpDX.Direct2D1.SolidColorBrush dxBrush = new SharpDX.Direct2D1.SolidColorBrush(RenderTarget, SharpDX.Color.Blue))
   {
     RenderTarget.FillRectangle(new SharpDX.RectangleF(ChartPanel.X, ChartPanel.Y, ChartPanel.W, ChartPanel.H), dxBrush);
   }
} |



 


 




| ns Calling the base.OnRender() method to ensure Plots are rendered along with custom render logic |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // call the base.OnRender() to ensure standard Plots work as designed
   base.OnRender(chartControl, chartScale);
 
   // custom render logic
} |



 


 




| ns Using multiple SharpDX objects to override the default plot appearance |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // get the starting and ending bars from what is rendered on the chart
   float startX = chartControl.GetXByBarIndex(ChartBars, ChartBars.FromIndex);
   float endX = chartControl.GetXByBarIndex(ChartBars, ChartBars.ToIndex);
 
   // Loop through each Plot Values on the chart
   for (int seriesCount = 0; seriesCount &lt; Values.Length; seriesCount++)
   {
     // get the value at the last bar on the chart (if it has been set)
     if (Values[seriesCount].IsValidDataPointAt(ChartBars.ToIndex))
     {
         double plotValue = Values[seriesCount].GetValueAt(ChartBars.ToIndex);
 
         // convert the plot value to the charts "Y" axis point
         float chartScaleYValue = chartScale.GetYByValue(plotValue);
 
         // calculate the x and y values for the line to start and end
         SharpDX.Vector2 startPoint = new SharpDX.Vector2(startX, chartScaleYValue);
         SharpDX.Vector2 endPoint = new SharpDX.Vector2(endX, chartScaleYValue);
 
         // draw a line between the start and end point at each plot using the plots SharpDX Brush color and style
         RenderTarget.DrawLine(startPoint, endPoint, Plots[seriesCount].BrushDX,
           Plots[seriesCount].Width, Plots[seriesCount].StrokeStyle);
 
         // use the chart control text form to draw plot values along the line
         SharpDX.DirectWrite.TextFormat textFormat = chartControl.Properties.LabelFont.ToDirectWriteTextFormat();
 
         // calculate the which will be rendered at each plot using it the plot name and its price
         string textToRender = Plots[seriesCount].Name + ": " + plotValue;
 
         // calculate the layout of the text to be drawn
         SharpDX.DirectWrite.TextLayout textLayout = new SharpDX.DirectWrite.TextLayout(Core.Globals.DirectWriteFactory,
           textToRender, textFormat, 200, textFormat.FontSize);
 
         // draw a line at each plot using the plots SharpDX Brush color at the calculated start point
         RenderTarget.DrawTextLayout(startPoint, textLayout, Plots[seriesCount].BrushDX);
 
         // dipose of the unmanaged resources used
         textLayout.Dispose();
         textFormat.Dispose();
     }
   }
}
 
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "OnRender Example";
     IsOverlay = true;
      
     AddPlot(Brushes.DarkKhaki, "Open");
     AddPlot(Brushes.SeaGreen, "High");
     AddPlot(Brushes.Crimson, "Low");
     AddPlot(Brushes.DodgerBlue, "Close");
   }
}
 
protected override void OnBarUpdate()
{
   Values[0][0] = Open[0];
   Values[1][0] = High[0];
   Values[2][0] = Low[0];
   Values[3][0] = Close[0];
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
 
 
 



</series></t>