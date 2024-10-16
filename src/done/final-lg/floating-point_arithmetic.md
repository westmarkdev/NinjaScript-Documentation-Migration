---
title: "Floating-Point Arithmetic"
pathName: floating-point_arithmetic
---

## Overview

Some common problems that you may encounter when comparing different double values are the caveats involved with floating-point arithmetic. Because of the way computers store floating-point numbers, under certain conditions, your value will be an approximation of the actual decimal number you wanted. If this situation arises in your code, your comparison logic may not execute as you had intended even if your logic was mathematically sound on paper. To address this issue, you will need to use a range comparison that takes into account the slight differences in the least significant digits of the floats.

## Example Comparison

For example, under normal mathematics, we would assume `double x` is equivalent to `double y`.

```csharp
double x = 90.10;
double y = 100 * 0.9010;
Print("double x: " + x);
Print("double y: " + y);
```

Even the output of this code segment suggests they are the same:

```csharp
double x = 90.1;
double y = 90.1;
```

Unfortunately, as demonstrated by this code segment, they are not.

```csharp
bool c = (x == y);
Print("x equals y: " + c);
```

This segment outputs the following:

```csharp
x equals y: False
```

This means when we try to check for equality, it would never evaluate to true even if it does mathematically.

```csharp
if (x == y)
// Do something. This will never be true.
```

## Range Comparison

Instead of comparing `double x` to `y` for exact equality, we will need to check a range.

```csharp
if (Math.Abs(x - y) < 0.0001)
// Do something
```

The arbitrary constant you choose to compare the range with should match the precision and accuracy of the floating-point numbers you are comparing.

## Using double.Epsilon

Alternatively, you can check the difference between the two variables against the [double.Epsilon](https://learn.microsoft.com/en-us/dotnet/api/system.double.epsilon?view=netframework-4.8) field. The `double.Epsilon` field represents the smallest possible double value.

```csharp
if (Math.Abs(x - y) < double.Epsilon)
// Do something
```

## Using Compare()

You can also use a `Compare()` method to accurately compare floating-point numbers. Take note that this method should only be used to compare price values since its precision is based on the instrument's tick size and may be unsuited for use in other floating-point situations.

```csharp
double newPriceRange = Close[0] - Open[0];
double oldPriceRange = Close[1] - Open[1];
if (Instrument.MasterInstrument.Compare(newPriceRange, oldPriceRange) == 1)
{
// Do something
}
```

The `Compare()` method returns a value of "1" if the first parameter is greater than the second, "-1" if the first parameter is less than the second, and "0" if the first parameter is equal to the second.

## Further Resources

For a more formal analysis of floating-point arithmetic, there are many resources online:

- [Floating Point Problems](http://docs.sun.com/ncg_goldberg.html)
- [Extreme Floating Point](http://www.codeproject.com/dotnet/extremefloatingpoint1.asp#terms)
