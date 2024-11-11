---
title: CurrentText
pathName: currenttext
parent: market_analyzer_column
status: imported
section: references
---

## Definition

Sets text to be displayed in the Market Analyzer column.

{% callout type="note" %}

**CurrentText** will overrule any value set for [**CurrentValue**](currentvalue). If both **CurrentValue** and **CurrentText** have assigned values, the value of **CurrentText** will display in the column.

{% /callout %}

## Property Value

A string representing text to display in the column.

## Syntax

**CurrentText**

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   // Print "Ask" in the column if an Ask price update is received
   if(marketDataUpdate.MarketDataType == MarketDataType.Ask)
       CurrentText = "Ask";
}
```
