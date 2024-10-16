---
title: "Attributes"
pathName: attributes
---

The following section documents both .NET native and NinjaScript custom [attributes](https://msdn.microsoft.com/en-us/library/5x6cd29c(v=vs.110).aspx) which are commonly used to define the behavior of a NinjaScript property or object. The attributes outlined in this section are primarily used to customize how properties display on the UI, but may also control how the object is compiled and executed at runtime.

{% callout type="note" %}
Notes:

1. The .NET Framework supplies many other pre-defined [system attributes](https://msdn.microsoft.com/en-us/library/2e39z096.aspx) which can technically be used for custom NinjaScript programming, but are NOT covered in this section and therefore are considered unsupported. 3rd party developers are encouraged to explore additional usage, but the resulting behavior CANNOT be guaranteed.
2. Not all attributes can be applied to all object types. For example, applying an attribute that is defined to target a class will NOT compile should you attempt to apply this attribute to a property type.
{% /callout %}

## Common Attributes

|  |  |
| --- | --- |
| [BrowsableAttribute](browsableattribute) | Determines if a property should be displayed in the NinjaTrader UI's property grid. |
| [CategoryOrderAttribute](categoryorderattribute) | Determines the sequence in which a NinjaScript object's [Display.GroupName](displayattribute) categories are arranged in relation to other categories in the UI. |
| [DisplayAttribute](displayattribute) | Determines how a property is displayed on the NinjaTrader UI's property grid. |
| [NinjaScriptPropertyAttribute](ninjascriptpropertyattribute) | Determines if a property should be included in the NinjaScript object's constructor as a parameter. |
| [RangeAttribute](rangeattribute) | Determines if the value of a property is valid within a specified range. |
| [XmlIgnoreAttribute](xmlignoreattribute) | Determines if a property participates in the XML serialization routines (saving workspaces or templates). |

## Applying Attributes

Attributes are applied directly before the property, method, or class, and are identified by wrapping brackets:

```csharp
[AnExampleAttribute] // a pseudo-attribute demonstrating how to target an object
public object AnExampleProperty // the property that is being targeted
{ get; set; }
```

{% callout type="tip" %}
Conventionally, the suffix "attribute" is provided to the object's name to help determine that it is an attribute; however, C# does not require you to specify the full name of an attribute. For example, DisplayAttribute() will compile the same as Display().
{% /callout %}
