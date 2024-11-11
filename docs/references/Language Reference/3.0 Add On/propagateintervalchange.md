---
title: PropagateIntervalChange()
pathName: propagateintervalchange
parent: add_on
section: references
status: imported
---

## Definition

In an **NTWindow**, **PropagateIntervalChange()** sends an interval to other windows with the same Interval Linking color configured.

{% callout type="note" %}

* A public BarsPeriod property must be defined in order to use **PropagateIntervalChange()**, as in the example below.
* For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](developing_add_ons).
{% /callout %}

## Examples

```csharp
// This custom method will be fired when an interval selector in a custom NTTabPage changes intervals
private void OnIntervalChanged(object sender, BarsPeriodEventArgs args)
{
   if (args.BarsPeriod == null)
       return;

   PropagateIntervalChange(args.BarsPeriod);
}

```
