---
status: double_check
pathName: volume_up_down
title: Volume Up Down
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

Variation of the [VOL](volume.md) (Volume) indicator that colors the volume histogram different color depending if the current bar is up or down bar.

## Syntax

**VolumeUpDown()**  
**VolumeUpDown(ISeries<`double`> input)**

### Returns default value  

**VolumeUpDown()[int barsAgo]**  
**VolumeUpDown[ISeries<`double`> input](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter

* Description

---

* input

* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* period

* Number of bars used in the calculation

---

{% /table %}

## Example

```csharp
// Prints the current value VolumeUpDown  
double value = VolumeUpDown()[0];  
Print("The current Volume value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
