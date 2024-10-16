---
title: "CategoryOrderAttribute"
pathName: /docs/desktop/categoryorderattribute
---

## Definition

Determines the sequence in which a NinjaScript object's [Display.GroupName](/docs/desktop/displayattribute) categories are arranged in relation to other categories in the UI. The default behavior will display each GroupName of an object in alphabetical order; however, this behavior can be changed by defining the CategoryOrder attribute before the object's declaration.

{% callout type="note" %}
&bull; The CategoryOrder attribute is ONLY valid on class-level declarations.  
&bull; Categories with values less than 1,000,000 appear at the very top of the property grid (excluding the Strategy Analyzer "General" category).  
&bull; NinjaTrader UI reserves using values ending in 000, 500 and the values documented below are subject to change.  
&bull; If you wish to inject your category between a standard NinjaScript category, please refer to the table below to locate the appropriate position (e.g., to set a property after "Data Series" and before the "Setup" use value of 2,000,001).  
{% /callout %}

## NinjaScript Indicators

The following table applies for Indicators configured from a Chart Indicator, Market Analyzer Indicator Column, or SuperDOM Indicator:

|  |  |
| --- | --- |
| Parameters | 1000000 |
| Data Series | 2000000 |
| Time Frame | 3000000 |
| Setup | 4000000 |
| Visual | 5000000 |
| Lines | 6000000 |
| Plots | 7000000 |

## NinjaScript Strategies

The following table applies to Chart Strategies, Control Center Strategies Grid, and the Strategy Analyzer:

|  |  |
| --- | --- |
| Parameters | 1000000 |
| Data Series | 2000000 |
| Time Frame | 3000000 |
| Setup | 4000000 |
| Historical Fill Processing | 5000000 |
| Optimize | 6000000 |
| Order Handling | 7000000 |
| Order Properties | 8000000 |

{% callout type="note" %}
The Strategy Analyzer "General" category is purposely excluded from this table and will always show at the top of the parameter grid.
{% /callout %}

## Syntax

`[Gui.CategoryOrder(string category, int order)]`

{% callout type="warning" %}
Attempting to modify the default NinjaScript Category ordering is NOT supported. Trying to do so may result in unexpected outcomes.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| category | A string identifying the [GroupName](/docs/desktop/displayattribute) to be categorized. |
| order | An int determining the sequence the Category displays. |

## Examples

```csharp
[Gui.CategoryOrder("My Strings", 1)] // display "My Strings" first
[Gui.CategoryOrder("My Bools", 2)] // then "My Bools"
[Gui.CategoryOrder("My Ints", 3)] // and finally "My Ints"
public class MyCustomIndicator : Indicator
{

#region Properties

[Display(GroupName="My Ints")]
public int MyCustomInt
{ get; set; }
[Display(GroupName="My Bools")]
public bool MyCustomBool
{ get; set; }
[Display(GroupName="My Strings")]
public string MyCustomString
{ get; set; }

#endregion

}
```