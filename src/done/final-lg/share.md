---
title: "Share()"
pathName: share
---

## Definition

Sends a message or screenshot to a social network or Share Service.

{% callout type="note" %}
This method can only be called once the [State](state) has reached `State.Realtime`. Calls to this method in any other State will be silently ignored.
You MUST configure an account with a Share Service provider from the [General Options](general_section).
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
Share(string serviceName, string message)
```

```csharp
Share(string serviceName, string message, object[] args)
```

```csharp
Share(string serviceName, string message, string screenshotPath)
```

```csharp
Share(string serviceName, string message, string screenshotPath, object[] args)
```

## Parameters

| Parameter      | Description                                                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| serviceName    | A string value representing the share service to be used.                                                                                                      |
| message        | A string value representing the text body sent to the social network or other Share providers. Note: The message is what appears in the text box of the Share window. |
| screenshotPath | Optional string path to a screenshot or other images sent to the social network or other Share providers.                                                      |
| args           | A generic `object[]` array used to designate additional information sent to the share service.                                                                  |

{% callout type="tip" %}

1. The "args" parameter differs for each share service used. If you are using a custom developed share adapter, you need to work with the developer of that adapter to understand what the "args" parameter represents for that adapter.
2. For the default NinjaTrader share adapters, the "args" array represents the following:
   - Mail share service:
     - `args[0]` = A string representing the email "To" field,
     - `args[1]` = A string representing the email "Subject" field
   - StockTwits share service:
     - `args[0]` = An enum representing the "StockTwitsSentiment" parameter
{% /callout %}

## Examples

```csharp
// using "args" as the Mail "To" and "Subject" parameters
Share("Gmail", "Test Message", new object[]{ "example@test.com", "Test Subject Line" });
```
