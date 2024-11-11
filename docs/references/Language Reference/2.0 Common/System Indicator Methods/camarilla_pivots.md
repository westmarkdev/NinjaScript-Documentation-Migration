---
title: Camarilla Pivots
pathName: camarilla_pivots
parent: system_indicator_methods
section: references
status: review
---

## Description

Camarilla pivots are a price analysis tool that generates potential support and resistance levels by multiplying the prior range then adding or subtracting it from the close.

## Syntax

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width)**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width)**

Returns R1 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R1[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R1[int barsAgo]**

Returns R2 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R2[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R2[int barsAgo]**

Returns R3 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R3[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R3[int barsAgo]**

Returns R4 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R4[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).R4[int barsAgo]**

Returns S1 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S1[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S1[int barsAgo]**

Returns S2 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S2[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S2[int barsAgo]**

Returns S3 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S3[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S3[int barsAgo]**

Returns S4 value  

**Pivots(PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S4[int barsAgo]**  

**Pivots(ISeries`<double>` input, PivotRange pivotRangeType, HLCCalculationMode priorDayHLC, double userDefinedClose, double userDefinedHigh, double userDefinedLow, int width).S4[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **input**
* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* **pivotRangeType**
* Sets the range for the type of pivot calculated. Possible values are:  
**PivotRange.Daily**  
**PivotRange.Weekly**  
**PivotRange.Monthly**

---

* **priorDayHLC**
* Sets how the prior range High, Low, Close values are calculated. Possible values are:  
**HLCCalculationMode.CalcFromIntradayData**  
**HLCCalculationMode.DailyBars**  
**HLCCalculationMode.UserDefinedValues**

---

* **userDefinedClose**
* Sets the close for Pivots calculations when using **HLCCalculationMode.UserDefinedValues**.

---

* **userDefinedHigh**
* Sets the high for Pivots calculations when using **HLCCalculationMode.UserDefinedValues**.

---

* **userDefinedLow**
* Sets the low for Pivots calculations when using **HLCCalculationMode.UserDefinedValues**.

---

* **width**
* Sets how long the Pivots lines will be drawn
{% /table %}

## Examples

```csharp
// Prints the current R1 pivot value  
double valueR1 = CamarillaPivots(PivotRange.Daily, HLCCalculationMode.CalcFromIntradayData, 0, 0, 0, 20).R1[0];  
Print("The current Camarilla Pivots' R1 value is " + valueR1.ToString());  
// Prints the current S2 pivot value  
double valueS2 = CamarillaPivots(PivotRange.Daily, HLCCalculationMode.CalcFromIntradayData, 0, 0, 0, 20).S2[0];  
Print("The current Camarilla Pivots' S2 pivot value is " + valueS2.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

{% callout type="note" %}

* When using **HLCCalculationMode.DailyBars** it can be expected that a value of 0 is returned when the daily bars have not been loaded yet. Due to the asynchronous nature of this indicator calling daily bars you should only access the pivot values when the indicator has loaded all required Bars objects. To ensure you are accessing accurate values you can use **.[IsValidDataPoint()**](isvaliddatapoint) as a check:

{% /callout %}

```csharp
if (CamarillaPivots(PivotRange.Daily, HLCCalculationMode.DailyBars, 0, 0, 0, 20).Pp.IsValidDataPoint(0))  
{  
    // Prints the current pivot point value  
    double valuePp = CamarillaPivots(PivotRange.Daily, HLCCalculationMode.DailyBars, 0, 0, 0, 20).Pp[0];  
    Print("The current Camarilla Pivots' pivot value is " + valuePp.ToString());  
}
```
