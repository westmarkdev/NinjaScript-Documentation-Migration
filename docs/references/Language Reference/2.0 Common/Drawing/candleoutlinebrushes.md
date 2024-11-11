---
title: CandleOutlineBrushes
pathName: candleoutlinebrushes
parent: drawing
section: references
status: review
---

## Definition

A collection of historical outline brushes for candlesticks.

## Property Value

A brush series type object. Accessing this property via an index value **int barsAgo** returns a [brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) structure representing the referenced bar's outline color.

{% callout type="note" %}

This will only return the color of a candlestick outline in which an explicit color overwrite was used. Otherwise it will return null.

{% /callout %}

## Syntax

**CandleOutlineBrushes**  
**CandleOutlineBrushes[int barsAgo]**

{% callout type="warning" %}

Warning: You may have up to 65,535 unique CandleOutlineBrushes instances, therefore, using [static predefined brushes](working_with_brushes) should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
// Sets the outline color of the current bar to black.
CandleOutlineBrushes[0] = Brushes.Black;

// Sets the outline color of the previous bar to blue.
CandleOutlineBrushes[1] = Brushes.Blue;
```
