---
title: BarsAgo
pathName: barsago
parent: chartanchor
section: references
status: imported
---

## Definition

Gets the number of bars back (x-axis coordinate) the chart anchor is drawn by a NinjaScript object. This value is the direct value which was passed to a NinjaScript Draw method. Please see the [Drawing](drawing) section for more information.

{% callout type="note" %}

This value will NOT work on manually drawn objects. This property is reserved for chart anchors which were drawn by another NinjaScript object (e.g, using a Draw method in an indicator). For manually drawn objects, please see the [SlotIndex](barindex) property.

{% /callout %}

## Property Value

A **int** value that value representing the **barsAgo** value used to drawn the anchor. This property is read-only.

## Syntax

**<`chartanchor`>.BarsAgo**
