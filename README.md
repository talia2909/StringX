# StringX

## Introduction

The `StringX.py` module defines a custom `String` class, offering extended functionalities beyond Python's built-in string type. The primary aim is to provide advanced string manipulation capabilities, including encoding/decoding mechanisms and rule-based transformations.

## Features

1. **Advanced String Representation**:
    - The module allows you to create string objects with a rich set of attributes and methods for manipulation.

2. **Overloaded Operators**:
    - Perform arithmetic and comparison operations on strings, such as addition (`+`), multiplication (`*`), and equivalence (`==`).

3. **Enhanced String Operations**:
    - `count()`: Count occurrences of a substring.
    - `isupper()`: Check if the string is in uppercase.
    - `islower()`: Check if the string is in lowercase.

4. **Encoding/Decoding Capabilities**:
    - Encode and decode strings using Base64 and other custom methods.
    - Apply rule-based transformations to strings.

5. **Custom Exceptions**:
    - Handle specific error scenarios related to the advanced operations of the `String` class.

## Class Definitions

### `String`

#### Attributes:
- `value`: Represents the actual string content.
- `bits`: Used in encoding/decoding operations.
- `lenght`: Represents the length of the string (Note: This might be a typo, consider using Python's `len` function).
- `stri_list`, `pair_original`: Internal representations for specific operations.
- `rules`: Contains rules for encoding/decoding.

#### Key Methods:
- `base64()`: Encode the string using Base64.
- ... (Other methods related to encoding/decoding and string manipulation).

### Custom Exceptions

- `Base64DecodeError`: Raised for errors during Base64 decoding.
- `CyclicCharsError`: Raised for cyclic character-related errors.
- `CyclicCharsDecodeError`: Raised for decoding errors related to cyclic characters.
- `BytePairError`: Raised for byte pair-related errors.
- `BytePairDecodeError`: Raised for decoding errors related to byte pairs.

## Usage

Instantiate the `String` class with your desired string content and optional rules for transformations:

```python
b = String('#d#ac', ['! = aa', '“ = !a', '# = “b'])
```

Invoke methods on the object to perform various operations:

```python
print(b.decode_byte_pair())
print(b.decode_byte_pair().byte_pair_encoding())
```

(Note: Sample usage might vary based on the complete functionality of the module).

## Conclusion

The `String.py` module provides an enriched set of string manipulation tools, making it suitable for applications requiring advanced string processing capabilities.

