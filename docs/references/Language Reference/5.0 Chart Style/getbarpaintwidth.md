---
title: GetBarPaintWidth()
pathName: getbarpaintwidth
parent: chart_style
status: imported
section: references
---

## Definition

Returns the painted width of the chart bar. The **GetBarPaintWidth()** method will return a minimum value of 1.

{% callout type="note" %}

This is an [abstract](https://msdn.microsoft.com/en-us/library/sf985hc5.aspx) method which is required to compile a ChartStyle object. If you do not plan on recalculating a barWidth, simply return the default barWidth parameter which is passed in this method. Please see the Examples section of this page for more information.

{% /callout %}

## Method Return Value

An **int** value

## Syntax

You must override this method using the following syntax:

**public override int GetBarPaintWidth(int barWidth)**

## Method Parameters

{% table %}

* Parameter
* Description

---

* **barWidth**
* An **int** value representing the current width of the bar to calculate
{% /table %}

## Examples

{% table %}

### Returning the default barWidth

```csharp

public override int GetBarPaintWidth(int barWidth)
{
    return barWidth
}

```

### Calculating and returning a new barWidth from the original barWidth

```csharp
public override int GetBarPaintWidth(int barWidth)
{
    // calculate a new bar width 
    return 1 + 2 * (barWidth - 1) + 2 * (int) Math.Round(Stroke.Width);
}
```
