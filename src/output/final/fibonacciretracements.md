---
title: "FibonacciRetracements"
pathName: /docs/desktop/fibonacciretracements
---

## Definition

Represents an interface that exposes information regarding a Fibonacci Retracements [IDrawingTool](/docs/desktop/idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the end point of the drawing object |
| [PriceLevels](/docs/desktop/pricelevels) | A collection of prices calculated by the drawing object |
| TextLocation | An enum determining the text location; can be set to TextLocation.Off to remove text |
| IsExtendedLinesLeft | A `bool` value determining if the draw object should draw lines to the far left side of the screen |
| IsExtendedLinesRight | A `bool` value determining if the draw object should draw lines to the far right side of the screen |

## Example

```csharp
// Instantiate a FibonacciRetracements object
FibonacciRetracements myFibRet = Draw.FibonacciRetracements(this, "tag1", true, 10, Low[10], 0, High[0]);
// Set the object's lines to extend to the right
myFibRet.IsExtendedLinesRight = true;
```
