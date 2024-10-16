---
title: "FundamentalDataEventArgs"
pathName: /docs/desktop/fundamentaldataeventargs
---

## Definition

Represents a change in fundamental data and is passed as a parameter in the [OnFundamentalData()](/docs/desktop/onfundamentaldata) method.

## Methods and Parameters

|  |  |
| --- | --- |
| DateTimeValue | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) value representing the time |
| DoubleValue | A double value representing fundamental data |
| FundamentalDataType | Possible values: {% <br> %} &bull; AverageDailyVolume{% <br> %} &bull; Beta{% <br> %} &bull; CalendarYearHigh{% <br> %} &bull; CalendarYearHighDate{% <br> %} &bull; CalendarYearLow{% <br> %} &bull; CalendarYearLowDate{% <br> %} &bull; CurrentRatio{% <br> %} &bull; DividendAmount{% <br> %} &bull; DividendPayDate{% <br> %} &bull; DividendYield{% <br> %} &bull; EarningsPerShare{% <br> %} &bull; FiveYearsGrowthPercentage{% <br> %} &bull; High52Weeks{% <br> %} &bull; High52WeeksDate{% <br> %} &bull; HistoricalVolatility{% <br> %} &bull; Low52Weeks{% <br> %} &bull; Low52WeeksDate{% <br> %} &bull; MarketCap{% <br> %} &bull; NextYearsEarningsPerShare{% <br> %} &bull; PercentHeldByInstitutions{% <br> %} &bull; PriceEarningsRatio{% <br> %} &bull; RevenuePerShare{% <br> %} &bull; SharesOutstanding{% <br> %} &bull; ShortInterest{% <br> %} &bull; ShortInterestRatio{% <br> %} &bull; VWAP |
| IsReset | A bool value representing if a UI reset is needed after a manual disconnect. {% <br> %} **Note**: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. |
| LongValue | A long value representing fundamental data |
| ToString() | A string representation of the FundamentalDataEventArgs object |

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

## Tips

1. Not all connectivity providers support all FundamentalDataTypes.
2. EarningsPerShare on eSignal is a trailing twelve months value. On IQFeed, it is the last quarter's value.
3. RevenuePerShare is a trailing twelve months value.
