---
title: stroke_class
pathName: stroke_class
status: review
section: references
parent: charts
---

## Definition

Objects derived from the Stroke class are used to characterize how a plot is visually displayed (plotted) on a chart.

## Syntax

**Stroke(Stroke stroke)**

**Stroke(Brush brush)**

**Stroke(Brush brush, float width)**

**Stroke(Brush brush, DashStyle dashStyleHelper, float width)**

## Parameters

{% table %}

* Parameter
* Description

---

* brush
* The brush used to draw the plot ([reference](http://msdn.microsoft.com/en-us/library/System.Windows.Media.Brush%28v=vs.110%29.aspx))

---

* dashStyleHelper
* Possible values:
  * DashStyleHelper.Dash
  * DashStyleHelper.DashDot
  * DashStyleHelper.DashDotDot
  * DashStyleHelper.Dot
  * DashStyleHelper.Solid

---

* stroke
* The [stroke](stroke_class.htm) object

---

* width
* The width of the stroke
{% /table %}

## Properties

{% table %}

---

* Brush
* The System.Windows.Media.Brush used to construct the stroke ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx))

---

* BrushDX
* A [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush.htm) used to actually render the stroke
  Note:  To avoid and resolve access violation exceptions, please see Warning and examples remarked below

---

* DashStyleDX
* A [SharpDX.Direct2D1.DashStyle](sharpdx_direct2d1_strokestyle_dashstyle.htm) used to render the stroke style
  Note:  To avoid and resolve access violation exceptions, please see Warning and examples remarked below

---

* DashStyleHelper
* A dashstyle used to construct the stroke. Possible values are:
  * DashStyleHelper.Dash
  * DashStyleHelper.DashDot
  * DashStyleHelper.DashDotDot
  * DashStyleHelper.Dot
  * DashStyleHelper.Solid

---

* RenderTarget
* The [RenderTarget](rendertarget.htm) drawing context used for the stroke.

Note: This property must be set before accessing a stroke's BrushDX property. Please see Warning and examples remarked below

---

* StrokeStyle
* A [SharpDX.Direct2D1.StrokeStyle](sharpdx_direct2d1_strokestyle.htm)

---

* Width
* A float representing the width in pixels
{% /table %}

{% callout type="warning" %}

There may be situations where a RenderTarget has not been set, and to prevent access violation exception before accessing the BrushDX or DashStyleDX properties, you should explicitly set the RenderTarget before attempting to access that property.  Please see the example below.

{% /callout %}

## Examples

See the [AddPlot()](addplot.htm) method for additional examples.

### Using a Stroke SharpDX Brush for Custom Rendering

```csharp
protected override void OnStateChange()  
{  
  if (State == State.SetDefaults)  
  {  
    IsOverlay = true;  
    // set the Stroke default to red brush  
    MyStroke = new Stroke(Brushes.Red);  
  }  
  else if (State == State.Configure)  
  {  
  }  
}  

public override void OnRenderTargetChanged()  
{  
  // Explicitly set the Stroke RenderTarget  
  if (RenderTarget != null)  
    MyStroke.RenderTarget = RenderTarget;  
}  

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  
{  
  // create two points from the top left corner  
  SharpDX.Vector2 pointA = new SharpDX.Vector2(0, 0);  
  // to 300 pixels offset X and Y to create a diagonal line  
  SharpDX.Vector2 pointB = new SharpDX.Vector2(300, 300);  

  // Draw the line using the Stroke SharpDX brush  
  RenderTarget.DrawLine(pointA, pointB, MyStroke.BrushDX, MyStroke.Width, MyStroke.StrokeStyle);  

}  

[NinjaScriptProperty]  
[Description("My Stroke")]  
public Stroke MyStroke { get; set; }
```

```csharp
protected override void OnStateChange()  
{  
  if (State == State.SetDefaults)  
  {  
    IsOverlay = true;  
    // set stroke default to blue brush  
    MyStroke = new Stroke(Brushes.Blue);  
  }  
  else if (State == State.Configure)  
  {  
  }  
}  

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  
{  
  // create two points from the top left corner  
  SharpDX.Vector2 pointA = new SharpDX.Vector2(0, 0);  
  // to 300 pixels offset X and Y to create a diagonal line  
  SharpDX.Vector2 pointB = new SharpDX.Vector2(300, 300);  

  NinjaTrader.Gui.Stroke MyStroke = new Stroke(Brushes.Blue);  

  // if BrushDX is null, convert the constructed brush to a DX brush  
  SharpDX.Direct2D1.Brush myBrush = MyStroke.BrushDX ?? MyStroke.Brush.ToDxBrush(RenderTarget);  
  RenderTarget.DrawLine(pointA, pointB, myBrush, MyStroke.Width, MyStroke.StrokeStyle);  

  myBrush.Dispose();  
}  

[NinjaScriptProperty]  
[Description("My Stroke")]  
public Stroke MyStroke { get; set; }
```
