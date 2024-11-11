---
status: double_check
pathName: volume
title: Volume (VOL)
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

Volume is simply the number of shares (or contracts) traded during a specified time frame (e.g., hour, day, week, month, etc). The analysis of volume is a basic yet very important element of technical analysis. Volume provides clues as to the intensity of a given price move.

... Courtesy of [Market In Out](http://www.marketinout.com/technical_analysis.php?id=114)

## Syntax

**VOL()**  
**VOL(ISeries<`double`> input)**

### Returns default value  

**VOL()[int barsAgo]**  
**VOL(ISeries<`double`> input)[int barsAgo]**

## Return Value

double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter

* Description

---

* input

* Indicator source data ([?](valid_input_data_for_indicator.md))

---

{% /table %}

## Example

```csharp
// Prints the current value VOL  
double value = VOL()[0];  
Print("The current VOL value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
