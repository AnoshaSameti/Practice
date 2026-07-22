![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🔓 Message Decryption

A simple Python program that decrypts an encoded message using a known plaintext character.

## ⁉ Problem

A hacker obtained several encrypted messages along with some additional information that can help decrypt them.

You are given:

- An encrypted message.
- An integer `n`.
- The actual plaintext character corresponding to the **nth letter** of the encrypted message.

Using this information, decrypt and print the original message.

> **Note:** Spaces are **not counted** as letters when determining the `n`th position.

### Example

**Input**

```text
dfh
2
b
```

**Output**

```text
abc
```


## 👀 Approach

The program:

1. Finds the position of the **nth letter** in the encrypted message (ignoring spaces).
2. Calculates the encryption shift using the known plaintext character.
3. Decrypts each letter while preserving spaces.
