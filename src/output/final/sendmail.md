---
title: "SendMail()"
pathName: /docs/desktop/sendmail
---

## Definition

Sends an email message through the default email sharing service.

{% callout type="note" %}

1. This method can only be called once the [State](/docs/desktop/state) has reached State.Realtime. Calls to this method in any other State will be silently ignored (in contrast to the implementation for [AddOns](/docs/desktop/alert_and_debug_concepts)).
2. You MUST configure an email account as a default "Mail" Share Service from the [General Options](/docs/desktop/general_section).
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
SendMail(string to, string subject, string text)
```

{% callout type="warning" %}
If mail is not received, please check the [Log](/docs/desktop/log_tab2) tab of the control center for any specific errors which could be related to delivering the message.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| to | The email recipient  |
| subject | Subject line of email |
| text | Message body of email |

## Examples

```csharp
// Generates an email message
SendMail("customer@winners.com", "Trade Alert", "Buy ES");
```
