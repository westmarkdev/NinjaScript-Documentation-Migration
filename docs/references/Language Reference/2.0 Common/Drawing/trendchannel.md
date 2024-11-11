---
status: double_check
title: TrendChannel
parent: draw_trendchannel
pathName: trendchannel
section: references
lg2m: true
---

## Definition

Represents an interface that exposes information regarding a Trend Channel [IDrawingTool](source_files/idrawingtool.md).

## Methods and Properties

{% table %}

* Parameter

* Description

---

* TrendStartAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the starting point of the drawing object

---

* TrendEndAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the end point of the drawing object

---

* ParallelStartAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the starting point of the second line used in the trend channel

---

* [PriceLevels](source_files/pricelevels.md)

* A collection of prices calculated by the drawing object

---

{% /table %}

## Example

```csharp
// Instantiate a TrendChannel object  
TrendChannel myTC = Draw.TrendChannel(this, "tag1", true, 10, Low[10], 0, High[0], 10, High[10] + 5 * TickSize);            
   
// Increase the y-axis position of the object's TrendEndAnchor  
myTC.TrendEndAnchor.Price += 15;
```
