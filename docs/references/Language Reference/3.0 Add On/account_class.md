---
title: Account Class
pathName: account_class
parent: add_on
section: references
status: imported
---

## Definition

The Account class can be used to subscribe to account-related events as well as access account-related information.

{% callout type="note" %}

Also happens when rewinding/fast forwarding Playback connections.

{% /callout %}

## Static Account Class Properties

{% table %}

* Property
* Description

---

* **All**
* A collection of Account objects

---

* **AccountStatusUpdate**
* Event handler for account status updates

---

* **SimulationAccountReset**
* Event handler for resets on sim accounts
{% /table %}

## Methods and Properties From Account instances

{% table %}

* Property
* Description

---

* **AccountItem**
* Represents various account variables used to reflect values the status of the account

---

* **AccountItemUpdate**
* Event handler for changes to account values

---

* **Cancel()**
* Cancels specified order(s) on the account

---

* **CancelAllOrders()**
* Cancels all orders of an instrument on the account

---

* **Change()**
* Changes specified order(s) on the account

---

* **Connection**
* A Connection representing the connection this account is associated with

---

* **CreateOrder()**
* Creates orders for the account that need to be submitted via Submit()

---

* **Denomination**
* A Currency representing the denomination currency of this connection

---

* **Executions**
* A collection of executions on this account

---

* **ExecutionUpdate**
* Event handler for when new executions come in, an existing execution is amended, or an execution is removed

---

* **Flatten()**
* Flattens the account on specified instrument(s)

---

* **Get()**
* Returns the value of an **AccountItem**

---

* **Name**
* A string representing the name of this account

---

* **Orders**
* A collection of orders on this account

---

* **OrderUpdate**
* Event handler for changes to orders

---

* **Positions**
* A collection of positions on this account

---

* **PositionUpdate**
* Event handler for changes to positions

---

* **Strategies**
* A collection of strategies on this account

---

* **Submit()**
* Submits specified order(s)
{% /table %}

## Example

```csharp
private Account myAccount;

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Find our Sim101 account
        lock (Account.All)
            myAccount = Account.All.FirstOrDefault(a => a.Name == "Sim101");

        // Subscribe to static events. Remember to unsubscribe with -= when you are done
        Account.AccountStatusUpdate += OnAccountStatusUpdate;

        if (myAccount != null)
        {
            // Print some information about our account using the AccountItem indexer
            Print(string.Format("Account Name: {0} Connection Name: {1} Cash Value {2}",
                myAccount.Name,
                myAccount.Connection.Options.Name,
                myAccount.Get(AccountItem.CashValue, Currency.UsDollar)));

            // Print the prices of the executions on our account
            lock (myAccount.Executions)
                foreach (Execution execution in myAccount.Executions)
                    Print("Price: " + execution.Price);

            // Subscribe to events. Remember to unsubscribe with -= when you are done
            myAccount.AccountItemUpdate += OnAccountItemUpdate;
            myAccount.ExecutionUpdate += OnExecutionUpdate;
        }
    }
    else if (State == State.Terminated)
    {
        // Unsubscribe to events
        myAccount.AccountItemUpdate -= OnAccountItemUpdate;
        myAccount.ExecutionUpdate -= OnExecutionUpdate;
        Account.AccountStatusUpdate -= OnAccountStatusUpdate;
    }
}

private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
    // Do something with the account status update
}

private void OnAccountItemUpdate(object sender, AccountItemEventArgs e)
{
    // Do something with the account item update
}

private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
    // Do something with the execution update
}
```
