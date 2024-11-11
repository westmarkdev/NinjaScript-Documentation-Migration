---
status: double_check
title: Woodies Pivots
pathName: woodies_pivots
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

Woodies CCI Club pivots indicator.

## Syntax

**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width)**  
**WoodiesPivots(ISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width)**  

Returns pivot point value  

**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width).PP[int barsAgo]**  

**WoodiesPivotsISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width).PP[int barsAgo]**  

Returns R1 value  
**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width).R1[int barsAgo]**  

**WoodiesPivots(ISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width).R1[int barsAgo]**  

Returns R2 value  
**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width).R2[int barsAgo]**  

**WoodiesPivots(ISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width).R2[int barsAgo]**  

Returns S1 value  
**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width).S1[int barsAgo]**  

**WoodiesPivots(ISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width).S1[int barsAgo]**  

Returns S2 value  
**WoodiesPivots(HLCCalculationModeWoodie priorDayHLC, int width).S2[int barsAgo]**  

**WoodiesPivots(ISeries<`double`> input, HLCCalculationModeWoodie priorDayHLC, int width).S2[int barsAgo]**

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

* priorDayHLC

* Sets how the prior range High, Low, Close values are calculated. Possible values are:

  * HLCCalculationModeWoodie.CalcFromIntradayData

  * HLCCalculationModeWoodie.DailyBars

  * HLCCalculationModeWoodie.UserDefinedValues

---

* width

* An int determining the width of the pivot values plotted

---

{% /table %}

## Example

```csharp
// Prints the current pivot point value  
double ppValue = WoodiesPivots(HLCCalculationModeWoodie.CalcFromIntradayData, 20).PP[0];  
Print("The current Woodies Pivots' pivot value is " + ppValue);  
   
// Prints the current S2 pivot value  
double s2Value = WoodiesPivots(HLCCalculationModeWoodie.CalcFromIntradayData, 20).S2[0];  
Print("The current Woodies Pivots' S2 pivot value is " + s2Value);
```

{% callout type="note" %}

Tip: When using HLCCalculationMode.**DailyBars** it can be expected that a value of 0 is returned when the daily bars have not been loaded yet. Due to the asynchronous nature of this indicator calling daily bars you should only access the pivot values when the indicator has loaded all required Bars objects. To ensure you are accessing accurate values you can use [.IsValidDataPoint()](isvaliddatapoint)as a check.

{% /callout %}

```csharp
// Evaluates that this is a valid Woodies Pivots value  
if (WoodiesPivots(HLCCalculationModeWoodie.DailyBars, 20).PP.IsValidDataPoint(0))  
{  
    // Prints the current pivot point value  
    double value = WoodiesPivots(HLCCalculationModeWoodie.DailyBars, 20).PP[0];  
    Print("The current Woodies Pivots' pivot value is " + value.ToString());  
}
```
