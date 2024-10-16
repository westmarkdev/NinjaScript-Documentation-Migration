---
title: "FibonacciExtensions"
pathName: /docs/desktop/fibonacciextensions
---

## Definition

Represents an interface that exposes information regarding a Fibonacci Extensions [IDrawingTool](/docs/desktop/idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the end point of the drawing object |
| ExtensionAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the extension point of the drawing object |
| [PriceLevels](/docs/desktop/pricelevels) | A collection of prices calculated by the drawing object |
| TextLocation | An enum determining the text location; can be set to TextLocation.Off to remove text |
| IsExtendedLinesLeft | A bool value determining if the draw object should draw lines to the far left side of the screen |
| IsExtendedLinesRight | A bool value determining if the draw object should draw lines to the far right side of the screen |

## Example

```csharp
// Instantiates a Fibonacci Extension
FibonacciExtensions myFibExt = Draw.FibonacciExtensions(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);
// Extend the Fibonacci Extension object's lines to the right
myFibExt.IsExtendedLinesRight = true;
```

