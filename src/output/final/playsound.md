---
title: "PlaySound()"
pathName: /docs/desktop/playsound
---

## Definition

Plays a .wav file while running on real-time data.

{% callout type="note" %}

1. This method will only execute once the [State](/docs/desktop/state) has reached State.Realtime. Calls to this method during State.Historical will be ignored (in contrast to the implementation for [AddOns](/docs/desktop/alert_and_debug_concepts)).
2. The default behavior is to play the .wav file in an asynchronous manner, which can result in calls to PlaySound() to play over one another. Sound files can optionally be configured to execute in a synchronous manner by enabling the Tools > Options > Sounds > "Play consecutively" property.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
PlaySound(string fileName)
```

{% callout type="warning" %}
The underlying framework used to play the sound requires the audio file to be in PCM .wav format. Using another file format will generate an error at runtime.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| fileName | The absolute file path of the .wav file to play |

{% callout type="tip" %}
You can obtain the default NinjaTrader installation directory to access the sounds folder by using the NinjaTrader.Core.Globals.InstallDir property. Please see the example below for usage.
{% /callout %}

## Examples

```csharp
// Plays the wav file mySound.wav
PlaySound(@"C:\mySound.wav");
// Plays the default Alert1 sound that comes packaged with NinjaTrader
PlaySound(NinjaTrader.Core.Globals.InstallDir + @"\sounds\Alert1.wav");
```
