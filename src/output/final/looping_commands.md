---
title: "Looping Commands"
pathName: /docs/desktop/looping_commands
---

## Looping Commands

Looping commands control the execution flow of your script. If you wanted to print the word NinjaTrader 100 times, you could either use 100 lines of code or do the same using a looping command in only a few lines of code.

## While Loop

```csharp
while (Boolean expression)
{
    // Do something here
}
```

```csharp
// Print NinjaTrader 100 times to the output window
int x = 0;
while (x < 100)
{
    Print("NinjaTrader");
    x = x + 1;
}
```

## Do While Loop

```csharp
do
{
    // Do something here
}
while (Boolean expression);
```

```csharp
// Print NinjaTrader 100 times to the output window
int x = 0;
do
{
    Print("NinjaTrader");
    x = x + 1;
}
while (x < 100);
```

## For Loop

```csharp
for (initializer; boolean expression; iterator)
{
    // Do something here
}
```

```csharp
// Print NinjaTrader 100 times to the output window
for (int x = 0; x < 100; x++)
{
    Print("NinjaTrader");
}
```

## Foreach Loop

```csharp
foreach (type identifier in collection)
{
    // Do something here
}
```

```csharp
// Count the number of oatmeal cookies in a cookie jar
int oatmealCookies = 0;
foreach (cookie in cookieJar)
{
    if (cookie.Type == Oatmeal)
    {
        oatmealCookies = oatmealCookies + 1;
    }
}
Print("There are " + oatmealCookies.ToString() + " oatmeal cookies in the cookie jar.");
```

## Break and Continue

You can use the break command to exit a loop at any time. The following example is an infinite loop, but we will break out after the first Print statement.

```csharp
// Exit the infinite loop after the first iteration
while (0 == 0)
{
    Print("NinjaTrader");
    break;
}
```

The continue command will jump ahead to the next iteration of the loop. The following example will never print "NinjaTrader," because the continue command sends control back to the top of the loop each time.

```csharp
// Never prints "NinjaTrader"
for (int x = 0; x < 100; x++)
{
    continue;
    Print("NinjaTrader");
}
```
