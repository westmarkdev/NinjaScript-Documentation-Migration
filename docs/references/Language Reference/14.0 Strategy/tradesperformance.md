---
section: references
status: review
parent: strategy
title: TradesPerformance
pathName: tradesperformance
---

## Definition

Performance profile of a **collection** of **Trade** objects.

## Methods and Properties

{% table %}

* Parameter
* Description

---

* AverageBarsInTrade
* A double value representing the average number of bars per trade

---

* AverageEntryEfficiency
* A double value representing the average entry efficiency

---

* AverageExitEfficiency
* A double value representing the average exit efficiency

---

* AverageTimeInMarket
* A TimeSpan value representing quantity-weighted average duration of a trade

---

* AverageTotalEfficiency
* A double value representing the average total efficiency

---

* TotalCommission
* A double value representing the total commission

---

* Currency
* Gets a TradesPerformanceValues object in currency

---

* GrossLoss
* A double value representing the gross loss

---

* GrossProfit
* A double value representing the gross profit

---

* LongestFlatPeriod
* A TimeSpan value representing longest duration of being flat

---

* MaxConsecutiveLoser
* An int value representing the maximum number of consecutive losses seen

---

* MaxConsecutiveWinner
* An int value representing the maximum number of consecutive winners seen

---

* MaxTime2Recover
* A TimeSpan value representing maximum time to recover from a draw down

---

* MonthlyStdDev
* A double value representing the monthly standard deviation

---

* MonthlyUlcer
* A double value representing the monthly Ulcer index

---

* NetProfit
* A double value representing the net profit

---

* Percent
* Gets a TradesPerformanceValues object in percent

---

* PerformanceMetrics
* An array of custom NinjaScript performance metrics

---

* Pips
* Gets a TradesPerformanceValues object in pips

---

* Points
* Gets a TradesPerformanceValues object in points

---

* ProfitFactor
* A double value representing the profit factor

---

* R2
* A double value representing the R-squared value

---

* RiskFreeReturn
* A double value representing the risk free return rate

---

* SharpeRatio
* A double value representing the Sharpe Ratio

---

* SortinoRatio
* A double value representing the Sortino Ratio

---

* Ticks
* Gets a TradesPerformanceValues object in ticks

---

* TotalQuantity
* An int value representing the total quantity

---

* TotalSlippage
* A double value representing the total slippage. This is presented in points, I.E. 0.25 for 1 execution on E-mini S&P 500 Futures.

---

* TradesCount
* An int value representing the trades count

---

* TradesPerDay
* An int value representing the avg trades per day

---
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Only trade if you have less than 5 consecutive losers in a row
    if (SystemPerformance.RealTimeTrades.TradesPerformance.MaxConsecutiveLoser < 5)
    {
        // Trade logic here
    }
}
```
