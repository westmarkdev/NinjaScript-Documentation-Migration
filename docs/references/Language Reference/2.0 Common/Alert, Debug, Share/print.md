---
section: references
title: Print()
pathName: print
parent: alert_debug_share
status: review
---

## Definition

Converts object data to a string format and appends the specified value as text to the NinjaScript **Output window**. Printing data to the NinjaScript Output window is a useful debugging technique to verify values while developing your custom NinjaScript object.

{% callout type="note" %}

Notes: The Print() method only targets the Output tab recently specified by set **PrintTo** property.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**Print(object value)**

{% callout type="warning" %}

Warning: High frequency of Print() method calls can represent a performance hit on your PC. Please see the NinjaScript section of the [Performance Tips](performance_tips2) article for more information.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **value**
* The object to print to the output window

{% /table %}

{% callout type="note" %}

Tips:

1. You can format prices aligned for easier debugging by using the **ToString()** method. E.g., **Low[0].ToString("0.00")** forces the format from 12.5 to 12.50. **Low[0].ToString("0.000")** forces 12.500.
2. You can format one or more objects in a specified string with the text equivalent of a corresponding object's value for better maintainability using the .NET **string.Format()** method. Please see the examples below.
{% /callout %}

## Examples

### Passing objects directly to Print() method

```csharp
protected override void OnBarUpdate()
{
   // Generates a message
   Print("This is a message");
   //Output:  This is a message
   Print("The high of the current bar is : " + High[0]);
   //Output:  The high of the current bar is : 2112.75
   // Prints the current bar SMA value to the output window
   Print(SMA(Close, 20)[0]);
   //Output: 2110.5;
}
```

### Passing string.Format() directly to Print() method

```csharp
protected override void OnBarUpdate()
{
   //Format and Print each bar value to the output window
   Print(string.Format("{0};{1};{2};{3};{4};{5}", Time[0], Open[0], High[0], Low[0], Close[0], Volume[0]));
   //Output:  2/24/2015 11:01:00 AM;2110.5;2110.5;2109.75;2110;1702
}
```

### Storing and reusing variables in Print() method

```csharp
protected override void OnBarUpdate()
{
   //store the Close[0] value in a variable which can be printed later
   double myValue = Close[0];
   //create and store a custom error message
   string myError = string.Format("Error on Bar {0}, value {1} was not expected", CurrentBar, myValue);
   //our first test case, if true print our error
   if(myValue > High[0])
     Print(myError);
   //Output: Error on Bar 233, value 1588.25 was not expected
   //reassign myValue
   myValue = Low[0];
   //our second test case (now uses Low[0]), if true print our error
   if(myValue > Close[0])
     Print(myError);
   //Output: Error on Bar 57, value 1585.5 was not expected
}
```
