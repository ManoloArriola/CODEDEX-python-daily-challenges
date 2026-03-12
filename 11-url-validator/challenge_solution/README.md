# World Wide Web — URL Validator

This challenge is inspired by the birth of the **World Wide Web** and Tim Berners-Lee’s original proposal for linked documents.

The goal is to validate whether a given web address follows a simplified URL format.

## Problem

Given a string representing a web address, determine whether it is valid or invalid according to these rules:

- It must start with `http://` or `https://`
- The domain must contain at least one dot `.`
- The domain may only contain:
  - letters
  - digits
  - hyphens `-`
  - dots `.`

Return:

- `"valid"` if all conditions are met
- `"invalid"` otherwise
