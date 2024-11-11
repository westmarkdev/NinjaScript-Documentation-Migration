---
title: Orders
pathName: orders_account
parent: account
section: references
status: changed
---

## Definition

A collection of Order objects generated for the specified account

## Property Value

An **Collection** of Order objects

{% callout type="note" %}

Please keep in mind that orders placed when in **State.Historical** are not submitted live to an account.

{% /callout %}

## Syntax

**<`account`>.Orders**

## Examples

```csharp
private Account myAccount;

protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Initialize myAccount
   }
}

private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
   // Print the name and order action of each order processed on the account
   foreach (Order order in myAccount.Orders)
   {
       Print(String.Format("Order placed: {0} - {1}", order.Name, order.OrderAction));
   }
}
```
