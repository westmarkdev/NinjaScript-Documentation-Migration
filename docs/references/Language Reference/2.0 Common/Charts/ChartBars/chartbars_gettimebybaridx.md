---
title: GetTimeByBarIdx()
pathName: gettimebybaridx
parent: chartbars
section: references
status: review
---

## Definition

Returns the **ChartBars** time value calculated from a bar index parameter provided.

## Method Return Value

A **DateTime** struct representing a bar time value at a specific bar index value.

## Syntax

**ChartBars.GetTimeByBarIdx(ChartControl chartControl, int barIndex)**

## Method Parameters

{% table %}

---

* **chartControl**
* The **ChartControl** object used to determine the chart's time axis

---

* **barIndex**
* An **int** value representing a bar index used to convert to a **ChartBar** index value
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   if (ChartBars != null)
   {
     Print(ChartBars.GetTimeByBarIdx(ChartControl, 50)); //8/11/2015 4:30:00 AM
   }
}
```
