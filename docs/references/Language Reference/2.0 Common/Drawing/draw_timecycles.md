---
title: Draw.TimeCycles()
pathName: draw_timecycles
parent: drawing
section: references
status: review
---

## Definition

Draws a time cycle based on two points.

## Method Return Value

A **TimeCycles** object that represents the draw object.

## Syntax

**Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, double endY, Brush brush, bool drawOnPricePanel)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, bool isGlobal, string templateName)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, bool drawOnPricePanel)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, bool isGlobal, string templateName)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, Brush areaBrush, int areaOpacity)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush, Brush areaBrush, int areaOpacity)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush)**

**Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush)**

## Parameters

{% table %}

---

* owner
* The hosting **NinjaScript** object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this").

---

* tag
* A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time.

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
* The brush used to color draw object ([reference](brushes)).

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
// Draws a Time Cycles object based on 10 bars back to the current bar that is cornflower blue with an opacity of 40
Draw.TimeCycles(this, "tag1", 0, 10, Brushes.CornflowerBlue, Brushes.CornflowerBlue, 40);

```
