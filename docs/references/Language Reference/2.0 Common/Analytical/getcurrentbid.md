---
title: GetCurrentBid()
pathName: getcurrentbid
parent: analytical
section: references
status: review
---

## Definition

Returns the current real-time bid price.

{% callout type="note" %}

Notes:

1. When accessed during **State.Historical**, the [Close](close) price of the evaluated bar is substituted. To access historical bid prices, please see [Developing for Tick Replay](developing_for_tick_replay.md).
2. The **GetCurrentBid()** method runs on the bar series currently updating determined by the **BarsInProgress** property. For [multi-instrument](multi_time_frame_instruments.md) scripts, an additional int "barsSeriesIndex" parameter can be supplied which forces the method to run on an supplementary bar series.
{% /callout %}

## Method Return Value

A **double** value representing the current bid price.

## Syntax  

**GetCurrentBid()**  
**GetCurrentBid(int barsSeriesIndex)**

## Parameters

{% table %}

* Parameter
* Description

---

* **barsSeriesIndex**
* An **int** value determining the bar series the method runs. Note: This optional parameter is reserved for multi-instrument scripts
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // Ensure we do not call GetCurrentBid() on historical data
   if (State == State.Historical)
     return;

   double currentBid = GetCurrentBid();
   Print("The Current Bid price is: " + currentBid);
   // The Current Bid price is: 1924.75
}

```csharp

protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Example's Indicator";
   }
   if (State == State.Configure)
   {
     //Add MSFT as our additional data series
     AddDataSeries("MSFT", BarsPeriodType.Minute, 1);
   }
}

protected override void OnBarUpdate()
{
   // Ensure we do not call GetCurrentBid() on historical data
   if (State == State.Historical)
     return;

   if (BarsInProgress == 0)
   {
     double primaryBid = GetCurrentBid(0);
     Print("The Primary Bid price is: " + primaryBid);
     // The Primary Bid price is: 1924.75
   }

   if (BarsInProgress == 1)
   {
     double msftBid = GetCurrentBid(1);
     Print("MSFT's Current Bid price is: " + msftBid);
     // MSFT's Current Bid is: 43.63
   }
}
```
