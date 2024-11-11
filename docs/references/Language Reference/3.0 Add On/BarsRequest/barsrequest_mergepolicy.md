---
title: MergePolicy
pathName: mergepolicy
parent: barsrequest
section: references
status: imported
---

## Definition

Determines the merge policy of the bars request.

{% callout type="note" %}

This property is ONLY applicable to Futures contracts. General information regarding merge policies can be found from the [Market Data Configuration](merge_policy) section. For an Instruments configured merge policy, please see the [MasterInstrument.MergePolicy](merge_policy) property.

{% /callout %}

## Property Value

Represents the MergePolicy used for the bars request.

Possible values are:

{% table %}

---

* DoNotMerge
* No merge policy is applied

---

* MergeBackAdjusted
* Merge policy is applied between contracts along with rollover offsets

---

* MergeNonBackAdjusted
* Merge policy is applied between contracts without offsets

---

* UseGlobalSettings
* Uses the value configured from Tools -> Options -> Market Data

---

* UseDefault
* Uses the default values configured for the [MasterInstrument](masterinstrument)
{% /table %}

## Syntax

**MergePolicy**

## Example

```csharp
// request the last 365 1 day bars
BarsRequest useGlobalRequest = new BarsRequest(Instrument.GetInstrument("ES 09-16"), 365);
useGlobalRequest.BarsPeriod = new BarsPeriod { BarsPeriodType = BarsPeriodType.Day, Value = 1 };

// use the merge policy the user has configured as their global setting
useGlobalRequest.MergePolicy = MergePolicy.UseGlobalSettings;
useGlobalRequest.Request(new Action<barsrequest, errorcode,="" string="">((barsRequest, errorCode, errorMessage) =>{

   Print("bars returned=" + barsRequest.Bars.Count);

}));

// dispose of the bars request if we are done with it
useGlobalRequest.Dispose();
```
