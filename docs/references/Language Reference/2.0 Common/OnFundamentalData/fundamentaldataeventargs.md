---
title: FundamentalDataEventArgs
pathName: fundamentaldataeventargs
parent: onfundamentaldata
section: references
status: review
---

## Definition

Represents a change in fundamental data and is passed as a parameter in the **OnFundamentalData()** method.

## Methods and Parameters

{% table %}

* DateTimeValue
* DoubleValue
* FundamentalDataType
* IsReset
* LongValue
* ToString()

---

* A **DateTime** value representing the time
* A **double** value representing fundamental data
* Possible values:
  * AverageDailyVolume
  * Beta
  * CalendarYearHigh
  * CalendarYearHighDate
  * CalendarYearLow
  * CalendarYearLowDate
  * CurrentRatio
  * DividendAmount
  * DividendPayDate
  * DividendYield
  * EarningsPerShare
  * FiveYearsGrowthPercentage
  * High52Weeks
  * High52WeeksDate
  * HistoricalVolatility
  * Low52Weeks
  * Low52WeeksDate
  * MarketCap
  * NextYearsEarningsPerShare
  * PercentHeldByInstitutions
  * PriceEarningsRatio
  * RevenuePerShare
  * SharesOutstanding
  * ShortInterest
  * ShortInterestRatio
  * VWAP

---

* A bool value representing if a UI reset is needed after a manual disconnect. Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset.
* A long value representing fundamental data
* A string representation of the FundamentalDataEventArgs object
{% /table %}

## Examples

```csharp
protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate)
{
    // Print some data to the Output window
    if (fundamentalDataUpdate.FundamentalDataType == FundamentalDataType.AverageDailyVolume)
        Print("Average Daily Volume = " + fundamentalDataUpdate.LongValue);
    else if (fundamentalDataUpdate.FundamentalDataType == FundamentalDataType.PriceEarningsRatio)
        Print("P/E Ratio = " + fundamentalDataUpdate.DoubleValue);
}
```

{% callout type="note" %}

* Not all connectivity providers support all FundamentalDataTypes.
* **EarningsPerShare** on eSignal is a trailing twelve months value. On IQFeed it is the last quarter's value.
* **RevenuePerShare** is a trailing twelve months value.

{% /callout %}
