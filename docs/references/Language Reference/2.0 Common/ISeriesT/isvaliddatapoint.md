---
title: IsValidDataPoint()
pathName: isvaliddatapoint
parent: iseriest
section: references
status: review
---

## Definition

Indicates if the specified input is set at a barsAgo value relative to the current bar. Please also see the **[Reset()](reset)** method for more information.

{% callout type="note" %}

* If called directly from the instance of the **NinjaScript** object, the value returned corresponds to the Input Series (e.g., Close, High, Low, SMA, etc.)
* When checking a **[Bar](bars)** or **[PriceSeries](priceseries)**, **IsValidDataPoint()** returns true as long as the barsAgo value falls between 0 and the total count for that series. These are special series which always contain a value set at every slot index for multi-series scripting purposes (e.g., comparing two price series with various session templates, or one series has more ticks than the other)
* For a **[Value](value.md)** series or custom **[Series<`t`>](seriest)**, **IsValidDataPoint()** returns true or false depending on if you have set a value at that index location
{% /callout %}

## Method Return Value

A bool value, when true indicates that specified data point is set; otherwise false.

## Syntax

**IsValidDataPoint(int barsAgo)**

**ISeries<t`>.IsValidDataPoint(int barsAgo)**

{ %callout type="warning" %}

* Calling **IsValidDataPoint()** will only work on a MaximumBarsLookBackInfinite series. Attempting to check **IsValidDataPoint()** on MaximumBarsLookBack256 series will throw an error. Please check the Log tab of the Control Center. In addition, since this method references barsAgo data, it cannot be used during **[OnRender (see note 5)](onrender)** - instead please use the **[IsValidDataPointAt](isvaliddatapointat)** during OnRender.
{% /table %}

## Parameters

{% table %}

* barsAgo
* An int representing from the current bar the number of historical bars the method will check.
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // only set plot value if hosted indicator is not reset
   if(SMA(20).IsValidDataPoint(0))
     MyPlot[0] = SMA(20)[0];
}
```
