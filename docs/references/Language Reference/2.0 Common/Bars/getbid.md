---
title: GetBid()
pathName: getbid
parent: bars
section: references
status: review
---

## Definition

Returns the bid price value at a selected absolute bar index value.

{% callout type="note" %}

* This method does NOT return the current real-time bid price, but rather the historical / real-time bid price at the desired index. For obtaining the current real-time bid price, please use **GetCurrentBid()**.

* This method returns expected values when 1 tick bid / ask stamped data is used and available from **your provider**.

{% /callout %}

## Method Return Value

A **double** value that represents the bidding price at the desired bar index.

## Syntax

**Bars.GetBid(int index)**

## Parameters

{% table %}

* Parameter
* Description

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
   if (Low[0] > Low[1] && Low[1] < Low[2])
   {
     EnterShortStopMarket(Bars.GetBid(CurrentBar));
   }
}
```
