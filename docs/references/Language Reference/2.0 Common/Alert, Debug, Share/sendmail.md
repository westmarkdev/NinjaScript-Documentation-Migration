---
section: references
title: SendMail()
pathName: sendmail
parent: alert_debug_share
status: review
---

## Definition

Sends an email message through the default email sharing service.

{% callout type="note" %}

Notes:  

1. This method can only be called once the **State** has reached **State.Realtime**. Calls to this method in any other State will be silently ignored (in contrast to the implementation for **AddOns**).
2. You MUST configure an email account as a default "Mail" Share Service from the **General Options**.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**SendMail(string to, string subject, string text)**

{% callout type="warning" %}

If mail is not received, please check the **Log** tab of the control center for any specific errors which could be related to delivering the message.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **to**
* The email recipient

---

* **subject**
* Subject line of email

---

* **text**
* Message body of email
{% /table %}

## Examples

```csharp
// Generates an email message
SendMail("customer@winners.com", "Trade Alert", "Buy ES");
```
