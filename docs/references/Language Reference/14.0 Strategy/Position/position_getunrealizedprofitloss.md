---
section: references
status: imported
parent: position
title: GetUnrealizedProfitLoss()
pathName: getunrealizedprofitloss
---

## Definition

Calculates the unrealized PnL for the strategy position.

## Method Return Value

A **double** value representing the unrealized PnL.

## Syntax

**Position.GetUnrealizedProfitLoss(PerformanceUnit unit, [double price])**

{% callout type="note" %}

* If no double argument is provided in the call, the current (real-time) Last price will be substituted in. In case Tools > Options > Trading > 'Use last price for Pnl' is unchecked or the instrument type is Forex / CFD the bid (for a long position) / ask (for a short position) would be used as a substitute.

* For back-testing a double price to compare against should be provided like in our example below.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **unit**
* Possible values:
  **PerformanceUnit.Currency**
  **PerformanceUnit.Percent**
  **PerformanceUnit.Pips**
  **PerformanceUnit.Points**
  **PerformanceUnit.Ticks**

---

* **price**
* Optional price passed in used to calculate the PnL such as **Close[0]**. This value is used as the current price and compared against your entry price for the PnL.
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // If not flat print our unrealized PnL
    if (Position.MarketPosition != MarketPosition.Flat)
        Print("Open PnL: " + Position.GetUnrealizedProfitLoss(PerformanceUnit.Points, Close[0]));
}
```
