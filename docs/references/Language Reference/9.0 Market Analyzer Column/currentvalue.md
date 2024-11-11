---
title: CurrentValue
pathName: currentvalue
parent: market_analyzer_column
status: imported
section: references
---

## Definition

The value to be displayed in the Market Analyzer Column

## Property Value

A double representing the value to be displayed in the column

## Syntax

**CurrentValue**

## Examples

```csharp
protected override void OnMarketData(Data.MarketDataEventArgs marketDataUpdate)
{
     CurrentValue = marketDataUpdate.Price;
}
```
