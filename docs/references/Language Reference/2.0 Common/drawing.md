---
title: Drawing
pathName: drawing
parent: common
section: references
status: review
---

You can use **NinjaScript** to draw custom shapes, lines, text and colors on price and indicator panels from both [Indicators](docs/references/Language%20Reference/2.0%20Common/system_indicator_methods.md) and [Strategies](strategies).

## Draw Methods and Associated Return Types

{% table %}

* Draw Method
* Return Type

---

* [Draw.AndrewsPitchfork()](draw_andrewspitchfork)
* [AndrewsPitchfork](andrewspitchfork)

---

* [Draw.Arc()](draw_arc)
* [Arc](arc)

---

* [Draw.ArrowDown()](draw_arrowdown)
* [ArrowDown](arrowdown)

---

* [Draw.ArrowLine()](draw_arrowline)
* [ArrowLine](arrowline)

---

* [Draw.ArrowUp()](draw_arrowup)
* [ArrowUp](arrowup)

---

* [Draw.Diamond()](draw_diamond)
* [Diamond](diamond)

---

* [Draw.Dot()](draw_dot)
* [Dot](dot)

---

* [Draw.Ellipse()](draw_ellipse)
* [Ellipse](ellipse)

---

* [Draw.ExtendedLine()](draw_extendedline)
* [ExtendedLine](extendedline)

---

* [Draw.FibonacciCircle()](draw_fibonaccicircle)
* [FibonacciCircle](fibonaccicircle)

---

* [Draw.FibonacciExtensions()](draw_fibonacciextensions)
* [FibonacciExtensions](fibonacciextensions)

---

* [Draw.FibonacciRetracements()](draw_fibonacciretracements)
* [FibonacciRetracements](fibonacciretracements)

---

* [Draw.FibonacciTimeExtensions()](draw_fibonaccitimeextensions)
* [FibonacciTimeExtensions](fibonaccitimeextensions)

---

* [Draw.GannFan()](draw_gannfan)
* [GannFan](gannfan)

---

* [Draw.HorizontalLine()](draw_horizontalline)
* [HorizontalLine](horizontalline)

---

* [Draw.Line()](draw_line)
* [Line](line)

---

* [Draw.Pathtool()](draw_pathtool)
* [Pathtool](pathtool)

---

* [Draw.Polygon()](draw_polygon)
* [Polygon](polygon)

---

* [Draw.Ray()](draw_ray)
* [Ray](ray)

---

* [Draw.Rectangle()](draw_rectangle)
* [Rectangle](rectangle)

---

* [Draw.Region()](draw_region)
* [Region](region)

---

* [Draw.RegionHighlightX()](draw_regionhighlightx)
* [RegionHighlightX](regionhighlightx)

---

* [Draw.RegionHighlightY()](draw_regionhighlighty)
* [RegionHighlightY](regionhighlighty)

---

* [Draw.RegressionChannel()](draw_regressionchannel)
* [RegressionChannel](regressionchannel)

---

* [Draw.RiskReward()](draw_riskreward)
* [RiskReward](riskreward)

---

* [Draw.Ruler()](draw_ruler)
* [Ruler](ruler)

---

* [Draw.Square()](draw_square)
* [Square](square)

---

* [Draw.Text()](draw_text)
* [Text](text)

---

* [Draw.TextFixed()](draw_textfixed)
* [TextFixed](textfixed)

---

* [Draw.TimeCycles()](draw_timecycles)
* [TimeCycles](timecycles)

---

* [Draw.TrendChannel()](draw_trendchannel)
* [TrendChannel](trendchannel.md)

---

* [Draw.Triangle()](draw_triangle)
* [Triangle](triangle.md)

---

* [Draw.TriangleDown()](draw_triangledown)
* [TriangleDown](triangledown.md)

---

* [Draw.TriangleUp()](draw_triangleup)
* [TriangleUp](triangleup.md)

---

* [Draw.VerticalLine()](draw_verticalline)
* [VerticalLine](verticalline.md)
{% /table %}

## Drawing Methods and Properties

{% table %}

* Property
* Description

---

* [AllowRemovalOfDrawObjects](allowremovalofdrawobjects)
* Determines if programmatically drawn DrawObjects can be manually removed from the chart

---

* [BackBrush](backbrush)
* Sets the brush used for painting the chart panel's background color for the current bar

---

* [BackBrushAll](backbrushall)
* Sets the brush used for painting the chart's background color for the current bar

---

* [BackBrushes](backbrushes)
* A collection of historical brushes used for the background colors for the chart panel

---

* [BackBrushesAll](backbrushesall)
* A collection of historical brushes used for the background colors for all chart panels

---

* [BarBrush](barbrush)
* Sets the brush used for painting the color of a price bar's body

---

* [BarBrushes](barbrushes)
* A collection of historical brushes used for painting the color of a price bar's body

---

* [Brushes](brushes)
* A collection of static, predefined Brushes supplied by the .NET Framework

---

* [CandleOutlineBrush](candleoutlinebrush)
* Sets the outline Brush of a candlestick

---

* [CandleOutlineBrushes](candleoutlinebrushes)
* A collection of historical outline brushes for candlesticks

---

* [DrawObjects](drawingtools_drawobjects)
* A collection holding all of the drawn chart objects for the primary bar series

---

* [IDrawingTool](idrawingtool)
* Represents an interface that exposes information regarding a drawn chart object

---

* [RemoveDrawObject()](removedrawobject)
* Removes a draw object from the chart based on its tag value

---

* [RemoveDrawObjects()](removedrawobjects)
* Removes all draw objects originating from the indicator or strategy from the chart

---

* [SimpleFont Class](simplefont_class)
* Defines a particular font configuration
{% /table %}

1. Custom graphics for custom indicators can be painted on either the price panel or indicator panel. You could for example have a custom indicator displayed in an indicator panel yet have associated custom graphics painted on the price panel. The "**DrawOnPricePanel**" property is set to true by default, which means that custom graphics will always be painted on the price panel, even if the indicator is plotted in a separate panel. If you want your custom graphics to be plotted on the indicator panel, set this property to false in the **OnStateChange()** method of your custom indicator.
2. Set unique tag values for each draw object, unless you intend for new draw objects to replace existing objects with the same tag. A common trick is to incorporate the bar number as part of the unique tag identifier. For example, if you wanted to draw a dot that indicated a buying condition above a bar, you could express it:
**Draw.Dot(this, CurrentBar.ToString() + "Buy", false, 0, High[0] + TickSize, Brushes.ForestGreen);**
3. Draw methods will not work if they are called from the **OnStateChange()** method.
