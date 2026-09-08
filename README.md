# Cryptik
## A simple Python encryption and decryption program using a custom substitution cipher.

#### Note: The text you see below is computer generated; basically; I'm lazy :)

## 🔐 Custom Substitution Cipher

This project was built to explore how encryption systems work, while practicing Python concepts such as **lists, loops, functions, conditionals, and random number generation**.

### ✨ Features

* 🔒 Encrypt text using a custom substitution key
* 🔓 Decrypt encrypted text back into the original text
* 🔑 View the current encryption key
* ✏️ Enter a custom encryption key
* 🎲 Generate a random encryption key
* ♻️ Prevent duplicate key combinations
* 🧩 Supports **95 different characters**, including:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Spaces
  * Common symbols and punctuation

### 🧠 How It Works

Each supported character is assigned a unique two-letter code.

For example, a key might contain mappings like:

```text
a → qx
b → ma
c → zt
d → br
```

When encrypting a message, the program finds each character's position in the `characters` list and replaces it with the two-letter code at the same position in the `key` list.

#### Encryption

```text
character
    ↓
find its index
    ↓
get key[index]
    ↓
two-letter encrypted code
```

#### Decryption

The process is reversed:

```text
two-letter code
    ↓
find its index in the key
    ↓
get characters[index]
    ↓
original character
```

### 🎲 Random Key Generation

The program can generate a new key automatically.

It randomly selects two lowercase letters to create combinations such as:

```text
aa
qx
ma
zt
br
...
```

Before adding a combination to the generated key, the program checks whether it already exists. This prevents duplicate key values.

The generated key contains **95 unique combinations**.

### 🚀 Usage

Run the Python file:

```bash
python3 main.py
```

You will see:

```text
1. Encrypt
2. Decrypt
3. Key functions
```

#### Encrypt

Choose `1` and enter the text you want to encrypt.

#### Decrypt

Choose `2` and enter the encrypted text.

#### Key Functions

Choose `3` to:

```text
1. Output current key
2. Enter new key
3. Generate new key
```

### ⚠️ Important

This project is intended for **learning and experimentation**.

It is a custom substitution cipher and should **not be considered secure cryptography** for protecting sensitive information. Modern cryptographic systems use much more sophisticated algorithms and security principles.

### 🛠️ Built With

* Python 3
* Python standard library
* `random`

### 📚 What I Learned

This project helped me practice:

* Python lists
* `for` loops
* `while` loops
* `if` statements
* Functions
* String manipulation
* List indexing
* Random number generation
* Duplicate detection
* Designing an algorithm from scratch

### 📌 Project Status

**Working**

The core encryption, decryption, custom key, and random key generation systems are implemented.

Future improvements could include:

* Saving keys to files
* Loading keys from files
* Better input validation
* A graphical interface
* More efficient encryption/decryption
* Stronger cryptographic methods
