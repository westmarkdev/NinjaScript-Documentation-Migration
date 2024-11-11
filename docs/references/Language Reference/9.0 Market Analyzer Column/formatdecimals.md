---
title: FormatDecimals
pathName: formatdecimals
parent: market_analyzer_column
status: imported
section: references
---

## Definition

Rounds the value contained in **CurrentValue** to a specified number of decimal places before displaying it in the Market Analyzer column.

## Property Value

An int representing a number of decimal places to which to round **CurrentValue**.

## Syntax

**FormatDecimals**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Round CurrentValue to one decimal place
        FormatDecimals = 1;
    }
}

protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
    CurrentValue = marketDataUpdate.Price;
}
```
