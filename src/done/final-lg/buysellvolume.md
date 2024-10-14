---
title: "BuySell Volume"
pathName: buysellvolume
---

## Description

The BuySellVolume indicator displays a real-time horizontal histogram of volume categorized as buy or sell trades. Trades are categorized in real-time as a buy (at the ask or above) or as a sell (at the bid or below) and then color coded. Trades in between the market are ignored.

{% callout type="note" %}
For historical calculations, [Tick Replay](tick_replay) must be enabled.
{% /callout %}

## Syntax

```csharp
BuySellVolume()
BuySellVolume(ISeries<double> input)

Returns buy volume
BuySellVolume().Buys[int barsAgo]
BuySellVolume(ISeries<double> input).Buys[int barsAgo]

Returns sell volume
BuySellVolume().Sells[int barsAgo]
BuySellVolume(ISeries<double> input).Sells[int barsAgo]
```

## Return Value

double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator)) |

## Example

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Indicators will inherit the Calculate mode from the hosting script.
        // Since BuySellVolume requires the use of Calculate.OnEachTick, we must ensure the hosting script has this Calculate mode set
        Calculate = Calculate.OnEachTick;
    }
}

protected override void OnBarUpdate()
{
    // This checks that 5,000 or more of the volume hit the bid or lower
    if (State == State.Historical || BuySellVolume().Sells[0] > 5000)
    {
        EnterLong();
    }
}
```

{% callout type="tip" %}
Since this indicator operates in a real-time environment, remember to check for State.Realtime, or enable Tick Replay on the associated Data Series. In the above example, we check that 5,000 or more of the volume hit the bid or lower. Our statement checks if the data is being calculated on historical data first; if true, we enter long; if not true (live), the statement then checks for the Buy Volume condition.
{% /callout %}

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
