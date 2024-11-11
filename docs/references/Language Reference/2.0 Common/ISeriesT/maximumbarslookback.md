---
title: MaximumBarsLookBack
pathName: maximumbarslookback
parent: iseriest
section: references
status: review
---

## Definition

Determines memory performance of custom **Series`<t>`** objects (such as **Series<`double`>**, **Series<`long`>**, etc.). When using **MaximumBarsLookBack.TwoHundredFiftySix**, only the last 256 values of the series object will be stored in memory and be accessible for reference. This results in significant memory savings when using multiple series objects. In the rare case should you need older values you can use **MaximumBarsLookBack.Infinite** to allow full access of the series.

{% callout type="note" %}

* **ISeries<`t`>** objects that hold bar data (such as Close, High, Volume, Time, etc) always use **MaximumBarsLookBack.Infinite** which ensures all data points are always accessible during the lifetime of your NinjaScript indicator or strategy.
* **Series<`double`>** objects that hold indicator **plot values** always use **MaximumBarsLookBack.Infinite** which ensures that charts always display the entire indicator's calculated values.
{% /callout %}

## Property Value

A **MaximumBarsLookBack** enum value. Default value is **MaximumBarsLookBack.TwoHundredFiftySix**.

Possible values are:

{% table %}

* MaximumBarsLookBack.TwoHundredFiftySix
* Only the last 256 values of the series object will be stored in memory and accessible for reference (improves memory performance)

---

* MaximumBarsLookBack.Infinite
* Allow full access of the series, but you will then not be able to utilize the benefits of memory optimization
{% /table %}

{% callout type="note" %}

A **MaximumBarsLookBack.TwoHundredFiftySix** series works as a circular ring buffer, which will "loop" when the series reaches full capacity. Specifically, once there are 256 entries in the series, new data added to the series overwrite the oldest data.

{% /callout %}

## Syntax

**MaximumBarsLookBack**

## Examples

### Setting all custom series to use the default **MaximumBarsLookBack**

```csharp
Series<double> myDoubleSeries = null;
Series<string> myStringSeries = null;

protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Example Indicator";
     // Store all series values instead of only the last 256 values
     MaximumBarsLookBack = MaximumBarsLookBack.Infinite;
   }
   else if (State == State.DataLoaded)
   {
     // The custom Series`<t>` below are all constructed using only the NinjaScriptBase object (i.e., "this")
     // therefore, the Series`<t>` **MaximumBarsLookBack is taken from the NinjaScript's configured MaximumBarsLookBack property
     myDoubleSeries = new Series<double>(this);
     myStringSeries = new Series<string>(this);
   }

```

### Optimizing custom series to use unique **MaximumBarsLookBack** behavior

```csharp
Series<double> myDoubleSeries = null;
Series<string> myStringSeries = null;

protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Example Indicator";
   }
   else if (State == State.DataLoaded)
   {
     // The custom Series`<t>` below are constructed using MaximumBarsLookBack parameter
     // therefore, each Series`<t>` will use their uniquely specified MaximumBarsLookBack properties
     myDoubleSeries = new Series<double>(this, MaximumBarsLookBack.Infinite); // stores all values
     myStringSeries = new Series<string>(this, MaximumBarsLookBack.TwoHundredFiftySix); // only the last 256 values (better performance)
   }
```
