---
title: Draw.Triangle()
pathName: draw_triangle
parent: drawing
section: references
status: review
---

## Definition

Draws a triangle.

## Method Return Value

A **Triangle** object that represents the draw object.

## Syntax

**Draw.Triangle(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int middleBarsAgo, double middleY, int endBarsAgo, double endY, Brush brush)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, DateTime startTime, double startY, DateTime middleTime, double middleY, DateTime endTime, double endY, Brush brush)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int middleBarsAgo, double middleY, int endBarsAgo, double endY, Brush brush, Brush areaBrush, int areaOpacity)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime midTime, double middleY, DateTime endTime, double endY, Brush brush, Brush areaBrush, int areaOpacity)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int middleBarsAgo, double middleY, int endBarsAgo, double endY, Brush brush, bool drawOnPricePanel)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int middleBarsAgo, double middleY, int endBarsAgo, double endY, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime midTime, double middleY, DateTime endTime, double endY, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int middleBarsAgo, double middleY, int endBarsAgo, double endY, bool isGlobal, string templateName)**  

**Draw.Triangle(NinjaScriptBase owner, string tag, DateTime startTime, double startY, DateTime middleTime, double middleY, DateTime endTime, double endY, bool isGlobal, string templateName)**

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
* Determines if the draw object will be included in the y-axis scale.

---

* startBarsAgo
* The number of bars ago (x value) of the 1st anchor point.

---

* startTime
* The time of the 1st anchor point.

---

* startY
* The y value of the 1st anchor point.

---

* middleBarsAgo
* The number of bars ago (x value) of the 2nd anchor point.

---

* midTime
* The time of the 2nd anchor point.

---

* middleY
* The y value of the 2nd anchor point.

---

* endBarsAgo
* The number of bars ago (x value) of the 3rd anchor point.

---

* endTime
* The time of the 3rd anchor point.

---

* endY
* The y value of the 3rd anchor point.

---

* brush
* The brush used to color the outline of draw object ([reference](brushes)).

---

* areaBrush
* The brush used to color the fill area of the draw object ([reference](brushes)).

---

* areaOpacity
* Sets the level of transparency for the fill color. Valid values between 0 - 100. (0 = completely transparent, 100 = no opacity).

---

* drawOnPricePanel
* Determines if the draw-object should be on the price panel or a separate panel.

---

* isGlobal
* Determines if the draw object will be global across all charts which match the instrument.

---

* templateName
* The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead).
{% /table %}

## Examples

```csharp
// Paints a blue triangle on the chart
Draw.Triangle(this, "tag1", 4, Low[4], 3, High[3], 1, Low[1], Brushes.Blue);
```
