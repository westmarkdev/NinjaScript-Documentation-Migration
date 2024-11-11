---
title: Aroon Oscillator
pathName: aroon_oscillator
parent: system_indicator_methods
section: references
status: review
---

## Description

A trend-following indicator that uses aspects of the Aroon indicator ("Aroon up" and "Aroon down") to gauge the strength of a current trend and the likelihood that it will continue. The Aroon oscillator is calculated by subtracting Aroon down from Aroon up. Readings above zero indicate that an uptrend is present, while readings below zero indicate that a downtrend is present.

Courtesy of [Investopedia](http://investopedia.com/terms/a/aroonoscillator.asp)

## Syntax

**AroonOscillator(int period)**  

**AroonOscillator(ISeries<`double`> input, int period)**

Returns default value  

**AroonOscillator[int period](int barsAgo)**  

**AroonOscillator[ISeries<`double`> input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// Prints the current values of a 20 period AroonOscillator using default price type
double upValue = AroonOscillator(20)[0];
Print("The current AroonOscillator value is " + upValue.ToString());

// Prints the current values of a 20 period AroonOscillator using high price type
double upValue = AroonOscillator(High, 20)[0];
Print("The current AroonOscillator value is " + upValue.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
