---
title: Draw.RegressionChannel()
pathName: draw_regressionchannel
parent: drawing
section: references
status: review
---

## Definition

Draws a regression channel.

## Method Return Value

A **RegressionChannel** object that represents the draw object.

## Syntax

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush)**

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush)**  

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, int endBarsAgo, Brush upperBrush, DashStyleHelper upperDashStyleHelper, int upperWidth, Brush middleBrush, DashStyleHelper middleDashStyleHelper, int middleWidth, Brush lowerBrush, DashStyleHelper lowerDashStyleHelper, int lowerWidth)**  

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, DateTime endTime, Brush upperBrush, DashStyleHelper upperDashStyleHelper, int upperWidth, Brush middleBrush, DashStyleHelper middleDashStyleHelper, int middleWidth, Brush lowerBrush, DashStyleHelper lowerDashStyleHelper, int lowerWidth)**  

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, bool isGlobal, string templateName)**  

**Draw.RegressionChannel(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, bool isGlobal, string templateName)**

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

* startBarsAgo
* The starting bar (x axis co-ordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back.

---

* startTime
* The starting time where the draw object will be drawn.

---

* endBarsAgo
* The end bar (x axis co-ordinate) where the draw object will terminate.

---

* endTime
* The end time where the draw object will terminate.

---

* brush
* The brush used to color the outline of draw object ([reference](brushes)).

---

* upperDashStyle, middleDashStyle, lowerDashStyle
* **DashStyleHelper.Dash**, **DashStyleHelper.DashDot**, **DashStyleHelper.DashDotDot**, **DashStyleHelper.Dot**, **DashStyleHelper.Solid**. Note: Fancier DashStyles like **DashDotDot** will require more resources than simple DashStyles like **Solid**.

---

* upperBrush, middleBrush, lowerBrush
* The line colors ([reference](brushes)).

---

* upperWidth, middleWidth, lowerWidth
* The line width.

---

* isGlobal
* Determines if the draw object will be global across all charts which match the instrument.

---

* templateName
* The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead).
{% /table %}

## Examples

```csharp
// Draws a regression channel from the low 10 bars back to the high of 5 bars back
Draw.RegressionChannel(this, "tag1", 10, 0, Brushes.Blue);
```
