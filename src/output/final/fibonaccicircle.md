---
title: "FibonacciCircle"
pathName: /docs/desktop/fibonaccicircle
---

## Definition

Represents an interface that exposes information regarding a Fibonacci Circle [IDrawingTool](/docs/desktop/idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](https://docs/desktop/idrawingtool#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](https://docs/desktop/idrawingtool#chartanchor) representing the end point of the drawing object |
| [PriceLevels](/docs/desktop/pricelevels) | A collection of prices calculated by the drawing object |
| IsTimePriceDividedSeparately | A `bool` value which when true determines if the time and price are calculated together as a ratio, or independently |
| IsTextDisplayed | A `bool` value determining if the draw object should display text on the chart. |

## Example

```csharp
// Instantiate a Fibonacci circle
FibonacciCircle myFibCirc = Draw.FibonacciCircle(this, "tag1", true, 10, Low[10], 0, High[0]);
// Ensure that text is being displayed on the Drawing Object
myFibCirc.IsTextDisplayed = true;
```

