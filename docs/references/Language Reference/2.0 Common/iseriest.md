---
title: ISeries
pathName: iseriest
parent: common
section: references
status: review
---

## Definition

**ISeries** is an interface that is implemented by all NinjaScript classes that manage historical data as an **ISeries`<double>`** (Open, High, Low, Close, etc), used for indicator input, and other object data. Please see the help guide article on [Working with Price Series](working_with_price_series) for a basic overview on how to access this information.

## Types of ISeries

{% table %}

* [Series<`t`>](seriest)
* Represents a generic custom data structure for custom development

---

* [PriceSeries](priceseries)
* Historical price data structured as an **ISeries`<double>`** interface (Close[0], High[0], Low[0], etc)

---

* [TimeSeries](timeseries)
* Historical time stamps structured as an **ISeries<`datetime`>** interface (Time[0])

---

* [VolumeSeries](volumeseries.md)
* Historical volume data structured as an **ISeries`<double>`** interface (Volume[0])
{% /table %}

## Methods and Properties

{% table %}

---

* [GetValueAt()](docs/references/Language%20Reference/2.0%20Common/ISeriesT/getvalueat.md)
* Returns the underlying input value at a specified bar index value.

---

* [IsValidDataPoint()](isvaliddatapoint)
* Indicates if the specified input is set at a barsAgo value relative to the current bar.

---

* [IsValidDataPointAt()](isvaliddatapointat)
* Indicates if the specified input is set at a specified bar index value.

---

* [Count](iseries_count)
* Return the number total number of values in the **ISeries** array
{% /table %}

{% callout type="note" %}

Tips: (see examples below)

1. By specifying a parameter of type **ISeries`<double>`**, you can then pass in an array of closing prices, an indicator, or a user defined data series.
2. When working with **ISeries`<double>`** objects in your code you may come across situations where you are not sure if the value being accessed is a valid value or just a "placeholder" value. To check if you are using valid values for your logic calculations that have been explicitly set, please use **.IsValidDataPoint(int barsAgo)** to check.
{% /callout %}

## Examples

### Using **ISeries** as a method parameter

```csharp

private double DoubleTheValue(ISeries`<double>` priceData)
{
    return priceData[0] * 2;
}

protected override void OnBarUpdate()
{
    Print(DoubleTheValue(Close));
    Print(DoubleTheValue(SMA(20)));
}

```

### Checking **ISeries** value before accessing

```csharp

protected override void OnBarUpdate()
{
    if (Input.IsValidDataPoint(0))
        Plot0[0] = Input[0];
}

```
