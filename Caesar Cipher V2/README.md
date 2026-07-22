![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🔐 Caesar Cipher Encryption

A Python implementation of a modified Caesar Cipher that encrypts a message using an increasing shift value.


## ⁉ Problem

The Caesar Cipher is a classic encryption algorithm that shifts each letter of the alphabet by a fixed amount.

In this variation, the shift increases by **1** for each consecutive letter.

For example, if the initial shift is **3**:

```text
Original:  ABC
A -> +3 -> D
B -> +4 -> F
C -> +5 -> H

Encrypted: DFH
```

**Note:** Spaces are **not counted** as letters, so they do not increase the shift.


## Input

The program receives:

1. An integer representing the initial shift.
2. A lowercase English sentence to encrypt.


### Example

**Input**

```text
3
abc
```

**Output**

```text
dfh
```


## Approach

The program:

- Normalizes the shift value.
- Iterates through each character.
- Increases the effective shift by one for every letter processed.
- Preserves spaces without counting them toward the shift.
