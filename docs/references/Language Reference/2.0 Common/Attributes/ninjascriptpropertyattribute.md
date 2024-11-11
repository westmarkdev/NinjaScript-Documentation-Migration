---
title: NinjaScriptPropertyAttribute
pathName: ninjascriptpropertyattribute
parent: attributes
section: references
status: imported
---

## Definition

Determines if the following declared property should be included in the **NinjaScript** object's constructor as a parameter. This is useful if you plan on calling a **NinjaScript** object from another (e.g., calling a custom indicator from a strategy) or customizing the display parameter data on a grid or from a chart. This also used to make parameters [optimizable](optimize_a_strategy) in the Strategy Analyzer.

{% callout type="note" %}

Warning: Only types which can be [Xml Serialized](xmlignoreattribute) should be marked as a **NinjaScriptAttribute**, otherwise you may run into errors when persisting values in various scenarios (e.g., saving workspace, or running [Strategy Optimizations](optimize_a_strategy)). Should you have a property you wish to use as user defined input, you will need to implement a secondary simple type (such as an int or string) as the value to be serialized as user input. Please see the example below which demonstrates using a simple type as the **NinjaScriptProperty** against types which cannot be serialized.

{% /callout %}

## Syntax

**[NinjaScriptProperty]**

## Parameters

This object contains no parameters.

## Examples

### Basic usage of **NinjaScriptProperty**

```csharp
#region Properties
// set **NinjaScriptProperty** to ensure this property is used when calling from another object
[NinjaScriptProperty]
public bool MyBool
{ get; set; }

// do not set **NinjaScriptProperty** since this property is not required to call

// nor do we wish to display it on the chart label

public int MyInt

{ get; set; }

//#endregion
```

### Using a simple type as the **NinjaScriptProperty** against types which cannot be serialized

```csharp
[NinjaScriptProperty]
[XmlIgnore] // cannot serialize type of **TimeSpan**, use the **BeginTimeSpanSerialize** object to persist properties
public TimeSpan BeginTimeSpan
{ get; set; }

// users will configure this "string" as the TimeSpan which will be set as a TimeSpan object used in data processing

[Browsable(false)] // prevents this property from showing up on the UI

[Display(Name = "Begin TimeSpan", GroupName = "NinjaScriptStrategyParameters", Order = 1)]

public string BeginTimeSpanSerialize

{

   get { return BeginTimeSpan.ToString(); }

   set { BeginTimeSpan = TimeSpan.Parse(value); }
}

```
