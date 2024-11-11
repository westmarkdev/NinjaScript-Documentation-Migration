---
title: GannFan
pathName: gannfan
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Gann Fan **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* Anchor

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object

---

* PriceLevels

* A collection of prices calculated by the drawing object

---

* GannFanDirection

* Possible values:

* **GannFanDirection.DownLeft**

* **GannFanDirection.DownRight**

* **GannFanDirection.UpLeft**

* **GannFanDirection.UpRight**

---

* PointsPerBar

* A **double** value representing the number of points per bar

---

* IsTextDisplayed

* A bool value representing if text will be drawn along with the draw object

---

{% /table %}

## Examples

```csharp
// Instantiate a GannFan object
GannFan myFan = Draw.GannFan(this, "tag1", true, 0, Low[0]);

// Instantiate a new PriceLevel to be used in the step below
PriceLevel myLevel = new PriceLevel(99, Brushes.Black);

// Change the object's price level at index 3
myFan.PriceLevels[3] = myLevel;
```
