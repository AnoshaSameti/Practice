# ⏱️ Human Readable Time

My Python solution to the Codewars kata **"Human Readable Time"**.


## ⁉ Problem

Convert a non-negative integer representing a number of **seconds** into a human-readable time format.

The output should follow the format:

```text
HH:MM:SS
```

where:

- `HH` = hours (00–99)
- `MM` = minutes (00–59)
- `SS` = seconds (00–59)

Each value must always contain **two digits**, adding a leading zero when necessary.


### Examples

| Input | Output |
|------:|:------|
| `0` | `00:00:00` |
| `5` | `00:00:05` |
| `60` | `00:01:00` |
| `86399` | `23:59:59` |
| `359999` | `99:59:59` |


## Approach

The solution:

1. Calculates the number of hours using integer division.
2. Computes the remaining minutes.
3. Determines the remaining seconds.
4. Formats each value as a two-digit number.
5. Returns the formatted time string.
