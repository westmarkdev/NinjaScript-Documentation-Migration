---
title: C# Method (Functions) Reference
pathName: c_method_functions_reference
parent: educational_resources
section: guides
status: imported
---

## Native Methods

The Microsoft .NET environment has a rich class library that you can access when developing custom indicators and strategies. There is a plethora of information available online and in print that details class libraries in great depth. Below are quick links to the Microsoft Developers Network for some of the basic classes whose functionality you may harness when developing in NinjaScript.

Complete [list of classes](https://msdn.microsoft.com/en-us/library/d11h6832(v=vs.90).aspx) in the Microsoft .NET environment.

[MSDN (Microsoft Developers Network) C# Language Reference](http://msdn.microsoft.com/en-us/library/ms228593.aspx)

[Keywords](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/index)

[Operators](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/index)

[Arrays](http://msdn.microsoft.com/en-us/library/9b9dty7d)

{% callout type="note" %}

System.Math
Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions.
Full list of [member](https://msdn.microsoft.com/en-us/library/xaz41263(v=vs.110).aspx) of the System.Math class.
{% /callout %}

```csharp
// Example of the Max method of the **System.Math** class
int myInteger = Math.Max(10, 20);
Print("The larger value between 10 and 20 is " + myInteger.ToString());
```

{% callout type="note" %}

System.DateTime
Represents an instant in time, typically expressed as a date and time of day.
Full list of [members](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.113).aspx) of the **System.DateTime** structure.
{% /callout %}

```csharp
// Example of the Now property member of the **System.DateTime** structure
DateTime startTime = DateTime.Now;
Print("Time elapsed is " + DateTime.Now.Subtract(startTime).TotalMilliseconds.ToString() + " milliseconds.");
```

{% callout type="note" %}

System.String
Represents text; that is, a series of unicode characters.
Full list of [members](https://msdn.microsoft.com/en-us/library/system.string(v=vs.113).aspx) of the **System.String** class.
{% /callout %}

```csharp
// Example of the ToUpper() method of the **System.String** class
string myString = "ninjatrader";
Print("The following word is in uppercase " + myString.ToUpper());
```
