---
title: Connection
pathName: connection
parent: account
section: references
status: imported
---

## Definition

Indicates the data connection used for the specified account.

## Property Value

An instance of the **Connection** class containing information about the connection used for a specified account.

## Syntax

**<`account`>.Connection**

## Examples

```csharp
private Account myAccount;

protected override void OnStateChange()

{

    if (State == State.SetDefaults)

    {

        myAccount = Account.All.FirstOrDefault(a => a.Name == "Sim101");

    }

}

private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)

{

    Print(String.Format("{0} connection updated", myAccount.Connection.Options.Name));

}

```
