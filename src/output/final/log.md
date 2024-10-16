---
title: "Log()"
pathName: /docs/desktop/log
---

## Definition

Generates a NinjaScript category log event record and associated time stamp which is output to the [Log](/docs/desktop/log_tab2) tab of the NinjaTrader Control Center / Account Data windows. The Log() method also writes records to the NinjaTrader log file which can be useful for supporting 3rd party code.

{% callout type="note" %}

1. Log events do NOT process to the NinjaScript output window. For temporary logging, please see the [Print()](/docs/desktop/print) method and [Output window](/docs/desktop/output).
2. The Log event time stamp represents the user configured Time zone from the Tools > Options > General category. This setting could be different from the computer system's time zone.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
Log(string message, LogLevel logLevel)
```

{% callout type="warning" %}
Each call to this method creates a log entry which takes memory to keep loaded in the Log tab of the Control Center. Excessive logging can result in huge portions of memory being allocated to display the log messages. Please see the NinjaScript section of the [Performance Tips](/docs/desktop/performance_tips2) article for more information.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| message | A `string` value representing the message to be logged |
| logLevel | Sets the message level for the log event. Different levels are color coded in the NinjaTrader log. {% <br> %} &bull; LogLevel.Alert (also generates a pop-up notification window with log message) {% <br> %} &bull; LogLevel.Error {% <br> %} &bull; LogLevel.Information {% <br> %} &bull; LogLevel.Warning |

## Examples

```csharp
// Generates a log message
Log("This is a log message", LogLevel.Information);
// Generates a log message with a notification window
Log("This will generate a pop-up notification window as well", LogLevel.Alert);
```

