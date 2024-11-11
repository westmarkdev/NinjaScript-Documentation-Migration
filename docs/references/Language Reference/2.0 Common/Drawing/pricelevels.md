---
section: references
title: PriceLevels Collection
pathName: pricelevels_collection
parent: drawing
status: review
---

## Definition

A collection of PriceLevel objects defining lines for multi-price-level **Drawing Tools** (Fibonacci tools, etc.). Each PriceLevel within the collection can be configured programmatically or analyzed to obtain the parameters of user-drawn objects.

{% callout type="note" %}

PriceLevels is only used with the following pre-built Drawing Tools, but it can be used with custom Drawing Tools, as well:

* [AndrewsPitchfork](draw_andrewspitchfork)
* [FibonacciCircle](draw_fibonaccicircle)
* [FibonacciExtensions](draw_fibonacciextensions)
* [FibonacciRetracements](draw_fibonacciretracements)
* [FibonacciTimeExtensions](draw_fibonaccitimeextensions)
* [GannFan](draw_gannfan)
* [TrendChannel](draw_trendchannel)
{% /callout %}

## Syntax

**PriceLevels[int idx]**  
**PriceLevels[int idx].GetPrice(double startPrice, double totalPriceRange, bool isInverted)**  
**PriceLevels[int idx].GetY(ChartScale chartScale, double startPrice, double totalPriceRange, bool isInverted)**

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* **GetPrice()**
* Returns a double which represents the price value at the specified price level

---

* **GetY()**
* Returns a float representing the y-pixel coordinate at the specified price level

---

* **Name**
* The Name property of the specified PriceLevel. Set to a formatted version of Value by default.

---

* **Stroke**
* The Stroke used to draw the line associated with the specified PriceLevel

---

* **Tag**
* A tag used to identify the specified PriceLevel. Null by default.

---

* **Value**
* The value of the PriceLevel in percentage terms
{% /table %}

## Examples

```csharp
// Define a FibonacciRetracements object outside of OnBarUpdate(), so the same object can be re-used**
FibonacciRetracements myRetracements;

protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Instantiate myRetracements
    myRetracements = Draw.FibonacciRetracements(this, "fib", true, 20, High[20], 2, Low[2]);

    // Print each price level and the corresponding value in the PriceLevels collection contain in myRetracements
    // setting isInverted correctly is important for the Fibonacci Retracements since it will define which starting point is used, as it changes based
    // on the anchors, i.e. if the Fibonacci is drawn from 100% to 0% (default) or the other inverted way (0% to 100%).
    foreach (PriceLevel p in myRetracements.PriceLevels)
    {
        Print(p.Value);
        Print(p.GetPrice(myRetracements.StartAnchor.Price, myRetracements.EndAnchor.Price - myRetracements.StartAnchor.Price, false));
    }
}
```

```csharp
// Define a TrendChannel object outside of OnBarUpdate(), so the same object can be re-used
TrendChannel myTCh;

protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Instantiate myTrendChannel
    myTCh = Draw.TrendChannel(this, "tc", true, 10, Low[10], 0, High[0], 10, High[10] + 5 * TickSize);

    // Print each price level and the corresponding value in the PriceLevels collection contain in myTrendChannel
    // For the TrendChannel the 0% is the Trend anchor, the 100% the Parallel anchor
    foreach (PriceLevel p in myTCh.PriceLevels)
    {
        Print(p.Value);
        Print(p.GetPrice(myTCh.TrendStartAnchor.Price, myTCh.ParallelStartAnchor.Price - myTCh.TrendStartAnchor.Price, false));
    }
}

```