










 


Plots







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategy_plots.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Plots | [Previous page](strategy_performancemetrics.htm)
[Return to chapter overview](strategy.htm)










Plotting functionality for NinjaScript Strategies is largely identical to the framework for Indicators. Please review the [Plots](plots.htm) / [AddPlot()](addplot.htm) page under the Indicators section.


 


An overview of the draw or plotting related methods / properties available to NinjaScript Strategies vs. Indicators is listed below -


 




|  |  |  |
| --- | --- | --- |
| Method or Property | Strategy  | Indicator |
| [AddChartIndicator()](addchartindicator.htm) | check | error |
| [AddLine()](addline.htm) | check | check |
| [AddPlot()](addplot.htm) | check | check |
| [AllowRemovalOfDrawObjects](allowremovalofdrawobjects.htm) | check | check |
| [AreLinesConfigurable](arelinesconfigurable.htm) | check | check |
| [ArePlotsConfigurable](areplotsconfigurable.htm) | check | check |
| [BackBrush](backbrush.htm) | check | check |
| [BackBrushAll](backbrushall.htm) | check | check |
| [BackBrushes](backbrushes.htm) | check | check |
| [BackBrushesAll](backbrushesall.htm) | check | check |
| [BarBrush](barbrush.htm) | check | check |
| [BarBrushes](barbrushes.htm) | check | check |
| [CandleOutlineBrush](candleoutlinebrush.htm) | check | check |
| [CandleOutlineBrushes](candleoutlinebrushes.htm) | check | check |
| [ChartBars](chartbars.htm) | check | check |
| [ChartControl](chartcontrol.htm) | check | check |
| [ChartIndicators[]](chartindicators.htm) | check | error |
| [ChartObjects](chartobjects.htm) | error | check |
| [ChartPanel](chartpanel.htm) | check | check |
| [DisplayInDataBox](displayindatabox.htm) | check | check |
| [Draw.Methods()](drawing.htm) | check | check |
| [DrawHorizontalGridLines](drawhorizontalgridlines.htm) | error | check |
| [DrawObjects](drawingtools_drawobjects.htm) | check | check |
| [DrawOnPricePanel](drawonpricepanel.htm) | check | check |
| [DrawVerticalGridLines](drawverticalgridlines.htm) | error | check |
| [ForceRefresh()](forcerefresh.htm) | error | check |
| [FormatPriceMarker()](formatpricemarker.htm) | check | check |
| [GetValueAt()](getvalueat.htm) | check | check |
| [IsAutoScale](isautoscale.htm) | check | check |
| [IsOverlay](isoverlay.htm) | check | check |
| [IsTradingHoursBreakLineVisible](istradinghoursbreaklinevisible.htm) | error | check |
| [IsValidDataPoint()](isvaliddatapoint.htm) | check | check |
| [Lines[]](lines.htm) | check | check |
| [MaxValue](maxvalue.htm) | check | check |
| [MinValue](minvalue.htm) | check | check |
| [OnCalculateMinMax()](oncalculateminmax.htm) | check | check |
| [OnRender()](onrender.htm) | check | check |
| [OnRenderTargetChanged()](onrendertargetchanged.htm) | check | check |
| [PaintPriceMarkers](paintpricemarkers.htm) | error | check |
| [Panel](panelindex.htm) | check | check |
| [PanelUI](panelui.htm) | check | check |
| [PlotBrushes[]](plotbrushes.htm) | check | check |
| [Plots[]](plots.htm) | check | check |
| [RemoveDrawObject()](removedrawobject.htm) | check | check |
| [RemoveDrawObjects()](removedrawobjects.htm) | check | check |
| [RenderTarget](rendertarget.htm) | check | check |
| [ScaleJustification](scalejustification.htm) | check | check |
| [SetZOrder()](setzorder.htm) | check | check |
| [ShowTransparentPlotsInDataBox](showtransparentplotsindatabox.htm) | check | check |
| [UserControllCollection[]](usercontrolcollection.htm) | check | check |
| [ZOrder](chart_zorder.htm) | check | check |






 
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
 
 
 



