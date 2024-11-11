---
title: Status
pathName: status
parent: connection_class
section: references
status: imported
---

## Definition

Indicates the current status of the primary data connection.

## Properties

**<`connection`>.Status**

## Examples

```csharp

private int priceLost;
private int mainLost;

private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
// Count the number of times OnAccountItemUpdate() is called with a lost price connection
if (myAccount.Connection.PriceStatus == ConnectionStatus.ConnectionLost)


priceLost += 1;

// Count the number of times OnAccountItemUpdate() is called with a lost primary connection

if (myAccount.Connection.Status == ConnectionStatus.ConnectionLost)
mainLost += 1;

// Print the number of times each connection was lost during OnAccountItemUpdate()
if (mainLost > 0 || priceLost > 0)
Print(String.Format("Main connection lost {0} times. Price feed lost {1} times.", mainLost, priceLost));


Print(String.Format("Main connection lost {0} times. Price feed lost {1} times.", 
mainLost, priceLost));
}
```