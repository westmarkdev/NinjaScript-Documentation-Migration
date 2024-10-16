---
title: "AndrewsPitchfork"
pathName: /docs/desktop/andrewspitchfork
---

## Definition

Represents an object that exposes information regarding an Andrews Pitchfork [IDrawingTool](/docs/desktop/idrawingtool).

The Standard Pitchfork creates a trend channel out of the 3 user-defined extreme price anchor points by connecting the first 2 points to form the anchor, and the next 2 points to form the retracement handle. From the first point, then a trendline is drawn through the 50% midpoint of the retracement handle, parallel lines originating at the other 2 points forming the channel, while multiple further price levels could be set to allow for finer analysis.

In contrast, the Schiff Pitchfork variant is constructed by shifting the first anchor of the Standard Pitchfork one-half the vertical distance between the first 2 anchor points.

As further alternation, the Modified Schiff Pitchfork variant is formed by moving the first anchor to the midpoint of the original pitchfork's anchor handle, with the trendline connecting our first 2 anchor points.

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](https://docs/desktop/idrawingtool#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](https://docs/desktop/idrawingtool#chartanchor) representing the end point of the drawing object |
| ExtensionAnchor | An [IDrawingTool's ChartAnchor](https://docs/desktop/idrawingtool#chartanchor) representing the extension point of the drawing object |
| [PriceLevels](/docs/desktop/pricelevels) | A collection of prices calculated by the drawing object |
| CalculationMethod | The AndrewsPitchforkCalculationMethod property determining which method is used to calculate the pitchfork. {% <br> %} Possible values are: {% <br> %} &bull; ModifiedSchiff {% <br> %} &bull; Schiff {% <br> %} &bull; StandardPitchfork |
| IsTextDisplayed | A bool value determining if the draw object should display text on the chart. |
| RetracementLineStroke | A [Stroke](/docs/desktop/stroke_class) object used to draw the center retracement line of the object |
| AnchorLineStroke | A [Stroke](/docs/desktop/stroke_class) object used to draw the object |

## Example

```csharp
// Instantiate an Andrews Pitchfork object
AndrewsPitchfork myFork = Draw.AndrewsPitchfork(this, "tag1", false, 7, Low[7], 5, High[5], 1, Low[1], false, "ForkTemplate");
// Print the tag used to draw the object
Print(myFork.Tag);
```
