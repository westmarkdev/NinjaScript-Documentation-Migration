---
title: "MarketDataEventArgs"
pathName: /docs/desktop/marketdataeventargs
---

## Definition

Represents a change in level one market data and is passed as a parameter in the [OnMarketData()](/docs/desktop/onmarketdata) method.

## Methods and Parameters

|  |  |
| --- | --- |
| Ask | A `double` value representing the ask price |
| Bid | A `double` value representing the bid price |
| Instrument | An `Instrument` object representing the instrument of the market data |
| IsReset | A `bool` value representing if a UI reset is needed after a manual disconnect. {% <br> %} **Note**: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. |
| MarketDataType | Possible values are: {% <br> %} &bull; MarketDataType.Ask{% <br> %} &bull; MarketDataType.Bid{% <br> %} &bull; MarketDataType.DailyHigh{% <br> %} &bull; MarketDataType.DailyLow{% <br> %} &bull; MarketDataType.DailyVolume{% <br> %} &bull; MarketDataType.Last{% <br> %} &bull; MarketDataType.LastClose (prior session close){% <br> %} &bull; MarketDataType.Opening{% <br> %} &bull; MarketDataType.OpenInterest (supported by IQFeed, Kinetick){% <br> %} &bull; MarketDataType.Settlement |
| Price | A `double` value representing the price |
| Time | A [DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime) structure representing the time |
| ToString() | A string representation of the `MarketDataEventArgs` object |
| Volume | A `long` value representing volume |

{% callout type="warning" %}
If used with [TickReplay](/docs/desktop/tick_replay), please keep in mind Tick Replay ONLY replays the Last market data event, and only stores the best inside bid/ask price at the time of the last trade event. You can think of this as the equivalent of the bid/ask price at the time a trade was reported. Please also see [Developing for Tick Replay](/docs/desktop/developing_for__tick_replay).
{% /callout %}

|  |
| --- |
| Tips {% <br> %} &bull; Not all connectivity providers support all MarketDataTypes. {% <br> %} &bull; For an example of how to use IsReset please see \MarketAnalyzerColumns\AskPrice.cs |

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
    // Print some data to the Output window
    if (marketDataUpdate.MarketDataType == MarketDataType.Last)
        Print("Last = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
    else if (marketDataUpdate.MarketDataType == MarketDataType.Ask)
        Print("Ask = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
    else if (marketDataUpdate.MarketDataType == MarketDataType.Bid)
        Print("Bid = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
}
```
