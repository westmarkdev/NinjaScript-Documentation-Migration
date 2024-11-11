---
status: double_check
title: XmlIgnoreAttribute
pathName: xmlignoreattribute
parent: attributes
section: references
lg2m: true
---

## Definition

Determines if the following declared property participates in the XML serialization routines which are used to save NinjaScript objects to a workspace or template.  The default behavior will attempt to serialize all public properties, however there may be some types of objects which cannot be serialized, or you may not wish for this property to be saved/restored.  Should that be the case, you can optionally set the object to be ignored by defining the XmlIgnore attribute.

{% callout type="note" %}

The **XmlIgnoreAttribute** object is a general purpose attribute made available from the .NET Framework.  The information on this page is written to demonstrate how you may use this object within NinjaScript conventions to be used for the NinjaTrader serialization (e.g., saving an indicator property to a workspace).  There are more methods and properties that you can learn about from MSDN's [XmlIgnoreAttribute Class](https://msdn.microsoft.com/en-us/library/system.xml.serialization.xmlignoreattribute(v=vs.110).aspx) which are NOT covered in this topic; as such there is NO guarantee they will work with the NinjaTrader serialization.

{% /callout %}

## Syntax

**[XmlIgnore]**  

**[XmlIgnore(bool)]**

## Parameters

This attribute does not require any parameters; default value is true and usage will ensure the property is ignored by XML routines.

## Examples

```csharp
#region Properties  
   
[XmlIgnore] // ensures that the property will NOT be saved/recovered as part of a chart template or workspace  
public Brush MyBrush    
{ get; set; }  
   
#endregion
```

{% callout type="note" %}

Tip:  A complete example of the usage of **XmlIgnore** attribute and workspace serialization can be found in the tips section of our support forum on [User Definable Color Inputs](user_definable_color_inputs)

{% / callout %}