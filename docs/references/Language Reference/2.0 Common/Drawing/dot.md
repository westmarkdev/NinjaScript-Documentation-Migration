---
title: Dot
pathName: dot
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Dot **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* Anchor

* An **IDrawingTool's ChartAnchor** representing the point of the drawing object

---

* AreaBrush

* A **Brush** object representing the fill color of the draw object

---

* OutlineBrush

* A **Brush** object representing the color of the draw object's outline

---

{% /table %}

## Examples

```csharp
// Instantiates a red dot on the current bar 1 tick below the low
Dot myDot = Draw.Dot(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);

// Disable the dot's Auto Scale property
myDot.IsAutoScale = false;
```
