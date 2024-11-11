---
title: MarketDepth
pathName: superdom_marketdepth
parent: superdom_column
status: imported
section: references
---

## Definition

The **OnMarketDepth()** method is called and guaranteed to be in the correct sequence for every change in level two market data (market depth) for the underlying instrument.

## Method Return Value

This method does not return a value.

## Syntax

**MarketDepth**

## Examples

```csharp
protected override void OnMarketDepth(Data.MarketDepthEventArgs marketDepthUpdate)

{
    if (marketDepthUpdate.MarketDataType == MarketDataType.Ask && marketDepthUpdate.Operation == Operation.Update)
        // Do something
}
```
