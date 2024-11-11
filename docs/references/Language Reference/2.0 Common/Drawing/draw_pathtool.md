---
title: Draw.PathTool()
pathName: draw_pathtool
parent: drawing
section: references
status: review
---

## Definition

Draws a path which can have a user defined set of anchors.

## Method Return Value

A **PathTool** object that represents the draw object.

## Syntax

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, List<`chartanchor`> chartAnchors, bool isGlobal, string templateName)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, List<`chartanchor`> chartAnchors, Brush brush, DashStyleHelper dashStyle)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, int anchor1BarsAgo, double anchor1Y, int anchor2BarsAgo, double anchor2Y, int anchor3BarsAgo, double anchor3Y)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime Anchor1Time, double anchor1Y, DateTime Anchor2Time, double anchor2Y, DateTime Anchor3Time, double anchor3Y)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, int anchor1BarsAgo, double anchor1Y, int anchor2BarsAgo, double anchor2Y, int anchor3BarsAgo, double anchor3Y, int anchor4BarsAgo, double anchor4Y)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime Anchor1Time, double anchor1Y, DateTime Anchor2Time, double anchor2Y, DateTime Anchor3Time, double anchor3Y, DateTime Anchor4Time, double anchor4Y)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, int anchor1BarsAgo, double anchor1Y, int anchor2BarsAgo, double anchor2Y, int anchor3BarsAgo, double anchor3Y, int anchor4BarsAgo, double anchor4Y, int anchor5BarsAgo, double anchor5Y)**

**Draw.PathTool(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime Anchor1Time, double anchor1Y, DateTime Anchor2Time, double anchor2Y, DateTime Anchor3Time, double anchor3Y, DateTime Anchor4Time, double anchor4Y, DateTime Anchor5Time, double anchor5Y)**

## Parameters

{% table %}

---

* owner
* The hosting **NinjaScript** object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this").

---

* tag
* A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time.

---

* isAutoScale
* Determines if the draw object will be included in the y-axis scale. Default value is false.

---

* chartAnchors
* A list of the chart anchors.

---

* anchor1BarsAgo
* The bar the first anchor of the object will be drawn at. A value of 10 would be 10 bars ago.

---

* anchor2BarsAgo
* The bar the second anchor of the object will be drawn at. A value of 10 would be 10 bars ago.

---

* anchor3BarsAgo
* The bar the third anchor of the object will be drawn at. A value of 10 would be 10 bars ago.

---

* anchor4BarsAgo
* The bar the forth anchor of the object will be drawn at. A value of 10 would be 10 bars ago.

---

* anchor5BarsAgo
* The bar the fifth anchor of the object will be drawn at. A value of 10 would be 10 bars ago.

---

* anchor1Y
* The first anchor y value.

---

* anchor2Y
* The second anchor y value.

---

* anchor3Y
* The third anchor y value.

---

* anchor4Y
* The forth anchor y value.

---

* anchor5Y
* The fifth anchor y value.

---

* Anchor1Time
* The time the first anchor of the object will be drawn at.

---

* Anchor2Time
* The time the second anchor of the object will be drawn at.

---

* Anchor3Time
* The time the third anchor of the object will be drawn at.

---

* Anchor4Time
* The time the forth anchor of the object will be drawn at.

---

* Anchor5Time
* The time the fifth anchor of the object will be drawn at.

---

* templateName
* The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead).
{% /table %}

## Examples

```csharp
// Draws a PathTool object based on bars ago and y anchors
Draw.PathTool(this, "tag1", false, 20, 194, 10, 184, 13, 176, 25, 182);

// Draws a PathTool object based on a list of anchors with specified times
List<chartanchor> anchors = new List<chartanchor>();
anchors.Add(new ChartAnchor(new DateTime(2018, 5, 25), 194, ChartControl));
anchors.Add(new ChartAnchor(new DateTime(2018, 6, 12), 184, ChartControl));
anchors.Add(new ChartAnchor(new DateTime(2018, 6, 7), 176, ChartControl));
anchors.Add(new ChartAnchor(new DateTime(2018, 5, 21), 182, ChartControl));
Draw.PathTool(this, "tag1", false, anchors, Brushes.CornflowerBlue, DashStyleHelper.Solid, Brushes.CornflowerBlue, 40);
```
