---
title: FibonacciCircle
pathName: fibonaccicircle
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Fibonacci Circle **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An IDrawingTool's ChartAnchor representing the starting point of the drawing object

---

* EndAnchor

* An IDrawingTool's ChartAnchor representing the end point of the drawing object

---

* PriceLevels

* A collection of prices calculated by the drawing object

---

* IsTimePriceDividedSeparately

* A bool value which when true determines if the time and price are calculated together as a ratio, or independently

---

* IsTextDisplayed

* A bool value determining if the draw object should display text on the chart.

---

{% /table %}

## Examples

```csharp
// Instantiate a Fibonacci circle
FibonacciCircle myFibCirc = Draw.FibonacciCircle(this, "tag1", true, 10, Low[10], 0, High[0]);

// Ensure that text is being displayed on the Drawing Object
myFibCirc.IsTextDisplayed = true;
```
