---
title: Line Class
pathName: line_class
parent: indicator
section: references
status: imported
---

## Definition

Objects derived from the **Line** class are used to characterize how an oscillator line is visually displayed (plotted) on a chart.

## Properties

{% table %}

* Brush
* BrushDX

---

* The System.Windows.Media.Brush used to construct the line ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx))
* A **SharpDX.Direct2D1.Brush** used to actually render the line

---

* DashStyleDX
* DashStyleHelper

---

* A **SharpDX.Direct2D1.DashStyle** used to render the stroke style
* A dashstyle used to construct the stroke. Possible values are:
  * **DashStyleHelper.Dash**
  * **DashStyleHelper.DashDot**
  * **DashStyleHelper.DashDotDot**
  * **DashStyleHelper.Dot**
  * **DashStyleHelper.Solid**

---

* Name
* RenderTarget

---

* A string representing the name of the line
* The **RenderTarget** drawing context used for the line.

---

* StrokeStyle
* Value
* Width

---

* A **SharpDX.Direct2D1.StrokeStyle**
* A double representing the value of the line
* A float representing the width in pixels
{% /table %}

## Examples

See the [AddLine()](addline) method for examples.
