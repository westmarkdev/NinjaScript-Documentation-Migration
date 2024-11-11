---
title: GetAsk()
pathName: getask
parent: bars
section: references
status: review
---

## Definition

Returns the ask price value at a selected absolute bar index value.

{% callout type="note" %}

* This method does NOT return the current real-time asking price, but rather the historical / real-time asking price at the desired index. For obtaining the current real-time asking price, please use **GetCurrentAsk**().
* This method returns expected values when 1 tick bid / ask stamped data is used and available from **your provider**.
{% /callout %}

## Method Return Value

A **double** value that represents the asking price at the desired bar index.

## Syntax

**Bars.GetAsk(int index)**

## Parameters

{% table %}

* **Parameter**
* **Description**

---

* **index**
* The absolute bar index value used
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // If the Highs of the two most recent bars are falling, place a long stop market order 
    // at the Ask price 
    if (High[0] < High[1] && High[1] < High[2])
    {
        EnterLongStopMarket(Bars.GetAsk(CurrentBar));
    }
}
```
