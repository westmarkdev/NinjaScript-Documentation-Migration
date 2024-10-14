










 


Drawing







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawing.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Drawing | [Previous page](usercontrolcollection.htm)
[Return to chapter overview](common.htm)










You can use NinjaScript to draw custom shapes, lines, text and colors on price and indicator panels from both [Indicators](indicator.htm) and [Strategies](strategy.htm). 


 


Draw Methods and Associated Return Types
----------------------------------------




|  |  |
| --- | --- |
| Draw Method | Return Type |
| [Draw.AndrewsPitchfork()](draw_andrewspitchfork.htm) | [AndrewsPitchfork](andrewspitchfork.htm) |
| [Draw.Arc()](draw_arc.htm) | [Arc](arc.htm) |
| [Draw.ArrowDown()](draw_arrowdown.htm) | [ArrowDown](arrowdown.htm) |
| [Draw.ArrowLine()](draw_arrowline.htm) | [ArrowLine](arrowline.htm) |
| [Draw.ArrowUp()](draw_arrowup.htm) | [ArrowUp](arrowup.htm) |
| [Draw.Diamond()](draw_diamond.htm) | [Diamond](diamond.htm) |
| [Draw.Dot()](draw_dot.htm) | [Dot](dot.htm) |
| [Draw.Ellipse()](draw_ellipse.htm) | [Ellipse](ellipse.htm) |
| [Draw.ExtendedLine()](draw_extendedline.htm) | [ExtendedLine](extendedline.htm) |
| [Draw.FibonacciCircle()](draw_fibonaccicircle.htm) | [FibonacciCircle](fibonaccicircle.htm) |
| [Draw.FibonacciExtensions()](draw_fibonacciextensions.htm) | [FibonacciExtensions](fibonacciextensions.htm) |
| [Draw.FibonacciRetracements()](draw_fibonacciretracements.htm) | [FibonacciRetracements](fibonacciretracements.htm) |
| [Draw.FibonacciTimeExtensions()](draw_fibonaccitimeextensions.htm) | [FibonacciTimeExtensions](fibonaccitimeextensions.htm) |
| [Draw.GannFan()](draw_gannfan.htm) | [GannFan](gannfan.htm) |
| [Draw.HorizontalLine()](draw_horizontalline.htm) | [HorizontalLine](horizontalline.htm) |
| [Draw.Line()](draw_line.htm) | [Line](line.htm) |
| [Draw.Pathtool()](draw_pathtool.htm) | [Pathtool](pathtool.htm) |
| [Draw.Polygon()](draw_polygon.htm) | [Polygon](polygon.htm) |
| [Draw.Ray()](draw_ray.htm) | [Ray](ray.htm) |
| [Draw.Rectangle()](draw_rectangle.htm) | [Rectangle](rectangle.htm) |
| [Draw.Region()](draw_region.htm) | [Region](region.htm) |
| [Draw.RegionHighlightX()](draw_regionhighlightx.htm) | [RegionHighlightX](regionhighlightx.htm) |
| [Draw.RegionHighlightY()](draw_regionhighlighty.htm) | [RegionHighlightY](regionhighlighty.htm) |
| [Draw.RegressionChannel()](draw_regressionchannel.htm) | [RegressionChannel](regressionchannel.htm) |
| [Draw.RiskReward()](draw_riskreward.htm) | [RiskReward](riskreward.htm) |
| [Draw.Ruler()](draw_ruler.htm) | [Ruler](ruler.htm) |
| [Draw.Square()](draw_square.htm) | [Square](square.htm) |
| [Draw.Text()](draw_text.htm) | [Text](text.htm) |
| [Draw.TextFixed()](draw_textfixed.htm) | [TextFixed](textfixed.htm) |
| [Draw.TimeCycles()](draw_timecycles.htm) | [TimeCycles](timecycles.htm) |
| [Draw.TrendChannel()](draw_trendchannel.htm) | [TrendChannel](trendchannel.htm) |
| [Draw.Triangle()](draw_triangle.htm) | [Triangle](triangle.htm) |
| [Draw.TriangleDown()](draw_triangledown.htm) | [TriangleDown](triangledown.htm) |
| [Draw.TriangleUp()](draw_triangleup.htm) | [TriangleUp](triangleup.htm) |
| [Draw.VerticalLine()](draw_verticalline.htm) | [VerticalLine](verticalline.htm) |



 


 


Drawing Methods and Properties




|  |  |
| --- | --- |
| Property | Description |
| [AllowRemovalOfDrawObjects](allowremovalofdrawobjects.htm) | Determines if programmatically drawn DrawObjects can be manually removed from the chart |
| [BackBrush](backbrush.htm) | Sets the brush used for painting the chart panel's background color for the current bar |
| [BackBrushAll](backbrushall.htm) | Sets the brush used for painting the chart's background color for the current bar |
| [BackBrushes](backbrushes.htm) | A collection of historical brushes used for the background colors for the chart panel |
| [BackBrushesAll](backbrushesall.htm) | A collection of historical brushes used for the background colors for all chart panels |
| [BarBrush](barbrush.htm) | Sets the brush used for painting the color of a price bar's body |
| [BarBrushes](barbrushes.htm) | A collection of historical brushes used for painting the color of a price bar's body |
| [Brushes](brushes.htm) | A collection of static, predefined Brushes supplied by the .NET Framework |
| [CandleOutlineBrush](candleoutlinebrush.htm) | Sets the outline Brush of a candlestick |
| [CandleOutlineBrushes](candleoutlinebrushes.htm) | A collection of historical outline brushes for candlesticks |
| [DrawObjects](drawingtools_drawobjects.htm) | A collection holding all of the drawn chart objects for the primary bar series |
| [IDrawingTool](idrawingtool.htm) | Represents an interface that exposes information regarding a drawn chart object |
| [RemoveDrawObject()](removedrawobject.htm) | Removes a draw object from the chart based on its tag value |
| [RemoveDrawObjects()](removedrawobjects.htm) | Removes all draw objects originating from the indicator or strategy from the chart |
| [SimpleFont Class](simplefont_class.htm) | Defines a particular font configuration |



 


 




|  |
| --- |
| 1.Custom graphics for custom indicators can be painted on either the price panel or indicator panel. You could for example have a custom indicator displayed in an indicator panel yet have associated custom graphics painted on the price panel. The "[DrawOnPricePanel](drawonpricepanel.htm)" property is set to true by default, which means that custom graphics will always be painted on the price panel, even if the indicator is plotted in a separate panel. If you want your custom graphics to be plotted on the indicator panel, set this property to false in the OnStateChange() method of your custom indicator. 2.Set unique tag values for each draw object, unless you intend for new draw objects to replace existing objects with the same tag. A common trick is to incorporate the bar number as part of the unique tag identifier. For example, if you wanted to draw a dot that indicated a buying condition above a bar, you could express it:  
Draw.Dot(this, CurrentBar.ToString() + "Buy", false, 0, High[0] + TickSize, Brushes.ForestGreen);
 
3. Draw methods will not work if they are called from the OnStateChange() method. |






 
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
 
 
 



