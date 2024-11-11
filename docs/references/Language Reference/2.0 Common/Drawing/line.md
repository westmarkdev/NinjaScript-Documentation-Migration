---
title: Draw.Line()
pathName: draw_line
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Line **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object

---

* EndAnchor

* An **IDrawingTool's ChartAnchor** representing the end point of the drawing object

---

* Stroke

* A **Stroke** object used to draw the object

---

{% /table %}

## Examples

```csharp
// Instantiate a Line object
NinjaTrader.NinjaScript.DrawingTools.Line myLine = Draw.Line(this, "tag1", false, 10, 1000, 0, 1001, Brushes.LimeGreen, DashStyleHelper.Dot, 2);

// Set a new Stroke for the object
myLine.Stroke = new Stroke(Brushes.Green, DashStyleHelper.Dash, 5);
```

{% callout type="note" %}

To differentiate between **NinjaTrader.NinjaScript.DrawingTools.Line** and **NinjaTrader.Gui.Line** when assigning a Line object, you will need to invoke the former path explicitly, as seen in the example above.

{% /callout %}
