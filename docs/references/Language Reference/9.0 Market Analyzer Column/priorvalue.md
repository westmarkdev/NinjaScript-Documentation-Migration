---
title: PriorValue
pathName: priorvalue
parent: market_analyzer_column
section: references
status: imported
---

## Definition

Contains the last value of **CurrentValue**. **PriorValue** is assigned the value of **CurrentValue** immediately before **CurrentValue** is updated.

## Property Value

A double containing the last value contained in **CurrentValue** before its most recent update.

## Syntax

**PriorValue**

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if (marketDataUpdate.MarketDataType == MarketDataType.Last)
   {
       CurrentValue = marketDataUpdate.Price;

       // Trigger an alert if the current Last price update is greater than the previous one
       if(CurrentValue > **PriorValue**)
           Alert("MA Alert", Priority.High, "Check Market Analyzer", "", 30, Brushes.Black, Brushes.White);
   }
}

```

{% callout type="note" %}

Additional notes or information can be placed here.
{% /callout %}

```
