---
title: GetBarIdxByTime()
pathName: getbaridxbytime
parent: chartbars
section: references
status: review
---

## Definition

Returns the **ChartBars** index value calculated from the time parameter provided.

## Method Return Value

An **int** representing the bar index value at a specific time.

## Syntax

**ChartBars.GetBarIdxByTime(ChartControl chartControl, DateTime time)**

## Method Parameters

{% table %}

---

* **chartControl**
* The **ChartControl** object used to determine the chart's time axis

---

* **time**
* The **DateTime** value used to convert to a ChartBar index value
{% /table %}

## Examples

```csharp

protected override void OnBarUpdate()
{
   if (ChartBars != null)
   {
     Print(ChartBars.GetBarIdxByTime(ChartControl, Time[0]));  
   }
}
```
