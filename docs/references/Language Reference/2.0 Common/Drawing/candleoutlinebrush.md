---
title: CandleOutlineBrush
pathName: candleoutlinebrush
parent: drawing
section: references
status: review
---

## Definition

Sets the outline Brush of a candlestick.

## Property Value

A **brush** object that represents the color of this price bar.

## Syntax

**CandleOutlineBrush**

{% callout type="warning" %}

You may have up to 65,535 unique **CandleOutlineBrushes** instances, therefore, using [static predefined brushes](working_with_brushes) should be favored. Alternatively, in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.

{% /callout %}

## Examples

```csharp
// Sets the candle outline color to black
CandleOutlineBrush = Brushes.Black;
```

{% callout type="warning" %}

* Warning:  You may have up to 65,535 unique CandleOutlineBrushes instances, therefore, using [static predefined brushes](working_with_brushes) should be favored.  Alternatively,  in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created.
{% /callout %}
