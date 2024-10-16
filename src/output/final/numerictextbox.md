---
title: "NumericTextBox"
pathName: /docs/desktop/numerictextbox
---

## Overview

NumericTextBox provides functionality for numeric text boxes to capture user input. This UI element can be defined in XAML for an AddOn if desired, with functionality and logic related to the text box defined in C#, as in the examples below.

{% callout type="note" %}
For a complete, working example of this class in use, download the framework example located on our [Developing AddOns Overview](/docs/desktop/developing_add_ons).
{% /callout %}

NumericTextBox inherits from [System.Windows.Controls.TextBox](https://msdn.microsoft.com/en-us/library/system.windows.controls.textbox(v=vs.110).aspx), and the following additional properties can be accessed for an instance of the class:

| Property | Description |
| --- | --- |
| Minimum | Determines the minimum value which can be entered |
| Maximum | Determines the maximum value which can be entered |
| ValueType | Determines the `System.Type` which can be accepted |

## Examples

## XAML Definition of the UI Element

| <!-- Create a grid in which to place the NumericTextBox -->
<grid>
   <!-- Define a NumericTextBox -->
   <t:numerictextbox grid.column="2" text="5" valuetype="{x:Type system:Int32}" width="50" x:name="daysBackSelector">
       <!-- Set the margins for the box -->
       <t:numerictextbox.margin>
           <thickness left="{StaticResource MarginButtonLeft}" right="{StaticResource MarginBase}" top="{StaticResource PaddingColumn}"></thickness>
       </t:numerictextbox.margin>
   </t:numerictextbox>
</grid> |

## C# Code Handling Logic

| private NumericTextBox daysBack;

private DependencyObject LoadXAML()
{
       // Find days back selector
       daysBack = LogicalTreeHelper.FindLogicalNode(pageContent, "daysBackSelector") as NumericTextBox;
} |
