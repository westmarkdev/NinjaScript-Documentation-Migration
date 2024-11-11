---
section: references
title: TimeCycles
pathName: timecycles
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a TimeCycles **IDrawingTool**.

## Methods and Properties

{%able %}

* Anchor
* OutlineStroke
* AreaBrush

---

* An **IDrawingTool's ChartAnchor** representing the point of the drawing object
* A Stroke used for the outline of the region
* A **Brush** object representing the fill color of the draw object
{% /table %}

## Examples

```csharp
// Instantiate a Time Cycles object
TimeCycles myTimeCycles = (this, "tag1", 0, 10, Brushes.CornflowerBlue, Brushes.CornflowerBlue, 40);

// Change the object's OutlineBrush
myTimeCycles.OutlineStroke = new Stroke(Brushes.Red);
```
