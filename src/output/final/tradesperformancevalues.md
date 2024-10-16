---
title: "TradesPerformanceValues"
pathName: /docs/desktop/tradesperformancevalues
---

## Definition

Performance values of a [collection](/docs/desktop/tradecollection) of [Trade](/docs/desktop/trade) objects.

- Currency and Point based calculations are per trade.
- Percent based calculations are per traded unit.

## Methods and Properties

|  |  |
| --- | --- |
| [AverageEtd](/docs/desktop/averageetd) | A double value representing avg end trade draw down. |
| [AverageMae](/docs/desktop/averagemae) | A double value representing avg maximum adverse excursion. |
| [AverageMfe](/docs/desktop/averagemfe) | A double value representing avg maximum favorable excursion. |
| [AverageProfit](/docs/desktop/averageprofit) | A double value representing avg profit. |
| [CumProfit](/docs/desktop/cumprofit) | A double value representing cumulative profit (percent is compounded). |
| [Drawdown](/docs/desktop/drawdown) | A double value representing draw down. |
| [LargestLoser](/docs/desktop/largestloser) | A double value representing largest loss. |
| [LargestWinner](/docs/desktop/largestwinner) | A double value representing largest gain. |
| [ProfitPerMonth](/docs/desktop/profitpermonth) | A double value representing profit per month always as a percent. |
| [StdDev](/docs/desktop/stddev) | A double value representing standard deviation on a per unit basis. |
| [Turnaround](/docs/desktop/turnaround) | A double value representing the turnaround. |
| [Ulcer](/docs/desktop/ulcer) | A double value representing the Ulcer value. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // If the profit on real-time trades is > $1000 stop trading
    if (SystemPerformance.RealTimeTrades.TradesPerformance.Currency.CumProfit > 1000)
        return;
}
```

