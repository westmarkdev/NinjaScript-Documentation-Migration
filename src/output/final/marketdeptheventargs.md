---
title: "MarketDepthEventArgs"
pathName: /docs/desktop/marketdeptheventargs
---

## Definition

Represents a change in level two market data also known as market depth and is passed as a parameter in the [OnMarketDepth()](/docs/desktop/onmarketdepth) method.

## Methods and Parameters

|  |  |
| --- | --- |
| Instrument | A `Instrument` object representing the instrument of the market data. |
| IsReset | A `bool` value representing if a UI reset is needed after a manual disconnect. {% <br> %} Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. |
| MarketDataType | Possible values are: {% <br> %} &bull; MarketDataType.Ask{% <br> %} &bull; MarketDataType.Bid |
| MarketMaker | A `string` representing the market maker id. |
| Operation | Represents the action you should take when building a level two book. {% <br> %} Possible values are: {% <br> %} &bull; Operation.Add{% <br> %} &bull; Operation.Update{% <br> %} &bull; Operation.Remove |
| Position | An `int` value representing the zero based position in the depth ladder. |
| Price | A `double` value representing the price. |
| Time | A `DateTime` structure representing the time. |
| ToString() | A `string` representation of the MarketDepthEventArgs object. |
| Volume | A `long` value representing volume. |

## Examples

```csharp
protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate)
{
    // Print some data to the Output window
    if (marketDepthUpdate.MarketDataType == MarketDataType.Ask && marketDepthUpdate.Operation == Operation.Update)
        Print("The most recent ask change is " + marketDepthUpdate.Price + " " + marketDepthUpdate.Volume);
}
```

{% callout type="tip" %}
For an example of how to use IsReset please see \MarketAnalyzerColumns\AskPrice.cs
{% /callout %}
